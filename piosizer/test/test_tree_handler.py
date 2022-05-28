import unittest

from pokersolverquery.solver import Solver

from piosizer import parse_evs
from piosizer.util.TreeHandler import TreeHandler


class MyTestCase(unittest.TestCase):
    def test_initialize(self):
        input_paths = [r'F:\Piosolver\saves\2022-05-28_09-12-58_BU vs BB SRP 33%',
                       r'F:\Piosolver\saves\2022-05-28_09-13-20_BU vs BB SRP 75%']
        tree_handler = TreeHandler(input_paths)
        self.assertEqual(len(tree_handler), 5)

        for x in tree_handler:
            print(x)

    def test_parse_ev(self):
        solver_path = r'F:\Piosolver\PioSOLVER2-pro.exe'
        solver = Solver(solver_path)
        solver.command(f'load_tree "%s"' % r'F:\Piosolver\saves\2022-05-28_09-12-58_BU vs BB SRP 33%\4s8d9s.cfr')

        self.assertEqual(parse_evs(solver.command('calc_results'), True), 27.225)

        solver.exit()

    def test_get_ev(self):
        pass


if __name__ == '__main__':
    unittest.main()
