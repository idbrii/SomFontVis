import time as t

class WaitTimer():
    """Simple timer class that will ideally provide constant duration loop
    iterations. You create it at the beginning of your loop and then sleep
    on it later, but it will take into account the time you have spent
    before sleeping.

        >>> timer = WaitTimer()
        >>> # do some processing
        >>> numbers = ['0']
        >>> for a in range(0,10000):
        ...     numbers += str(a) + numbers[a%3]    # some random calculation
        ...
        >>> timer.waitFromCreateTime( 0.01 )
        >>> # shouldn't wait at all
        >>> timer.waitFromCreateTime( 1.0 )
        >>> # shouldn't wait for a full second
    """
    def __init__(self):
        """capture current time"""
        self.startTime = t.time()       # seconds
        self.skipCheck = False

    def waitFromCreateTime(self, duration):
        """wait for time to pass starting counting from object creation
        @param duration Time in seconds to wait
        """
        timePassed = t.time() - self.startTime
        duration -= timePassed
        if duration > 0:
            t.sleep( duration )


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
