# FetchLogsIDNotFoundError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **str** | The identifier of the entity that was not found. | 

## Example

```python
from warg_openapi.models.fetch_logs_id_not_found_error import FetchLogsIDNotFoundError

# TODO update the JSON string below
json = "{}"
# create an instance of FetchLogsIDNotFoundError from a JSON string
fetch_logs_id_not_found_error_instance = FetchLogsIDNotFoundError.from_json(json)
# print the JSON string representation of the object
print FetchLogsIDNotFoundError.to_json()

# convert the object into a dict
fetch_logs_id_not_found_error_dict = fetch_logs_id_not_found_error_instance.to_dict()
# create an instance of FetchLogsIDNotFoundError from a dict
fetch_logs_id_not_found_error_from_dict = FetchLogsIDNotFoundError.from_dict(fetch_logs_id_not_found_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


