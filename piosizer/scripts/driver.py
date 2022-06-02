import click
import numpy
import shutil

from pathlib import Path
from pokersolverquery.solver import Solver

from piosizer import get_evs
from piosizer.util.TreeHandler import TreeHandler


@click.command()
@click.option('-s', '--solver-path')
@click.option('-o', '--output-path')
@click.option('--oop', is_flag=True, show_default=True, default=False)
@click.argument('input_paths', nargs=-1)
def run(solver_path, output_path, oop, input_paths):
    log = open("log.txt", "a")
    solver = Solver(solver_path)
    tree_handler = TreeHandler(input_paths)
    for files in tree_handler:
        if len(files) > 1:
            evs = numpy.array(get_evs(solver, files, not oop))

            for index, file in enumerate(files):
                log.write(f"%s: %f\n" % (file, evs[index]))

            file = files[numpy.argmax(evs)]
            log.write(f"Copying %s...\n" % file)

            # Copy highest EV file
            shutil.copy(file, output_path)
        log.write("\n")

    log.close()


