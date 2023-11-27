from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import copy


class RequestValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if not self.is_request_type_allowed(request):
            return JSONResponse(
                status_code=405,
                content={"detail": "Only POST requests are allowed."},
            )
        if not self.is_endpoint_allowed(request):
            return JSONResponse(
                status_code=404,
                content={"detail": "Endpoint not allowed."},
            )
        return await call_next(request)

    def is_endpoint_allowed(self, request: Request):

        return request.url.path == "/upload"

    def is_request_type_allowed(self, request: Request):
        return request.method == "POST"
