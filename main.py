import gmplot 
import pandas as pd

# arquivo = r"data\clientes.xlsx"
arquivo = r"data\world_country_and_usa_states_latitude_and_longitude_values.csv"
dataset = pd.read_csv(arquivo)
# dataset = pd.read_excel(arquivo)

latitudes = dataset.loc[:, 'latitude'][:5000] #CRIAR LISTA C/ OS VALORES DA COLUNA LATITUDE (APENAS OS PRIMEIROS 5000 REGISTROS)
longitudes = dataset.loc[:, 'longitude'][:5000] #CRIAR LISTA C/ OS VALORES DA COLUNA LATITUDE (APENAS OS PRIMEIROS 5000 REGISTROS)

#VARIÁVEIS COM OS DEFAULTS P/ PLOT DO MAPA
lat, lng = -23, -45 
zoom = 2

#PLOT DO MAPA 
gmap = gmplot.GoogleMapPlotter(lat, lng, zoom)
gmap.scatter(latitudes, longitudes, 'red', size = 20)

# # gmap.apikey = '<API-KEY>'
gmap.draw('result/mapa.html')




