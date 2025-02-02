# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from GeorisqueApi.models.geo_json_object import GeoJsonObject  # noqa: F401,E501

class Point(GeoJsonObject):
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
        'coordinates': 'LngLatAlt'
    }
    if hasattr(GeoJsonObject, "swagger_types"):
        swagger_types.update(GeoJsonObject.swagger_types)

    attribute_map = {
        'coordinates': 'coordinates'
    }
    if hasattr(GeoJsonObject, "attribute_map"):
        attribute_map.update(GeoJsonObject.attribute_map)

    def __init__(self, coordinates=None, *args, **kwargs):  # noqa: E501
        """Point - a model defined in Swagger"""  # noqa: E501
        self._coordinates = None
        self.discriminator = None
        if coordinates is not None:
            self.coordinates = coordinates
        GeoJsonObject.__init__(self, *args, **kwargs)

    @property
    def coordinates(self):
        """Gets the coordinates of this Point.  # noqa: E501


        :return: The coordinates of this Point.  # noqa: E501
        :rtype: LngLatAlt
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Point.


        :param coordinates: The coordinates of this Point.  # noqa: E501
        :type: LngLatAlt
        """

        self._coordinates = coordinates

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
        if issubclass(Point, dict):
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
        if not isinstance(other, Point):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
