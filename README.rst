ListeningSocketHandler
======================

.. image:: https://travis-ci.org/bencord0/ListeningSocketHandler.png

The opposite of logging.handlers.SocketHandler

Example Usage
-------------

1. Create a logger

    >>> import logging
    >>> from listeningsockethandler import ListeningSocketHandler
    >>> log = logging.getLogger()
    >>> log.setLevel(logging.DEBUG)

2. Create some handlers

    A normal StreamHandler that outputs to stderr and
    a ListeningSocketHandler bound to port 12345.

    >>> sh = logging.StreamHandler()
    >>> sh.setLevel(logging.WARN)
    >>> lh = ListeningSocketHandler(12345)
    >>> lh.setLevel(logging.DEBUG)

3. Add handlers to the logger

    >>> log.addHandler(sh)
    >>> log.addHandler(lh)

4. Log some things

    >>> log.info("An informational message")
    >>> log.warn("A warning message")
    A warning message

5. Connect to the logger, and log more detailed events

    In a new shell, connect to the logger.

    $ telnet localhost 12345

    Back in python, use different log levels.

    >>> log.critical("A critical message")
    A critical message
    >>> log.debug("A debugging message")

    Watch the detailed stream in the telnet session.

    A critical message
    A debugging message


