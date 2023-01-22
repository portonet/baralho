/*import {randint, choice} from 'random'*/
from 'random' import {randint, shuffle}

class Card:{

    espadas = 0
    copas = 1
    paus = 2
    ouros = 3
    
    corespadas = 0 
    corpaus = 0 
    corouros = 1
    corcopas = 1
     //#region 0=preta e 1=vermelha;
    

    def __init__(self, naipe=0, valor=0, cor=0):
        self.naipe = naipe
        self.valor = valor
        self.cor = cor


}