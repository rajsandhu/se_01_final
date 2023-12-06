""" 
the first exercise for the final exam 06.12.2023
Dojo-Style SE_01 Assessment: 6 Dec 2023
gems-ex.1pdf
Raj Sandhu
"""



def make_grid():
    made_grid = "m g sample text"
    return made_grid

def swap_cells(matrix):
    swapped_matrix = "s m sample text " + matrix 
    return swapped_matrix

def test_for_line(swapped_matrix):
    legality = "t f l sample text" + swapped_matrix
    return legality

def main():
    # (1) make a 3x3 grid of numbers, each cell assigned 1-5, repeats possible
    grid = make_grid()
    # (2) swap the contents of two cells
    swapped_grid = swap_cells(grid)
    # (3) test whether any rows or columns now contain indentical numbers
    is_move_legal = test_for_line(swapped_grid)
    # (4) print result
    print(is_move_legal)
    
if __name__ == "__main__":
    main()