#!/usr/bin/env python3
""" simple db class """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import TypeVar
from user import Base, User


class DB:
    """ db class """

    def __init__(self):
        """ init """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ create a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """ add a user to the db """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs: dict) -> TypeVar('User'):
        """ find user by attribute """
        return self._session.query(User).filter_by(**kwargs).one()

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """ update user attrs """
        user = self.find_user_by(id=user_id)
        for attr in kwargs:
            if hasattr(user, attr):
                user.attr = kwargs[attr]
            else:
                raise ValueError
        self._session.commit()
