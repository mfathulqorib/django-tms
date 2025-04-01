import os


def get_env_variable(var_name, default=None):
    """Get the environment variable or raise an error if not found."""
    value = os.getenv(var_name, default)
    if value is None:
        raise ValueError(f"Missing required environment variable: {var_name}")
    return value
