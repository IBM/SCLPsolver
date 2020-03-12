

class foo():

    def _do_foo(self):
        print("foo")

    def do_foo(self):
        self._do_foo()

class bar(foo):

    def _do_foo(self):
        print("bar")


a = bar()
a.do_foo()