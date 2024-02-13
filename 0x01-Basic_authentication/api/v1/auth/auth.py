#!/usr/bin/env python3
''' auth.py '''

from typing import List, TypeVar
from flask import request


class Auth:
    ''' Auth class '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        return False

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user based on the request."""
        return None
