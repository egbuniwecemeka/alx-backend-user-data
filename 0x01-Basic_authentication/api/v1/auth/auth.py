#!/usr/bin/env python3
""" script to manage API authentication """

from flask import request
from api.v1.views.users import User
from typing import List, Optional


class Auth:
    """Manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authorization is required for a certain path,
           Returns:
                True if path isn;t in excluded_paths
                True if path is None
                True if excluded_paths is None
                False if path is in excluded_paths

        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        # Check if path ends with /, otherwise add it
        if not path.endswith('/'):
            path += '/'
        
        # Now, checked path is checked to see if its in the extended_path
        for slashed_path in excluded_paths:
            if slashed_path.endswith('/') and path == excluded_paths:
                return False


    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request.
           For now always return None.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> Optional['User']:
        """Retrieves the current user based on the request.
           For now, always return None
        """
        return None
