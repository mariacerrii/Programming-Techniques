from gestionale.vendite.ordini import Ordine, RigaOrdine, OrdineConSconto
from gestionale.core.prodotti import Prodotto, crea_prodotto_standard, ProdottoRecord
from gestionale.core.clienti import Cliente, ClienteRecord

print("=======================================================")

p1 = Prodotto("Ebook Reader", 120.0, 1, "AAA")
p2 = crea_prodotto_standard("Tablet", 750)

print (p1)
print (p2)
print("=======================================================")

c1 = Cliente("Mario Rossi", "mail@mail.com", "Gold")

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2, 10)], cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2, 10)], cliente1, 0.1)

print(ordine)
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto: ", ordine_scontato.totale_netto())
print("Totale lordo scontato: ", ordine_scontato.totale_lordo(0.22))

print("-------------------------------------------------------------------")

#Nel package gestionale, scriviamo un modulo fatture.py che contenga:
# - una classe Fattura che contiene un Ordine, un numero_fattura e una data
# - un metodo genera_fattura() che restituisce una stringa formattata con tutte le info della fattura



##ciao brhkhrs ihyioyouyouioii