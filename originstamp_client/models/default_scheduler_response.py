# coding: utf-8

"""
    OriginStamp Documentation

    <br/>The following documentation describes the API v3 for OriginStamp. With this documentation you are able to try out the different requests and see the responses. For the authorization, add your API key to the Authorization header of your request.<br/><h2>Invoice</h2><p>The invoice is based on your individual usage. The following table illustrates the request types, that are billed in credits.</p><table><tr><th>Request Type</th><th>Condition</th><th>Credits</th><tr><td style='border-bottom-style:solid; border-color: #c0c0c0;'></td><tr><th>Submission</th><th>create timestamp</th><th>1 Credit</th><tr><th>Submission</th><th>timestamp already exists</th><th>0.3 Credits</th><tr><th>Status</th><th>no timestamp information available</th><th>0.1 Credit</th><tr><th>Status</th><th>timestamp information</th><th>0.3 Credits</th><tr><th>Proof</th><th>no proof available</th><th>0.1 Credits</th><tr><th>Proof</th><th>merkle tree as proof</th><th>3 Credits</th><tr><th>Proof</th><th>seed as proof</th><th>3 Credits</th><tr><th>Proof</th><th>PDF Certificate</th><th>5 Credits</th><tr><th>Notification</th><th>webhook notification</th><th>1.5 Credits</th><tr><th>Notification</th><th>mail notification</th><th>5 Credits</th><tr><th>Notification</th><th>trigger webhook</th><th>5 0.3</th></table><br/><h2>Common Problems</h2><ul><li>Make sure you set the Authorization with your API key</li><li>If a cloudflare error occurs, please set a custom UserAgent header.</li><li>Please have a look at the models below to find out what each field means.</li></ul>  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from originstamp_client.models.scheduler_response import SchedulerResponse  # noqa: F401,E501


class DefaultSchedulerResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'SchedulerResponse',
        'error_code': 'int',
        'error_message': 'str'
    }

    attribute_map = {
        'data': 'data',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, data=None, error_code=None, error_message=None):  # noqa: E501
        """DefaultSchedulerResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    @property
    def data(self):
        """Gets the data of this DefaultSchedulerResponse.  # noqa: E501

        Generic response object which contains the response data, e.g. timestamp information.  # noqa: E501

        :return: The data of this DefaultSchedulerResponse.  # noqa: E501
        :rtype: SchedulerResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DefaultSchedulerResponse.

        Generic response object which contains the response data, e.g. timestamp information.  # noqa: E501

        :param data: The data of this DefaultSchedulerResponse.  # noqa: E501
        :type: SchedulerResponse
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def error_code(self):
        """Gets the error_code of this DefaultSchedulerResponse.  # noqa: E501

        Contains the error of the request. If the error code is 0, everything is fine.  # noqa: E501

        :return: The error_code of this DefaultSchedulerResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DefaultSchedulerResponse.

        Contains the error of the request. If the error code is 0, everything is fine.  # noqa: E501

        :param error_code: The error_code of this DefaultSchedulerResponse.  # noqa: E501
        :type: int
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this DefaultSchedulerResponse.  # noqa: E501

        Contains the error message, that possibly occurred. If it is empty, everything is fine.  # noqa: E501

        :return: The error_message of this DefaultSchedulerResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DefaultSchedulerResponse.

        Contains the error message, that possibly occurred. If it is empty, everything is fine.  # noqa: E501

        :param error_message: The error_message of this DefaultSchedulerResponse.  # noqa: E501
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

        self._error_message = error_message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DefaultSchedulerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
