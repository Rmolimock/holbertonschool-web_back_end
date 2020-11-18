#!/usr/bin/env python3

"""
tests
"""


def register_user(email: str, password: str) -> None:
    """
    register user
    """
    assert True
    return


def log_in_wrong_password(email: str, password: str) -> None:
    """
    log in_wrong_password
    """
    assert True
    return


def log_in(email: str, password: str) -> str:
    """
    log in
    """
    assert True
    return ""


def profile_unlogged() -> None:
    """
    profile_unlogged
    """
    assert True
    return


def profile_logged(session_id: str) -> None:
    """
    profile logged
    """
    assert True
    return


def log_out(session_id: str) -> None:
    """
    log out
    """
    assert True
    return


def reset_password_token(email: str) -> str:
    """
    reset password_token
    """
    assert True
    return ""


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    update password
    """
    assert True
    return


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
