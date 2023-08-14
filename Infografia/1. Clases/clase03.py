class Carro:
    marca = "subaru"
    
    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.cilindrada = cilindrada
        self.kilometraje = kilometraje
    
    def encender(self):
        print("ruuuunnnn")
        
carro = Carro("subaru", 1500, 2000)
carro.encender()

print(f"marca auto1: {carro.marca}")

carro2 = Carro("renault", 1700, 8000)
print(f"marca auto2: {carro2.marca}")