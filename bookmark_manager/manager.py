# -*- coding: utf-8 -*-

# ========================================
# External imports
# ========================================


# ========================================
# Internal imports
# ========================================


# ========================================
# Constants
# ========================================
    

# ========================================
# Variables
# ========================================
    

# ========================================
# Classes
# ========================================

# Create a manager for bookmarks
class BookmarkManager:
    """Create a manager for bookmarks

    Attributes
    ----------
    None

    Methods
    -------
    add_bookmark(self, url)
      Add bookmark

    Notes
    -----
    None

    Examples
    --------
    >>> None
    """

    def __init__(self) -> None:
        self.urls = []

    def add_bookmark(self, url) -> None:
        self.urls.append(url)

    def get_bookmarks(self) -> list:
        return self.urls

# ========================================
# Functions
# ========================================
