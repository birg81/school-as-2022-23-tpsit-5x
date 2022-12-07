# FastAPI (test)

Prima di procedere forse è il caso di modificare il contenuto del file batch, in quanto questi era configurato per funzionare col pc della mia rete con IP 192.168.1.58 e col browser predefinito che adopero al solo scopo di avviare automaticamente la pagina sul IP indicato.
Per tanto basta cambiare IP e BROWSER (l'IP è stato indicato solo per far si che potessi, una volta avviato il file dal pc, richiamarlo anche dal telefono la pagina)
È un file che cerca di essere di esempio ed ha un po' tante cose mischiate, vuole essere una summa di cose.
Su http://localhost/ verrà mostrato banalmente una pagina HTML, i link in essa contenuti riportano ai diversi esempi

Dopo aver modificato il file batch, prima di avviarlo è importante installare i diversi componenti richiesti; quindi cmd da amministratore, installare quanto segue:
```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install Jinja2
pip install pysqlite3
```
forse anche
```bash
pip install typing-extensions
```