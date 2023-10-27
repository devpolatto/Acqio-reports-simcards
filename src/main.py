import argparse

from modules.PathTools import PathTools

from modules.concatFiles import mergerFiles

def main():

     parser = argparse.ArgumentParser(description='Passagem de argumento para a execução do script')
     parser.add_argument('-p', '--path', type=str, help="Caminho até os arquivos: EX: '/Downloads/diretorio'")
     args = parser.parse_args()

     pathTools = PathTools()
     pathToFiles: str = ''

     try: 
          pathToFiles = pathTools.getAbsolutePath(args.path)
     except Exception as error:
          print('Deu falha -> ', error)


     df = mergerFiles(pathToFiles, ',', '.csv')

     print(df['metric.ICCID'])

     

if __name__ == '__main__':
     main()