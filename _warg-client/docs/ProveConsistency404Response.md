# ProveConsistency404Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**type** | **str** | The type of entity that was not found. | 
**id** | **int** | The identifier of the entity that was not found. | 

## Example

```python
from _warg_client.models.prove_consistency404_response import ProveConsistency404Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProveConsistency404Response from a JSON string
prove_consistency404_response_instance = ProveConsistency404Response.from_json(json)
# print the JSON string representation of the object
print ProveConsistency404Response.to_json()

# convert the object into a dict
prove_consistency404_response_dict = prove_consistency404_response_instance.to_dict()
# create an instance of ProveConsistency404Response from a dict
prove_consistency404_response_from_dict = ProveConsistency404Response.from_dict(prove_consistency404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


