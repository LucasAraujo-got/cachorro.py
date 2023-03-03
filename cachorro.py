class Cachorro:
    def __init__(self, nome, raca, peso, data_nascimento):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.data_nascimento = data_nascimento
    
    def latir(self):
        print(f"{self.nome} está latindo!")
    
    def caminhar(self, distancia):
        print(f"{self.nome} caminhou {distancia} metros!")
    
    def comer(self, comida):
        print(f"{self.nome} comeu {comida}!")
    
    def idade(self):
        dia_nascimento, mes_nascimento, ano_nascimento = map(int, self.data_nascimento.split("/"))
        dia_atual, mes_atual, ano_atual = map(int, "03/03/2023".split("/"))
        
        idade = ano_atual - ano_nascimento
        
        if mes_atual < mes_nascimento:
            idade -= 1
        elif mes_atual == mes_nascimento and dia_atual < dia_nascimento:
            idade -= 1
        
        print(f"{self.nome} tem {idade} anos.")


cachorro1 = Cachorro("Bolinha", "Poodle", 5.2, "01/03/2019")
cachorro2 = Cachorro("Rex", "Pastor Alemão", 30.1, "15/08/2017")
cachorro3 = Cachorro("Lola", "Bulldog Francês", 10.5, "10/11/2020")

cachorro1.latir()
cachorro1.caminhar(50)
cachorro1.comer("ração")
cachorro1.idade()

cachorro2.latir()
cachorro2.caminhar(100)
cachorro2.comer("frango")
cachorro2.idade()

cachorro3.latir()
cachorro3.caminhar(20)
cachorro3.comer("biscoitos")
cachorro3.idade()
