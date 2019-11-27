import unittest


def run_tests():
    testmodules = [
        'TestBop',
        'TestPrepareData',
        'TestRequestHandler',
        ]

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    run_tests()
