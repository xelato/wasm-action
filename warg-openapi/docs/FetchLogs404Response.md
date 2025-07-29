# FetchLogs404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **int** | The log length that was not found. | 

## Example

```python
from warg_openapi.models.fetch_logs404_response import FetchLogs404Response

# TODO update the JSON string below
json = "{}"
# create an instance of FetchLogs404Response from a JSON string
fetch_logs404_response_instance = FetchLogs404Response.from_json(json)
# print the JSON string representation of the object
print FetchLogs404Response.to_json()

# convert the object into a dict
fetch_logs404_response_dict = fetch_logs404_response_instance.to_dict()
# create an instance of FetchLogs404Response from a dict
fetch_logs404_response_from_dict = FetchLogs404Response.from_dict(fetch_logs404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


