import logs as logging
logger = logging.get_logger(__name__)


class LogExceptionsMiddleware(object):
    """Logging all exceptions coming from views.
    
    This middleware should come before all middlewares handling views errors and returning a response
    as those errors should be logged explicitly there. 
    """
    
    def process_exception(self, request, exception):
        logger.exception(exception)
        return None