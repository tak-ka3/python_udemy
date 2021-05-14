# テストケースを中に書くことによって、そのメソッドの使い方がすぐにわかる
# どういう時にエラーが出るのか、そして入力パターンなどがよくわかる
class Cal(object):
  def add_num_and_double(self, x, y):
    """Add and double

    >>> c = Cal()
    >>> c.add_num_and_double(1, 2)
    5
    >>> c.add_num_and_double('1', '2')
    Traceback (most recent call last):
    ...
    ValueError
    """
    if type(x) is not int or type(y) is not int:
      raise ValueError
    result = x+y
    result *= 2
    return result

if __name__ == "__main__":
  import doctest
  doctest.testmod()