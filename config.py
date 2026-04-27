# Listaria Configuration File

# Flask Configuration
DEBUG = False
TESTING = False

# Server Configuration
HOST = "0.0.0.0"
PORT = 5000

# Security
MAX_CONTENT_LENGTH = 16 * 1024  # 16KB max request size
JSON_SORT_KEYS = False

# Session
PERMANENT_SESSION_LIFETIME = 86400  # 24 hours

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
