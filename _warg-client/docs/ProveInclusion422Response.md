# ProveInclusion422Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**reason** | **str** | The reason why the bundle could not be generated. | 
**log_id** | **str** | Represents a supported hash. | 
**root** | **str** | Represents a supported hash. | 
**found** | **str** | Represents a supported hash. | 
**message** | **str** | The failure error message. | 

## Example

```python
from _warg_client.models.prove_inclusion422_response import ProveInclusion422Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProveInclusion422Response from a JSON string
prove_inclusion422_response_instance = ProveInclusion422Response.from_json(json)
# print the JSON string representation of the object
print ProveInclusion422Response.to_json()

# convert the object into a dict
prove_inclusion422_response_dict = prove_inclusion422_response_instance.to_dict()
# create an instance of ProveInclusion422Response from a dict
prove_inclusion422_response_from_dict = ProveInclusion422Response.from_dict(prove_inclusion422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


