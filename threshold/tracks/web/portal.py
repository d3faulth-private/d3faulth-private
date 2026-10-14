"""Deliberately flawed, offline authorization model for The Threshold."""
import json
from pathlib import Path
import sys


def handle(request, fixture):
    session = fixture['sessions'].get(request.get('session'))
    if not session or not session['active']:
        return {'status': 401, 'error': 'active session required'}
    document = fixture['documents'].get(request.get('document'))
    if document is None:
        return {'status': 404, 'error': 'document not found'}
    organization = request.get('organization', session['organization'])
    if document['organization'] != organization:
        return {'status': 403, 'error': 'organization mismatch'}
    return {'status': 200, 'document': document}


def main():
    fixture = json.loads((Path(__file__).parent / 'evidence/portal.json').read_text())
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict):
            raise ValueError('request must be a JSON object')
        for field in ('session', 'document', 'organization'):
            if field in request and not isinstance(request[field], str):
                raise ValueError('request fields must be strings')
        print(json.dumps(handle(request, fixture), indent=2))
    except (ValueError, TypeError) as exc:
        print(json.dumps({'status': 400, 'error': str(exc)}))
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
