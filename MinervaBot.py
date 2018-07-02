from getpass import getpass
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def inserir_dados(salvar=None):
    # Pergunta ao usuario CPF e senha
    for label in driver.find_elements_by_tag_name('label'):
        if label.get_attribute('for') == 'pat_id':
            idcpf = driver.find_element_by_name('bor_id')
            inputcpf = input('%s ' % label.text)
        elif label.get_attribute('for') == 'pat_password':
            inputpassword = getpass('%s ' % label.text)

    # Pergunta ao usuario se deseja salvar os dados de login
    if salvar == None:
        resposta = input('Salvar dados em arquivo? (s/N) ')
        if resposta.lower() in {'sim', 's'}:
            salvar = True
        else:
            salvar = False

    print()
    return inputcpf, inputpassword, salvar

def ler_dados(arquivo):
    file = open(arquivo, 'r')
    read = file.read()
    inputlist = read.split('\n')
    return inputlist[0], inputlist[1]

def salvar_dados(arquivo, inputcpf, inputpassword, salvar):
    if not salvar: return
    file = open(arquivo, 'w')
    file.write('%s\n%s' % (inputcpf, inputpassword))

# Coloca o Chrome em modo headless
options = Options()
options.set_headless(True)

# Abre o driver e entra na minerva
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://minerva.ufrj.br')

# Acha a secao de login e a acessa
login = driver.find_element_by_link_text('Login')
login.send_keys(Keys.RETURN)

# Le os dados para login
try:
    inputcpf, inputpassword = ler_dados('login.txt')
    salvar = True
except FileNotFoundError:
    print("Falha ao encontrar o arquivo de login")
    inputcpf, inputpassword, salvar = inserir_dados(None)
except IndexError:
    print("Arquivo de login incompleto")
    inputcpf, inputpassword, salvar = inserir_dados(True)

# Entra em loop ate obter sucesso no login
while True:
    # Acha as entradas para o id e senha
    idcpf = driver.find_element_by_name('bor_id')
    password = driver.find_element_by_name('bor_verification')

    # Preenche as entradas com os parametros dados
    idcpf.clear()
    idcpf.send_keys(inputcpf)
    password.send_keys(inputpassword, Keys.RETURN)

    # Checa mensagem de erro no login
    feedback = driver.find_element_by_class_name('feedbackbar')
    if feedback.text == ' ':
        salvar_dados('login.txt', inputcpf, inputpassword, salvar)
        break
    else:
        print(feedback.text.strip())
        inputcpf, inputpassword, salvar = inserir_dados(salvar)

# Acha o botao de fechar o popup e o fecha
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'myModal'))
    ) # Aguarda o popup estar disponivel
except exceptions.TimeoutException:
    pass
else:
    popup = driver.find_element_by_css_selector(
        '.modal-footer > button[data-dismiss="modal"]')
    popup.send_keys(Keys.RETURN)

# Acha a secao emprestimos e a acessa
emprestimos = driver.find_element_by_css_selector('a[href*="bor-loan"]')
emprestimos.send_keys(Keys.RETURN)

# Acha o botao de renovar todos
try:
    renovartodos = driver.find_element_by_partial_link_text('Renovar Todos')
except exceptions.NoSuchElementException:
    mensagem = driver.find_element_by_class_name('text3')
    print(mensagem.text)
else:
    # Clica em renovar todos
    renovartodos.send_keys(Keys.RETURN)

    # Imprime na tela o resultado da renovacao
    tabela = driver.find_elements_by_tag_name('table')[-1]
    linhas = tabela.find_elements_by_tag_name('tr')
    cabecalho = linhas[0].find_elements_by_tag_name('th')
    for livro in linhas[1:]:
        corpo = livro.find_elements_by_tag_name('td')
        for x in range(len(corpo)):
            print(cabecalho[x].text, end=': ')
            print(corpo[x].text)

driver.quit()
