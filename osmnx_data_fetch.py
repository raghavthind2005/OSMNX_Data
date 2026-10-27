import time
import requests
import osmnx as ox
from osmnx._errors import ResponseStatusCodeError, InsufficientResponseError

ox.settings.log_console = True
bbox = (-122.4003, 37.7867, -122.3931, 37.7917)

waits = [0, 30, 60, 120, 240, 480]   # exponential backoff
for wait in waits:
    if wait:
        print(f"Waiting {wait}s before retrying.")
        time.sleep(wait)
    try:
        b = ox.features.features_from_bbox(bbox, {"building": True})
        print(len(b), "buildings fetched and cached")
        break
    except (ResponseStatusCodeError, InsufficientResponseError,
            requests.exceptions.RequestException) as e:
        print("Attempt failed:", str(e).splitlines()[0])
else:
    print("All attempts failed.")