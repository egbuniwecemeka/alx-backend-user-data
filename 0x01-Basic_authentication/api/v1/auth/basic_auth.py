#!/usr/bin/env python3
"""BasicAuth Class"""

from api.v1.auth.auth import Auth
import base64


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


    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        
        if not isinstance(base64_authorization_header, str):
            return None
        
        try:
            # Decode Base64 header
            decoded_bytes = base64.base64decode(base64_authorization_header)

            # Return decoded byte as UTF8 string
            return decoded_bytes.decode('utf8')
        except(base64.binascii.Error, UnicodeDecodeError):
            # Return None if decoding fails
            return None
