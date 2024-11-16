#!/usr/bin/env python3
""" script to manage API authentication """

from flask import request
from typing import List, TypeVar


class Auth:
    """Manages API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns false (args will be used later)"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """Returns None as request will be flask object"""s
        return request
    
    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None as request will be flask object"""
        return request