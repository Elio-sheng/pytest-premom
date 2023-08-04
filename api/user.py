from core.rest_client import RestClient


class UserService(RestClient):
    def webUserLogin(self, **kwargs):
        return self.request("/user/user/web/sign/in", method="POST", **kwargs)

    def thirdUserLogin(self, **kwargs):
        return self.request("/user/web/sign/in/third", method="POST", **kwargs)

    def webRegister(self, **kwargs):
        return self.request("/user/web/sign/up", method="POST", **kwargs)

    def userDelete(self,**kwargs):
        return self.request("/user/user/cancellation/account/delete/reason", method="POST", **kwargs)