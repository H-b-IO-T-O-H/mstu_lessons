import requests

TEST_URL = 'https://httpbin.org/get'

if __name__ == '__main__':
    resp = requests.get(TEST_URL)
    resp_json: str = resp.json()

    print(resp_json)
