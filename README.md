# MinervaBot
Um bot que usa *Selenium* para automatizar a renovação online de livros das bibliotecas da UFRJ.

## Requerimentos
* Python 3.5
* Selenium (Testado com a versão mais recente: 3.4.1)
* ChromeDriver 2.29

## Uso

Depois de instalar os requerimentos o próximo passo é editar o arquivo **teste.txt** e substituir "CPF" pelo seu CPF e "Senha" pela sua senha na http://minerva.ufrj.br.
Ou seja, de:

    CPF
    Senha
    
Para:

    12345678900
    minhaSenha
    
Agora basta executar o MinervaBot.py

    python MinervaBot.py
