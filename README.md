# La mia giornata

App web personale per gestire le cose da fare in giornata: **appuntamenti** con orario e **task** (to-do list) con priorità.

## Funzioni
- Riepilogo del giorno: percentuale completata, prossimo appuntamento con il conto alla rovescia
- Le 3 priorità del giorno (tocca la ★)
- Aggiunta rapida in linguaggio naturale: `Dentista domani 15:30 #salute !alta`
- Categorie colorate (Lavoro, Personale, Salute, Casa, Studio, Finanze) con filtri
- Sotto-attività spuntabili dentro ogni task
- Note del giorno
- Vista settimana e pagina Statistiche (serie di giorni, grafico 14 giorni, per categoria, per priorità)
- Dati di esempio al primo avvio (si cancellano con un tocco)
- Vista giornaliera con barra della settimana (scorri a destra/sinistra per cambiare giorno)
- Appuntamenti ordinati per ora, con evidenziato quello in corso
- Task ordinati per priorità (Alta / Media / Bassa), con ora opzionale
- Ripetizioni: ogni giorno, lun-ven, ogni settimana, ogni mese
- Task in ritardo mostrati su "Oggi", con "Sposta tutti a oggi"
- Barra di avanzamento della giornata
- Tema chiaro/scuro, installabile sul telefono (PWA), funziona offline
- Backup / ripristino in JSON

I dati restano nel browser del dispositivo (localStorage). Nessun server, nessun costo.

## Pubblicazione su GitHub Pages
Settings → Pages → Source: "Deploy from a branch" → Branch `main`, cartella `/ (root)` → Save.
Dopo un minuto l'app è su `https://<utente>.github.io/<repo>/`.

## Installarla sul telefono
- iPhone (Safari): Condividi → "Aggiungi a schermata Home"
- Android (Chrome): menu ⋮ → "Installa app"

## Link magico (aggiungere elementi da Claude)
Claude può preparare un link `https://lwzazzolw-cyber.github.io/task-app/#add=...` o un codice `GIORNATA:...`.
- Tocca il link, oppure incolla il codice nella barra "Aggiungi al volo".
- L'app mostra l'anteprima e chiede conferma. Gli elementi già presenti vengono saltati.
- Su iPhone, se usi l'app dalla schermata Home, usa il **codice** (Safari e l'app installata hanno memorie separate).

Generatore: `python3 tools/link.py elementi.json` (formato descritto nel file).
