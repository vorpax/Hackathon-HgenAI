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

class PaginatedResponseTim(object):
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
        'results': 'int',
        'page': 'int',
        'total_pages': 'int',
        'data': 'list[Tim]',
        'response_code': 'int',
        'message': 'str',
        'next': 'str',
        'previous': 'str'
    }

    attribute_map = {
        'results': 'results',
        'page': 'page',
        'total_pages': 'total_pages',
        'data': 'data',
        'response_code': 'response_code',
        'message': 'message',
        'next': 'next',
        'previous': 'previous'
    }

    def __init__(self, results=None, page=None, total_pages=None, data=None, response_code=None, message=None, next=None, previous=None):  # noqa: E501
        """PaginatedResponseTim - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self._page = None
        self._total_pages = None
        self._data = None
        self._response_code = None
        self._message = None
        self._next = None
        self._previous = None
        self.discriminator = None
        if results is not None:
            self.results = results
        if page is not None:
            self.page = page
        if total_pages is not None:
            self.total_pages = total_pages
        if data is not None:
            self.data = data
        if response_code is not None:
            self.response_code = response_code
        if message is not None:
            self.message = message
        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous

    @property
    def results(self):
        """Gets the results of this PaginatedResponseTim.  # noqa: E501

        Le nombre total de résultats  # noqa: E501

        :return: The results of this PaginatedResponseTim.  # noqa: E501
        :rtype: int
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedResponseTim.

        Le nombre total de résultats  # noqa: E501

        :param results: The results of this PaginatedResponseTim.  # noqa: E501
        :type: int
        """

        self._results = results

    @property
    def page(self):
        """Gets the page of this PaginatedResponseTim.  # noqa: E501

        Le numéro de page actuelle  # noqa: E501

        :return: The page of this PaginatedResponseTim.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PaginatedResponseTim.

        Le numéro de page actuelle  # noqa: E501

        :param page: The page of this PaginatedResponseTim.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def total_pages(self):
        """Gets the total_pages of this PaginatedResponseTim.  # noqa: E501

        Le nombre total de pages  # noqa: E501

        :return: The total_pages of this PaginatedResponseTim.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PaginatedResponseTim.

        Le nombre total de pages  # noqa: E501

        :param total_pages: The total_pages of this PaginatedResponseTim.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def data(self):
        """Gets the data of this PaginatedResponseTim.  # noqa: E501

        Le tableau contenant la réponse du endpoint  # noqa: E501

        :return: The data of this PaginatedResponseTim.  # noqa: E501
        :rtype: list[Tim]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PaginatedResponseTim.

        Le tableau contenant la réponse du endpoint  # noqa: E501

        :param data: The data of this PaginatedResponseTim.  # noqa: E501
        :type: list[Tim]
        """

        self._data = data

    @property
    def response_code(self):
        """Gets the response_code of this PaginatedResponseTim.  # noqa: E501

        Le code HTTP de la réponse  # noqa: E501

        :return: The response_code of this PaginatedResponseTim.  # noqa: E501
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this PaginatedResponseTim.

        Le code HTTP de la réponse  # noqa: E501

        :param response_code: The response_code of this PaginatedResponseTim.  # noqa: E501
        :type: int
        """

        self._response_code = response_code

    @property
    def message(self):
        """Gets the message of this PaginatedResponseTim.  # noqa: E501

        Le message d'erreur si applicable  # noqa: E501

        :return: The message of this PaginatedResponseTim.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PaginatedResponseTim.

        Le message d'erreur si applicable  # noqa: E501

        :param message: The message of this PaginatedResponseTim.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def next(self):
        """Gets the next of this PaginatedResponseTim.  # noqa: E501

        Le lien vers la page de résultat suivante  # noqa: E501

        :return: The next of this PaginatedResponseTim.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PaginatedResponseTim.

        Le lien vers la page de résultat suivante  # noqa: E501

        :param next: The next of this PaginatedResponseTim.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this PaginatedResponseTim.  # noqa: E501

        Le lien vers la page de résultat précédente  # noqa: E501

        :return: The previous of this PaginatedResponseTim.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this PaginatedResponseTim.

        Le lien vers la page de résultat précédente  # noqa: E501

        :param previous: The previous of this PaginatedResponseTim.  # noqa: E501
        :type: str
        """

        self._previous = previous

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
        if issubclass(PaginatedResponseTim, dict):
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
        if not isinstance(other, PaginatedResponseTim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
