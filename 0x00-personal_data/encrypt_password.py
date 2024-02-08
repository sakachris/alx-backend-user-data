#!/usr/bin/env python3
''' encrypt_password.py '''

import bcrypt


def hash_password(password: str) -> bytes:
    ''' hashing a password using bcrypt '''
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' checking if pasword is valid '''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
