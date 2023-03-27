# Provide your information as the values of these variables:
myName = 'Blake, Perrin'
myTechID = '10382316'
myTechEmail = 'bep020' #only your email id omit @latech.edu
###########################################################

import sys
from hashSet import HashSet

def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
    
  return col

def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])
        
  return square

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

def cardinality(x):
  return len(x)

def rule1(group):
      ### IMPLEMENT THIS FUNCTION ###

  changed = False
  
  # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
  # have same number of duplicate sets in a group (row, column, square) as 
  # the cardinality of the duplicate set size, then they must each get one 
  # value from the duplicate set. In this case the values of the duplicate 
  # set may be removed from all the other sets in the group. 

  
  # go through all the elements of the group which are alredy sorted from
  # smallest to largest cardinality
  for cell in group:
        
    # get the cardinality of the set
    card = cardinality(cell)    

    duplicates = []
    numDuplicates = 0

    duplicates.append(cell)
    # if there are cardinality sets with cardinality elements then the other
    # sets can't have any of these values in them since these sets will have
    # to each have one of the cardinality values
    for duplicate in group:
      if len(duplicate) == len(cell) and duplicate.issuperset(cell) and duplicate != cell:
        # print("Duplicate Items: ", end="")
        # for item in duplicate:
        #   print("{} ".format(item), end="")
        # print()
        # print("Cell Items: ", end="")
        # for item in cell:
        #   print("{} ".format(item), end="")
        # print()
        duplicates.append(duplicate)
      # duplicates.append(duplicate for duplicate in group if len(duplicate) == len(cell) and duplicate.issuperset(cell))
      # duplicates.append(cell)

    # go through the sets and for each set different from the given set take
    # out all the elements that are in given set
    if len(duplicates) == card and card > 1:
        for otherCell in group:
          # otherCell.difference_update(cell)

          # changed = True
          copy = HashSet(otherCell)
          copy.difference_update(cell)
          if otherCell not in duplicates and len(copy) > 0:
            otherCell.difference_update(duplicates[0])
            changed = True

  return changed
  
def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  # RULE 2 - Reduce set size by throwing away elements that appear in other
  # sets in the group


  # pick an element of the group
  for cell in group:

    # for all the other elements of the group remove the elements that appear
    # in other elements of the group. These can be satisfied by other elements
    # of the group
    if len(cell) == 1:
      for otherCell in group:
        if otherCell != cell:
          otherCell.difference_update(cell)
          changed = True
          # copy = HashSet(otherCell)
          # copy.difference_update(cell)
          # if len(copy) > 0:
          #   otherCell.difference_update(cell)
          #   changed = True
      continue
    copies = []
    cells = []
    copy = HashSet(cell)
    for otherCell in group:
      if otherCell != cell:
        # cell.difference_update(otherCell)
        # changed = True
        copy.difference_update(otherCell)
    if len(copy) == 1:
      cell.clear()
      for item in copy:
        cell.add(item)
      changed = True
    # complete = False
    # for copy in copies:
    #   if len(copy) > 1:
    #     complete = True
    #   else:
    #     complete = False
    # if complete == True:
    #   for i in range(len(copies)):
    #     copies[i].difference_update(cells[i])
    #     changed = True
          
        
  # When done, if there is one value left then it can only be satisfied by
  # this cell. This is a most constrained rule. If end up with 0 elements,
  # then not enough information yet to constrain this choice. If didn't
  # improve the situation at all, let's continue looking at other elements
  # in the row. 

  return changed

# def rule1(group):
#   ### IMPLEMENT THIS FUNCTION ###

#   changed = False
  
#   # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
#   # have same number of duplicate sets in a group (row, column, square) as 
#   # the cardinality of the duplicate set size, then they must each get one 
#   # value from the duplicate set. In this case the values of the duplicate 
#   # set may be removed from all the other sets in the group. 

  
#   # go through all the elements of the group which are already sorted from
#   # smallest to largest cardinality
#   for i in range(len(group)):
#     duplicates = []
#     num_duplicates = 0
#     duplicates.append(group[i])
#     for j in range(len(group)):
#       if i == j:
#         continue
#       else:
#           if len(group[i]) == len(group[j]):
#             if group[i].issuperset(group[j]):
#               # print("duplicate found!")
#               # print("Group {} Items: {}".format(i, group[i].items))
#               # print("Group {} Items: {}".format(j, group[j].items))
#               # print("appending duplicate set")
#               duplicates.append(group[j])
#               num_duplicates += 1
#     print("Cardinality: {}".format(cardinality(group[i])))
#     print("Length: {}".format(len(duplicates)))
#     if cardinality(group[i]) == len(duplicates):
#       for cell in group:
#         if cell not in duplicates and len(duplicates) > 1:
#           cell.difference_update(duplicates[1])
#           changed = True
#           # copy = HashSet(cell)
#           # copy.difference_update(duplicates[0])
#           # if cardinality(copy) >= 1:
#           #   print()
#           #   print("reducing set, len = card")
#           #   print()
#           #   cell.difference_update(duplicates[0])
#           #   changed = True



#     #     else:
#     #       if len(group[i]) == len(group[j]):
#     #         if group[i].issuperset(group[j]):
#     #           changed = True
#     #         else:
#     #           group[j].difference_update(group[i])
#     #           changed = True
#     # else:
#     #   changed = False

#     # if there are cardinality sets with cardinality elements then the other
#     # sets can't have any of these values in them since these sets will have
#     # to each have one of the cardinality values 

#   # go through the sets and for each set different from the given set take
#   # out all the elements that are in given set

#   return changed
  
# def rule2(group):
#   ### IMPLEMENT THIS FUNCTION ###

#   changed = False
#   # RULE 2 - Reduce set size by throwing away elements that appear in other
#   # sets in the group

#   for cell in group:
#     if len(cell) == 1:
#       for cell2 in group:
#         if cell2 != cell:
#           cell2.difference_update(cell)
#       print(cardinality(cell))
#     else:
#       otherCells = []
#       for otherCell in group:
#         if otherCell != cell and len(otherCell) > 1:
#           otherCells.append(otherCell)

#       for otherCell in otherCells:
#         copy = HashSet(cell)
#         copy.difference_update(otherCell)
#         if cardinality(copy) >= 1:
#           cell.difference_update(otherCell)
#           changed = True




#   # # pick an element of the group
#   # for i in range(len(group)):
#   #   if cardinality(group[i]) == 1:
#   #     print("Cardinality = 1")
#   #     print()
#   #     for j in range(len(group)):
#   #       if i == j:
#   #         changed = False
#   #         continue
#   #       else:
#   #         for item in group[i]:
#   #           group[j].discard(item)
#   #         changed = True
#   #   else:
#   #     for j in range(len(group)):
#   #       print("i: {} | j: {}".format(i, j))
#   #       if i == j:
#   #         print("i = j")
#   #         print()
#   #         changed = True
#   #         continue
#   #       else:
#   #         print("Creating a Copy")
#   #         copy = group[i].difference(group[j])
#   #         if cardinality(copy) == 0:
#   #           print("Cardinality = 0")
#   #           print()
#   #           changed = True
#   #         else:
#   #           print("Deleting Items")
#   #           group[i].difference_update(group[j])
#   #           print(cardinality(group[i]))
#   #           print(group[i].items)
#   #           print()
#   #           changed = True
#   #         # print(cardinality(group[i]))
#     print(cardinality(cell))
#   #   # print("Group {} After Deleting Elements:".format(i))
#   #   # print(group[i].items)
#   # print()
#   # # print()

#   # #   if cardinality(group[i]) == 1:
#   # #     for j in range(i, len(group)):
#   # #         for item in group[i]:
#   # #           group[j].discard(item)
#   # #   print(cardinality(group[i]))
#   # #   if cardinality(group[i]) == 1:
#   # #       changed == 
#   print()
            
            
        

#   # for all the other elements of the group remove the elements that appear
#   # in other elements of the group. These can be satisfied by other elements
#   # of the group

#   # When done, if there is one value left then it can only be satisfied by
#   # this cell. This is a most constrained rule. If end up with 0 elements,
#   # then not enough information yet to constrain this choice. If didn't
#   # improve the situation at all, let's continue looking at other elements
#   # in the row. 

#   return changed

# def rule1(group):
#     changed = False
#     # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
#     # have same number of duplicate sets in a group (row, column, square) as 
#     # the cardinality of the duplicate set size, then they must each get one 
#     # value from the duplicate set. In this case the values of the duplicate 
#     # set may be removed from all the other sets in the group. 

#     # go through all the elements of the group which are already sorted from
#     # smallest to largest cardinality
#     for s in sorted(group, key=len):

#         # get the cardinality of the set
#         cardinality = len(s)

#         # if there are cardinality sets with cardinality elements then the other
#         # sets can't have any of these values in them since these sets will have
#         # to each have one of the cardinality values
#         if sum(len(t) == cardinality for t in group) == cardinality:
#             # go through the sets and for each set different from the given set take
#             # out all the elements that are in given set
#             for t in group:
#                 if t != s:
#                     for elem in s:
#                         if elem in t:
#                             t.remove(elem)
#                             changed = True

#     return changed

# def rule2(group):
#     changed = False
#     # RULE 2 - Reduce set size by throwing away elements that appear in other
#     # sets in the group

#     # pick an element of the group
#     for s in group:
#         # create a set of all the elements in the other sets in the group
#         other_elems = HashSet(elem for t in group if t != s for elem in t)

#         # remove the elements that appear in other sets in the group
#         old_elems = HashSet(s)
#         s.difference_update(other_elems)

#         # When done, if there is one value left then it can only be satisfied by
#         # this cell. This is a most constrained rule. If end up with 0 elements,
#         # then not enough information yet to constrain this choice. If didn't
#         # improve the situation at all, let's continue looking at other elements
#         # in the row. 
#         if len(s) == 1:
#             # s.clear()
#             # s.update(old_elems)
#             changed = True
#         elif len(s) == 0:
#             s.update(old_elems)
    
#     return changed


def reduceGroup(group):
  changed = False 
  # this sorts the sets from smallest to largest based cardinality
  group.sort(key=cardinality)
  # print("Before Simplifying with Rule 2")
  # for cell in group:
  #   for item in cell:
  #     print("{} ".format(item), end="")
  #   print()
  # print()
  changed = rule2(group)
  # print("Before Simplifying with Rule 1")
  # for cell in group:
  #   for item in cell:
  #     print("{} ".format(item), end="")
  #   print()
  # print()
  changed = rule1(group)
  # print("After Simplifying")
  # for cell in group:
  #   for item in cell:
  #     print("{} ".format(item), end="")
  #   print()
  # print()
  
  return changed

def reduceGroups(groups):
  changed = False
  for group in groups:
    if reduceGroup(group):
      changed = True
      
  return changed

def reduce(matrix):
    changed = True
    groups = getGroups(matrix)
    
    while changed:
        changed = reduceGroups(groups)

def printMatrix(matrix):
  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) != 1:
        sys.stdout.write("x ")
      else:
        for k in matrix[i][j]:
          sys.stdout.write(str(k) + " ")

    sys.stdout.write("\n")

def main():
  file = open(sys.argv[1], "r")
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

  print("Solving this puzzle:")
  printMatrix(matrix)

  # groups = getGroups(matrix)
  # group = groups[26]
  # print()
  # print("Before Simplifying")
  # for cell in group:
  #   for item in cell:
  #     print("{} ".format(item), end="")
  #   print()
  # rule2(group)
  # rule1(group)
  # print("After Simplifying")
  # for cell in group:
  #   for item in cell:
  #     print("{} ".format(item), end="")
  #   print()
  reduce(matrix)

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
