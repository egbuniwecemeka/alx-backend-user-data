#!/usr/bin/env python3
"""BasicAuth Class"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        # Extract and return the basic part after `Basic `
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 header
            decoded_bytes = base64.b64decode(base64_authorization_header)

            # Return decoded byte as UTF8 string
            return decoded_bytes.decode('utf8')
        except(base64.binascii.Error, UnicodeDecodeError):
            # Return None if decoding fails
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_email, user_password = decoded_base64_authorization_header.split(
            ':', 1
        )
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns the user instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Using the search method to find users email
        users = User.search({'email':user_email})

        # If no user is found, return None
        if not users or len(users) == 0:
            return None

        # Assuming the first matched value is used
        user = users[0]

        # Verify the password with password validating method
        if not user.is_valid_password(user_pwd):
            return None

        # Return user instance if all checks passes
        return user
