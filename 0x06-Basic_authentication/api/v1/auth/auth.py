#!/usr/bin/env python3

"""
This module contains one class, SessionAuth
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def __init__(self):
        """ empty init for now """
        pass

    def create_session(self, user_id: str = None) -> str:
        """ create and return a session id, given a user id """
        from uuid import uuid4
        if not user_id or not type(user_id) == str:
            return None
        self.id = str(uuid4())
        # stored as {session_id: user_id, session_id: user_id}
        SessionAuth.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return a user id given a session id """
        if not session_id or not type(session_id) == str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ return a user object from given session id """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ logout from current session """
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del SessionAuth.user_id_by_session_id[session_id]
        return True
Russells-MacBook-Pro:v1 russellmolimock$ cat auth/auth.py 
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
