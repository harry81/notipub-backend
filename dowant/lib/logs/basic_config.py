import logging

import settings


def setup():
    """Configure root logger as a basic logger for the application."""
    logging.basicConfig(**settings.BASIC_CONF())
