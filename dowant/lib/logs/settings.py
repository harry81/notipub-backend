import logging
import os

"""
Setting up the root logger:

    from lib.logs import basic_config
    basic_config.setup()

Using logging in the code:

    from lib.logs import logs as logging
    logger = logging.get_logger(__name__)
    logger.critical('Hit!')


Project's settings:

    LOGS_VERBOSE_NAMESPACES = ['myproject.app1', 'myproject.app2']
    LOGS_STDOUT_NAMESPACES = ['myproject'] if 'runserver' in sys.argv else []
    LOGS_LOGLEVEL = 'WARNING'
"""

## settings that can be changed in projects settings file ##

def LOGS_LOGLEVEL():
    """Loglevel for all the loggers. Default is 'INFO'."""
    from django.conf import settings
    AVAILABLE_LOGLEVELS = ['CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO', 'NOTSET', 'WARN', 'WARNING']
    LOGS_LOGLEVEL = getattr(settings, 'LOGS_LOGLEVEL', 'INFO') 
    if LOGS_LOGLEVEL not in AVAILABLE_LOGLEVELS:
        raise Exception("Bad value of LOGS_LOGLEVEL. '%s' is not in: %s." % (settings.LOGS_LOGLEVEL, ', '.join(AVAILABLE_LOGLEVELS)))
    else:    
        LOGLEVEL = getattr(logging, LOGS_LOGLEVEL)
    return LOGLEVEL

def LOGS_VERBOSE_NAMESPACES():
    """Namespaces of the loggers that should have a verbose formatter.
    
    The format of the verbose formatter is defined as: "%(name)s %(appserver)s %(settings)s %(release)s %(mode)s %(pathname)s %(funcName)s %(asctime)s %(levelname)s %(message)s"
    It needs an extra dict passed so should be wrapped in a LoggerAdapter.
    
    Otherwise a simple format is: "%(name)s %(funcName)s %(asctime)s %(levelname)s %(message)s"
    """
    from django.conf import settings
    LOGS_VERBOSE_NAMESPACES = getattr(settings, 'LOGS_VERBOSE_NAMESPACES', [])
    if not type([]) == type(LOGS_VERBOSE_NAMESPACES):
        raise Exception("Bad value of LOGS_VERBOSE_NAMESPACES. '%s' is not a list." % settings.LOGS_VERBOSE_NAMESPACES)
    return LOGS_VERBOSE_NAMESPACES

def LOGS_STDOUT_NAMESPACES():
    """Namespaces of the loggers that should have an additional stdout handler."""
    from django.conf import settings
    LOGS_STDOUT_NAMESPACES = getattr(settings, 'LOGS_STDOUT_NAMESPACES', [])
    if not type([]) == type(LOGS_STDOUT_NAMESPACES):
        raise Exception("Bad value of LOGS_STDOUT_NAMESPACES. '%s' is not a list." % settings.LOGS_STDOUT_NAMESPACES)
    return LOGS_STDOUT_NAMESPACES
    
def LOGS_NAME_OVERRIDE():
    """A named that will be used for all the loggers regardless how they are called in the code. 
    Works only for loggers instantiated using this library.
    """
    from django.conf import settings
    LOGS_NAME_OVERRIDE =  getattr(settings, 'LOGS_NAME_OVERRIDE', None)
    if LOGS_NAME_OVERRIDE and not LOGS_NAME_OVERRIDE in NAMED_CONF().keys():
        raise Exception("Bad value of LOGS_NAME_OVERRIDE. '%s' is not in: %s" % (settings.LOGS_NAME_OVERRIDE, ', '.join(NAMED_CONF.keys())))
    return LOGS_NAME_OVERRIDE
    
    
## fixed (internal conf) settings ##

# simple default format for the formatters
SIMPLE_FORMAT = "%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s"

# verbose format for the formatters
VERBOSE_FORMAT = "%(asctime)s %(name)s %(appserver)s %(settings)s %(release)s %(mode)s %(pathname)s %(funcName)s %(levelname)s %(message)s"

# context for a LoggerAdapter using the VERBOSE FORMAT
def VERBOSE_CTX():
    from django.conf import settings
    return {
        'appserver': settings.HOSTNAME,
        'settings': settings.SETTINGS_FILE,
        'release': settings.RELEASE_TAG,
        'mode': settings.OPERATION_MODE,
    }

# path to the log file
def FILENAME(name):
    from django.conf import settings
    log_path = settings.LOG_FOLDER_ROOT
    
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    return os.path.join(log_path, '%s-%s.log' % (name, settings.OPERATION_MODE))


# configuration for the root logger
def BASIC_CONF():
    return {"level": LOGS_LOGLEVEL(),
            "format": SIMPLE_FORMAT,
            "filename": FILENAME('django'),
            "filemode": 'a+',
            }


#  configurations for defined named loggers
def NAMED_CONF():
    return {
        'cronjobs': {"level": LOGS_LOGLEVEL(),
                     "format": SIMPLE_FORMAT,
                     "filename": FILENAME('cronjobs'),
                     "filemode": 'a+',
                     },
        'tests': {"level": LOGS_LOGLEVEL(),
                  "format": SIMPLE_FORMAT,
                  "filename": FILENAME('tests'),
                  "filemode": 'a+',
                  }
    }
