# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta

class Pessoa(object):

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    def envelhecer(self):
        self.idade += 1

class Atleta(Pessoa):
    __metaclass__ = ABCMeta
    esporte = None

    def __init__(self, nome=None, idade=None):
        super(Atleta, self).__init__(nome, idade)

    @abstractmethod
    def praticar_esporte(self):
        print '%s vai praticar %s...' %(self.nome, self.esporte)

class Ciclista(Atleta):

    def __init__(self, nome=None, idade=None):
        super(Ciclista, self).__init__(nome, idade)
        self.esporte = 'Ciclismo'

    def praticar_esporte(self):
        super(Ciclista, self).praticar_esporte()
        self.pedalar()

    def pedalar(self):
        print "%s começou a pedalar!" % self.nome

class Nadador(Atleta):

    def __init__(self, nome=None, idade=None):
        super(Nadador, self).__init__(nome, idade)
        self.esporte = 'Natação'

    def praticar_esporte(self):
        super(Nadador, self).praticar_esporte()
        self.nadar()

    def nadar(self):
        print "%s começou a nadar!" % self.nome

class Corredor(Atleta):

    def __init__(self, nome=None, idade=None):
        super(Corredor, self).__init__(nome, idade)
        self.esporte = 'Corrida'

    def praticar_esporte(self):
        super(Corredor, self).praticar_esporte()
        self.correr()

    def correr(self):
        print "%s começou a correr!" % self.nome

class TriAtleta(Ciclista, Nadador, Corredor):

    def __init__(self, nome=None, idade=None):
        super(TriAtleta, self).__init__(nome, idade)
        self.esporte = 'triatletismo'

    def praticar_esporte(self):
        super(TriAtleta, self).praticar_esporte()

francisco = TriAtleta("Francisco", 21)
francisco.praticar_esporte()
