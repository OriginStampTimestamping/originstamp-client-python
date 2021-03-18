# originstamp_client.BulkApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bulk_timestamp**](BulkApi.md#create_bulk_timestamp) | **POST** /v4/timestamp/bulk/create | Bulk Submission
[**get_seed_status**](BulkApi.md#get_seed_status) | **GET** /v4/timestamp/status/seed/{seed_id} | Seed Status


# **create_bulk_timestamp**
> list[DefaultOfTimestampResponse] create_bulk_timestamp(authorization, timestamp_bulk_request)

Bulk Submission

With this interface you can submit multiple hashes at once. If your API key is valid, your hashes are added to seeds and scheduled for timestamping. You are also able to submit additional information with every hash, such as a comment or notification target. If the hash already exists, the 'created' field in the response is set to 'false' and the notification(s) of the corresponding hash will be ignored. To later query the status of any hash for a certain blockchain you can use the 'seed_id' field of its inner timestamp structure. This field can be used to query the timestamping status of the selected seed. This is recommended if a large number of hashes were transmitted in a certain time frame. Once a hash is successfully created for a certain crypto currency, we can notify your desired target with the timestamp information (via POST Request). A webhook for a submitted hash is triggered as soon as the tamper-proof timestamp with the selected crypto currency has been created. 

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.BulkApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
timestamp_bulk_request = originstamp_client.TimestampBulkRequest() # TimestampBulkRequest | DTO for the bulk hash submission. Add all relevant information concerning your hash submissions.

try:
    # Bulk Submission
    api_response = api_instance.create_bulk_timestamp(authorization, timestamp_bulk_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->create_bulk_timestamp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **timestamp_bulk_request** | [**TimestampBulkRequest**](TimestampBulkRequest.md)| DTO for the bulk hash submission. Add all relevant information concerning your hash submissions. | 

### Return type

[**list[DefaultOfTimestampResponse]**](DefaultOfTimestampResponse.md)

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
api_instance = originstamp_client.BulkApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
seed_id = 'seed_id_example' # str | ID of the timestamp seed

try:
    # Seed Status
    api_response = api_instance.get_seed_status(authorization, seed_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->get_seed_status: %s\n" % e)
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

