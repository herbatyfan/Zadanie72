class Osoba:
  def __init__(self, imie, nazwisko, firma, stanowisko, mail):
      self.imie = imie
      self.nazwisko = nazwisko
      self.firma = firma
      self.stanowisko = stanowisko
      self.mail = mail
  def __str__(self):
      return f'{self.imie} {self.nazwisko} {self.firma} {self.stanowisko} {self.mail} '
  def contact(self):
      print (f"Kontaktuje się z: {self.imie} {self.nazwisko} {self.firma} {self.stanowisko} {self.mail}" )
  @property
  def lent(self):
      print(len(self.imie)+len(self.nazwisko)+1)
Zdzislaw = Osoba(imie="Zdzislaw", nazwisko="Dyrma", firma="PaFaWag", stanowisko="odwaznik", mail="zdzislaw.dyrma@gmail.com")
Stanislaw = Osoba(imie="Stanislaw", nazwisko="Paluch", firma = "Wegiel", stanowisko="pracownik", mail="paluch@wp.pl")
Jerzy = Osoba(imie="Jerzy", nazwisko="Kiler", firma="TaxiKorp", stanowisko="taksowkarz",mail="j.kiler@gmail.com")
lista = []
lista.append(Zdzislaw) 
lista.append(Stanislaw)
lista.append(Jerzy)
lista[0].contact()
lista[0].lent
lista[1].contact()
lista[1].lent
lista[2].contact()
lista[2].lent
