def get_api_url(env):
    """
    Returns the API URL based on the environment.

    Parameters:
        env (str): The environment name.

    Returns:
        str: The API URL corresponding to the given environment.

    Raises:
        ValueError: If the environment name is invalid.
    """
    if env == 'test':
        return 'http://api.test.premom.tech'
    elif env == 'mtest':
        return 'http://api.mtest.premom.tech'
    elif env == 'prod':
        return 'http://api.premom.tech'
    else:
        raise ValueError('Invalid environment name')