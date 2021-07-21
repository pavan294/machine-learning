import os
import re
import pandas as pd
import numpy as np
import pdcast as pdc
output = pd.DataFrame()
pattern1 = "^\d{14}_\d{8}_11XEWETRADING--L_an_11XDOW-STADE---D_TenneT.csv$"
pattern2 = "^\d{14}_\d{8}_11XDOW-STADE---D_an_11XEWETRADING--L_TenneT.csv$"
for file in os.listdir():
    if(re.match(pattern1, file) or re.match(pattern2, file)):
        df = pd.read_csv(file, delimiter=";", 
                         names=["A", "B", "C", "D", "E", "F", "G", 
                                "H", "I", "J"])
        df_downcast = pdc.downcast(df)
        for index, row in df_downcast.iterrows():
            if float(row['H'].replace(',', ".")) > 0:
                output = output.append(row, ignore_index=True)
output_downcast = pdc.downcast(output)
output_downcast.to_csv("data.csv", sep=";", index=False, header=None)
