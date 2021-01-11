#!/usr/bin/env python3
"""
user session module docstring for holberton checker
"""
from models.base import Base


class UserSession(Base):
    """ user session module docstring for holberton checker """
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.session_id = kwargs.get('session_id')
        self.user_id = kwargs.get('user_id')
