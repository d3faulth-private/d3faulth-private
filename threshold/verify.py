#!/usr/bin/env python3
"""Offline result check for The Threshold assessment 01.

No networking, uploads, account access, or membership decisions.
Exit codes: 0 = matching fixed findings, 1 = mismatch, 2 = input error.
"""
import argparse
import hashlib
import hmac
import json
from pathlib import Path
import sys

EXPECTED = {'web': 'aad6d4552bcaee3ee4dff767be362c2e55b090614e19bc198830629a13943ee5', 'reversing': '85289ce8eb2c77571d0c88bc955bf095de2796334d6c97505670acb953660e28', 'forensics': 'fff37565358aa244b71a11dc0a65de9a2047b1c1f5abb9691ab2b2eb3922c40b', 'linux': 'bc08c2a6e728e733774ffea4b8aa96b1aa89437d7c07c1da2aff20b22af2d712', 'tooling': '78a7ad07d505304c6cb049a3e64c1f129e4f80c2cd04a0bbe71a91abede956d6'}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key: ' + key)
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError('non-finite JSON value: ' + value)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('track', nargs='?', choices=sorted(EXPECTED))
    parser.add_argument('answer', nargs='?', type=Path)
    parser.add_argument('--list', action='store_true', help='list available tracks')
    args = parser.parse_args(argv)
    if args.list:
        print('The Threshold / assessment 01\n' + '\n'.join(sorted(EXPECTED)))
        return 0
    if args.track is None or args.answer is None:
        parser.error('provide a track and a JSON answer file, or use --list')
    try:
        with args.answer.open('rb') as stream:
            raw = stream.read(65537)
        if len(raw) > 65536:
            raise ValueError('answer file exceeds 64 KiB')
        answer = json.loads(raw.decode('utf-8-sig'), object_pairs_hook=unique_object, parse_constant=reject_constant)
        if not isinstance(answer, dict):
            raise ValueError('answer must be a JSON object')
        canonical = json.dumps(answer, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
    except (OSError, ValueError, RecursionError) as exc:
        print('INPUT ERROR: ' + str(exc), file=sys.stderr)
        return 2
    actual = hashlib.sha256(canonical).hexdigest()
    if hmac.compare_digest(actual, EXPECTED[args.track]):
        print('MATCH — fixed findings verified. Prepare the required writeup and supporting work.')
        print('This is a local practice check, not a membership approval or submission.')
        return 0
    print('NO MATCH — revisit the evidence, exact identifiers, JSON types, and required fields.')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
