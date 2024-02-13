#!/usr/bin/env python3
''' auth.py '''

from typing import List, TypeVar
from flask import request
import fnmatch


class Auth:
    ''' Auth class '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        '''if path.endswith('/'):
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path == excluded_path:
                return False'''

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                # Remove trailing slash for comparison
                excluded_path = excluded_path[:-1]
            if path.endswith('/'):
                # Remove trailing slash for comparison
                path = path[:-1]
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the request."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user based on the request."""
        return None
