"""Offline byte transformation. Recover the input that matches TARGET."""
import sys

TARGET = [104, 247, 45, 165, 36, 151, 144, 245, 215, 24, 248, 176, 44, 56, 134, 90, 196, 220, 213, 69, 121, 132]


def transform(raw):
    state = 0x53
    result = []
    for index, value in enumerate(raw):
        state = (state * 73 + 41) & 0xff
        shift = index % 5 + 1
        value ^= state
        value = ((value << shift) | (value >> (8 - shift))) & 0xff
        result.append((value + 29 * index + 7) & 0xff)
    return result


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 signal.py YOUR_CANDIDATE')
        return 2
    accepted = transform(sys.argv[1].encode('utf-8')) == TARGET
    print('MATCH' if accepted else 'NO MATCH')
    return 0 if accepted else 1


if __name__ == '__main__':
    raise SystemExit(main())
