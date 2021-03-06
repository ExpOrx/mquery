import os
from plugins import parse_plugin_list

INDEX_DIR = "/mnt/samples"
BACKEND = os.environ.get("MQUERY_BACKEND", "tcp://ursadb:9281")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
JOB_EXPIRATION_MINUTES = int(
    os.environ.get("JOB_EXPIRATION_MINUTES", 0)
)  # infinite by default
PLUGINS = parse_plugin_list(os.environ.get("MQUERY_PLUGINS", ""))
