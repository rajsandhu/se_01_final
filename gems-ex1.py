""" 
the second exercise for the final exam 06.12.2023
Dojo-Style SE_01 Assessment: 6 Dec 2023
gems-ex2.pdf
Raj Sandhu

objective: expand the 3x3 grid of exercise 1 pdf to 4x4 grid.

note: 4 cell lines are now valid, and 3 cell lines are still valid

"""

# NOT NECESSARY AT THIS STEP
# import random


# this function makes a random grid, unnecessary at this step
  # ----------  
# def make_grid():
#     made_grid = [[0 for _ in range(3)] for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             made_grid[i][j] = random.randint(1, 5)
#     return made_grid

def make_grid():
    # expanding grid to match graphical changes from 5 to 7 gem types
    # new gems are orange hexagon (6) and white decahedron (7)
    # ------- original made grid
    made_grid = [[2,1,2,3],[5,4,4,5],[2,5,3,4],[6,7,6,1]]
    # # -------- test made grid, to pass 4 line test row
    # made_grid = [[1,1,1,1],[5,4,4,5],[2,5,3,4],[6,7,6,1]]
    # # -------- test made grid, to pass 4 line test column
    # made_grid = [[1,1,2,3],[1,4,4,5],[1,5,3,4],[1,7,6,1]]
    return made_grid


def swap_cells(matrix):
   # TEST
   print("this is the original grid: {}".format(matrix))

   # Ask the user for the coordinates of the two cells
   while True:
       try:
           i1 = int(input("Enter the row number of the first cell (i1): ")) - 1
           j1 = int(input("Enter the column number of the first cell (j1): ")) - 1
           i2 = int(input("Enter the row number of the second cell (i2): ")) - 1
           j2 = int(input("Enter the column number of the second cell (j2): ")) - 1

           # Check if the coordinates are valid
           if 0 <= i1 < 4 and 0 <= j1 < 4 and 0 <= i2 < 4 and 0 <= j2 < 4:
               break
           else:
               print("Invalid coordinates. Please enter numbers between 1 and 3.")
       except ValueError:
           print("Invalid input. Please enter a number.")

   # Swap the contents of the two cells
   matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

   # TEST
   print("this is the swapped grid: {}".format(matrix))

   # a simple return
   return matrix

def test_for_line(swapped_matrix):
    # Check rows
    for row in swapped_matrix:
        if row.count(row[0]) == len(row) or row.count(row[0] == 4):
            print("row test for 4: the move was valid, returns true")
            return True


  # Check columns
    for col in range(len(swapped_matrix[0])):
        column = [row[col] for row in swapped_matrix]
        if column.count(column[0]) == len(column) or column.count(column[0] == 4):
            print("column test for 4: the move was valid, returns true")
            return True

 # Check for 3-cell-length lines
    for i in range(len(swapped_matrix)):
        for j in range(len(swapped_matrix[i])):
            if i < len(swapped_matrix) - 2 and swapped_matrix[i][j] == swapped_matrix[i+1][j] == swapped_matrix[i+2][j]:
                print("row test for 3: the move was valid, returns true")
                return True


            if j < len(swapped_matrix[i]) - 2 and swapped_matrix[i][j] == swapped_matrix[i][j+1] == swapped_matrix[i][j+2]:
                print("row test for 3: the move was valid, returns true")
                return True



    # If no identical numbers found in rows or columns
    return False

def print_legality(result):
    if result == True:
        print("This was a legal move")
    if result == False:
        print("This was an *illegal* move")    
    
def main():
    # (1) make a 3x3 grid of numbers, each cell assigned 1-5, repeats possible
    grid = make_grid()
    # (2) swap the contents of two cells
    swapped_grid = swap_cells(grid)
    # (3) test whether any rows or columns now contain indentical numbers
    is_move_legal = test_for_line(swapped_grid)
    # (4) print result
    print_legality(is_move_legal)
    
if __name__ == "__main__":
    main()