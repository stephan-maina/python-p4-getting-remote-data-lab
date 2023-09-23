import requests

class GetRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_get_request(self, endpoint, params=None, headers=None):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, headers=headers)

            # Check if the response status code is 200 (OK)
            if response.status_code == 200:
                return response.json()  # Parse JSON response and return it
            else:
                response.raise_for_status()  # Raise an exception for non-200 status codes
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage:
    base_url = "https://api.example.com"
    requester = GetRequester(base_url)
    
    # Define the API endpoint and optional parameters/headers
    endpoint = "data"
    params = {"param1": "value1", "param2": "value2"}
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

    # Send a GET request and handle the response
    response_data = requester.send_get_request(endpoint, params=params, headers=headers)
    
    # Process the response data as needed
    if response_data:
        print(response_data)
