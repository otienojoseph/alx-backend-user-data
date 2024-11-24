#!/usr/bin/env python3
"""BasicAuth authentication module"""

import base64
from typing import TypeVar

from models.base import Base
from models.user import User
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
            decode_base64_authorization_header (str): Authorization
            header value

        Returns:
            str: The Base64 decoded 'Authorization' header or None if
            invalid
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

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        Extracts the Base64 part of the 'authorization' header
        for Basic Auth and decodes it

        Args:
            decoded_base64_authorization_header (str): Decoded
            authorization header value

        Returns:
            str: The user email and password from the Base64 decoded
            value or None if invalid
        """
        if not decoded_base64_authorization_header or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        user_email = decoded_base64_authorization_header.split(':')[0]
        user_pass = decoded_base64_authorization_header[len(user_email)+1:]
        return user_email, user_pass

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
        Method returns the 'User' instance based on his email and pass

        Args:
            user_email (str): User email
            user_pwd (str): User password

        Returns:
            User instance based on user email and password
        """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None

        # search for User by search
        try:
            users = User.search({"email": user_email})
            if not users or len(users) == 0:
                return None
        except Exception as e:
            return None

        # return None if user_pwd != instance password
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user
