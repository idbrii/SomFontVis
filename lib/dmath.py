def clamp(val, minVal, maxVal):
    """ clamp(int, int, int) -> int
    Clamp a value between two inclusive values
    assert b <= clamp(a,b,c) <= c

    >>> clamp( 10, 2, 100 )
    10
    >>> clamp( 100, 2, 100 )
    100
    >>> clamp( -10, 2, 100 )
    2
    >>> clamp( 500, 2, 100 )
    100
    """
    return max( min(val, maxVal), minVal )



def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
