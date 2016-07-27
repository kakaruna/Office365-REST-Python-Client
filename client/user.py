from client.group_collection import GroupCollection
from client.principal import Principal
from client.runtime.resource_path_entry import ResourcePathEntry


class User(Principal):
    """Represents a user in Microsoft SharePoint Foundation. A user is a type of SP.Principal."""

    @property
    def groups(self):
        """Gets a collection of group objects that represents all of the groups for the user."""
        if self.is_property_available('Groups'):
            return self.properties['Groups']
        else:
            return GroupCollection(self.context, ResourcePathEntry(self.context, self.resource_path, "Groups"))
