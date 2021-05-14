import unittest

releasename = 'lesson'
import calculation

class CalTest(unittest.TestCase):
  def setUp(self):
    print('setUp')
    self.cal = calculation.Cal()

  def tearDown(self):
    print('clean up')
    del self.cal

  # これでテストをスキップすることも可能
  @unittest.skipIf(releasename=='lesson', 'skip!!')
  #@unittest.skip('skip!')
  def test_add_num_and_double(self):
    cal = calculation.Cal()
    self.assertEqual(cal.add_num_and_double(1, 1), 4)

  def test_add_num_and_double_raise(self):
    cal = calculation.Cal()
    with self.assertRaises(ValueError):
      cal.add_num_and_double('1', '1')

if __name__ == '__main__':
  unittest.main()