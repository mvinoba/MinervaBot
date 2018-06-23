'''
Este programa automatiza o processo de renovacao dos livros no site da Minerva
Escrito por Vinicius Figueiredo pela primeira vez em 06/2016, usando uma ideia de Matheus Bernini, a quem agradeco!
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Pega os valores do arquivo de texto de login
file = open('login.txt', 'r')
read = file.read()
inputlist = read.split('\n')

# Parametros de login
inputcpf = inputlist[0]
inputpassword = inputlist[1]

# Abre o driver e entra na minerva
driver = webdriver.Chrome()
driver.get('http://minerva.ufrj.br')

# Acha a secao de login e a acessa
login = driver.find_element_by_link_text('Login')
login.send_keys(Keys.RETURN)

# Acha as entradas para o id e senha
idcpf = driver.find_element_by_name('bor_id')
password = driver.find_element_by_name('bor_verification')

# Preenche as entradas com os parametros dados
idcpf.send_keys(inputcpf)
password.send_keys(inputpassword, Keys.RETURN)

# Acha o botao de fechar o popup e o fecha
driver.implicitly_wait(10)  # Aguarda o modal dialog estar disponivel
popup = driver.find_element_by_css_selector(
    '.modal-footer > button[data-dismiss="modal"]')
popup.send_keys(Keys.RETURN)

# Acha a secao emprestimos e o acessa
emprestimos = driver.find_element_by_css_selector("a[href*='bor-loan']")
emprestimos.send_keys(Keys.RETURN)

# Clica em renovar todos
renovartodos = driver.find_element_by_partial_link_text("Renovar Todos")
renovartodos.send_keys(Keys.RETURN)