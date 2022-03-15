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
		
	def print_pracownik(self):
		print(f"dane pracownika - firma: {self.firma}, stanowisko pracy: {self.stanowisko}"
		      f", lata pracy: {self.latapracy}, płaca: {self.placa} zł")
		
	def czypracownik(self):
		return True
	
print("**************************************")
em1 = Pracownik("Karol",45,99,176,"ABC","dyrektor",6700,12)
print(f"kolor oczu: {em1.kolor_oczu}")
em1.print_osoba()
print(f"wiek za 10 lat: {em1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {em1.czypracownik()}")
em1.print_pracownik()

class Sport:
	
	def __init__(self,dyscyplina,lata_upr,best_wynik):
		self.dyscyplina = dyscyplina
		self.lata_upr = lata_upr
		self.best_wynik = best_wynik
		
	def infosport(self):
		print(f"dysycyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr},"
		      f"życiówka: {self.best_wynik}")
		
		
class Ekstra:
	pass

class Student(Pracownik,Sport,Ekstra):
	
	def __init__(self,imie,wiek,waga,wzrost,nr_studenta,kierunek,rok_ukon,
	             firma="",stanowisko="",placa="",latapracy="",
	             dyscyplina="",lata_upr="",best_wynik=""):
		Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,placa,latapracy)
		Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
		self.nr_studenta = nr_studenta
		self.kierunek = kierunek
		self.rok_ukon = rok_ukon
		
	def print_student(self):
		print(f"infromacje o studencie nr {self.nr_studenta}, kierunek: {self.kierunek}"
		      f", rok ukończenia studiów: {self.rok_ukon}")
		
	def czypracownik(self):
		if self.firma == "":
			return False
		else:
			return True
		
print("**************************************")

s1 = Student("Olaf",22,77,177,5678,"budowlany",2023)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()} lat/a")
print(f"czy osoba jest pracownikiem? {s1.czypracownik()}")

	