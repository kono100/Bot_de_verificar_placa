from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

placa = input("Digite a Placa : ")

# Passo 1: Abrir a URL
url = "https://consultaplacasbr.com.br/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

# Número de vezes que você deseja rolar
num_rolagens = 1

# Rolar para baixo várias vezes usando execute_script
for _ in range(num_rolagens):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.1)  # Aguarde um breve momento entre as rolagens

# Passo 2: Encontrar o campo de placa e enviar a placa corretamente
# placa = "foe0f09"
placa_input = driver.find_element("id", "text-6600")
placa_input.clear()  # Limpar o campo antes de enviar a placa

# Enviar cada caractere individualmente para garantir a ordem correta
for char in placa:
    placa_input.send_keys(char)
    time.sleep(0.1)  # Aguardar um curto intervalo entre as teclas

# Passo 3: Clicar no botão "Consultar Placa"
consultar_button = driver.find_element("class name", "u-btn-1")
consultar_button.click()

# Aguarde alguns segundos para a página carregar
time.sleep(5)  # Aumentado para 5 segundos

# Tratamento de exceção para obter informações da placa, marca, cor e modelo
try:
    # Placa
    placa_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-50')]")
    placa = placa_element.text
except NoSuchElementException:
    placa = "Informação de placa não encontrada"

try:
    # Marca
    marca_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-6')]")
    marca = marca_element.text
except NoSuchElementException:
    marca = "Informação de marca não encontrada"

try:
    # Cor
    cor_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-20')]")
    cor = cor_element.text
except NoSuchElementException:
    cor = "Informação de cor não encontrada"

# Tentar obter informações do modelo com tratamento de exceção
try:
    modelo_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-8')]")
    modelo = modelo_element.text
except NoSuchElementException:
    modelo = "Informação de modelo não encontrada"



try:
    especie_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-30')]")
    especie = especie_element.text
except NoSuchElementException:
    especie = "Informação de especie não encontrada"

# segmento
try:
    segmento_element = driver.find_element("xpath", "//td[contains(@class, 'u-table-cell-36')]")
    segmento = segmento_element.text
except NoSuchElementException:
    segmento = "Informação de segmento não encontrada"


# Passo 4: Imprimir as informações no terminal
print(f"Placa: {placa}")
print(f"Marca: {marca}")
print(f"Cor: {cor}")
print(f"Modelo: {modelo}")
print(f"Especie: {especie}")
print(f"segmento: {segmento}")

# Fechar o navegador
driver.quit()
