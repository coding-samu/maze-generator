# Usa un'immagine base di Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del progetto nella directory di lavoro
COPY / /app/maze_generator/
COPY requirements.txt /app/

# Installa le dipendenze necessarie
RUN pip install --no-cache-dir -r requirements.txt

# Definisci il comando di avvio per il container
CMD ["python", "maze_generator/maze.py"]
