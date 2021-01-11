#!/usr/bin/env python3

"""
This module handles the SessionAuth class
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """ SessionAuth class """
    user_id_by_session_id = {}

    def __init__(self):
        """ init """
        pass

    def create_session(self, user_id: str = None) -> str:
        """ create session id, given a user id """
        from uuid import uuid4
        if not user_id or not type(user_id) == str:
            return None
        self.id = str(uuid4())
        SessionAuth.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return user id given a session id """
        if not session_id or not type(session_id) == str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ return user object from given session id """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id:
            return User.get(user_id)
        return None

    def destroy_session(self, request=None):
        """ destroy current session """
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id:
            del SessionAuth.user_id_by_session_id[session_id]
            return True
        return False
