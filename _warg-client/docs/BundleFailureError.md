# BundleFailureError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The HTTP status code for the error. | 
**reason** | **str** | The reason why the bundle could not be generated. | 
**message** | **str** | The failure error message. | 

## Example

```python
from _warg_client.models.bundle_failure_error import BundleFailureError

# TODO update the JSON string below
json = "{}"
# create an instance of BundleFailureError from a JSON string
bundle_failure_error_instance = BundleFailureError.from_json(json)
# print the JSON string representation of the object
print BundleFailureError.to_json()

# convert the object into a dict
bundle_failure_error_dict = bundle_failure_error_instance.to_dict()
# create an instance of BundleFailureError from a dict
bundle_failure_error_from_dict = BundleFailureError.from_dict(bundle_failure_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


