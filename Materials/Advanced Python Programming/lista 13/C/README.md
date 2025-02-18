Skorzystałem z Sphinx 

Instalacja

pip install sphinx

Przechodzimy do katalogu z projektem i uruchamiamy 

sphinx-quickstart

Edytujemy plik conf.py i dodajem do listy "extensions" 

'sphinx.ext.autodoc'

Urzywamy 

sphinx-apidoc -o <katalog_wyjsciowy> <sciezka_do_modulow>

Budujemy 

sphinx-build -b html <katalog_zrodlowy> <katalog_wyjsciowy>
