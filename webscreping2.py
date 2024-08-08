import requests
from bs4 import BeautifulSoup

# URL de la sección "Deportes" del periódico Excelsior
url = 'https://www.excelsior.com.mx/adrenalina'

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar los artículos de la sección "Deportes"
    articles = soup.find_all('article')

    # Extraer la información de los artículos
    for article in articles:
        # Extraer el título
        title_tag = article.find('h2', class_='title')
        title = title_tag.text.strip() if title_tag else 'Sin título'

        # Extraer el resumen
        summary_tag = article.find('p', class_='summary')
        summary = summary_tag.text.strip() if summary_tag else 'Sin resumen'

        # Extraer el enlace
        link_tag = article.find('a')
        link = link_tag['href'] if link_tag else 'Sin enlace'

        print(f'Título: {title}')
        print(f'Resumen: {summary}')
        print(f'Enlace: {link}')
        print('---')
else:
    print(f'Error al acceder a la página: {response.status_code}')