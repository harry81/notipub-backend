import logging
import logging.handlers
import settings


## loggers ##

def get_named_logger(name):
    """Return a named logger according to the given name or a custom one specified in settings file."""
    
    if settings.LOGS_NAME_OVERRIDE():
        name = settings.LOGS_NAME_OVERRIDE()
        conf = settings.NAMED_CONF()[name]
    else:
        conf = settings.BASIC_CONF()
    
    logger = logging.getLogger(name)
    logger.setLevel(conf['level'])
    
    # resetting handlers
    logger.handlers = [] 

    # adding a log rotating file handler
    handler = logging.handlers.WatchedFileHandler(conf['filename'],
                                                  mode=conf['filemode'])
    formatter = logging.Formatter(conf['format'])
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.propagate = False
    return logger


## handlers, formatters, adapters ##

def get_stdout_handler(name):
    """Return a basic StreamHandler for logs to be printed out to stdout in local development env."""
    
    if in_namespaces(name, settings.LOGS_STDOUT_NAMESPACES()):
        return logging.StreamHandler()
    return None

def get_verbose_formatter(name):
    """Return a very verbose formatter for debug needs across various appservers, code releases etc."""
    
    if in_namespaces(name, settings.LOGS_VERBOSE_NAMESPACES()):
        return logging.Formatter(settings.VERBOSE_FORMAT)
    return None

def get_verbose_LoggerAdapter(logger):
    """Return a LoggerAddapter which attaches to the Logger a dictionary used by the formatter."""
    
    return logging.LoggerAdapter(logger, settings.VERBOSE_CTX())


## helpers ##

def in_namespaces(name, namespaces):
    """ Check if any of the the strings in a list of strings starts with a given string."""
    
    return any(name.startswith(namespace) for namespace in namespaces)
