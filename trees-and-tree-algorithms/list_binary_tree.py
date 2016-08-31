# Implementation of a Binary Tree using Lists as internal storage technique

def binary_tree(r):
  # Constructs a list with root node at index[0]
  # and two empty sublists for the children

  return [r, [], []]

def insert_left(root, new_branch):
  # Adds a left subtree to the root of a Tree
  # If the tree already has a left subtree,
  # it is pushes it down as the left-subtree of the new_branch

  r = root.pop(1)
  if len(r) > 0:
    root[1] = [new_branch, r, []]
  else:
    root[1] = [new_branch, [], []]

def insert_right(root, new_branch):
  # Adds a right subtree to the root of a Tree
  # If the tree already has a right subtree,
  # it is pushes it down as the right-subtree of the new_branch
  r = root.pop(2)
  if len(r) > 0:
    root[2] = [new_branch, [], r]
  else:
    root[2] = [new_branch, [], []]

def get_root_val(root):
  return root[0]

def set_root_val(root, val):
  root[0] = val

def get_left_child(root):
  return root[1]

def get_right_child(root):
  return root[2]


def main():

  root = binary_tree(1)
  insert_left(root, 11)
  insert_right(root, 21)
  insert_left(root, 10)
  insert_right(r, 20)
  first_right_child = get_right_child(root)
  insert_left(first_right_child, 21)
  first_left_child = root.get_left_child()
  insert_right(first_left_child, 12)

if __name__ == '__main__':
  main()
