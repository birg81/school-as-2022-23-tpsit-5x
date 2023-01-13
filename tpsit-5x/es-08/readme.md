<table>
<tr>
<td>
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" height="120px" />
</td>
<td>
<img src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png" height="75px" />
</td>
<td>
<img src="https://jinja.palletsprojects.com/en/3.1.x/_images/jinja-logo.png" width="150px" />
</td>
</tr>
</table>

# FastAPI (test)

Prima di procedere forse è il caso di modificare il contenuto del file batch, in quanto questi era configurato per funzionare col pc della mia rete con IP 192.168.1.59 e col browser predefinito che adopero al solo scopo di avviare automaticamente la pagina sul IP indicato.
Per tanto, basta cambiare IP e BROWSER (l'IP è stato indicato solo per far si che potessi, una volta avviato il file dal pc, richiamarlo anche dal telefono la pagina)
È un file che cerca di essere di esempio ed ha un po' tante cose mischiate, vuole essere una summa di cose (tra le quali anche una cartella della tombola).
Su http://localhost/ verrà mostrato banalmente una pagina HTML, i link in essa contenuti riportano ai diversi esempi

Dopo aver modificato il file batch, prima di avviarlo è importante installare i diversi componenti richiesti; quindi cmd da amministratore, installare quanto segue:
```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install Jinja2
pip install typing-extensions (opzionale)
```
od equivalentemente scrivendo:
```bash
python -m pip install uvicorn fastapi Jinja2
```
* **uvicorn** è un semplice server in python
* **fastapi** è il nostro framework stateless che ritorna valori in formato json e costruzione di rotte
* **Jinja2** è un motore di rendering, ovvero un package che permette di integrare codice python all'interno delle pagine html in magniera completamente trasparente al visitatore della pagina
* **typing-extensions** serve a fare il controllo statico del tipo. Sebbene python non sia fortemente tipizzato, questo pacchetto è in grado di forzare i tipi dei diversi parametri
* **sqlite3** sebbene non è previsto nell'installazione, questi permette il binding con un DBMS locale sqlite
Inoltre è possibile consultare i pacchetti installati attraverso il seguente comando
```bash
python -m pip list
```
Installate le diverse dipendenze, come si può vedere nei file batch creati a seguito, il miglior modo per avviare la webapp è il seguente
```bash
python -m uvicorn <NomeFileSenzaEstensione>:<NomeOggetto> --reload
```
di seguito sono indicate le opzioni più significative da dare al comando visto sopra
* ```--reload``` questa opzione permette ad ogni modifica del file .py di poter ricaricare automaticamente il server
* ```--no-use-colors``` questa opzione può essere molto utile se si lancia la webapp dal prompt di windows in quanto questo non è in grado di interpretare i colori e di conseguenza visualizza solo delle scritte senza significato; diversametne powershell è in grado di interpretare correttamente il codice a colori tipico dei terminali UNIX-Like
* ```--port``` per indicare la porta sulla quale girare, può essere in tal caso interessante indicare la porta 80 che viene usata di default per il protocollo HTTP
* ```--host``` per indicare l'host sul quale gira la web app; tale opzione si rileva particolarmente interessante in quanto indicando l'indirizzo IP del proprio dispositivo sarà possibile raggiungere la webapp da tutta la rete locale
