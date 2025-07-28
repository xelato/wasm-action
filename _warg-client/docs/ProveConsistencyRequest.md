# ProveConsistencyRequest

A request to prove the consistency of the registry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | The starting log length. | 
**to** | **int** | The ending log length. | 

## Example

```python
from _warg_client.models.prove_consistency_request import ProveConsistencyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProveConsistencyRequest from a JSON string
prove_consistency_request_instance = ProveConsistencyRequest.from_json(json)
# print the JSON string representation of the object
print ProveConsistencyRequest.to_json()

# convert the object into a dict
prove_consistency_request_dict = prove_consistency_request_instance.to_dict()
# create an instance of ProveConsistencyRequest from a dict
prove_consistency_request_from_dict = ProveConsistencyRequest.from_dict(prove_consistency_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


