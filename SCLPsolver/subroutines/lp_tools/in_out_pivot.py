class in_out_pivot():

    __slots__ =['in_', 'out_']

    def __init__(self):
        self.in_ = set()
        self.out_ = set()

    def pivot(self, in_, out_):
        if in_ in self.out_:
            self.out_.remove(in_)
        else:
            self.in_.add(in_)
        if out_ in self.in_:
            self.in_.remove(out_)
        else:
            self.out_.add(out_)

    def extr(self, set_out_, set_in_):
        for p in self.out_:
            if p in set_in_:
                set_in_.remove(p)
            else:
                set_out_.add(p)
        for p in self.in_:
            if p in set_out_:
                set_out_.remove(p)
            else:
                set_in_.add(p)
        self.in_ = set_out_
        self.out_ = set_in_