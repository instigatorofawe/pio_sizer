from pathlib import Path

from pokersolverquery.solver import Solver

base_directory = str(Path(__file__).resolve().parent.parent)


def get_evs(solver: Solver, files, ip=True):
    """
    Get EVs of each tree
    :param solver:
    :param files:
    :param ip: Get EVs for IP if true, else OOP
    :return:
    """
    evs = []
    for file in files:
        solver.command(f'load_tree %s' % file)
        evs.append(parse_evs(solver.command('calc_results'), ip))
    return evs


def parse_evs(input, ip):
    """
    Parse IP
    :param input:
    :return:
    """
    if ip:
        return float(input[1].split()[2])
    else:
        return float(input[0].split()[2])
