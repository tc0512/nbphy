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
class Time: #时间t，传入s
    def __init__(self, val):
        self.val = val
    def century(self):
        return self.val/3153600000
    def year(self):
        return self.val/31536000
    def day(self):
        return self.val/86400
    def hour(self):
        return self.val/3600
    def minute(self):
        return self.val/60
    def millisecond(self):
        return self.val*1000
    def microsecond(self):
        return self.val*1000000
    def nanosecond(self):
        return self.val*1000000000
