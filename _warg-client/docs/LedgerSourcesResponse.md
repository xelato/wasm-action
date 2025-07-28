# LedgerSourcesResponse

A response containing the registry ledger sources.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_algorithm** | **str** | The type of hash algorithm used for log and record IDs. | [optional] 
**sources** | [**List[LedgerSourcesResponseSourcesInner]**](LedgerSourcesResponseSourcesInner.md) | The ledger sources. | [optional] 

## Example

```python
from _warg_client.models.ledger_sources_response import LedgerSourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerSourcesResponse from a JSON string
ledger_sources_response_instance = LedgerSourcesResponse.from_json(json)
# print the JSON string representation of the object
print LedgerSourcesResponse.to_json()

# convert the object into a dict
ledger_sources_response_dict = ledger_sources_response_instance.to_dict()
# create an instance of LedgerSourcesResponse from a dict
ledger_sources_response_from_dict = LedgerSourcesResponse.from_dict(ledger_sources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


