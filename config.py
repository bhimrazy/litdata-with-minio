import os
from pathlib import Path
from dotenv import load_dotenv


class DotDict(dict):
    """A dictionary that allows for dot notation access."""

    def __getattr__(self, item):
        if item in self:
            value = self[item]
            if isinstance(value, dict):
                return DotDict(value)
            return value
        raise AttributeError(f"'DotDict' object has no attribute '{item}'")

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def load_config():
    """Loads environment variables and returns them as a DotDict object."""
    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)

    config_dict = {
        "minio": {
            "bucket": os.getenv("MINIO_BUCKET"),
        },
        "aws": {
            "access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
            "secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
            "endpoint_url": os.getenv("AWS_ENDPOINT_URL"),
        },
        "data": {
            "optimized_dir": os.getenv("OPTIMIZED_DATA_DIR"),
            "cache_dir": os.getenv("CACHE_DIR"),
        },
    }

    return DotDict(config_dict)
