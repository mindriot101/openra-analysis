import requests
import os
import json
import tempfile


CACHE_NAME = os.path.join(tempfile.gettempdir(), 'openra_map_hash_names.json')
ROOT_URL = 'http://resource.openra.net/map/hash/{map_hash}'


def build_map_hash_to_name_mapping(hashes, force=False):
    if not os.path.isfile(CACHE_NAME) or force:
        results = build_cached_results(hashes)
        with open(CACHE_NAME, 'w') as outfile:
            json.dump(results, outfile, indent=2)

    with open(CACHE_NAME) as infile:
        return json.load(infile)


def build_cached_results(hashes):
    result = {}
    for h in hashes:
        map_name = fetch_map_name(h)
        result[h] = map_name
    return result


def fetch_map_name(hash):
    url = ROOT_URL.format(map_hash=hash)
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        return None

    payload = response.json()
    return payload[0]['title']
