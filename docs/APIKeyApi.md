# originstamp_client.APIKeyApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key_usage**](APIKeyApi.md#get_api_key_usage) | **GET** /v3/api_key/usage | Usage


# **get_api_key_usage**
> DefaultUsageResponse get_api_key_usage(authorization)

Usage

With this interface you can receive the current usage of your API key. The usage statistic refers to the associated account.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.APIKeyApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.

try:
    # Usage
    api_response = api_instance.get_api_key_usage(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeyApi->get_api_key_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 

### Return type

[**DefaultUsageResponse**](DefaultUsageResponse.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

