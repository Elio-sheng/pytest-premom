from core.result_base import ResultBase
from api.user import UserService
from common.logger import logger
import os


def webUserLogin(title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code,expect_msg):
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
    ResultBase(res, expect_code, expect_msg, expect_msg, res)   #断言

def webRegister(title, email, password, OSType, lastName, firstName, except_result, expect_code, expect_msg):
    json_data = {
        "email": email,
        "password": password,
        "OSType": OSType,
        "lastName": lastName,
        "firstName": firstName
    }
    header = {
        "InstallId": "s4m11r14kkrhqqg4f17869",
        "apiVersion": "42",
        "Content-Type": "application/json"
    }
    webUser = UserService(base_url=os.environ.get("API_URL"))
    res = webUser.webRegister(json=json_data, headers=header)
    logger.info(res.json())
    # logger.info("预期code===>> {}".format(expect_code))
    # logger.info("实际code===>> {}".format(res.status_code))
    # logger.info("预期msg===>> {}".format(expect_msg))
    # logger.info("实际msg===>> {}".format(res.text))
    ResultBase(res, expect_code, expect_msg, expect_msg, res)   #断言