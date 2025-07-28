# IncorrectProofError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**reason** | **str** | The reason why the bundle could not be generated. | 
**root** | **str** | Represents a supported hash. | 
**found** | **str** | Represents a supported hash. | 

## Example

```python
from _warg_client.models.incorrect_proof_error import IncorrectProofError

# TODO update the JSON string below
json = "{}"
# create an instance of IncorrectProofError from a JSON string
incorrect_proof_error_instance = IncorrectProofError.from_json(json)
# print the JSON string representation of the object
print IncorrectProofError.to_json()

# convert the object into a dict
incorrect_proof_error_dict = incorrect_proof_error_instance.to_dict()
# create an instance of IncorrectProofError from a dict
incorrect_proof_error_from_dict = IncorrectProofError.from_dict(incorrect_proof_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


