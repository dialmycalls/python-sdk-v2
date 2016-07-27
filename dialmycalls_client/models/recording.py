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


class Recording(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, type=None, seconds=None, url=None, processed=None, created_at=None, updated_at=None):
        """
        Recording - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'seconds': 'int',
            'url': 'str',
            'processed': 'bool',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'seconds': 'seconds',
            'url': 'url',
            'processed': 'processed',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._name = name
        self._type = type
        self._seconds = seconds
        self._url = url
        self._processed = processed
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this Recording.
        Unique identifier for this recording.

        :return: The id of this Recording.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Recording.
        Unique identifier for this recording.

        :param id: The id of this Recording.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Recording.
        The recording name.

        :return: The name of this Recording.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Recording.
        The recording name.

        :param name: The name of this Recording.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Recording.
        The recording type. Options: text or sound

        :return: The type of this Recording.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Recording.
        The recording type. Options: text or sound

        :param type: The type of this Recording.
        :type: str
        """

        self._type = type

    @property
    def seconds(self):
        """
        Gets the seconds of this Recording.
        The length of the recording.

        :return: The seconds of this Recording.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """
        Sets the seconds of this Recording.
        The length of the recording.

        :param seconds: The seconds of this Recording.
        :type: int
        """

        self._seconds = seconds

    @property
    def url(self):
        """
        Gets the url of this Recording.
        The URL of the recording file.

        :return: The url of this Recording.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Recording.
        The URL of the recording file.

        :param url: The url of this Recording.
        :type: str
        """

        self._url = url

    @property
    def processed(self):
        """
        Gets the processed of this Recording.
        Whether the recording is ready for use.

        :return: The processed of this Recording.
        :rtype: bool
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """
        Sets the processed of this Recording.
        Whether the recording is ready for use.

        :param processed: The processed of this Recording.
        :type: bool
        """

        self._processed = processed

    @property
    def created_at(self):
        """
        Gets the created_at of this Recording.
        When the recording was created.

        :return: The created_at of this Recording.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Recording.
        When the recording was created.

        :param created_at: The created_at of this Recording.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Recording.
        When the recording was last updated.

        :return: The updated_at of this Recording.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Recording.
        When the recording was last updated.

        :param updated_at: The updated_at of this Recording.
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
