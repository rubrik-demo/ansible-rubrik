# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GatewayInfo(Model):
    """GatewayInfo.

    :param address:
    :type address: str
    :param ports:
    :type ports: list of int
    """

    _validation = {
        'address': {'required': True},
        'ports': {'required': True},
    }

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'ports': {'key': 'ports', 'type': '[int]'},
    }

    def __init__(self, address, ports):
        self.address = address
        self.ports = ports
