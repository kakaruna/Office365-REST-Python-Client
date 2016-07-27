from client.runtime.action_type import ActionType
from client.runtime.odata.odata_path_parser import ODataPathParser


class ClientQuery(object):
    """Client query"""

    def __init__(self, url, action_type=ActionType.ReadEntry, parameters=None):
        self.__url = url
        self.__actionType = action_type
        self.__payload = parameters

    @staticmethod
    def create_entry_query(parent_client_object, parameters):
        qry = ClientQuery(parent_client_object.url, ActionType.CreateEntry, parameters)
        return qry

    @staticmethod
    def update_entry_query(client_object):
        qry = ClientQuery(client_object.url, ActionType.UpdateEntry, client_object.to_json())
        return qry

    @staticmethod
    def service_operation_query(client_object, action_type, method_name, method_params=None):
        url = client_object.url + ODataPathParser.from_method(method_name, method_params)
        qry = ClientQuery(url, action_type)
        return qry

    @staticmethod
    def delete_entry_query(client_object):
        qry = ClientQuery(client_object.url, ActionType.DeleteEntry)
        return qry

    @property
    def url(self):
        return self.__url

    @property
    def action_type(self):
        return self.__actionType

    @property
    def payload(self):
        return self.__payload

    @property
    def id(self):
        return id(self)

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return self.url == other.url
