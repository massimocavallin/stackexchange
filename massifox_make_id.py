import pandas as pd
import numpy as np
import sys
import requests, sys,os
import mygene

def make_id(row): 
    if row['ensembl'] is np.nan and row['ensembl.gene'] is np.nan:  # 1) If both the value of 'ensembl' and 'ensembl.gene' is 'NaN', then output is "Not found".
        return 'Not Found'
    elif row['ensembl'] is np.nan:                                  # 2) If the value of 'ensembl' is 'NaN', then just print the value of 'ensembl.gene'
        return row['ensembl.gene']
    else:                                                           # 3) (otherwise) If the value of 'ensembl.gene' is 'NaN', then print first part of the value of 'ensembl' 
        return row['ensembl'][0]['gene']


read_content=open("protein_HRPD.txt",'r').read()
all_data= read_content.splitlines()
unique_gene_name = list(set(all_data))

mg = mygene.MyGeneInfo()
xli = unique_gene_name
#xli = ['MAPK3','Dnmt3b','IFNA1', 'MYC','IL2', 'FSHB', 'SRSF2', 'PTPRN2', 'CREB1', 'PIK3R1','IL2','CTNNB1','ADAM12']
s=mg.querymany(xli, scopes="symbol", fields=[ "ensembl.gene"], species="human", as_dataframe=True)

s['id'] = s.apply(lambda x: make_id(x), axis=1)
print(s['id'])
