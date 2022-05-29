# -*- coding: utf-8 -*-

# ========================================
# External imports
# ========================================


# ========================================
# Internal imports
# ========================================

import bookmark_manager

# ========================================
# Constants
# ========================================
    

# ========================================
# Variables
# ========================================
    

# ========================================
# Classes
# ========================================

class TestApi:

    def test_add_bookmark(self):
        BOOKMARK_TO_BE_ADDED = "https://www.youtube.com/watch?v=MPpPu6c8wsM"
        manager              = bookmark_manager.BookmarkManager()
        manager.add_bookmark(BOOKMARK_TO_BE_ADDED)
        assert BOOKMARK_TO_BE_ADDED in manager.get_bookmarks()

# ========================================
# Functions
# ========================================

