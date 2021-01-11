#!/usr/bin/env python3

"""
This module contains one class, SessionAuth
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth verifies session_id against those stored in storage """
    def create_session(self, user_id=None):
        """ create a session and store session_id in storage """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return
        user = UserSession(user_id=user_id, session_id=session_id)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ get user_id associated with session_id from storage """
        if not session_id:
            return None
        try:
            user_list = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_list:
            return None
        from datetime import datetime, timedelta
        start = timedelta(seconds=self.session_duration)
        if datetime.now() > user_list[0].created_at + start:
            return None
        return user_list[0].user_id

    def destroy_session(self, request=None):
        """ destroy session of given user_id in request """
        from os import getenv
        if not request:
            return None
        session_id = self.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        user = UserSession.search(user_id)
        if not user:
            return None
        user.remove()
