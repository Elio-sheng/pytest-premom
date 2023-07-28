import os
from core.rest_client import RestClient


class UserService(RestClient):
    def __init__(self, base_url, **kwargs):
        # Initialize the RestClient object with the API root URL
        self.base_url = base_url

    def webUserLogin(self, **kwargs):
        return self.post("/user/user/web/sign/in", **kwargs)

    def thirdUserLogin(self, **kwargs):
        return self.post("/user/web/sign/in/third", **kwargs)

    def webRegister(self, **kwargs):
        return self.post("/user/web/sign/up", **kwargs)


base_url = os.environ["API_URL"]
userservice = UserService(base_url)
