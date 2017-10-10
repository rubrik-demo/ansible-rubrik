# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BaseGuestCredentialDetail(Model):
    """BaseGuestCredentialDetail.

    :param username:
    :type username: str
    """

    _validation = {
        'username': {'required': True},
    }

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
    }

    def __init__(self, username):
        self.username = username
