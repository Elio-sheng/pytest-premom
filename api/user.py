import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class UserService(RestClient):
    def __init__(self, api_root_url, **kwargs):
        """
        Initialize UserService object.

        Args:
            api_root_url (str): The root URL of the API.
            **kwargs: Additional keyword arguments.
        """
        super(UserService, self).__init__(api_root_url, **kwargs)

    def webUserLogin(self, **kwargs):
        """
        Perform web user login.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/user/web/sign/in", **kwargs)

    def thirdUserLogin(self, **kwargs):
        """
        Perform third user login.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/web/sign/in/third", **kwargs)

    def webRegister(self, **kwargs):
        """
        Perform web user registration.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/web/sign/up", **kwargs)


userservice = UserService(api_root_url)
