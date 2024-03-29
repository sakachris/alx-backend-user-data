#!/usr/bin/env python3
''' api/v1/auth/session_auth.py '''

from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    ''' Ingeriting Auth class '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' creating a session '''
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' returns user id based on session id '''
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        ''' returns current user '''
        if request is None:
            return None
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        if user_id:
            return User.get(user_id)
        return None

    def destroy_session(self, request=None) -> bool:
        ''' deletes the user session / logout '''
        if request is None:
            return False

        session_id_cookie = self.session_cookie(request)
        if session_id_cookie is None:
            return False

        user_id = self.user_id_for_session_id(session_id_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id_cookie]
        return True
