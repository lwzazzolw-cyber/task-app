#!/usr/bin/env python3
"""Crea il link magico e il codice da incollare per aggiungere elementi a "La mia giornata".

Uso: python3 tools/link.py elementi.json
elementi.json è una lista di oggetti con chiavi brevi:
  k  "a" appuntamento | "t" task          (obbligatorio)
  n  titolo                               (obbligatorio)
  d  data AAAA-MM-GG                      (obbligatorio)
  h  ora inizio HH:MM   e  ora fine HH:MM   l  luogo
  p  priorità "a" alta | "m" media | "b" bassa
  c  categoria: lavoro personale salute casa studio finanze
  r  ripeti: daily weekdays weekly monthly
  o  note    s  lista di sotto-attività    f  true = tra le 3 priorità

Per modificare elementi esistenti aggiungi "x":
  {"x":"del","n":"Pranzo con Marco","d":"2026-11-18"}   elimina (d e h opzionali, aiutano a trovarlo)
  {"x":"done","n":"Pagare la bolletta"}                 segna come fatto
  {"x":"reset","n":"reset"}                             svuota tutta l'agenda (prima degli altri elementi del link)
Il titolo si confronta senza maiuscole/accenti; va bene anche una parte, se è unica.
"""
import base64, json, sys

BASE = "https://lwzazzolw-cyber.github.io/task-app/"

def encode(items):
    raw = json.dumps(items, ensure_ascii=False, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")

if __name__ == "__main__":
    items = json.load(open(sys.argv[1]))
    code = encode(items)
    print("LINK:   " + BASE + "#add=" + code)
    print("CODICE: GIORNATA:" + code)
