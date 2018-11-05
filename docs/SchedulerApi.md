# originstamp_client.SchedulerApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_next_scheduling_time**](SchedulerApi.md#get_next_scheduling_time) | **POST** /v3/submission/times | NextSchedule


# **get_next_scheduling_time**
> DefaultSchedulerResponse get_next_scheduling_time(authorization, scheduler_request)

NextSchedule

Get the next scheduling time for hash submissions to the blockchain.

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
scheduler_request = originstamp_client.SchedulerRequest() # SchedulerRequest | Request DTO for next schedules.

try:
    # NextSchedule
    api_response = api_instance.get_next_scheduling_time(authorization, scheduler_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerApi->get_next_scheduling_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **scheduler_request** | [**SchedulerRequest**](SchedulerRequest.md)| Request DTO for next schedules. | 

### Return type

[**DefaultSchedulerResponse**](DefaultSchedulerResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

