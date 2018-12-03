import os


class Config(dict):
    
    def __init__(self, filename):
        if os.path.exists(filename):
            self.filename = filename
        else:
            print("No such file '{}'".format(x), file=sys.stderr)
        
        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip()
                    dict.__setitem__(self, key, val)
    
    def __str__(self):
        return "; ".join(["{} = {}".format(i, self[i]) for i in self])
    
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self._write_to_file()
        
    def __delitem__(self, key):
        print("called")
        dict.__delitem__(self, key)
        self._write_to_file()

    def _write_to_file(self):
        with open(self.filename, "w") as f:
            f.truncate()
            for i in self:
                f.write("{} = {}\n".format(i, self[i]))
