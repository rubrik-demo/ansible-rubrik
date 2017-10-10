# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QstarLocationSummary(Model):
    """QstarLocationSummary.

    :param id: QStar archival location identifier
    :type id: str
    :param definition: Details of the QStar archival location
    :type definition: :class:`QstarLocationDefinition
     <rubriklib_int.models.QstarLocationDefinition>`
    """

    _validation = {
        'id': {'required': True},
        'definition': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'definition': {'key': 'definition', 'type': 'QstarLocationDefinition'},
    }

    def __init__(self, id, definition):
        self.id = id
        self.definition = definition
