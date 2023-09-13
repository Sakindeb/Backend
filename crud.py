import requests

# Define the API endpoint URL and the person ID to delete
api_url = 'http://127.0.0.1:5000/api'  # Update with your API URL
person_id_to_delete = 1  # Replace with the ID of the person you want to delete

# Send a DELETE request to delete the person by ID
response = requests.delete(f"{api_url}/{person_id_to_delete}")

# Check the response status and content
if response.status_code == 200:
    print(f"Person with ID {person_id_to_delete} deleted successfully")
else:
    print(f"Failed to delete person with ID {person_id_to_delete}: {response.text}")

