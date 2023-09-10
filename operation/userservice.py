from core.result_base import ResultBase
from api.user import UserService
from common.logger import logger
import os


def webUserLogin(title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code, expect_msg):
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
    # result = ResultBase

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
    webUser = UserService(base_url=os.environ.get("API_URL"))
    res = webUser.webUserLogin(json=json_data, headers=header)

    logger.info(res.json())
    # logger.info("实际code ==>> {}".format(res.status_code))
    # logger.info("预期code ==>> {}".format(expect_code))
    # logger.info("实际msg ==>> {}".format(res.text))
    # logger.info("预期msg ==>> {}".format(expect_msg))
    ResultBase(res, expect_code, expect_msg, expect_msg, expect_msg )





    # result.success = False
    # logger.info(res.json())
    # if res.json()["init"] == True:
    #     result.success = True
    # elif res.json()["code"] == "SIGN_PASSWORD_NOT_MATCHED":
    #     result.success = True
    # elif res.json()["code"] == "SIGN_INVALID_REGISTER_ACCOUNT":
    #     result.success = True
    # elif res.json()["code"] == "SIGN_INVALID_REGISTER_PASSWORD":
    #     result.success = True
    # elif res.json()["code"] == "SIGN_USER_NOT_EXIST":
    #     result.success = True
    # else:
    #     result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(
    #         res.json()["code"], res.json())
    #
    # # result.msg = res.json()
    # result.response = res

    # return result
