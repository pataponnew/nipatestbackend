class ErrException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    def __str__(self):
        return repr(str(self.code) + " : " + self.msg)