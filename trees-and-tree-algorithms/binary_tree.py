class BinaryTree():
  # Implementation of a Binary Tree using Nodes as internal storage technique

  def __init__(self, root):
    self.key = root
    self.left_child = None
    self.right_child = None

  def insert_left(self, new_node):
    '''
    Adds a left subtree to the root of a Tree
    If the tree already has a left subtree,
    it is pushes it down as the left-subtree of the subtree
    '''
    if self.left_child == None:
      self.left_child = BinaryTree(new_node)
    else:
      new_left_child = BinaryTree(new_node)
      new_left_child.left_child = self.left_child
      self.left_child = new_left_child

  def insert_right(self, new_node):
    '''
    Adds a right subtree to the root of a Tree
    If the tree already has a right subtree,
    it is pushes it down as the right-subtree of the subtree
    '''
    if self.right_child == None:
      self.right_child = BinaryTree(new_node)
    else:
      new_right_child = BinaryTree(new_node)
      new_right_child.right_child = self.right_child
      self.right_child = BinaryTree(new)

  def get_right_child(self):
    ''' Returns the current node's right child'''
    return self.right_child

  def get_left_child(self):
    ''' Returns the current node's left child '''
    return self.left_child

  def set_root_val(self, new_val):
    self.key = new_val

  def get_root_val(self):
    ''' Returns the value stored at the node'''
    return self.key

def main():
  btree = BinaryTree('a')
  btree.insert_left('b')
  btree.insert_right('c')

  l_child = btree.get_left_child()
  l_child.insert_right('d')

  r_child = btree.get_right_child()
  r_child.insert_left('e')
  r_child.insert_right('f')

  assert(btree.get_root_val() == 'a')
  assert(btree.get_left_child().get_root_val() == 'b')
  assert(btree.get_right_child().get_root_val()  == 'c')
  assert(btree.get_left_child().get_right_child().get_root_val()  == 'd')
  assert(btree.get_right_child().get_left_child().get_root_val()  == 'e')
  assert(btree.get_right_child().get_right_child().get_root_val()  == 'f')
  print('Test Pass')



if __name__ == '__main__':
  main()
