[READE.md](https://github.com/user-attachments/files/25110432/READE.md)
 Simulador de Batalha RPG em Python

Este projeto é um simulador de combate em turnos desenvolvido em **Python**, focado na aplicação de conceitos de **Programação Orientada a Objetos (POO)**.

O sistema simula uma batalha automática entre um time de heróis (Guerreiro e Mago) contra um inimigo poderoso (Arqueiro), demonstrando o uso de Herança, Polimorfismo e lógica de jogo condicional.

O que foi desenvolvido

O código consiste em uma estrutura de classes onde:
-Classe Mãe (`Personagem`):** Define os atributos básicos (nome, vida) e métodos comuns (`sofre_dano`, `esta_vivo`).
-Classes Filhas (`Guerreiro`, `Mago`, `Arqueiro`):** Herdam de `Personagem` e implementam suas próprias versões do método `atacar` (Polimorfismo) e atributos únicos (Mana, Força, Flechas, Poções).

Recentemente, foi implementada uma **Lógica de Inteligência Artificial (IA)** para o Mago, permitindo que ele decida entre atacar ou curar aliados dependendo da situação da batalha.

 Regras do Jogo e Mecânicas

A batalha ocorre em um loop `while` até que uma das equipes seja derrotada.

### As Equipes
1. - Heróis: Clovis (Guerreiro) e Beto (Mago).
2. - Inimigo (Boss): Rogerio (Arqueiro), com vida elevada.

### Habilidades das Classes

 Classe / Atributo Especial / Comportamento de Ataque/ Mecânica Especial/

- Guerreiro  Força  Dano baseado na força.  20% de chance de (Dano Crítico) (2x). 
- Mago  Mana & Poções  Gasta 10 Mana para dano alto. /Cura: Usa poção (+25 HP) em si ou no aliado se a vida estiver baixa. 
- Arqueiro Flechas  Gasta flechas para atacar.  Usa o arco como "arma branca" (dano baixo) se as flechas acabarem. 

 Fluxo de Combate
1.  O **Arqueiro** escolhe um alvo aleatório (Guerreiro ou Mago) e ataca.
2.  O alvo sobrevivente contra-ataca imediatamente.
3.  O **Mago** avalia o cenário:
    * Se o Guerreiro estiver com pouca vida (< 40), ele usa uma **Poção de Cura**.
    * Se ele mesmo estiver com pouca vida (< 30), ele se cura.
    * Caso contrário, ele lança uma magia ofensiva no inimigo.

 Como Executar


1.  Clone este repositório ou baixe o arquivo do código (ex: `rpg.py`).
2.  Abra o terminal ou prompt de comando na pasta do arquivo.
3.  Execute o comando:

```bash
python rpg.py
