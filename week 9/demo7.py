import requests

def fetch_json(url, timeout=10):
    '''Fetch a URL and reuturn parsed JSON, or None ono any error.'''
    try:
        r = requests.get(url,timeout = timeout)
        r.raise_for_status() #raises HTTPError if 4xx/5xx
        return r.json()
    except requests.exception.Timout:
        print(f"Error: {url} took too long to respond")
        return None
    except requests.exeception.HTTPError as e:
        print(f"Error: HTTP {e.response.status_code} from {url}")
        return None
    except requests.exceptions.RewuestException as e:
        print(f"Error: could not reach {url}: {e}")
        return None
    except ValueError:
        print(f"Error: response from {url} was not valid JSON")
        return None
