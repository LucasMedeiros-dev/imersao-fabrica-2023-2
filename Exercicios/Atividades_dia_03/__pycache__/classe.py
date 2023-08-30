from abc import ABC, abstractmethod

class IAnimanl(ABC):
  
    @abstractmethod
    def falar(self):
        '''### Defina na classe filha''' 
    @abstractmethod
    def andar(self):
        '''### Defina na classe filha'''
    

class Cachorro(IAnimanl):
    def falar(self):
        print('auau')
    def andar(self):
        print('ando com as quatro patas')

class Pessoa:
    def __init__(self, nome,idade):
        self._nome = nome
        self.idade = idade
        self.__humano = True
        
    def fala_pessoa(self):
        print('Falando')
    
    def mostra_nome(self):
        print(self._nome)
        

Bolinha = Cachorro()

Bolinha.andar()

Lucas = Pessoa("Lucas",21)

Lucas.mostra_nome()
Lucas.fala_pessoa()