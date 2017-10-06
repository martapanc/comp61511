# Everything is in a docstring!
"""
>>> 1+1
2
>>> 1+1 #Note that the supplied expected answer is *wrong*. This test will fail
3
>>> [1, 2, 3][1]
2
"""

 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
