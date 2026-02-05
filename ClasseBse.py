import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        return 10
    
    def sofre_dano(self, dano):
        self.vida -= dano
        if self.vida < 0: self.vida = 0
        print(f"{self.nome} sofreu {dano} de dano. Vida agora: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0


class Guerreiro(Personagem): 
    def __init__(self, nome, vida, forca): 
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self): 
        dano = self.forca
        if random.random() < 0.2:  
            dano *= 2
            print(f"{self.nome} acertou um CRÍTICO com a espada!")
        else:
            print(f"{self.nome} ataca com espada!")
        return dano


class Mago(Personagem): 
    def __init__(self, nome, vida, mana): 
        super().__init__(nome, vida)
        self.mana = mana
        self.pocoes = 3  

    def curar(self, alvo):
        
        if self.pocoes > 0:
            self.pocoes -= 1
            cura = 25
            alvo.vida += cura
            print(f"--- {self.nome} usou POÇÃO DE CURA em {alvo.nome}! (+25 HP). Vida de {alvo.nome}: {alvo.vida} ---")
            print(f"(Poções restantes: {self.pocoes})")
        else:
            print(f"{self.nome} tentou usar poção, mas não tem mais!")

    def atacar(self): 
        if self.mana >= 10:
            self.mana -= 10
            dano = 25
            if random.random() < 0.15:  
                dano *= 2
                print(f"{self.nome} lançou uma Magia CRÍTICA! Mana restante: {self.mana}")
            else:
                print(f"{self.nome} lançou Magia! Mana restante: {self.mana}")
            return dano
        else:
            print(f"{self.nome} usa ataque fraco! Mana insuficiente.")
            return 5


class Arqueiro(Personagem): 
    def __init__(self, nome, vida, flechas): 
        super().__init__(nome, vida)
        self.flechas = flechas

    def atacar(self):
        if self.flechas > 0: 
            self.flechas -= 1
            dano = 15
            if random.random() < 0.25:  
                dano *= 2
                print(f"{self.nome} disparou uma FLECHA CRÍTICA! Flechas restantes: {self.flechas}")
            else:
                print(f"{self.nome} disparou uma flecha! Flechas restantes: {self.flechas}")
            return dano
        else:
            print(f"{self.nome} está sem flechas e usa o arco como arma!")
            return 2


P1 = Guerreiro("Clovis", 100, 12)
P2 = Mago("Beto", 80, 40)
P3 = Arqueiro("Rogerio", 200, 10)

print(f"--- {P1.nome} e {P2.nome} vs {P3.nome} ---")


while (P1.esta_vivo() or P2.esta_vivo()) and P3.esta_vivo():
     
    alvos_vivos = []
    if P1.esta_vivo(): alvos_vivos.append(P1)
    if P2.esta_vivo(): alvos_vivos.append(P2)

    if alvos_vivos:
        alvo = random.choice(alvos_vivos)
        dano = P3.atacar()
        alvo.sofre_dano(dano)
    
        if not alvo.esta_vivo():
            print(f"{alvo.nome} foi derrotado!")
        else:
            
            dano = alvo.atacar()
            P3.sofre_dano(dano)
    
    if P2.esta_vivo() and P3.esta_vivo():
        
        usou_pocao = False
    
        if P2.pocoes > 0:
           
            if P1.esta_vivo() and P1.vida < 40:
                P2.curar(P1)
                usou_pocao = True
                    
            elif P2.vida < 30:
                P2.curar(P2)
                usou_pocao = True
       
   
        if not usou_pocao:
            dano = P2.atacar()
            P3.sofre_dano(dano)

print("\nFINISH HIM")
if P3.esta_vivo():
    print(f"{P3.nome} venceu!")
else:
    print(f"{P1.nome} e {P2.nome} venceram!")