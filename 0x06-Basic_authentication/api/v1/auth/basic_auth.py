#!/usr/bin/env python3

"""
Basic Auth class module docstring for holberton checker
"""

import base64
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """ Basic Auth class module docstring for holberton checker
    """
    def __init__(self):
        pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Basic Auth class module docstring for holberton checker
        """
        a = authorization_header
        if not a or not isinstance(a, str) or not a.startswith("Basic "):
            return
        return a[6:]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """ Basic Auth class module docstring for holberton checker """
        auth = b64_auth_header
        if not isinstance(auth, str) or not auth:
            return None
        try:
            return base64.b64decode(auth.encode('utf-8')).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, enc_b64_auth_headr: str) -> (str, str):
        """ Basic Auth class module docstring for holberton checker """
        auth = enc_b64_auth_headr
        bad_return = (None, None)
        if not isinstance(auth, str) or not auth or ':' not in auth:
            return bad_return
        email = auth.split(':')[0]
        password = auth.split(':', 1)[1]
        return (email, password)

    def user_object_from_credentials(self, e: str, p: str) -> TypeVar('User'):
        """ Basic Auth class module docstring for holberton checker """
        if not e or not isinstance(e, str):
            return None
        if not p or not isinstance(p, str):
            return None
        # ret None if no user with that email
        # same if that user's pwd is wrong
        try:
            email = {"email": e}
            from models.user import User
            user = User.search(email)
        except Exception:
            return None
        if not user:
            return None
        if user[0].is_valid_password(p):
            return user[0]
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Basic Auth class module docstring for holberton checker """
        auth = self.authorization_header(request)
        base = self.extract_base64_authorization_header(auth)
        decode = self.decode_base64_authorization_header(base)
        user = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(user[0], user[1])
