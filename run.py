import pytest
import argparse
from common import env
from common.logger import logger
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', default='dev', help='Environment to run against')
    args = parser.parse_args()
    api_url = env.get_api_url(args.env)
    os.environ['API_URL'] = api_url
    logger.info('API URL: {}'.format(api_url))
    pytest.main()
