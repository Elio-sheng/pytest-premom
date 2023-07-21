from core.result_base import ResultBase
from api.user import userservice
from common.logger import logger


def webUserLogin(email, password, deviceId):
    """
    注册用户信息
    :param email: 注册邮箱
    :param password: 密码
    :param deviceId: 设备 ID
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "username": email,
        "password": password,
        "deviceId": deviceId,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = userservice.webUserLogin(json=json_data, headers=header)
    logger.info(res.json())
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(
            res.json()["code"], res.json())
    result.msg = res.json()["message"]
    result.response = res
    return result
