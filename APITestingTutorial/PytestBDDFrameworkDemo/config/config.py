import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "config",
    "config.ini"
)
config.read(config_path)

# Read active environment
active_env = config.get("environment", "active")

# Read environment-specific base URL
base_url = config.get(active_env, "BASE_URL")

# Read auth details
username = config.get("auth", "username")
password = config.get("auth", "password")

# Read headers
headers = {
    "Content-Type": config.get("headers", "content_type")
}
