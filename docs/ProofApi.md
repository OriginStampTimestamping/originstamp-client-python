# originstamp_client.ProofApi

All URIs are relative to *https://api.originstamp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_proof**](ProofApi.md#get_proof) | **POST** /v3/timestamp/proof/url | Proof


# **get_proof**
> DefaultOfDownloadLinkResponse get_proof(authorization, proof_request_url)

Proof

Generates the download URL for Proof (Seed / Merkle Tree). This interface must be used to obtain the proof or certificate of your tamper-proof timestamp. The parameters are as follows: Cryptocurrency (e.g., Bitcoin, Ethereum,..), type of evidence (e.g., certificate, merkle tree) and the associated hash. The entries are analyzed, e.g., whether a valid timestamp exists for the hash. Then the URL and the filename are returned, with which your proof can be saved. Please note that the download link is only valid for 5 minutes. When using cURL to fetch the proof with the download link make sure to specify \"application/octet-stream\" in the \"Accept\" header.

### Example
```python
from __future__ import print_function
import time
import originstamp_client
from originstamp_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = originstamp_client.ProofApi()
authorization = 'authorization_example' # str | A valid API key is essential for authorization to handle the request.
proof_request_url = originstamp_client.ProofRequest() # ProofRequest | Information needed to return the proof.

try:
    # Proof
    api_response = api_instance.get_proof(authorization, proof_request_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProofApi->get_proof: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A valid API key is essential for authorization to handle the request. | 
 **proof_request_url** | [**ProofRequest**](ProofRequest.md)| Information needed to return the proof. | 

### Return type

[**DefaultOfDownloadLinkResponse**](DefaultOfDownloadLinkResponse.md)

### Authorization

[API Key Authorization](../README.md#API Key Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

