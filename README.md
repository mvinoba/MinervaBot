# MinervaBot
Um bot que usa *Selenium* para automatizar a renovação online de livros das bibliotecas da UFRJ.

## Download

Caso tenha preferência por usar a versão executável, que não requer nem o Python nem o módulo Selenium para funcionar, basta fazer o download do `MinervaBot-0.1.rar` na [release mais recente](https://github.com/mvinoba/MinervaBot/releases) e ler as instruções de uso.

## Requerimentos
* Python 3.5
* Selenium (Testado com a versão mais recente: 3.4.1)
* ChromeDriver 2.32

## Uso

Depois de instalar os requerimentos ou fazer o download do executável o próximo passo é editar o arquivo **teste.txt** e substituir `CPF` pelo seu CPF e `Senha` pela sua senha na http://minerva.ufrj.br.
Ou seja, de:

    CPF
    Senha
    
Para:

    12345678900
    minhaSenha
    
Agora basta executar o MinervaBot.py

    python MinervaBot.py
