class Displacement: #距离s，传入m
    def __init__(self, val):
        self.val = val
    def kilometre(self):
        return self.val/1000
    def decimetre(self):
        return self.val*10
    def centimetre(self):
        return self.val*100
    def millimetre(self):
        return self.val*1000
    def micrometre(self):
        return self.val*1000000
    def nanometre(self):
        return self.val*1000000000
