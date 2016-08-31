import unittest
import min_heap

class TestMinHeapMethods(unittest.TestCase):
  def setUp(self):
    self.emptyBH= min_heap.BinaryHeap()
    self.bh = min_heap.BinaryHeap()
    self.bh.insert(5)
    self.bh.insert(7)
    self.bh.insert(3)
    self.bh.insert(11)


  def test_is_empty(self):
    self.assertTrue(self.emptyBH.is_empty())
    self.assertFalse(self.bh.is_empty())

  def test_size(self):
    self.assertEqual(self.emptyBH.size(), 0)
    self.assertEqual(self.bh.size(), 4)

  def test_find_min(self):
    self.assertEqual(self.bh.find_min(), 3)

  def test_del_min(self):
    self.assertEqual(self.bh.del_min(), 3)
    self.assertEqual(self.bh.size(), 3)


if __name__ == '__main__':
  unittest.main()
