from common.logger import logger


class ResultBase():
    def __init__(self, res, status_code, contains, equals, key):
        """

        :param res: 请求
        :param status_code: 状态码
        :param contains: 包含值
        :param equals: 相等
        :param key: 要判断的键值
        """
        self.res = res
        self.status_code = status_code
        self.contains = contains
        self.equals = equals
        self.key = key
        self.assert_request_code()
        self.assert_result_contain()
        self.assert_result_equal()

    def assert_request_code(self):
        # logger.info("测试响应状态码是否正确")
        assert self.status_code == self.res.status_code

    def assert_result_contain(self):
        # logger.info("测试是否包含xxx")
        # logger.info(self.res.text)
        assert self.contains in self.res.text, self.contains+"不存在"

    def assert_result_equal(self):
        try:
            # logger.info("测试键值是否相等")
            assert self.equals == self.res.json()[self.key], self.equals+"不是预期值"
        except:
            logger.info("不是响应的json文本或key值不存在")


