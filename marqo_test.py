import marqo
import json
import pprint

mq = marqo.Client(url='http://localhost:8882')


def create_base_index():
    mq.create_index(
            "index",
            model="hf/e5-base-v2"
    )

def get_mappings(data):
    json_obj = data[0]
    # Parse the JSON object if it's a string
    if isinstance(json_obj, str):
        json_obj = json.loads(json_obj)
    
    # Extract all keys from the JSON object
    keys = list(json_obj.keys())
    
    # Calculate the weight for each key
    num_keys = len(keys)
    weight = 1.0 / num_keys if num_keys > 0 else 0
    
    # Create the weights dictionary
    weights = {key: weight for key in keys}
    
    return {
            'mapped_data': {
                'type': "multimodal_combination",
                "wiehgts": weights,
            },
        }

def add_index(data):  
    mq.index("index").add_documents(
            documents=data,
            mappings=get_mappings(data),
            tensor_fields=['mapped_data']        
    )

if __name__ == "__main__":
    create_base_index()
