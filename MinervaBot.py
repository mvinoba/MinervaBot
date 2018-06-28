from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Pega os valores do arquivo de texto de login
file = open('login.txt', 'r')
read = file.read()
inputlist = read.split('\n')

# Parametros de login
inputcpf = inputlist[0]
inputpassword = inputlist[1]

# Coloca o Chrome em modo headless
options = Options()
options.add_argument('--headless')

# Abre o driver e entra na minerva
driver = webdriver.Chrome(chrome_options=options)
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
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'myModal'))
    ) # Aguarda o popup estar disponivel
except TimeoutException:
    pass
else:
    popup = driver.find_element_by_css_selector(
        '.modal-footer > button[data-dismiss="modal"]')
    popup.send_keys(Keys.RETURN)

# Acha a secao emprestimos e o acessa
emprestimos = driver.find_element_by_css_selector('a[href*="bor-loan"]')
emprestimos.send_keys(Keys.RETURN)

# Clica em renovar todos
renovartodos = driver.find_element_by_partial_link_text('Renovar Todos')
renovartodos.send_keys(Keys.RETURN)

# Imprime na tela o resultado da renovacao
tabela = driver.find_elements_by_tag_name('table')[-1]
linhas = tabela.find_elements_by_tag_name('tr')
cabecalho = linhas[0].find_elements_by_tag_name('th')
for livro in linhas[1:]:
    corpo = livro.find_elements_by_tag_name('td')
    for x in range(len(corpo)):
        print(cabecalho[x].get_attribute('innerText'), end=': ')
        print(corpo[x].get_attribute('innerText').strip())
