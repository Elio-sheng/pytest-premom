from common.logger import logger
from operation.userservice import webUserLogin


class TestLogin():
    def test_userservice_login(self, anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone, except_result, expect_code, expect_msg):
        # Print a message to indicate the start of the test case
        logger.info("*************** 开始执行用例 ***************")
        # Call the webUserLogin function with the provided parameters
        # result = webUserLogin(anonymousId, bindAnonymous, email, password, phoneID, platform, timeZone)

        # Log the expected result, code, and message

        # logger.info(result)
        # Print a message to indicate the end of the test case
        logger.info("*************** 结束执行用例 ***************")