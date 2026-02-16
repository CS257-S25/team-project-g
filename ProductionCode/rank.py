"""Module containing a Rank class for representing the number of bans a item has"""


class Rank:
    """Rank class to represent the number of bans a item has"""

    def __init__(self, name, bans: int):
        self.name = name
        self.bans = bans

    def __str__(self) -> str:
        """Method for displaying rank
        Args: None
        Returns:
            string with name and number of bans formatted
        """
        return f"{self.name}: {self.bans}"

    def get_name(self):
        """Get method for name instance attribute
        Args: None
        Returns:
            name object
        """
        return self.name

    def get_bans(self):
        """Get method for bans instance attribute
        Args: None
        Returns:
           bans int
        """
        return self.bans
