#!/usr/bin/env python3
"""BasicAuth authentication module"""

import base64
from .auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class for managing Basic Authentication

    Methods:
        extract_base64_authorization_header(authorization_header: str
            ) -> str: Extracts the Base64 part of the Authorization
            header
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the 'authorization' header
        for Basic Auth

        Args:
            authorization_header (str): Authorization header value

        Returns:
            str: The Base64 encoded part of the 'Authorization' header or
            None if invalid
        """
        if not authorization_header or not isinstance(
            authorization_header, str
                ) or not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Extracts the Base64 part of the 'authorization' header
        for Basic Auth and decodes it

        Args:
            authorization_header (str): Authorization header value

        Returns:
            str: The Base64 encoded part of the 'Authorization' header or
            None if invalid
        """
        if not base64_authorization_header or not isinstance(
            base64_authorization_header, str
        ):
            return None

        try:
            decoded_auth = base64.b64decode(base64_authorization_header)
            return decoded_auth.decode(encoding='utf-8')
        except Exception:
            return None
