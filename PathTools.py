import os
import pathlib

class PathTools():
     # def __init__(self, path):
     #    self.path = path
     
     def __validate_path(self, path: str)->bool:
          if os.path.exists(path):
               return True
          else:
               return False
          
          
     def getAbsolutePath(self, path: str):

          if not isinstance(path, str):
               raise TypeError('A string was expected, but an int was passed')
               return
          

          home = pathlib.Path.cwd().home()
          pathComplet = home.joinpath(home.__str__()+f'{path}')

          if self.__validate_path(pathComplet):
               return pathComplet
          else:
               raise ValueError('Directory not found on file system')

          

     
     

