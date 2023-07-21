import pytest
from operation.userservice import webUserLogin
from common.logger import logger


class TestLogin():
    def test_userservice_login(self, email, password, deviceId):
        logger.info("*************** 开始执行用例 ***************")
        logger.info(f"{email}, {deviceId}, {password}")
        logger.info("*************** 结束执行用例 ***************")
