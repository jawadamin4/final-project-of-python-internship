import requests

# The URL of your API endpoint
url = 'http://127.0.0.1:8000/fetch-data/'  # Replace with the correct URL if needed

# Make the POST request
response = requests.post(url)

# Check the response status code
if response.status_code == 201:
    # Request was successful
    data = response.json()
    print(data)  # This will print the serialized data from the API
else:
    # Request failed
    print("Failed to fetch data:", response.json())
