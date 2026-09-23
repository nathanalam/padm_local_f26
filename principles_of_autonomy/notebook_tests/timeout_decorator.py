"""Platform-compatible timeout decorator for the local notebook tests.

The upstream ``timeout-decorator`` package relies on ``SIGALRM`` by default,
which is unavailable on Windows.  The official grading environment is Linux,
so preserve the real timeout there.  On Windows, leave the function unchanged
so the local tests can run without changing student submission files.
"""

import os

import timeout_decorator as _timeout_decorator


def timeout(seconds=None, **kwargs):
    """Apply a real timeout on Unix and a no-op timeout on Windows."""
    if os.name == "nt":
        def decorate(function):
            return function

        return decorate

    return _timeout_decorator.timeout(seconds, **kwargs)

