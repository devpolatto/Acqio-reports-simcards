import unittest

from modules.PathTools import PathTools

class TestPathTools(unittest.TestCase):

     def test_given_invalid_path_should_error_message_must_be_returned(self):

          pathTools = PathTools()
          dataInputs: tuple(str) = ('/Document', r'\Document', 'Document', '~Document')

          for dataInput in dataInputs:
               with self.assertRaises(ValueError):
                    pathTools.getAbsolutePath(dataInput)


     def test_given_a_value_of_type_other_than_string_should_error_message_must_be_returned(self):

          pathTools = PathTools()
          dataInput: int = 100

          with self.assertRaises(TypeError):
               pathTools.getAbsolutePath(dataInput)


if __name__ == '__main__':
    unittest.main(verbosity=3)
