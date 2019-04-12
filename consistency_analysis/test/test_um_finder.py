import unittest
from os import path
from cobra.io import read_sbml_model
from ..unconnected_modules import UmFinder


def create_test_model():
    data_folder = path.join(path.dirname(path.abspath(__file__) ), 'data')
    sbml_fname = path.join(data_folder, 'iJO1366.xml')
    model = read_sbml_model(sbml_fname)
    return model


class TestUmFinder(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self._model = create_test_model()

    def setUp(self):

        for r in self._model.reactions:
            if not r.id.startswith('EX'):
                continue
            r.bounds = (-1000, 1000)

        self._um_finder = UmFinder(self._model, report=False)

    def test_model(self):
        print("Testing model %s:" % self._model.id, end=" ")
        self.assertTrue(len(self._model.reactions) == 2583)
        self.assertTrue(len(self._model.metabolites) == 1805)
        print('OK!')

    def test_umfinder(self):
        print("Testing unconnected modules calculation:", end=" ")
        self.setUp()
        self.assertTrue(len(self._um_finder.blocked_reactions) == 226)
        self.assertTrue(len(self._um_finder.gap_metabolites) == 203)
        self.assertTrue(len(self._um_finder.unconnected_modules) == 104)
        print('OK!')


if __name__ == '__main__':
    unittest.main()

