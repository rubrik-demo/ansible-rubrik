# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IpmiUpdate(Model):
    """IpmiUpdate.

    :param password: IPMI password, password should be 5-20 characters.
    :type password: str
    :param access:
    :type access: :class:`IpmiAccessUpdate
     <rubriklib_int.models.IpmiAccessUpdate>`
    """

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'access': {'key': 'access', 'type': 'IpmiAccessUpdate'},
    }

    def __init__(self, password=None, access=None):
        self.password = password
        self.access = access
