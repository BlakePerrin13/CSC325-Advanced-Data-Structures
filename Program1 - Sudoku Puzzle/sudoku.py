# Provide your information as the values of these variables:
myName = 'Blake, Perrin'
myTechID = '10382316'
myTechEmail = 'bep020' #only your email id omit @latech.edu
###########################################################

# Importing libraries and classes needed to run the program.
import sys
from hashSet import HashSet

# Function to add columns from the matrix into the column group.
def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
  return col

# Function to add squares from the matrix into the squares group.
def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])  
  return square

# Function that creates all of the row, column, and square groups.
def getGroups(matrix):
  groups = []
  # get rows
  for i in range(9):
    groups.append(list(matrix[i]))
  # get columns
  for i in range(9):
    groups.append(getColumn(matrix,i))
  # get squares
  # squares are processed left-right, up-down
  for i in range(0,9,3): 
    for j in range(0,9,3):
      groups.append(getSquare(matrix,i,j))
  return groups

# Method to get the cardinality of the specified group.
def cardinality(x):
  return len(x)

# Method to reduce a specified group using Rule1.
def rule1(group):
  ### IMPLEMENT THIS FUNCTION ###

  # Begin by assuming the matrix is unchanged
  changed = False
  
  # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
  # have same number of duplicate sets in a group (row, column, square) as 
  # the cardinality of the duplicate set size, then they must each get one 
  # value from the duplicate set. In this case the values of the duplicate 
  # set may be removed from all the other sets in the group. 

  # go through all the elements of the group which are already sorted from
  # smallest to largest cardinality
  for cell in group:
    
    # get the cardinality of the set
    card = cardinality(cell)    

    # Initialize a list to store duplicate cells. Append the current cell to the list.
    duplicates = []
    duplicates.append(cell)

    # if there are cardinality sets with cardinality elements then the other
    # sets can't have any of these values in them since these sets will have
    # to each have one of the cardinality values
    # Go through the list of cells again, looking for duplicate cells.
    for duplicate in group:
          
      # If the duplicate cell has the same length of the current cell, check if they are equal.
      if len(duplicate) == len(cell) and duplicate.issuperset(cell) and duplicate != cell:

        # If the duplicate cell is equal to the current cell, append it to the list of duplicates.
        duplicates.append(duplicate)

    # go through the sets and for each set different from the given set take
    # out all the elements that are in given set
    # If the length of the list of duplicates equals the cardinality of the current cell, remove possible values from other cells.
    if len(duplicates) == card and card > 1:
        for otherCell in group:

          # Create a copy of the other cell before deleting items.
          copy = HashSet(otherCell)
          copy.difference_update(cell)

          # After deleting, if the number of items in the "other cell" is greater than zero, continue with deletion, otherwise do nothing.
          if otherCell not in duplicates and len(copy) > 0:
            otherCell.difference_update(duplicates[0])

            # We have changed the matrix, set changed to true.
            changed = True

  return changed

# Method to reduce a specified group using Rule2.
def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  # Begin by assuming the matrix is unchanged.
  changed = False

  # RULE 2 - Reduce set size by throwing away elements that appear in other
  # sets in the group
  # pick an element of the group
  for cell in group:

    # for all the other elements of the group remove the elements that appear
    # in other elements of the group. These can be satisfied by other elements
    # of the group
    # If the cardinality of the cell is 1 (Cell is fully reduced), remove that value from the other cells.
    if len(cell) == 1:
      for otherCell in group:
            
        # Check to make sure the "Other Cell" is not the current cell"
        if otherCell != cell:
              
          # Remove the current cells value from the other cell.
          otherCell.difference_update(cell)

          # We have changed the matrix, set changed to true.
          changed = True
      # Move to the next cell in the group.
      continue

    # Create a copy of the current cell.
    copy = HashSet(cell)

    # Loop through the other cells in the group.
    for otherCell in group:
          
      # Check to make sure the "Other Cell" is not the current cell.
      if otherCell != cell:
        
        # Remove any values found in the other cells, from the current cell. (This is not permanent)
        copy.difference_update(otherCell)
      
    # When done, if there is one value left then it can only be satisfied by
    # this cell. This is a most constrained rule. If end up with 0 elements,
    # then not enough information yet to constrain this choice. If didn't
    # improve the situation at all, let's continue looking at other elements
    # in the row.
    
    # If the copy contains only one value after deletion, that value must belong in that cell.
    if len(copy) == 1:
      # Clear the values in the actual cell, not the copy.
      cell.clear()

      # Add the value from the copy to the cell.
      for item in copy:
        cell.add(item)

      # We have changed the matrix, set changed to true.
      changed = True 

  return changed

# Method that calls the Rule1 and Rule2 methods until the puzzle is solved.
def reduceGroup(group):
  changed = False 

  # this sorts the sets from smallest to largest based cardinality.
  group.sort(key=cardinality)

  # Run rule2 on the group.
  changed = rule2(group)

  # Run rule1 on the group.
  changed = rule1(group)
  
  return changed

# Method to iterate through each group until each is reduced correctly.
def reduceGroups(groups):
  changed = False
  for group in groups:
    if reduceGroup(group):
      changed = True   
  return changed

# Method to begin reducing each group
def reduce(matrix):
    changed = True
    groups = getGroups(matrix)
    
    while changed:
        changed = reduceGroups(groups)

# Method to print the unsolved and solved puzzle.
def printMatrix(matrix):
  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) != 1:
        sys.stdout.write("x ")
      else:
        for k in matrix[i][j]:
          sys.stdout.write(str(k) + " ")
    sys.stdout.write("\n")

###########################################################
# Main Program
###########################################################
def main():
  # Open the specified file
  file = open(sys.argv[1], "r")

  # Initialize an empty matrix and populate it based on values from the given sudoku file.
  matrix = []
  for line in file:
    lst = line.split()
    row = []

    for val in lst:
      if val == 'x':
        s = HashSet(range(1,10))
      else:
        s = HashSet([eval(val)])
      row.append(s)

    matrix.append(row)

  # Print the unsolved Sudoku puzzle.
  print("Solving this puzzle:")
  printMatrix(matrix)

  # Begin reducing the matrix until the puzzle is solved.
  reduce(matrix)

  # Print the solved Sudoku puzzle.
  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
