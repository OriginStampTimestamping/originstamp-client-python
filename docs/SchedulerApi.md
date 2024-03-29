# originstamp_client.SchedulerApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_currencies**](SchedulerApi.md#get_active_currencies) | **GET** /v3/currencies/get | Get active currencies


# **get_active_currencies**
> DefaultOfListOfCurrencyModel get_active_currencies(authorization)

Get active currencies

Returns an array with all active currencies.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.SchedulerApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.

try:
    # Get active currencies
    api_response = api_instance.get_active_currencies(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerApi->get_active_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 

### Return type

[**DefaultOfListOfCurrencyModel**](DefaultOfListOfCurrencyModel.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

