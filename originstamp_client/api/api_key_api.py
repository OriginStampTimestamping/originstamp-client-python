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


class APIKeyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_api_key_usage(self, authorization, **kwargs):  # noqa: E501
        """Usage  # noqa: E501

        With this interface you can receive the current usage of your API key. The usage statistic refers to the associated account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_key_usage(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :return: DefaultUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_api_key_usage_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_api_key_usage_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def get_api_key_usage_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Usage  # noqa: E501

        With this interface you can receive the current usage of your API key. The usage statistic refers to the associated account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_api_key_usage_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: A valid API key is essential for authorization to handle the request. (required)
        :return: DefaultUsageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
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
        auth_settings = ['API Key Authorization']  # noqa: E501

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
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
