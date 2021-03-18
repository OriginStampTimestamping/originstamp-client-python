# OriginStamp Python Client

[![Build Status](https://travis-ci.com/OriginStampTimestamping/originstamp-client-python.svg?token=pQzQz38vk99v2uad9eWc&branch=master)](https://travis-ci.com/OriginStampTimestamping/originstamp-client-python)

![](https://resources.originstamp.com/images/logo/originstamp-logo-landscape-mc_248x53.png)

> A Python implementation of the OriginStamp API. For endpoint documentation see [OriginStamp Documentation](https://docs.originstamp.com).

For more information, please visit [https://originstamp.com](https://originstamp.com).

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install the python package using the following command:

```sh
pip install originstamp-client==2.0.1
```

See [PyIP](https://pypi.org/project/originstamp-client/) for latest available version.

You may need to run `pip` with root permission.

Then import the package:
```python
import originstamp_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import originstamp_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.originstamp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeyApi* | [**get_api_key_usage**](docs/APIKeyApi.md#get_api_key_usage) | **GET** /v3/api_key/usage | Usage
*BulkApi* | [**create_bulk_timestamp**](docs/BulkApi.md#create_bulk_timestamp) | **POST** /v4/timestamp/bulk/create | Bulk Submission
*BulkApi* | [**get_seed_status**](docs/BulkApi.md#get_seed_status) | **GET** /v4/timestamp/status/seed/{seed_id} | Seed Status
*ProofApi* | [**get_proof**](docs/ProofApi.md#get_proof) | **POST** /v3/timestamp/proof/url | Proof
*SchedulerApi* | [**get_active_currencies**](docs/SchedulerApi.md#get_active_currencies) | **GET** /v3/currencies/get | Get active currencies
*TimestampApi* | [**create_timestamp**](docs/TimestampApi.md#create_timestamp) | **POST** /v4/timestamp/create | Submission
*TimestampApi* | [**get_hash_status**](docs/TimestampApi.md#get_hash_status) | **GET** /v4/timestamp/{hash_string} | Status
*TimestampApi* | [**get_seed_status**](docs/TimestampApi.md#get_seed_status) | **GET** /v4/timestamp/status/seed/{seed_id} | Seed Status
*WebhookApi* | [**get_webhook_status**](docs/WebhookApi.md#get_webhook_status) | **POST** /v3/webhook/information | Webhook
*WebhookApi* | [**register_webhook_notification**](docs/WebhookApi.md#register_webhook_notification) | **POST** /v3/webhook/register | Webhook
*WebhookApi* | [**trigger_timestamp_webhook**](docs/WebhookApi.md#trigger_timestamp_webhook) | **POST** /v3/webhook/start | Dev


## Documentation For Models

 - [CurrencyModel](docs/CurrencyModel.md)
 - [DefaultOfDownloadLinkResponse](docs/DefaultOfDownloadLinkResponse.md)
 - [DefaultOfListOfCurrencyModel](docs/DefaultOfListOfCurrencyModel.md)
 - [DefaultOfTimestampData](docs/DefaultOfTimestampData.md)
 - [DefaultOfTimestampResponse](docs/DefaultOfTimestampResponse.md)
 - [DefaultOfVoid](docs/DefaultOfVoid.md)
 - [DefaultOfWebhookResponse](docs/DefaultOfWebhookResponse.md)
 - [DefaultOfstring](docs/DefaultOfstring.md)
 - [DefaultUsageResponse](docs/DefaultUsageResponse.md)
 - [DownloadLinkResponse](docs/DownloadLinkResponse.md)
 - [ManualWebhookRequest](docs/ManualWebhookRequest.md)
 - [Notification](docs/Notification.md)
 - [ProofRequest](docs/ProofRequest.md)
 - [TimestampBulkRequest](docs/TimestampBulkRequest.md)
 - [TimestampData](docs/TimestampData.md)
 - [TimestampRequest](docs/TimestampRequest.md)
 - [TimestampResponse](docs/TimestampResponse.md)
 - [UsageResponse](docs/UsageResponse.md)
 - [WebhookRequest](docs/WebhookRequest.md)
 - [WebhookResponse](docs/WebhookResponse.md)


## API Key Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

mail@originstamp.com

