# ProveInclusionRequest

A request to prove the inclusion of log leafs in a checkpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_length** | **int** | The checkpoint log length to prove the inclusion for. | 
**leafs** | **List[int]** | The log leaf registry log index to prove the inclusion for. | 

## Example

```python
from warg_openapi.models.prove_inclusion_request import ProveInclusionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProveInclusionRequest from a JSON string
prove_inclusion_request_instance = ProveInclusionRequest.from_json(json)
# print the JSON string representation of the object
print ProveInclusionRequest.to_json()

# convert the object into a dict
prove_inclusion_request_dict = prove_inclusion_request_instance.to_dict()
# create an instance of ProveInclusionRequest from a dict
prove_inclusion_request_from_dict = ProveInclusionRequest.from_dict(prove_inclusion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


