import pytest
import os
from common.logger import logger
from common.read_data import yaml
from api.user import UserService

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
userTestdata = None
# Define global variable
global_url = None


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
    try:
        with open(data_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
    except FileNotFoundError:
        pytest.skip(f"File not found: {data_file_path}")
    except Exception as ex:
        pytest.skip(f"Error loading YAML file: {ex}")
    else:
        return yaml_data


# base_data = get_data("base_data.yml")
# api_data = get_data("api_test_data.yml")
# scenario_data = get_data("scenario_test_data.yml")


def pytest_generate_tests(metafunc):
    """Parameterize the tests from a YAML file.

    The YAML file structure should be like this:
        TestXXX:                        # Class
          test_soco_xxx:                # Function
            parameters: paramA, paramB  # Parameter list
            values:
              - [valA1, valA2]          # Test cases
              - [valA2, valB2]
    """
    global userTestdata
    if not userTestdata:
        # Fetch testdata from YAML file
        userTestdata = get_data("userservice_test_data.yml")

    classname = metafunc.cls.__name__
    funcname = metafunc.function.__name__
    funcdata = userTestdata.get(classname)[funcname]
    if funcdata:
        parameters = funcdata['parameters']
        # Convert argument lists to tuples
        values = [tuple(v) if isinstance(v, list) else v for v in funcdata['values']]
        logger.info(f"Parameters: {parameters}")
        logger.info(f"Values: {values}")
        metafunc.parametrize(parameters, values)
        

def pytest_addoption(parser):
    """
    向pytest命令行解析器添加选项。

    参数：
        parser（argparse.ArgumentParser）：pytest命令行解析器。

    返回：
        无
    #  这段代码定义了一个函数pytest_addoption，它接受一个类型为argparse.ArgumentParser的参数parser。在函数内部，使用addini方法向parser对象添加了三个选项（test_url，prod_url，mtest_url）。每个选项都有一个描述和一个默认值。
    """
    parser.addini("test_url", "url for the test environment", default="http://api.test.premom.tech")
    parser.addini("prod_url", "url for the prod environment", default="https://api.premom.com")
    parser.addini("mtest_url", "url for the mtest environment", default="http://api.mtest.premom.tech")

    parser.addoption("--env", action="store",default="test", help="Specify the enviroment to run the test")


    # parser.addoption("--env", action="store", default="test", help="Specify the environment to run the tests")

# @pytest.fixture(scope="session")
# def base_url(request):
#     env = request.config.getoption("--env")
#     return request.config.getini(env)

@pytest.fixture(scope='session', autouse=True)
def switch_env(request):
    """
    这是一个名为switch_env的Pytest夹具，它在整个测试会话中自动使用。
    它获取--env命令行选项的值，并将其赋值给env变量。 然后，它从pytest.ini文件中获取配置选项{env}_url的值，
    并将其赋值给global_url变量。 如果在pytest.ini中找不到--env的值，它将回退到默认环境'test'。
    它记录一条信息消息，指示用于测试的环境env和global_url URL。 最后，它返回global_url的值。
    参数：

    request：Pytest提供的请求对象。
    返回：

    str：全局环境的URL。
    """
    global global_url
    env = request.config.getoption("--env")
    try:
        global_url = request.config.getini(f'{env}_url')
    except ValueError:
        logger.info(f"未知环境：{env}。回退到默认环境：test。")
        global_url = request.config.getini('test_url')
    logger.info(f"在 {env} 环境下使用 URL {global_url} 运行测试")
    os.environ["API_URL"] = global_url
    return global_url


@pytest.fixture(scope="class", autouse=True)
def GetToken():
    json_data = {
      "anonymousId": "",
      "bindAnonymous": "true",
      "email": "test103@premom.com",
      "password": "123456",
      "phoneID": "decbb1ef-e41c-4cbd-9265-902415f00504",
      "platform": "iPhone XR 13.3",
      "timeZone": "+0800"
    }
    header = {
        "Content-Type": "application/json"
    }
    logger.info(global_url)
    userservice = UserService(base_url=global_url)
    res = userservice.webUserLogin(json=json_data, headers=header)
    logger.info(res.headers["authToken"])
    logger.info(res.json())