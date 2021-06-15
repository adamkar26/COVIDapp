# Instrukcja instalacji aplikacji 

## Instalacja z użyciem dockera
1. Zainstaluj Dockera
2. Z poziomu głównego folderu aplikacji wykonaj komendę
`docker compose up`

3. Aplikacja powinna się uruchomić na porcie 8000
4. Z poziomu terminala kontenera dockera wykonaj poniższe komedny:

    `pip install tensorflow`
   
   `pip install scikit-image`
5. Dokonaj migracji bazy danych wykonując polecenia:
    
    `python manage.py makemigrations`
   
    `python manage.py migrate `
6. Utwórz konto administatora systemu:
    
    `python manage.py createsuperuser`
   
## Instalacja z użyciem loklanego środowiska
1. Zainstaluj wszystkie zależności
2. W pliku `COVIDapp/settings.py` podaj ustawienia bazy danych
3. Dalsze kroki tak samo jak w przypadku użycia Dockera