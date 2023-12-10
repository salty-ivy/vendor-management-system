from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class HttpException(APIException):
    """
    Custom exception that returns an HTTP response
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Custom exception message"

    def __init__(self, detail=None, code=None):
        # override attributes with provided arguments
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.status_code = code

        # Call the response method to generate the response
        self.response()

    def response(self):
        response_data = {"detail": str(self.detail)}
        return Response(response_data, status=self.status_code)
