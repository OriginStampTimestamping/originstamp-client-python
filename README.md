# OriginStamp Python Client

[![Build Status](https://travis-ci.com/OriginStampTimestamping/originstamp-client-python.svg?token=pQzQz38vk99v2uad9eWc&branch=master)](https://travis-ci.com/OriginStampTimestamping/originstamp-client-python)

![](https://originstamp.com/assets/images/logo/logo_simple_small.png)

> A Python implementation of the OriginStamp API. For endpoint documentation see [OriginStamp Documentation](https://doc.originstamp.org)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://originstamp.com](https://originstamp.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install the python package using the following command:

```sh
pip install originstamp-client==1.0.0
```

See [PyIP](https://pypi.org/project/originstamp-client/) for latest available version.

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
*SchedulerApi* | [**get_next_scheduling_time**](docs/SchedulerApi.md#get_next_scheduling_time) | **POST** /v3/submission/times | NextSchedule
*TimestampApi* | [**create_timestamp**](docs/TimestampApi.md#create_timestamp) | **POST** /v3/timestamp/create | Submission
*TimestampApi* | [**get_api_key_usage**](docs/TimestampApi.md#get_api_key_usage) | **GET** /v3/api_key/usage | Usage
*TimestampApi* | [**get_hash_status**](docs/TimestampApi.md#get_hash_status) | **GET** /v3/timestamp/{hash_string} | Status
*TimestampApi* | [**get_proof**](docs/TimestampApi.md#get_proof) | **POST** /v3/timestamp/proof | Proof
*TimestampApi* | [**trigger_timestamp_webhook**](docs/TimestampApi.md#trigger_timestamp_webhook) | **POST** /v3/webhook/start | Dev


## Documentation For Models

 - [DefaultSchedulerResponse](docs/DefaultSchedulerResponse.md)
 - [DefaultTimestampResponse](docs/DefaultTimestampResponse.md)
 - [DefaultUsageResponse](docs/DefaultUsageResponse.md)
 - [Defaultstring](docs/Defaultstring.md)
 - [Notification](docs/Notification.md)
 - [ProofRequest](docs/ProofRequest.md)
 - [ResponseEntity](docs/ResponseEntity.md)
 - [SchedulerRequest](docs/SchedulerRequest.md)
 - [SchedulerResponse](docs/SchedulerResponse.md)
 - [TimestampData](docs/TimestampData.md)
 - [TimestampRequest](docs/TimestampRequest.md)
 - [TimestampResponse](docs/TimestampResponse.md)
 - [UsageResponse](docs/UsageResponse.md)
 - [WebhookRequest](docs/WebhookRequest.md)


## Author

mail@originstamp.com

