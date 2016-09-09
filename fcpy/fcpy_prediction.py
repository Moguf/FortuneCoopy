
import sklearn

from sqliteater import SQLiteater

class FcpyPrediction(object):
    def __init__(self):
        self.db = SQLiteater()
        self.db.openDB('../data/mystocks.db')
    
    def run(self):
        pass

    def close(self):
        self.db.close()

if __name__ == '__main__':
    tmp = FcpyPrediction()
    tmp.run()
    tmp.close()

    
