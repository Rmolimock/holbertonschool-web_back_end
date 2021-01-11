#!/usr/bin/env python3

"""
auth class module docstring for holberton checker
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    auth class module docstring for holberton checker
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ auth class module docstring for holberton checker
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
            if path in excluded or path == excluded:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ rauth class module docstring for holberton checker """
        if request and "Authorization" in request.headers:
            return request.headers.get("Authorization")
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ auth class module docstring for holberton checker """
        return None

    def session_cookie(self, request=None):
        """ auth class module docstring for holberton checker """
        from os import getenv
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookies.get(session_name, None)
        return None
