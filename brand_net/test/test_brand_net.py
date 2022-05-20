import unittest

import gensim.downloader as api
import igraph as ig
from brand_net.concepts import find_concepts

class Testing(unittest.TestCase):

    def test_string(self):
        self.assertEqual(find_concepts(),9)

if __name__ == '__main__':
    unittest.main()
