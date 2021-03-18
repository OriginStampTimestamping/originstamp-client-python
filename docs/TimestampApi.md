# originstamp_client.TimestampApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_timestamp**](TimestampApi.md#create_timestamp) | **POST** /v4/timestamp/create | Submission
[**get_hash_status**](TimestampApi.md#get_hash_status) | **GET** /v4/timestamp/{hash_string} | Status
[**get_seed_status**](TimestampApi.md#get_seed_status) | **GET** /v4/timestamp/status/seed/{seed_id} | Seed Status


# **create_timestamp**
> DefaultOfTimestampResponse create_timestamp(authorization, timestamp_request)

Submission

With this interface you can submit your hash. If your API key is valid, your hash is added  seeds and scheduled for timestamping. You are also able to submit additional information, such as a comment or notification target. If the hash already exists, the 'created' field in the response is set to 'false' and any notification(s) for this hash will be ignored. To later query the status of the hash for a certain blockchain you can use the 'seed_id' field of its inner timestamp structure. This field can be used to query the timestamping status of the selected seed. This is recommended if a large number of hashes were transmitted in a certain time frame. Once a hash is successfully created for a certain crypto currency, we can notify your desired target with the timestamp information (via POST Request). A webhook is triggered as soon as the tamper-proof timestamp with the selected crypto currency has been created. 

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.TimestampApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
timestamp_request = originstamp_client.TimestampRequest() # TimestampRequest | DTO for the hash submission. Add all relevant information concerning your hash submission.

try:
    # Submission
    api_response = api_instance.create_timestamp(authorization, timestamp_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->create_timestamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **timestamp_request** | [**TimestampRequest**](TimestampRequest.md)| DTO for the hash submission. Add all relevant information concerning your hash submission. | 

### Return type

[**DefaultOfTimestampResponse**](DefaultOfTimestampResponse.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hash_status**
> DefaultOfTimestampResponse get_hash_status(authorization, hash_string)

Status

This interface returns information of a certain hash read from the URL path. If the status of several hashes is to be checked, it is preferable to use the seed status interface. This reduces the required requests and can be tailored to a desired blockchain. All 'created' fields are always set to false for a status request.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.TimestampApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
hash_string = 'hash_string_example' # str | The hash in string representation.

try:
    # Status
    api_response = api_instance.get_hash_status(authorization, hash_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->get_hash_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **hash_string** | **str**| The hash in string representation. | 

### Return type

[**DefaultOfTimestampResponse**](DefaultOfTimestampResponse.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seed_status**
> DefaultOfTimestampData get_seed_status(authorization, seed_id)

Seed Status

With this interface you can request the status for a certain seed. This is used when checking the status of previously submitted hashes and avoids sending individual status requests for each hash.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.TimestampApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
seed_id = 'seed_id_example' # str | ID of the timestamp seed

try:
    # Seed Status
    api_response = api_instance.get_seed_status(authorization, seed_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->get_seed_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **seed_id** | **str**| ID of the timestamp seed | 

### Return type

[**DefaultOfTimestampData**](DefaultOfTimestampData.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

