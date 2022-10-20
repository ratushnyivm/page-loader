import logging.config

LOGGING = {
    'version': 1,
    'formatters': {
        'consoled': {
            'format': '%(asctime)s :: %(levelname)s :: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'consoled'
        },
    },

    'loggers': {
        'PageLoader': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("PageLoader")
