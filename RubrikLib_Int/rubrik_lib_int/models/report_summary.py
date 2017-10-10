# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .report_create import ReportCreate


class ReportSummary(ReportCreate):
    """ReportSummary.

    :param name: The name of the report.
    :type name: str
    :param report_template: The template this report is based on. Possible
     values include: 'ProtectionTasksDetails', 'ProtectionTasksSummary',
     'SystemCapacity', 'SlaComplianceSummary'
    :type report_template: str or :class:`enum <rubriklib_int.models.enum>`
    :param id: ID of the report.
    :type id: str
    :param report_type: Type of the report. Possible values include: 'Canned',
     'Custom'
    :type report_type: str or :class:`enum <rubriklib_int.models.enum>`
    :param update_status: The most recent update status of this report. NOTE:
     This field is likely to change
    :type update_status: str
    """

    _validation = {
        'name': {'required': True},
        'report_template': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'report_template': {'key': 'reportTemplate', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'report_type': {'key': 'reportType', 'type': 'str'},
        'update_status': {'key': 'updateStatus', 'type': 'str'},
    }

    def __init__(self, name, report_template, id=None, report_type=None, update_status=None):
        super(ReportSummary, self).__init__(name=name, report_template=report_template)
        self.id = id
        self.report_type = report_type
        self.update_status = update_status
