# coding: utf-8

"""
    OriginStamp Client

    OpenAPI spec version: 3.0
    OriginStamp Documentation: https://docs.originstamp.com
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ManualWebhookRequest(object):
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
        'hash': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'hash': 'hash',
        'webhook_url': 'webhook_url'
    }

    def __init__(self, hash=None, webhook_url=None):  # noqa: E501
        """ManualWebhookRequest - a model defined in Swagger"""  # noqa: E501

        self._hash = None
        self._webhook_url = None
        self.discriminator = None

        self.hash = hash
        self.webhook_url = webhook_url

    @property
    def hash(self):
        """Gets the hash of this ManualWebhookRequest.  # noqa: E501

        SHA-256 Hash in Hex representation.  # noqa: E501

        :return: The hash of this ManualWebhookRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ManualWebhookRequest.

        SHA-256 Hash in Hex representation.  # noqa: E501

        :param hash: The hash of this ManualWebhookRequest.  # noqa: E501
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def webhook_url(self):
        """Gets the webhook_url of this ManualWebhookRequest.  # noqa: E501

        The target URL to which we send the timestamp information of the requested hash via a post request.  # noqa: E501

        :return: The webhook_url of this ManualWebhookRequest.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this ManualWebhookRequest.

        The target URL to which we send the timestamp information of the requested hash via a post request.  # noqa: E501

        :param webhook_url: The webhook_url of this ManualWebhookRequest.  # noqa: E501
        :type: str
        """
        if webhook_url is None:
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501

        self._webhook_url = webhook_url

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
        if issubclass(ManualWebhookRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ManualWebhookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
