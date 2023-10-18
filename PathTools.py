import os
import pathlib

class PathTools:
     # def __init__(self, path):
     #    self.path = path
     
     def __validate_path(self, path: str)->bool:
          if os.path.exists(path):
               return True
          else:
               return False
          
          
     def getAbsolutePath(self, path: str)->str:
          home = pathlib.Path.cwd().home()
          pathComplet = home.joinpath(home.__str__()+f'{path}')
          
          if self.__validate_path(pathComplet):
               return pathComplet
          else:
               return 'Caminho invalido'


          

     
     

