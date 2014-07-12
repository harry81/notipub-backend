import custom


def get_logger(name=''):
    """Get a named logger using python's logging module.
    
    This serves as a lightweight wrapper around python's logging module.
    
    The named logger may have a different configuration set in 'get_named_logger',
    additional stdout handler returned by 'get_stdout_handler' and 
    formatters of all handlers changed to a verbose one returned by 'get_verbose_formatter'.
    
    Look in 'settings.py' for available settings You can put in the project's settings
    and that influence the above mentioned features.
    
    Example use in the code:
        
        from lib.logs import logs as logging
        logger = logging.get_logger(__name__)
        logger.critical('Hit!')
    
    :param name: logger's name
    :type name: string
    
    :rtype: Logger
    """
    # get a defined named logger or a one using basic conf
    logger = custom.get_named_logger(name)
    
    # checking for an additional stdout handler
    stdout_handler = custom.get_stdout_handler(name)
    if stdout_handler:
        # adding a stdout handler
        logger.addHandler(stdout_handler)

    # checking for an change to a verbose formatter
    verbose_formatter = custom.get_verbose_formatter(name) 
    if verbose_formatter:
        # setting up verbose formatter for all handlers
        for handler in logger.handlers:
            handler.setFormatter(verbose_formatter)
        logger = custom.get_verbose_LoggerAdapter(logger)
        
    return logger
    

