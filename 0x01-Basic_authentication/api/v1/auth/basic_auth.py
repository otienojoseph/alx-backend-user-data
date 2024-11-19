#!/usr/bin/env python3
"""Basic Auth module"""

from auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """
        Method that returns the Base64 part of the 'authorization'
        header for Basic Authentication

        Args:
            authorization_header (str): Authorization header

        Returns:
            The Base64 part of the 'Authorization' header for
            basic authentication
        """
        if not authorization_header or not isinstance(
            authorization_header, str
                ) or not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split()[1]
