# FetchNames404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **str** | The identifier of the entity that was not found. | 

## Example

```python
from _warg_client.models.fetch_names404_response import FetchNames404Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchNames404Response from a JSON string
fetch_names404_response_instance = FetchNames404Response.from_json(json)
# print the JSON string representation of the object
print FetchNames404Response.to_json()

# convert the object into a dict
fetch_names404_response_dict = fetch_names404_response_instance.to_dict()
# create an instance of FetchNames404Response from a dict
fetch_names404_response_from_dict = FetchNames404Response.from_dict(fetch_names404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


