#!/usr/bin/env python3
''' api/v1/auth/basic_auth.py '''

from .auth import Auth
import base64


class BasicAuth(Auth):
    ''' Inheriting Auth class '''
    def extract_base64_authorization_header(
            self, authorization_header: str,
            ) -> str:
        ''' extract_base64 auth header '''
        if authorization_header is None or not isinstance(
                authorization_header, str
        ):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' decode base64 '''
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' returns email and password '''
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
