import time
import requests
import yaml
import argparse


def test_endpoints(endpoints,availability):
    for endpoint in endpoints:
        if len(endpoint['url'].split('//'))>1:
            if len(endpoint['url'].split('//')[1].split('/'))>0:
                    domain = endpoint['url'].split('//')[1].split('/')[0]
        if domain not in availability:
            availability[domain] = (0, 0)
        headers = endpoint.get("headers", {})
        method = endpoint.get("method", "GET")
        url = endpoint.get("url")
        data = endpoint.get("body",{})
        name = endpoint.get("name")
        try:
            start_time = time.time()
            response = requests.request(method, url, headers=headers, data=data)
            latency = (time.time() - start_time)
            if response.status_code >= 200 and response.status_code <= 299 and latency < 0.5:
                availability[domain] = (availability[domain][0] + 1, availability[domain][1])
            else:
                availability[domain] = (availability[domain][0], availability[domain][1] + 1)
        except requests.exceptions.RequestException:
            availability[domain] = (availability[domain][0], availability[domain][1] + 1)
    return availability

def main(config_file_path):
    with open(config_file_path) as f:
        endpoints = yaml.safe_load(f)

    if isinstance(endpoints, dict):
        endpoints = list(endpoints.values())

    availability = {}

    while True:
        test_endpoints(endpoints, availability)
        for domain, (success, failure) in availability.items():
            total = success + failure
            availability_percentage = success / total * 100 if total != 0 else 0
            print(f"{domain} has {availability_percentage:.0f}% availability percentage")
        time.sleep(15)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test the availability of HTTP endpoints defined in a YAML configuration file.')
    parser.add_argument('config_file', type=str, help='Path to the YAML configuration file')
    args = parser.parse_args()
    main(args.config_file)
