#!/usr/bin/env python3

"""
This module contains one class, SessionAuth
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Session Expiration Class """
    def __init__(self):
        """ init """
        try:
            session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """ create a session with expiration """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {}
        session_dictionary['user_id'] = user_id
        session_dictionary['created_at'] = datetime.now()
        SessionExpAuth.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ return the user associated with a given session """
        if not session_id:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if 'user_id' not in SessionExpAuth.user_id_by_session_id[session_id]:
            u_id = None
        else:
            u_id = SessionExpAuth.user_id_by_session_id[session_id]['user_id']
        if self.session_duration <= 0:
            return u_id
        c = 'created_at'
        if c not in SessionExpAuth.user_id_by_session_id[session_id]:
            return None
        start = SessionExpAuth.user_id_by_session_id[session_id]['created_at']
        if datetime.now() > start + timedelta(seconds=self.session_duration):
            return None
        return u_id
