# coding: utf-8

"""
    OriginStamp Client

    OpenAPI spec version: 3.0
    OriginStamp Documentation: https://docs.originstamp.com
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from originstamp_client.api_client import ApiClient


class TimestampApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_timestamp(self, authorization, timestamp_request, **kwargs):  # noqa: E501
        """Submission  # noqa: E501

        You can submit your hash with this function. If your api key is valid, your hash is added to batch and is scheduled for timestamping. If the hash already exists, the created flag in the response is set to false and the notification(s) of the current request will be totally ignored. You are also able to submit additional information, such as comment or notification credentials. Once a hash is successfully created for a certain crypto-currency, we can notify your desired target with the timestamp information (POST Request). The webhook is triggered as soon as the tamper-proof timestamp with the selected crypto currency has been created. Additionally, it is possible to include a preprint URL in the hash submission. Before the generation of the timestamp hash you can create a random UUID Version 4 and include https://originstamp.com/u/UUID where UUID is your UUID e.g. in a document you want to timestamp. In the preprint URL field you include your UUID and then it is possible to verify the timestamp within the document (or whatever).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_timestamp(authorization, timestamp_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param TimestampRequest timestamp_request: DTO for the hash submission. Add all relevant information concerning your hash submission. (required)
        :return: DefaultTimestampResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_timestamp_with_http_info(authorization, timestamp_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_timestamp_with_http_info(authorization, timestamp_request, **kwargs)  # noqa: E501
            return data

    def create_timestamp_with_http_info(self, authorization, timestamp_request, **kwargs):  # noqa: E501
        """Submission  # noqa: E501

        You can submit your hash with this function. If your api key is valid, your hash is added to batch and is scheduled for timestamping. If the hash already exists, the created flag in the response is set to false and the notification(s) of the current request will be totally ignored. You are also able to submit additional information, such as comment or notification credentials. Once a hash is successfully created for a certain crypto-currency, we can notify your desired target with the timestamp information (POST Request). The webhook is triggered as soon as the tamper-proof timestamp with the selected crypto currency has been created. Additionally, it is possible to include a preprint URL in the hash submission. Before the generation of the timestamp hash you can create a random UUID Version 4 and include https://originstamp.com/u/UUID where UUID is your UUID e.g. in a document you want to timestamp. In the preprint URL field you include your UUID and then it is possible to verify the timestamp within the document (or whatever).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_timestamp_with_http_info(authorization, timestamp_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param TimestampRequest timestamp_request: DTO for the hash submission. Add all relevant information concerning your hash submission. (required)
        :return: DefaultTimestampResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'timestamp_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_timestamp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_timestamp`")  # noqa: E501
        # verify the required parameter 'timestamp_request' is set
        if ('timestamp_request' not in params or
                params['timestamp_request'] is None):
            raise ValueError("Missing the required parameter `timestamp_request` when calling `create_timestamp`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'timestamp_request' in params:
            body_params = params['timestamp_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v3/timestamp/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultTimestampResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_api_key_usage(self, authorization, **kwargs):  # noqa: E501
        """Usage  # noqa: E501

        With this interface you can receive the current api usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_key_usage(authorization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :return: DefaultUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_api_key_usage_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_api_key_usage_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_api_key_usage_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Usage  # noqa: E501

        With this interface you can receive the current api usage.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_api_key_usage_with_http_info(authorization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :return: DefaultUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_api_key_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_api_key_usage`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v3/api_key/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultUsageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_hash_status(self, authorization, hash_string, **kwargs):  # noqa: E501
        """Status  # noqa: E501

        The request returns information of a certain hash read from the URL parameter. The input parameter is a hash in hex representation. Field \"created\" always set to false.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hash_status(authorization, hash_string, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param str hash_string: The hash in string representation. (required)
        :return: DefaultTimestampResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_hash_status_with_http_info(authorization, hash_string, **kwargs)  # noqa: E501
        else:
            (data) = self.get_hash_status_with_http_info(authorization, hash_string, **kwargs)  # noqa: E501
            return data

    def get_hash_status_with_http_info(self, authorization, hash_string, **kwargs):  # noqa: E501
        """Status  # noqa: E501

        The request returns information of a certain hash read from the URL parameter. The input parameter is a hash in hex representation. Field \"created\" always set to false.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_hash_status_with_http_info(authorization, hash_string, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param str hash_string: The hash in string representation. (required)
        :return: DefaultTimestampResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'hash_string']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hash_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_hash_status`")  # noqa: E501
        # verify the required parameter 'hash_string' is set
        if ('hash_string' not in params or
                params['hash_string'] is None):
            raise ValueError("Missing the required parameter `hash_string` when calling `get_hash_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hash_string' in params:
            path_params['hash_string'] = params['hash_string']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v3/timestamp/{hash_string}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DefaultTimestampResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_proof(self, authorization, proof_request, **kwargs):  # noqa: E501
        """Proof  # noqa: E501

        This request can be used to proof a submission of a hash. This interface is required to request the evidence. With the help of this proof the verification of a timestamp independent from OriginStamp is necessary. A guide for the verification can be found herehttps://github.com/OriginStampTimestamping/originstamp-verification . Usually, the proof should be requested for each transferred hash and kept with the timestamped data so that an independent verification of the timestamp is possible at any time. As input, the used currency, the hash string and the type of proof is required. Then a file with the information for the submission proof will be returned. If the hash was submitted in an API version lower than 3, a XML file containing the essential information of the Merkle Tree will be returned. Otherwise, the seed file will be returned.  The file name can be found in the header of the response. An example could look like this: content-disposition: attachment; filename=\"certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf\" A sample XML file can be found here https://originstamp.org/assets/proof/proof_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.xml and a sample PDF can be found here https://originstamp.org/assets/proof/certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_proof(authorization, proof_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param ProofRequest proof_request: Information needed to return the hash status information. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_proof_with_http_info(authorization, proof_request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_proof_with_http_info(authorization, proof_request, **kwargs)  # noqa: E501
            return data

    def get_proof_with_http_info(self, authorization, proof_request, **kwargs):  # noqa: E501
        """Proof  # noqa: E501

        This request can be used to proof a submission of a hash. This interface is required to request the evidence. With the help of this proof the verification of a timestamp independent from OriginStamp is necessary. A guide for the verification can be found herehttps://github.com/OriginStampTimestamping/originstamp-verification . Usually, the proof should be requested for each transferred hash and kept with the timestamped data so that an independent verification of the timestamp is possible at any time. As input, the used currency, the hash string and the type of proof is required. Then a file with the information for the submission proof will be returned. If the hash was submitted in an API version lower than 3, a XML file containing the essential information of the Merkle Tree will be returned. Otherwise, the seed file will be returned.  The file name can be found in the header of the response. An example could look like this: content-disposition: attachment; filename=\"certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf\" A sample XML file can be found here https://originstamp.org/assets/proof/proof_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.xml and a sample PDF can be found here https://originstamp.org/assets/proof/certificate_6d70a947e19398f1106ad70a60bd34a8305bdcb624b5b7d43782315517e79cad.pdf .  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_proof_with_http_info(authorization, proof_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param ProofRequest proof_request: Information needed to return the hash status information. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'proof_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_proof" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_proof`")  # noqa: E501
        # verify the required parameter 'proof_request' is set
        if ('proof_request' not in params or
                params['proof_request'] is None):
            raise ValueError("Missing the required parameter `proof_request` when calling `get_proof`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'proof_request' in params:
            body_params = params['proof_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v3/timestamp/proof', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trigger_timestamp_webhook(self, authorization, webhook_request, **kwargs):  # noqa: E501
        """Dev  # noqa: E501

        With this interface you can trigger manual webhook to see how a webhooks looks like. Please use a hash, that was already timestamped before such as https://originstamp.org/s/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 . Usually, the webhook is triggered as soon as the tamper-proof time stamp with the selected crypto currency has been created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_timestamp_webhook(authorization, webhook_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param WebhookRequest webhook_request: DTO for webhook request. (required)
        :return: Defaultstring
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.trigger_timestamp_webhook_with_http_info(authorization, webhook_request, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_timestamp_webhook_with_http_info(authorization, webhook_request, **kwargs)  # noqa: E501
            return data

    def trigger_timestamp_webhook_with_http_info(self, authorization, webhook_request, **kwargs):  # noqa: E501
        """Dev  # noqa: E501

        With this interface you can trigger manual webhook to see how a webhooks looks like. Please use a hash, that was already timestamped before such as https://originstamp.org/s/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 . Usually, the webhook is triggered as soon as the tamper-proof time stamp with the selected crypto currency has been created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.trigger_timestamp_webhook_with_http_info(authorization, webhook_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :param WebhookRequest webhook_request: DTO for webhook request. (required)
        :return: Defaultstring
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'webhook_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_timestamp_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `trigger_timestamp_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_request' is set
        if ('webhook_request' not in params or
                params['webhook_request'] is None):
            raise ValueError("Missing the required parameter `webhook_request` when calling `trigger_timestamp_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'webhook_request' in params:
            body_params = params['webhook_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v3/webhook/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Defaultstring',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
