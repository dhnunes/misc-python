"""

singleton.py - Example of Singleton Patterns Implementation

At this file we have classic and borg ( monostate ), design pattern.

"""

class Singleton():
"""

This is a classic Singleton Pattern.

Direct objects of this instance share the same state since we are returning
the same memory position to all instantiated objects.

This model of Singleton however, don't work with inheritance.

"""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Borg():
"""

This is a Borg Singleton Pattern.

In this implementation, all direct objects of this instance and all inheritance
done with this class as parent will share the same __dict__ which in this case
is __shared_state.

If you need to have a descendant of your partent Borg Singleton with a different
state, you need to reset the __shared_state, by declaring it again with a new dict.

"""

    __shared_state = {}

    def __new__(cls, *args, **kargs):
        obj = super(Borg, cls).__new__(cls, *args, **kargs)
        obj.__dict__ = cls.__shared_state
        return(obj)
