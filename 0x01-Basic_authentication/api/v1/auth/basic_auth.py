#!/usr/bin/env python3
''' api/v1/auth/basic_auth.py '''

from .auth import Auth


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
