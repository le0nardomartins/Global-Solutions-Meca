import folium
from geopy.geocoders import Nominatim
import requests
import webbrowser

def obter_coordenadas(endereco):
    geolocator = Nominatim(user_agent="hospital_locator")

    try:
        location = geolocator.geocode(endereco, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print("Coordenadas não encontradas para o endereço:", endereco)
            return None
    except Exception as e:
        print("Erro ao obter coordenadas:", str(e))
        return None

def obter_mapa(coordenadas, hospitais):
    mapa = folium.Map(location=coordenadas, zoom_start=13)

    folium.Marker(
        location=coordenadas,
        popup='Sua localização',
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

    for hospital in hospitais:
        folium.Marker(
            location=[hospital['geometry']['location']['lat'], hospital['geometry']['location']['lng']],
            popup=hospital['name'],
            icon=folium.Icon(color='red')
        ).add_to(mapa)

    return mapa

def salvar_mapa(mapa, file_path='mapa_hospitais.html'):
    mapa.save(file_path)

def obter_hospitais_proximos(api_key, coordenadas, raio=5000, tipo='hospital'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': f'{coordenadas[0]},{coordenadas[1]}',
        'radius': raio,
        'type': tipo,
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        hospitais = response.json().get('results', [])
        return hospitais
    except requests.exceptions.RequestException as e:
        print("Erro ao obter hospitais próximos:", str(e))
        return []

def gerar_mapa_hospitais(endereco_usuario):
    coordenadas_usuario = obter_coordenadas(endereco_usuario)

    if coordenadas_usuario:
        api_key = 'AIzaSyCKBpEQOuC01QuSyC_jX_MUzbuygWwwEic'
        hospitais_proximos = obter_hospitais_proximos(api_key, coordenadas_usuario)

        mapa = obter_mapa(coordenadas_usuario, hospitais_proximos)
        salvar_mapa(mapa)

        # Abre automaticamente a página HTML no navegador
        webbrowser.open('mapa_hospitais.html', new=2)

        print("O mapa foi gerado em HTML.")
    else:
        print("Não foi possível obter coordenadas para o endereço fornecido.")

if __name__ == "__main__":
    endereco_usuario = input("Digite o endereço ou localização: ")
    gerar_mapa_hospitais(endereco_usuario)
