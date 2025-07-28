# FetchLogsResponse

A response containing the requested logs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**more** | **bool** | Whether there may be more records available.  This occurs when the number of records returned for a log reaches the requested limit.  If &#x60;true&#x60;, the client should make another request with the new last known record identifiers.  | [optional] 
**operator** | [**List[PublishedRecordEnvelope]**](PublishedRecordEnvelope.md) | The operator log records for the given checkpoint since the last known record. | [optional] 
**warnings** | [**List[FetchWarning]**](FetchWarning.md) | An optional list of warnings. | [optional] 
**packages** | **object** | The map of package log identifier to package records. | [optional] 

## Example

```python
from _warg_client.models.fetch_logs_response import FetchLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchLogsResponse from a JSON string
fetch_logs_response_instance = FetchLogsResponse.from_json(json)
# print the JSON string representation of the object
print FetchLogsResponse.to_json()

# convert the object into a dict
fetch_logs_response_dict = fetch_logs_response_instance.to_dict()
# create an instance of FetchLogsResponse from a dict
fetch_logs_response_from_dict = FetchLogsResponse.from_dict(fetch_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


