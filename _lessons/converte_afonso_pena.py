import pandas as pd
import geopandas as gpd

df = pd.read_csv('../../fcd/assets/05-BabyPandas/data/20240301_feira_afonso_pena_barraca.csv', sep=';', na_values='N-E')
area = gpd.GeoSeries.from_wkt(df['GEOMETRIA']).area * 3.28084
df = df[['ID_FEIRA_AFONSO_PENA_BARRACA', 'CODIGO_VAGA', 'NOME_FANTASIA',
       'NOME_FEIRANTE', 'NOME_PREPOSTO', 'NOME_SETOR', 'PRODUTOS']]
df['NUMERO_PRODUTOS_CADASTRADOS'] = df['PRODUTOS'].str.count(', ') + 1
df['AREA'] = area
df.dropna().to_csv('afonso_pena.csv', index=False)

