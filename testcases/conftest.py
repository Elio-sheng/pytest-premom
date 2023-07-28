import pytest
import os
from common.logger import logger
from common.read_data import yaml
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