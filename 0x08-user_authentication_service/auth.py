#!/usr/bin/env python3
""" auth class """

import bcrypt


def _hash_password(password: str) -> str:
    """ create a salted hash for the password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
