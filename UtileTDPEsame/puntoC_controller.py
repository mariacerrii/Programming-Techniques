import flet as ft


# ============================================================
# 1. TOP 5 NODI CON PIÙ ARCHI USCENTI + SOMMA PESI USCENTI
# GRAFO ORIENTATO E PESATO
# MODEL: getTop5ArchiUscenti()
# ============================================================
# CONTROLLER:
top5 = self._model.getTop5ArchiUscenti()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("TOP 5 NODI PER ARCHI USCENTI")
)

for nodo, numero, peso in top5:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo: {nodo} | "
            f"Archi uscenti: {numero} | "
            f"Somma pesi uscenti: {peso}"
        )
    )

self._view.update_page()


# ============================================================
# 2. TOP 5 NODI CON GRADO MAGGIORE
# MODEL: getTop5Nodi()
# ============================================================
# CONTROLLER:

top5 = self._model.getTop5Nodi()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("TOP 5 NODI PER GRADO")
)

for nodo, grado in top5:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo: {nodo} | Grado: {grado}"
        )
    )

self._view.update_page()


# ============================================================
# 3. COMPONENTI DEBOLMENTE CONNESSE
# GRAFO ORIENTATO
# MODEL: getComponentiDeboli()
# ============================================================
# CONTROLLER:

numero, nodi = self._model.getComponentiDeboli()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text(f"Numero componenti debolmente connesse: {numero}")
)

self._view._txt_result.controls.append(
    ft.Text(f"Dimensione componente maggiore: {len(nodi)}")
)

for nodo in nodi:
    self._view._txt_result.controls.append(
        ft.Text(f"Nodo: {nodo}")
    )

self._view.update_page()


# ============================================================
# 4. COMPONENTI CONNESSE DI DIMENSIONE > 1
# GRAFO NON ORIENTATO
# MODEL: getComponentiMaggioriDiUno()
# ============================================================
# CONTROLLER:

componenti = self._model.getComponentiMaggioriDiUno()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("COMPONENTI CONNESSE DI DIMENSIONE > 1")
)

if not componenti:
    self._view._txt_result.controls.append(
        ft.Text("Nessuna componente con più di un nodo.")
    )

for componente in componenti:

    self._view._txt_result.controls.append(
        ft.Text(f"Dimensione componente: {len(componente)}")
    )

    for nodo in componente:
        self._view._txt_result.controls.append(
            ft.Text(f"Nodo: {nodo}")
        )

self._view.update_page()


# ============================================================
# 5. NODO CON MASSIMO NUMERO DI ARCHI USCENTI
# GRAFO ORIENTATO
# MODEL: getNodoMaxArchiUscenti()
# ============================================================
# CONTROLLER:

risultato = self._model.getNodoMaxArchiUscenti()

self._view._txt_result.controls.clear()

if risultato is not None:
    nodo, numero = risultato

    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo con più archi uscenti: {nodo} | "
            f"Numero archi: {numero}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Grafo vuoto.")
    )

self._view.update_page()


# ============================================================
# 6. ARTISTA CON INFLUENZA MASSIMA
# INFLUENZA = PESI USCENTI - PESI ENTRANTI
# MODEL: getArtistaMaxInfluenza()
# ============================================================
# CONTROLLER:

risultato = self._model.getArtistaMaxInfluenza()

self._view._txt_result.controls.clear()

if risultato is not None:
    artista, influenza = risultato

    self._view._txt_result.controls.append(
        ft.Text(
            f"Artista con maggiore influenza: {artista} | "
            f"Influenza: {influenza}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Grafo vuoto.")
    )

self._view.update_page()


# ============================================================
# 7A / 8A. NODO CON GRADO MAGGIORE
# MODEL: getNodoMaxGrado()
# ============================================================
# CONTROLLER:

risultato = self._model.getNodoMaxGrado()

self._view._txt_result.controls.clear()

if risultato is not None:
    nodo, grado = risultato

    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo con grado maggiore: {nodo} | "
            f"Grado: {grado}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Grafo vuoto.")
    )

self._view.update_page()


# ============================================================
# 7B / 8B. NODO CON SOMMA PESI INCIDENTI MASSIMA
# MODEL: getNodoMaxPesoIncidente()
# ============================================================
# CONTROLLER:

risultato = self._model.getNodoMaxPesoIncidente()

self._view._txt_result.controls.clear()

if risultato is not None:
    nodo, peso = risultato

    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo con somma pesi incidenti massima: {nodo} | "
            f"Somma pesi: {peso}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Grafo vuoto.")
    )

self._view.update_page()


# ============================================================
# 7C. TOP 5 ARCHI CON PESO MAGGIORE
# MODEL: getTop5ArchiPeso()
# ============================================================
# CONTROLLER:

top5 = self._model.getTop5ArchiPeso()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("TOP 5 ARCHI PER PESO")
)

for u, v, dati in top5:
    self._view._txt_result.controls.append(
        ft.Text(
            f"{u} -- {v} | "
            f"Peso: {dati.get('weight', 1)}"
        )
    )

self._view.update_page()


# ============================================================
# 7C BIS. TOP 5 ARCHI PER PESO + ORDINE ALFABETICO
# MODEL: getTop5ArchiPesoAlfabetico()
# ============================================================
# CONTROLLER:

top5 = self._model.getTop5ArchiPesoAlfabetico()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("TOP 5 ARCHI PER PESO E ORDINE ALFABETICO")
)

for u, v, dati in top5:
    self._view._txt_result.controls.append(
        ft.Text(
            f"{u} -- {v} | "
            f"Peso: {dati.get('weight', 1)}"
        )
    )

self._view.update_page()


# ============================================================
# 7D. NODO PIÙ GIOVANE
# MODEL: getNodoPiuGiovane()
# ============================================================
# CONTROLLER:

giovane = self._model.getNodoPiuGiovane()

self._view._txt_result.controls.clear()

if giovane is not None:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo più giovane: {giovane} | "
            f"Data di nascita: {giovane.date_of_birth}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Nessun nodo con data di nascita disponibile.")
    )

self._view.update_page()


# ============================================================
# 7E. NODO PIÙ ANZIANO
# MODEL: getNodoPiuAnziano()
# ============================================================
# CONTROLLER:

anziano = self._model.getNodoPiuAnziano()

self._view._txt_result.controls.clear()

if anziano is not None:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo più anziano: {anziano} | "
            f"Data di nascita: {anziano.date_of_birth}"
        )
    )
else:
    self._view._txt_result.controls.append(
        ft.Text("Nessun nodo con data di nascita disponibile.")
    )

self._view.update_page()


# ============================================================
# 9 / 11. COMPONENTE MAGGIORE ORDINATA PER GRADO
# MODEL: getComponenteMaxPerGrado()
# ============================================================
# CONTROLLER:

numero, risultati = self._model.getComponenteMaxPerGrado()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text(f"Numero componenti connesse: {numero}")
)

self._view._txt_result.controls.append(
    ft.Text(f"Dimensione componente maggiore: {len(risultati)}")
)

for nodo, grado in risultati:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo: {nodo} | Grado: {grado}"
        )
    )

self._view.update_page()

# ============================================================
#  variabile di quello sopra in ORDINE ALFABETICO + NUMERO BRANI (GIUGNO B)
# ============================================================
def handleStampaInfo(self, e):
    numero, album = self._model.getInfoComponenti()

    self._view._txt_result.controls.clear()

    # Numero totale componenti
    self._view._txt_result.controls.append(
        ft.Text(f"Numero componenti connesse: {numero}")
    )

    # Dimensione componente maggiore
    self._view._txt_result.controls.append(
        ft.Text(f"Componente maggiore: {len(album)} album")
    )

    # Dettagli degli album in ordine alfabetico
    for a in album:
        self._view._txt_result.controls.append(
            ft.Text(
                f"Album: {a.Title} | "
                f"Numero brani: {len(a.tracks)}"
            )
        )
    self._view.update_page()


# ============================================================
# 10. COMPONENTE MAGGIORE ORDINATA PER PESO MASSIMO INCIDENTE
# MODEL: getComponenteMaxPerPeso()
# ============================================================
# CONTROLLER:

numero, risultati = self._model.getComponenteMaxPerPeso()

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text(f"Numero componenti connesse: {numero}")
)

self._view._txt_result.controls.append(
    ft.Text(f"Dimensione componente maggiore: {len(risultati)}")
)

for nodo, peso in risultati:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Nodo: {nodo} | "
            f"Peso massimo arco incidente: {peso}"
        )
    )

self._view.update_page()


# ============================================================
# 12. PERCORSO MASSIMO NELL'ALBERO DFS
# NON NECESSARIAMENTE IL PIÙ LUNGO NEL GRAFO ORIGINALE
# MODEL: getPercorsoMassimoDFS(source)
# ============================================================
# CONTROLLER:
# ATTENZIONE: source deve essere l'OGGETTO nodo selezionato.

percorso = self._model.getPercorsoMassimoDFS(source)

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("PERCORSO NELL'ALBERO DFS")
)

for nodo in percorso:
    self._view._txt_result.controls.append(
        ft.Text(f"Nodo: {nodo}")
    )

self._view._txt_result.controls.append(
    ft.Text(
        f"Lunghezza percorso: {max(0, len(percorso) - 1)} archi"
    )
)

self._view.update_page()


# ============================================================
# 13 / 14. NODI ADIACENTI ORDINATI PER PESO DECRESCENTE
# MODEL: getViciniOrdinati(source)
# ============================================================
# CONTROLLER:
# ATTENZIONE: source deve essere l'OGGETTO nodo selezionato.

vicini = self._model.getViciniOrdinati(source)

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text(f"Nodi adiacenti a {source}: {len(vicini)}")
)

for nodo, peso in vicini:
    self._view._txt_result.controls.append(
        ft.Text(
            f"Vicino: {nodo} | Peso: {peso}"
        )
    )

self._view.update_page()


# ============================================================
# 15A. VISITA DFS
# MODEL: getDFS(source)
# ============================================================
# CONTROLLER:

nodi = self._model.getDFS(source)

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("VISITA DFS")
)

for nodo in nodi:
    self._view._txt_result.controls.append(
        ft.Text(f"Nodo: {nodo}")
    )

self._view.update_page()


# ============================================================
# 15B. VISITA BFS
# MODEL: getBFS(source)
# ============================================================
# CONTROLLER:

nodi = self._model.getBFS(source)

self._view._txt_result.controls.clear()

self._view._txt_result.controls.append(
    ft.Text("VISITA BFS")
)

for nodo in nodi:
    self._view._txt_result.controls.append(
        ft.Text(f"Nodo: {nodo}")
    )

self._view.update_page()