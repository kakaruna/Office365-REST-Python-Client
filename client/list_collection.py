from client.runtime.action_type import ActionType
from client.runtime.client_object_collection import ClientObjectCollection
from client.runtime.client_query import ClientQuery
from client.runtime.resource_path_service_operation import ResourcePathServiceOperation
from list import List


class ListCollection(ClientObjectCollection):
    """Lists collection"""

    def get_by_title(self, list_title):
        """Retrieve List client object by title"""
        return List(self.context,
                    ResourcePathServiceOperation(self.context, self.resource_path, "GetByTitle", [list_title]))

    def get_by_id(self, list_id):
        """Retrieve List client object by id"""
        return List(self.context,
                    ResourcePathServiceOperation(self.context, self.resource_path, "GetById", [list_id]))

    def ensure_site_assets_library(self):
        """Gets a list that is the default asset location for images or other files, which the users
        upload to their wiki pages."""
        list_site_assets = List(self.context)
        qry = ClientQuery.service_operation_query(self, ActionType.UpdateMethod, "ensuresiteassetslibrary")
        self.context.add_query(qry, list_site_assets)
        return list_site_assets

    def ensure_site_pages_library(self):
        """Gets a list that is the default location for wiki pages."""
        list_site_pages = List(self.context)
        qry = ClientQuery.service_operation_query(self, ActionType.UpdateMethod, "ensuresitepageslibrary")
        self.context.add_query(qry, list_site_pages)
        return list_site_pages

    def add(self, list_creation_information):
        """Creates a List resource"""
        list_new = List(self.context)
        qry = ClientQuery.create_entry_query(self, list_creation_information.payload)
        self.context.add_query(qry, list_new)
        self.add_child(list_new)
        return list_new
