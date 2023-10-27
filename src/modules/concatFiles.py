import pandas as pd
import os

def mergerFiles(pathDir: str, delimiter: str, extension: str = '.csv', verbose=False):

     dataFiles = [f for f in os.listdir(pathDir) if f.endswith('.csv')]

     fileInfo = []
     merged_df = pd.DataFrame()

     for dataFile in dataFiles:
          filePath = os.path.join(pathDir, dataFile)
          df = pd.read_csv(filePath, delimiter=",")

          merged_df = pd.concat([merged_df, df], ignore_index=True)
          # merged_df.to_csv(f'{pathDir}/{outputFileName}', index=False)

          # if verbose:
          #      num_rows, num_columns = df.shape
          #      column_names = df.columns.tolist()
          #      csvFileInfoJson = {
          #           "File": csvPath, 
          #           "Num_rows": num_rows, 
          #           "Num_Columns": num_columns,
          #           "Columns_List": column_names
          #      }
          #      csvFileInfo.append(csvFileInfoJson)
               
          #      for info in csvFileInfo:
          #           print(info)
               
     
     return merged_df