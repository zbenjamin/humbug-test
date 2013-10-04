import time

class MyError(Exception):
    def __init__(self, error):
        self.error = error

def do_throw():
    raise MyError("foo")

start = time.time()
for i in xrange(1, 700):
    try:
        do_throw()
    except MyError:
        continue
print time.time() - start
