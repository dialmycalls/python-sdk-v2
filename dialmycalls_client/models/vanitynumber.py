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


class Vanitynumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, phone=None, status=None, minutes_used=None, minutes_allowed=None, voicemails_new=None, voicemails_old=None, created_at=None, updated_at=None):
        """
        Vanitynumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'phone': 'str',
            'status': 'str',
            'minutes_used': 'float',
            'minutes_allowed': 'float',
            'voicemails_new': 'int',
            'voicemails_old': 'int',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'phone': 'phone',
            'status': 'status',
            'minutes_used': 'minutes_used',
            'minutes_allowed': 'minutes_allowed',
            'voicemails_new': 'voicemails_new',
            'voicemails_old': 'voicemails_old',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._phone = phone
        self._status = status
        self._minutes_used = minutes_used
        self._minutes_allowed = minutes_allowed
        self._voicemails_new = voicemails_new
        self._voicemails_old = voicemails_old
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this Vanitynumber.
        Unique identifier for this group.

        :return: The id of this Vanitynumber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vanitynumber.
        Unique identifier for this group.

        :param id: The id of this Vanitynumber.
        :type: str
        """

        self._id = id

    @property
    def phone(self):
        """
        Gets the phone of this Vanitynumber.
        The phone number.

        :return: The phone of this Vanitynumber.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Vanitynumber.
        The phone number.

        :param phone: The phone of this Vanitynumber.
        :type: str
        """

        self._phone = phone

    @property
    def status(self):
        """
        Gets the status of this Vanitynumber.
        The status of the vanity number. Options: active, onhold, billingdecline, pendingdelete

        :return: The status of this Vanitynumber.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Vanitynumber.
        The status of the vanity number. Options: active, onhold, billingdecline, pendingdelete

        :param status: The status of this Vanitynumber.
        :type: str
        """

        self._status = status

    @property
    def minutes_used(self):
        """
        Gets the minutes_used of this Vanitynumber.
        The amount of minutes used since last billing.

        :return: The minutes_used of this Vanitynumber.
        :rtype: float
        """
        return self._minutes_used

    @minutes_used.setter
    def minutes_used(self, minutes_used):
        """
        Sets the minutes_used of this Vanitynumber.
        The amount of minutes used since last billing.

        :param minutes_used: The minutes_used of this Vanitynumber.
        :type: float
        """

        self._minutes_used = minutes_used

    @property
    def minutes_allowed(self):
        """
        Gets the minutes_allowed of this Vanitynumber.
        The amount of minutes included with the vanity number before billed additionally.

        :return: The minutes_allowed of this Vanitynumber.
        :rtype: float
        """
        return self._minutes_allowed

    @minutes_allowed.setter
    def minutes_allowed(self, minutes_allowed):
        """
        Sets the minutes_allowed of this Vanitynumber.
        The amount of minutes included with the vanity number before billed additionally.

        :param minutes_allowed: The minutes_allowed of this Vanitynumber.
        :type: float
        """

        self._minutes_allowed = minutes_allowed

    @property
    def voicemails_new(self):
        """
        Gets the voicemails_new of this Vanitynumber.
        The amount of voicemails that have not been downloaded.

        :return: The voicemails_new of this Vanitynumber.
        :rtype: int
        """
        return self._voicemails_new

    @voicemails_new.setter
    def voicemails_new(self, voicemails_new):
        """
        Sets the voicemails_new of this Vanitynumber.
        The amount of voicemails that have not been downloaded.

        :param voicemails_new: The voicemails_new of this Vanitynumber.
        :type: int
        """

        self._voicemails_new = voicemails_new

    @property
    def voicemails_old(self):
        """
        Gets the voicemails_old of this Vanitynumber.
        The amount of voicemails that have been downloaded.

        :return: The voicemails_old of this Vanitynumber.
        :rtype: int
        """
        return self._voicemails_old

    @voicemails_old.setter
    def voicemails_old(self, voicemails_old):
        """
        Sets the voicemails_old of this Vanitynumber.
        The amount of voicemails that have been downloaded.

        :param voicemails_old: The voicemails_old of this Vanitynumber.
        :type: int
        """

        self._voicemails_old = voicemails_old

    @property
    def created_at(self):
        """
        Gets the created_at of this Vanitynumber.
        When the keyword was created.

        :return: The created_at of this Vanitynumber.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Vanitynumber.
        When the keyword was created.

        :param created_at: The created_at of this Vanitynumber.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Vanitynumber.
        When the keyword was last updated.

        :return: The updated_at of this Vanitynumber.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Vanitynumber.
        When the keyword was last updated.

        :param updated_at: The updated_at of this Vanitynumber.
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
