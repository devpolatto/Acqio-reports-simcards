import argparse

from PathTools import PathTools

def main():

     parser = argparse.ArgumentParser(description='Passagem de argumento para a execução do script')
     parser.add_argument('-p', '--path', type=str, help="Caminho até os arquivos: EX: '/Downloads/diretorio'")
     args = parser.parse_args()

     pathTools = PathTools()

     try: 
          absolutePath = pathTools.getAbsolutePath(args.path)
          print(absolutePath)
     except Exception as error:
          print('Deu falha -> ', error)

if __name__ == '__main__':
     main()