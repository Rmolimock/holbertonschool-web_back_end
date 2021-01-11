#!/usr/bin/env python3

"""
This module is for session exp auth which tracks sess timestamp
"""

from os import getenv
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ This module is for session exp auth which tracks sess timestamp """
    def __init__(self):
        """ This module is for session exp auth which tracks timestamp """
        try:
            session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """ This module is for session exp auth which tracks timestamp """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_dict = {}
        session_dict['created_at'] = datetime.now()
        session_dict['user_id'] = user_id
        SessionExpAuth.user_id_by_session_id[session_id] = session_dict
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ This module is for session exp auth which tracks timestamp """
        if not session_id:
            return None
        if session_id not in self.user_id_by_session_id:
            return None
        if 'user_id' not in SessionExpAuth.user_id_by_session_id[session_id]:
            user_id = None
        else:
            user_id = SessionExpAuth.user_id_by_session_id[session_id]['user_id']
        if self.session_duration <= 0:
            return user_id
        u_id = SessionExpAuth.user_id_by_session_id[session_id]
        if 'created_at' not in u_id:
            return None
        created = SessionExpAuth.user_id_by_session_id[session_id]['created_at']
        if created + timedelta(seconds=self.session_duration) < datetime.now():
            return None
        return user_id
