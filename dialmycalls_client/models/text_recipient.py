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


class TextRecipient(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, firstname=None, lastname=None, email=None, phone=None, status=None, successful=None):
        """
        TextRecipient - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str',
            'phone': 'str',
            'status': 'str',
            'successful': 'bool'
        }

        self.attribute_map = {
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email',
            'phone': 'phone',
            'status': 'status',
            'successful': 'successful'
        }

        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._phone = phone
        self._status = status
        self._successful = successful

    @property
    def firstname(self):
        """
        Gets the firstname of this TextRecipient.
        The recipient's first name.

        :return: The firstname of this TextRecipient.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this TextRecipient.
        The recipient's first name.

        :param firstname: The firstname of this TextRecipient.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this TextRecipient.
        The recipient's last name.

        :return: The lastname of this TextRecipient.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this TextRecipient.
        The recipient's last name.

        :param lastname: The lastname of this TextRecipient.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this TextRecipient.
        The recipient's email address.

        :return: The email of this TextRecipient.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this TextRecipient.
        The recipient's email address.

        :param email: The email of this TextRecipient.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """
        Gets the phone of this TextRecipient.
        The recipient's phone number.

        :return: The phone of this TextRecipient.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this TextRecipient.
        The recipient's phone number.

        :param phone: The phone of this TextRecipient.
        :type: str
        """

        self._phone = phone

    @property
    def status(self):
        """
        Gets the status of this TextRecipient.
        Status of the text. Options: delivered, undeliverable, enroute, unknown, non_mobile, queued

        :return: The status of this TextRecipient.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TextRecipient.
        Status of the text. Options: delivered, undeliverable, enroute, unknown, non_mobile, queued

        :param status: The status of this TextRecipient.
        :type: str
        """

        self._status = status

    @property
    def successful(self):
        """
        Gets the successful of this TextRecipient.
        Whether the text was successful or not.

        :return: The successful of this TextRecipient.
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this TextRecipient.
        Whether the text was successful or not.

        :param successful: The successful of this TextRecipient.
        :type: bool
        """

        self._successful = successful

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
