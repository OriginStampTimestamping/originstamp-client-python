# originstamp_client.WebhookApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_webhook_status**](WebhookApi.md#get_webhook_status) | **POST** /v3/webhook/information | Webhook
[**register_webhook_notification**](WebhookApi.md#register_webhook_notification) | **POST** /v3/webhook/register | Webhook
[**trigger_timestamp_webhook**](WebhookApi.md#trigger_timestamp_webhook) | **POST** /v3/webhook/start | Dev


# **get_webhook_status**
> DefaultOfWebhookResponse get_webhook_status(authorization, webhook_request)

Webhook

RESTful interface to receive the status of a webhook. Based on the input parameters (target URL, hash and currency), we look up the most recent entry in the notification queue.This method is intended to support the webhook integration.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.WebhookApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
webhook_request = originstamp_client.WebhookRequest() # WebhookRequest | DTO for registering webhook information.

try:
    # Webhook
    api_response = api_instance.get_webhook_status(authorization, webhook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_webhook_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **webhook_request** | [**WebhookRequest**](WebhookRequest.md)| DTO for registering webhook information. | 

### Return type

[**DefaultOfWebhookResponse**](DefaultOfWebhookResponse.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook_notification**
> DefaultOfVoid register_webhook_notification(authorization, webhook_request)

Webhook

Method which allows a subscription for a webhook notification. If this method is called, a new entry is added to notification queue that is triggered as soon as a tamper-proof timestamp or the hash is created. An empty data payload means that the entry was created successfully.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.WebhookApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
webhook_request = originstamp_client.WebhookRequest() # WebhookRequest | DTO for querying webhook information.

try:
    # Webhook
    api_response = api_instance.register_webhook_notification(authorization, webhook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->register_webhook_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **webhook_request** | [**WebhookRequest**](WebhookRequest.md)| DTO for querying webhook information. | 

### Return type

[**DefaultOfVoid**](DefaultOfVoid.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_timestamp_webhook**
> DefaultOfstring trigger_timestamp_webhook(authorization, manual_webhook_request)

Dev

With this interface you can trigger manual webhook to see how a webhook looks like. Please use a hash, that was already timestamped before such as https://redir.originstamp.com/hash/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 . Usually, the webhook is triggered as soon as the tamper-proof time stamp with the selected crypto currency has been created.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.WebhookApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
manual_webhook_request = originstamp_client.ManualWebhookRequest() # ManualWebhookRequest | DTO for webhook request.

try:
    # Dev
    api_response = api_instance.trigger_timestamp_webhook(authorization, manual_webhook_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->trigger_timestamp_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **manual_webhook_request** | [**ManualWebhookRequest**](ManualWebhookRequest.md)| DTO for webhook request. | 

### Return type

[**DefaultOfstring**](DefaultOfstring.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

