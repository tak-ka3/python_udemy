import logging
import threading
import time

logging.basicConfig(
  level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1():
  logging.debug('start')
  time.sleep(5)
  logging.debug('end')

def worker2(x, y=1):
  logging.debug('start')
  logging.debug(x)
  logging.debug(y)
  time.sleep(2)
  logging.debug('end')
  
if __name__ == '__main__':
  # 最初に始めるスレッドの定義
  t1 = threading.Thread(name='rename worker1', target=worker1)
  t1.setDaemon(True) # t1が終わるのも待たない
  t2 = threading.Thread(target=worker2, args=(100, ), kwargs={'y':200})
  # ここでスレッドをスタートさせる
  t1.start()
  t2.start()
  print('started')
  t1.join() # これをすることで例えデーモン化されたスレッドであってもちゃんと終了を待つ