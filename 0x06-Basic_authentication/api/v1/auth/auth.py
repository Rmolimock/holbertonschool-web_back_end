#!/usr/bin/env python3

"""
This module contains one class, Auth
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if path is an exception and does not require authentication
        """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if not isinstance(path, str):
            raise TypeError('path must be a string')
        for excluded in excluded_paths:
            if excluded.endswith("*"):
                excluded = excluded[:-1]
                if path.startswith(excluded):
                    return False
            if path == excluded or path in excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ return the authorization value of the request """
        if not request or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ return None for now """
        return None

    def session_cookie(self, request=None):
        """ return the cookie value from a request """
        if not request:
            return None
        from os import getenv
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name, None)
