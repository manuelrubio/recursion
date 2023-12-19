def find_path_maze(M, row, col, incr, exit_row, exit_col):
    # Base case: check if path found
    if row == exit_row and col == exit_col:
        return True  # Solution found
    else:
        sol_found = False
        # Generate candidates
        k = 0
        while not sol_found and k < 4:

            # New candidate cell
            new_col = col + incr[k][0]
            new_row = row + incr[k][1]

            # Test candidate validity
            if (new_row >= 0 and new_row < len(M)
                    and new_col >= 0 and new_col < len(M[0])
                    and M[new_row][new_col] == 'E'):

                # Add to path (partial solution)
                M[new_row][new_col] = 'P'

                # Try to expand path starting at new cell
                sol_found = find_path_maze(
                    M, new_row, new_col, incr,
                    exit_row, exit_col)

                # Mark as empty if new cell not in solution
                if not sol_found:
                    M[new_row][new_col] = 'E'

            k = k + 1

        return sol_found


def find_path_maze_wrapper(M, enter_row, enter_col,
                           exit_row, exit_col):
    # search directions
    incr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    M[enter_row][enter_col] = 'P'
    return find_path_maze(M, enter_row, enter_col, incr,
                          exit_row, exit_col)


# Test
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def read_maze_from_file(filename):
    file = open(filename, 'r')
    M = []
    for line in file.readlines():
        M.append([x[0] for x in line.split(' ')])
    file.close()
    return M


gray = (0.75, 0.75, 0.75)
black = (0, 0, 0)
red = (0.75, 0, 0)
green = (0, 0.75, 0)


def draw_maze(M, enter_row, enter_col, exit_row, exit_col):
    nrows = len(M)
    ncols = len(M[0])
    fig = plt.figure()
    fig.patch.set_facecolor('white')
    ax = plt.gca()

    if enter_row is not None and enter_col is not None:
        ax.add_patch(Rectangle((enter_col, nrows - enter_row),
                               1, -1, linewidth=0, facecolor=green,
                               fill=True))
    if exit_row is not None and exit_col is not None:
        ax.add_patch(Rectangle((exit_col, nrows - exit_row),
                               1, -1, linewidth=0, facecolor=red,
                               fill=True))

    for row in range(0, nrows):
        for col in range(0, ncols):
            if M[row][col] == 'W':
                ax.add_patch(Rectangle((col, nrows - row), 1, -1,
                                       linewidth=0, facecolor=gray))
            elif M[row][col] == 'P':
                circ = plt.Circle((col + 0.5, nrows - row - 0.5),
                                  radius=0.15, color=black, fill=True)
                ax.add_patch(circ)

    ax.add_patch(Rectangle((0, 0), ncols, nrows, edgecolor=black,
                           fill=False))
    plt.axis('equal')
    plt.axis('off')
    plt.show()


M = read_maze_from_file('maze01_input.txt')  # Some file
# Enter at top-left, exit at bottom-right
if find_path_maze_wrapper(M, 0, 0, len(M) - 1, len(M[0]) - 1):
    draw_maze(M, 0, 0, len(M) - 1, len(M[0]) - 1)
