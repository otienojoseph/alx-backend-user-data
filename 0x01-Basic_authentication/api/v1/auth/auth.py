#!/usr/bin/env python3
"""Authentication file"""

from typing import TypeVar, List
from flask import request


class Auth:
    """
    Class to manage API Authentication

    Methods:
        require_auth(path, excluded_paths):
            Determines if path requires authentication
        authorization_header(request):
            Retrieves the authorization header from request
        current_user(request):
            Retrieves the current user

    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if path requires authentication

        Args:
            path (str): The path to check
            excluded_paths (List[str]): A list of paths that dont require
                authentication

        Returns:
            bool: False (default behaviour for now)
        """
        if not path or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for exluded in excluded_paths:
            if exluded == path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authentication header from request

        Args:
            request: The flask request object

        Returns:
            str: None (default behaviour for now)
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user

        Args:
            request: The flask request object

        Returns:
            TypeVar('User'): None (default behaviour for now)
        """
        return None
