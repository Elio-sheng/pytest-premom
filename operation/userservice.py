from core.result_base import ResultBase
from api.user import UserService
from common.logger import logger
import os


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
    api_url = os.environ["API_URL"]
    webUser = UserService(base_url=api_url)
    res = webUser.webUserLogin(json=json_data, headers=header)

    logger.info(res.json())

    result.success = False
    logger.info(res.json()["init"])
    if res.json()["init"] == True:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(
            res.json()["code"], res.json())

    # result.msg = res.json()
    result.response = res

    return result
