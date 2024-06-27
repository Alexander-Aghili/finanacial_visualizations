import json

def iterate_json_components(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            
            # Check if the data is a list
            if isinstance(data, list):
                for index, item in enumerate(data):
                    print(f"Item {index + 1}: {item}")
            else:
                print("The JSON file does not contain a JSON array.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to your JSON file
json_file_path = 'data.json'
from marqo_test import add_index

with open(json_file_path, 'r') as file:
    data = json.load(file)
    add_index(data)
         
# Call the function
#iterate_json_components(json_file_path)
