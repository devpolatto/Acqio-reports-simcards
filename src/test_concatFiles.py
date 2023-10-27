import unittest
import pandas as pd

from modules.concatFiles import mergerFiles
from modules.PathTools import PathTools

class ConcatFiles(unittest.TestCase):

     def test_should_dataFrame_instance_must_be_returned(self):

          pathToFiles = PathTools().getAbsolutePath('/Documents/reports_simcards')

          result = mergerFiles(pathToFiles, ',', '.csv' )
          self.assertIsInstance(result, pd.DataFrame)



if __name__ == '__main__':
    unittest.main(verbosity=3)