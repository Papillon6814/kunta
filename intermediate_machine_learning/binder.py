"""binder"""

import logging


class NoBoundError(Exception):
    """No variables in globals"""


class Binder:
    """Binder class"""

    def __init__(self):
        self.bound = False
        self.g = None

    def bind(self, global_vars):
        """bind"""
        if self.bound:
            if id(global_vars) == id(self.g):
                logging.warning("Ignoring repeated attempt to bind to globals")
            else:
                raise NoBoundError(
                    "Attempted to bind different vars to already-bound binder"
                )
        else:
            self.g = global_vars
            self.bound = True

    def readonly_globals(self):
        """globals"""
        return ReadOnlyGlobals(self.g)


class ReadOnlyGlobals:
    """Readonly wrapper around captured globals dict, plus some convenience methods."""

    def __init__(self, g):
        self.g = g

    def __getitem__(self, key):
        # TODO: maybe wrap KeyError in some custom exception?
        # Or maybe there should be two ways of looking up a key, one of which has
        # the semantics "if this key is missing, the user did something terribly wrong"
        return self.g[key]

    def __contains__(self, key):
        return key in self.g

    def keys(self):
        """keys of global variables"""
        return self.g.keys()

    def lookup(self, keys):
        """find a key of global variables"""
        return [self.g[k] for k in keys]

    # No __setitem__


binder = Binder()
