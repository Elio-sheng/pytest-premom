from common.logger import logger
from operation.userservice import webUserLogin,webRegister


class TestLogin():
    def test_userservice_login(self, title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone,except_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserLogin function with the provided parameters
        result = webUserLogin(title, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code,expect_msg)

        # Log the expected result, code, and message

        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")

class TestRegister():
    def test_userservice_register(self, title, email, password, OSType, lastName, firstName, except_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserRegister function with the provided parameters
        result = webRegister(title, email, password, OSType, lastName, firstName, except_result, expect_code, expect_msg)

        # Log the expected result, code, and message

        logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")