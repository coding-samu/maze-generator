# Usa l'immagine ufficiale di PostgreSQL
FROM postgres:13

# Copia il file di inizializzazione SQL nella directory appropriata
COPY init.sql /docker-entrypoint-initdb.d/

# Specifica una variabile d'ambiente per la password dell'utente "postgres"
ENV POSTGRES_PASSWORD=mysecretpassword
