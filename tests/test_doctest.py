import unittest
import doctest

def load_tests(loader, tests, ignore):
    for name in ['httpcache', 'dllist', 'lrucache', 'memcachemap']:
        m = __import__(name)
        tests.addTests(doctest.DocTestSuite(m))
    return tests

