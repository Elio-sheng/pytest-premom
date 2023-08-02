from core.result_base import ResultBase
from api.user import UserService
from common.logger import logger



def webUserLogin(anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone):
    """
    Register user information.

    Args:
        anonymousId (str): Anonymous ID.
        bindAnonymous (bool): Flag indicating if the user should be bound to the anonymous ID.
        email (str): User's email address.
        password (str): User's password.
        phoneID (str): User's phone ID.
        platform (str): User's platform.
        timeZone (str): User's time zone.

    Returns:
        ResultBase: Custom keyword result.

    """
    result = ResultBase()

    json_data = {
        "anonymousId": anonymousId,
        "bindAnonymous": bindAnonymous,
        "email": email,
        "password": password,
        "phoneID": phoneID,
        "platform": platform,
        "timeZone": timeZone,
    }

    header = {
        "Content-Type": "application/json"
    }

    res = userservice.webUserLogin(json=json_data, headers=header)

    logger.info(res.json())

    result.success = False
    logger.info(res.json()["code"])
    if res.json()["code"] == "SIGN_INVALID_REGISTER_PASSWORD":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(
            res.json()["code"], res.json())

    result.msg = res.json()["message"]
    result.response = res

    return result
