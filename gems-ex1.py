""" 
the first exercise for the final exam 06.12.2023
Dojo-Style SE_01 Assessment: 6 Dec 2023
gems-ex.1pdf
Raj Sandhu
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
    made_grid = [[1,2,3],[4,4,5],[5,3,4]]
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
           if 0 <= i1 < 3 and 0 <= j1 < 3 and 0 <= i2 < 3 and 0 <= j2 < 3:
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
      if row.count(row[0]) == len(row):
        print("row test: the move was valid, returns true")
        return True


  # Check columns
  for col in range(len(swapped_matrix[0])):
      column = [row[col] for row in swapped_matrix]
      if column.count(column[0]) == len(column):
        print("column test: the move was valid, returns true")
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