import pandas as pd
import matplotlib.pyplot as plt
import requests


# 1. Consultar la API
respuesta = requests.get(
    'http://127.0.0.1:5000/votes/statistics'
)


# 2. Convertir la respuesta a JSON
datos = respuesta.json()


# 3. Convertir los resultados en una tabla de Pandas
df = pd.DataFrame(datos['results'])


# 4. Crear la gráfica
df.plot(
    x='name',
    y='total_votes',
    kind='bar',
    legend=False
)


# 5. Nombre de los ejes
plt.xlabel('Candidatos')
plt.ylabel('Votos')


# 6. Título
plt.title('Estado actual de los votos')


# 7. Girar los nombres de los candidatos
plt.xticks(rotation=45)


# 8. Ajustar la gráfica
plt.tight_layout()


# 9. Mostrar la gráfica
plt.show()