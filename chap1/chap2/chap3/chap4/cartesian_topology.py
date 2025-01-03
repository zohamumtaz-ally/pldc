from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

neighbour_processes = [0, 0, 0, 0]

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

grid_rows = int(np.floor(np.sqrt(size)))
grid_columns = size // grid_rows

if grid_rows * grid_columns > size:
    grid_columns -= 1
if grid_rows * grid_columns > size:
    grid_rows -= 1
