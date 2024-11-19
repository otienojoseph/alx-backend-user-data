#!/usr/bin/env python3
"""BasicAuth authentication module"""

from auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class for managing Basic Authentication

    Methods:
        extract_base64_authorization_header(authorization_header: str
        ) -> Extracts the Base64 part of the Authorization header
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
