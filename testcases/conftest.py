import pytest
import os
from common.logger import logger
from common.read_data import yaml
from api.user import UserService

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
userTestdata = None


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
    """Add option to pass --testenv=test to pytest cli command"""
    parser.addoption(
        "--testenv", action="store", default="dev", choices=["mtest", "prod", "test"], help="env：表示测试环境，默认dev环境"
    )


@pytest.fixture(scope="module", autouse=True)
def testurl(request):
    env_mapping = {
        'test': 'http://api.test.premom.tech/',
        'mtest': 'http://api.mtest.premom.tech/',
        'prod': 'http://api.premom.tech/'
    }
    env = request.config.getoption("--testenv")
    logger.info(env)
    logger.info(env_mapping.get(env))
    os.environ["API_URL"] = env_mapping.get(env)


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
    base_url = os.environ["API_URL"]
    logger.info(base_url)
    userservice = UserService(base_url=base_url)
    # logger.info()
    res = userservice.webUserLogin(json=json_data, headers=header)
    logger.info(res.headers["authToken"])