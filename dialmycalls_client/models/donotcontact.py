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


class Donotcontact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, phone=None, type=None, created_at=None, updated_at=None):
        """
        Donotcontact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'phone': 'str',
            'type': 'str',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'phone': 'phone',
            'type': 'type',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._phone = phone
        self._type = type
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this Donotcontact.
        Unique identifier for this group.

        :return: The id of this Donotcontact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Donotcontact.
        Unique identifier for this group.

        :param id: The id of this Donotcontact.
        :type: str
        """

        self._id = id

    @property
    def phone(self):
        """
        Gets the phone of this Donotcontact.
        The phone number that is on the donotcontact list.

        :return: The phone of this Donotcontact.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Donotcontact.
        The phone number that is on the donotcontact list.

        :param phone: The phone of this Donotcontact.
        :type: str
        """

        self._phone = phone

    @property
    def type(self):
        """
        Gets the type of this Donotcontact.
        The type of the donotcontact. Options: call, text

        :return: The type of this Donotcontact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Donotcontact.
        The type of the donotcontact. Options: call, text

        :param type: The type of this Donotcontact.
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """
        Gets the created_at of this Donotcontact.
        When the donotcontact was created.

        :return: The created_at of this Donotcontact.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Donotcontact.
        When the donotcontact was created.

        :param created_at: The created_at of this Donotcontact.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Donotcontact.
        When the donotcontact was last updated.

        :return: The updated_at of this Donotcontact.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Donotcontact.
        When the donotcontact was last updated.

        :param updated_at: The updated_at of this Donotcontact.
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
