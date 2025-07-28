# FetchLogsRequest

A request to fetch logs from the registry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_length** | **int** | The registry checkpoint log length to fetch from. | 
**limit** | **int** | The limit of operator and packages records to return for the fetch request. | [optional] [default to 100]
**operator** | **str** | Represents a supported hash. | [optional] 
**packages** | **object** | The map of package log identifier to last known package record fetch token.  If the last package record identifier is null, records are returned from the start of the log.  | [optional] 

## Example

```python
from _warg_client.models.fetch_logs_request import FetchLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FetchLogsRequest from a JSON string
fetch_logs_request_instance = FetchLogsRequest.from_json(json)
# print the JSON string representation of the object
print FetchLogsRequest.to_json()

# convert the object into a dict
fetch_logs_request_dict = fetch_logs_request_instance.to_dict()
# create an instance of FetchLogsRequest from a dict
fetch_logs_request_from_dict = FetchLogsRequest.from_dict(fetch_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


