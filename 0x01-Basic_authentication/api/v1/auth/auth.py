#!/usr/bin/env python3
""" script to manage API authentication """

from flask import request
from api.v1.views.users import User
from typing import List, TypeVar


class Auth:
    """Manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authorization is required for a certain path,
           for now, always return False
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request.
           For now always return None.
        """
        return None
    
    def current_user(self, request=None) -> TypeVar['User']:
        """Retrieves the current user based on the request.
           For now, always return None
        """
        return None