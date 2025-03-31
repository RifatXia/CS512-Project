import connexion
import six

from swagger_server import util


def table_extract_post(body=None):  # noqa: E501
    """Upload a table image and get recognized result.

    Upload a table image. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
