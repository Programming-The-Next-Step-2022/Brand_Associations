import unittest

import gensim.downloader as api
import igraph as ig
from brand_net.concepts import find_concepts

# This one is unfinished (only a skeleton of unittesting)
class Testing(unittest.TestCase):

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
