# coding: utf-8

"""
    DialMyCalls API

    The DialMyCalls API

    OpenAPI spec version: 2.0.1
    Contact: support@dialmycalls.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Incomingtext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, from_number=None, to_number=None, message=None, created_at=None, updated_at=None):
        """
        Incomingtext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'from_number': 'str',
            'to_number': 'str',
            'message': 'str',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'from_number': 'from_number',
            'to_number': 'to_number',
            'message': 'message',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._from_number = from_number
        self._to_number = to_number
        self._message = message
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this Incomingtext.
        Unique identifier for this text.

        :return: The id of this Incomingtext.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Incomingtext.
        Unique identifier for this text.

        :param id: The id of this Incomingtext.
        :type: str
        """

        self._id = id

    @property
    def from_number(self):
        """
        Gets the from_number of this Incomingtext.
        The phone number the text message was sent from.

        :return: The from_number of this Incomingtext.
        :rtype: str
        """
        return self._from_number

    @from_number.setter
    def from_number(self, from_number):
        """
        Sets the from_number of this Incomingtext.
        The phone number the text message was sent from.

        :param from_number: The from_number of this Incomingtext.
        :type: str
        """

        self._from_number = from_number

    @property
    def to_number(self):
        """
        Gets the to_number of this Incomingtext.
        The phone number the text message was sent to.

        :return: The to_number of this Incomingtext.
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """
        Sets the to_number of this Incomingtext.
        The phone number the text message was sent to.

        :param to_number: The to_number of this Incomingtext.
        :type: str
        """

        self._to_number = to_number

    @property
    def message(self):
        """
        Gets the message of this Incomingtext.
        The text message that was sent.  This data is URL encoded.

        :return: The message of this Incomingtext.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Incomingtext.
        The text message that was sent.  This data is URL encoded.

        :param message: The message of this Incomingtext.
        :type: str
        """

        self._message = message

    @property
    def created_at(self):
        """
        Gets the created_at of this Incomingtext.
        When the text message was created.

        :return: The created_at of this Incomingtext.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Incomingtext.
        When the text message was created.

        :param created_at: The created_at of this Incomingtext.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Incomingtext.
        When the text message was last updated.

        :return: The updated_at of this Incomingtext.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Incomingtext.
        When the text message was last updated.

        :param updated_at: The updated_at of this Incomingtext.
        :type: str
        """

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other