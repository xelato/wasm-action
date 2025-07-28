# LedgerSourcesResponseSourcesInner

Ledger source HTTP get URL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_registry_index** | **int** | The first registry index included in the source. | 
**last_registry_index** | **int** | The last registry index included in the source. | 
**url** | **str** | The HTTP GET URL to fetch the source. | 
**content_type** | **str** | The content type of source. | 
**accept_ranges** | **bool** | Flag indicating if the server accepts byte ranges with &#x60;Range&#x60; header. | [optional] 

## Example

```python
from warg_openapi.models.ledger_sources_response_sources_inner import LedgerSourcesResponseSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LedgerSourcesResponseSourcesInner from a JSON string
ledger_sources_response_sources_inner_instance = LedgerSourcesResponseSourcesInner.from_json(json)
# print the JSON string representation of the object
print LedgerSourcesResponseSourcesInner.to_json()

# convert the object into a dict
ledger_sources_response_sources_inner_dict = ledger_sources_response_sources_inner_instance.to_dict()
# create an instance of LedgerSourcesResponseSourcesInner from a dict
ledger_sources_response_sources_inner_from_dict = LedgerSourcesResponseSourcesInner.from_dict(ledger_sources_response_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


