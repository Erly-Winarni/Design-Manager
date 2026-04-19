from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.jwt_handler import verify_token

class JWTBearer(HTTPBearer):

    def __init__(self, auto_error=True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:
            if credentials.scheme != "Bearer":
                raise HTTPException(status_code=403, detail="Invalid scheme")
            
            verify_token(credentials.credentials)
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid token")