# originstamp_client.TimestampApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_timestamp**](TimestampApi.md#create_timestamp) | **POST** /v3/timestamp/create | Submission
[**get_api_key_usage**](TimestampApi.md#get_api_key_usage) | **GET** /v3/api_key/usage | Usage
[**get_hash_status**](TimestampApi.md#get_hash_status) | **GET** /v3/timestamp/{hash_string} | Status
[**get_proof**](TimestampApi.md#get_proof) | **POST** /v3/timestamp/proof | Proof
[**trigger_timestamp_webhook**](TimestampApi.md#trigger_timestamp_webhook) | **POST** /v3/webhook/start | Dev


# **create_timestamp**
> DefaultTimestampResponse create_timestamp(authorization, timestamp_request)

Submission

You can submit your hash with this function. If your api key is valid, your hash is added to batch and is scheduled for timestamping. If the hash already exists, the created flag in the response is set to false and the notification(s) of the current request will be totally ignored. You are also able to submit additional information, such as comment or notification credentials. Once a hash is successfully created for a certain crypto-currency, we can notify your desired target with the timestamp information (POST Request). The webhook is triggered as soon as the tamper-proof timestamp with the selected crypto currency has been created. Additionally, it is possible to include a preprint URL in the hash submission. Before the generation of the timestamp hash you can create a random UUID Version 4 and include https://originstamp.com/u/UUID where UUID is your UUID e.g. in a document you want to timestamp. In the preprint URL field you include your UUID and then it is possible to verify the timestamp within the document (or whatever). 

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

[**DefaultTimestampResponse**](DefaultTimestampResponse.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_usage**
> DefaultUsageResponse get_api_key_usage(authorization)

Usage

With this interface you can receive the current api usage.

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

try:
    # Usage
    api_response = api_instance.get_api_key_usage(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->get_api_key_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 

### Return type

[**DefaultUsageResponse**](DefaultUsageResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hash_status**
> DefaultTimestampResponse get_hash_status(authorization, hash_string)

Status

The request returns information of a certain hash read from the URL parameter. The input parameter is a hash in hex representation. Field \"created\" always set to false.

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

[**DefaultTimestampResponse**](DefaultTimestampResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_proof**
> str get_proof(authorization, proof_request)

Proof

This request can be used to proof a submission of a hash. This interface is required to request the evidence. With the help of this proof the verification of a timestamp independent from OriginStamp is necessary. A guide for the verification can be found herehttps://github.com/OriginStampTimestamping/originstamp-verification . Usually, the proof should be requested for each transferred hash and kept with the timestamped data so that an independent verification of the timestamp is possible at any time. As input, the used currency, the hash string and the type of proof is required. Then a file with the information for the submission proof will be returned. If the hash was submitted in an API version lower than 3, a XML file containing the essential information of the Merkle Tree will be returned. Otherwise, the seed file will be returned.  The file name can be found in the header of the response. An example could look like this: content-disposition: attachment; filename=\"certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf\" A sample XML file can be found here https://originstamp.org/assets/proof/proof_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.xml and a sample PDF can be found here https://originstamp.org/assets/proof/certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf .

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
proof_request = originstamp_client.ProofRequest() # ProofRequest | Information needed to return the hash status information.

try:
    # Proof
    api_response = api_instance.get_proof(authorization, proof_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->get_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **proof_request** | [**ProofRequest**](ProofRequest.md)| Information needed to return the hash status information. | 

### Return type

**str**

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_timestamp_webhook**
> Defaultstring trigger_timestamp_webhook(authorization, webhook_request)

Dev

With this interface you can trigger manual webhook to see how a webhooks looks like. Please use a hash, that was already timestamped before such as https://originstamp.org/s/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 . Usually, the webhook is triggered as soon as the tamper-proof time stamp with the selected crypto currency has been created.

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
webhook_request = originstamp_client.WebhookRequest() # WebhookRequest | DTO for webhook request.

try:
    # Dev
    api_response = api_instance.trigger_timestamp_webhook(authorization, webhook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimestampApi->trigger_timestamp_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **webhook_request** | [**WebhookRequest**](WebhookRequest.md)| DTO for webhook request. | 

### Return type

[**Defaultstring**](Defaultstring.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

