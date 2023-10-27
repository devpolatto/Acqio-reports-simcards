import argparse
import pandas as pd

from modules.PathTools import PathTools

from modules.concatFiles import mergerFiles

def main():

     parser = argparse.ArgumentParser(description='Passagem de argumento para a execução do script')
     parser.add_argument('-p', '--path', type=str, help="Caminho até os arquivos: EX: '/Downloads/diretorio'")
     args = parser.parse_args()

     pathTools = PathTools()

     try: 
          pathToFiles = pathTools.getAbsolutePath(args.path)
     except Exception as error:
          print('Deu falha -> ', error)


     df = mergerFiles(pathToFiles, ',', '.csv') # return the dataFrame

     df = df.drop_duplicates(subset='metric.ICCID', keep='first') # Remove data duplicates

     df['metric.ICCID'] = df['metric.ICCID'].astype(str) # Convert metric.ICCID column form Dtype object to str

     df['@timestamp'] = pd.to_datetime(df['@timestamp'], format='%b %d, %Y @ %H:%M:%S.%f') # converte pro formato datetime

     df['@timestamp_formatted'] = df['@timestamp'].dt.strftime('%d/%m/%Y')

     move_to_position = 1
     column = df['@timestamp_formatted']
     columnData = 'Data'

     if columnData in df.columns:
          df.insert(move_to_position, 'Data', column)

     df.insert(move_to_position, 'Data', column)
     df.drop('@timestamp', axis=1, inplace=True)
     df.drop('@timestamp_formatted', axis=1, inplace=True)

     # df.to_csv(f'{pathToFiles}/newMergedFile.csv', index=False)
     df.to_excel(f'{pathToFiles}/newMergedFile.xlsx', index=False)
     print(df.head())
     print(df.info())


__version__="0.0.1"

if __name__ == '__main__':
     main()

