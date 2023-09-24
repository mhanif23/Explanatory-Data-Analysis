import pandas as pd

data = pd.read_csv('G:\FileNif\DataMining\diskominfo-od_17142_jml_layanan_aplikasi_umum_aplikasi_khusus__perangkat_d_data.csv')

data.info()

data.head(5)

data.describe()