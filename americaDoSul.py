import geopandas as gpd
import folium
import mapclassify as mapc
import matplotlib as matplot
import os
from trabalho import Grafo 

diretorio_shapefile = "C:\Users\Usuário\Documents\materiais\5 periodo\grafos\trabalho/a__031_001_americaDoSul"

nome_arquivo_shapefile = "a__031_001_americaDoSul.shp"

caminho_arquivo_shapefile = os.path.join(
    diretorio_shapefile, nome_arquivo_shapefile)

mundo = gpd.read_file(caminho_arquivo_shapefile)

cores_grupos = {
    0: "red",
    1: "blue",
    2: "green",
    3: "purple"
}

mapeamento_cores_paises = {}

grafoAmericaDoSul = Grafo()

grupos_valores = grafoAmericaDoSul.americaDoSul()


for grupo, paises in grupos_valores.items():
    cor_grupo = cores_grupos.get(grupo, "black")
    for pais in paises:
        mapeamento_cores_paises[pais] = cor_grupo


mapa = folium.Map(location=[0, 0], zoom_start=2)

folium.GeoJson(mundo).add_to(mapa)


def estilo_paises(feature):
    nome_pais = feature["properties"]["NAME"]
    cor = mapeamento_cores_paises.get(nome_pais, "black")

    return {"fillColor": cor, "fillOpacity": 0.7}


folium.GeoJson(
    mundo,
    style_function=estilo_paises
).add_to(mapa)


folium.LayerControl().add_to(mapa)

mapa.save("mapa_colorido_americaDoSul.html")
mapa
