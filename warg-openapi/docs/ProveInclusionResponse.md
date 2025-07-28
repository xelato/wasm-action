# ProveInclusionResponse

A response containing the inclusion proof bundle.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **bytearray** | The log inclusion proof bundle. | 
**map** | **bytearray** | The map inclusion proof bundle. | 

## Example

```python
from warg_openapi.models.prove_inclusion_response import ProveInclusionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProveInclusionResponse from a JSON string
prove_inclusion_response_instance = ProveInclusionResponse.from_json(json)
# print the JSON string representation of the object
print ProveInclusionResponse.to_json()

# convert the object into a dict
prove_inclusion_response_dict = prove_inclusion_response_instance.to_dict()
# create an instance of ProveInclusionResponse from a dict
prove_inclusion_response_from_dict = ProveInclusionResponse.from_dict(prove_inclusion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


