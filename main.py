class Osoba:
	
	kolor_oczu = "niebieski"
	
	def __init__(self,imie,wiek,waga,wzrost):
		self.imie =imie
		self.wiek = wiek
		self.waga = waga
		self.wzrost = wzrost
		self.info()
		
	def info(self):
		print("tworzenie nowej instancji osoby.....")
		
	def print_osoba(self):
		print(f"osoba - imię:{self.imie}, wiek: {self.wiek} lat, "
		      f"wzrost: {self.wzrost} cm, waga: {self.waga} kg")
		      
	def wiekza10lat(self):
		return self.wiek + 10
	
	def czypracownik(self):
		return False
	
	
p1 = Osoba("Jan",34,78,178)
print(f"kolor oczu: {p1.kolor_oczu}")
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {p1.czypracownik()}")

print("**************************************")

p2 = Osoba("Olga",8,32,145)
p2.kolor_oczu = "piwne"
print(f"kolor oczu: {p2.kolor_oczu}")
p2.print_osoba()
print(f"wiek za 10 lat: {p2.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {p2.czypracownik()}")

class Pracownik(Osoba):
	
	def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,placa,latapracy):
		super().__init__(imie,wiek,waga,wzrost)
		self.firma = firma
		self.stanowisko = stanowisko
		self.placa = placa
		self.latapracy = latapracy