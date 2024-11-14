# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# %%

# Inicialize o navegador com o WebDriver Manager (testar no windows pois rodei no linux)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# %%

# Acessar o site na página de RJ
driver.get("https://carregados.com.br/estacoes?estado=rio+de+janeiro+(rj)")
# %%
# Aguardar página recrregar
driver.implicitly_wait(10)

# %%

# Listas
nomes_locais = []
tipos = []
enderecos = []
usos_restritos = []
estacoes = []
conectores = []
distancias = []
avaliacoes = []
# %%

try:
    # Capturando todos os elementos para cada seletor CSS
    elementos_nome_local = driver.find_elements(By.CSS_SELECTOR, "h2")
    elementos_tipo = driver.find_elements(By.CSS_SELECTOR, "p.font-bold.capitalize")
    elementos_endereco = driver.find_elements(By.CSS_SELECTOR, "p.text-muted-foreground")
    elementos_uso_restrito = driver.find_elements(By.CSS_SELECTOR, "div.bg-yellow-500")
    elementos_estacoes = driver.find_elements(By.CSS_SELECTOR, "p.font-bold.text-primary")
    elementos_conector = driver.find_elements(By.CSS_SELECTOR, "div.text-sm")
    elementos_distancia = driver.find_elements(By.CSS_SELECTOR, "p.uppercase.text-primary")
    elementos_avaliacoes = driver.find_elements(By.CSS_SELECTOR, "div.bg-secondary")
# Loop para extrair os textos e adicionar às listas
    for elemento in elementos_nome_local:
        nomes_locais.append(elemento.text)

    for elemento in elementos_tipo:
        tipos.append(elemento.text)

    for elemento in elementos_endereco:
        enderecos.append(elemento.text)

    for elemento in elementos_uso_restrito:
        usos_restritos.append(elemento.text)

    for elemento in elementos_estacoes:
        estacoes.append(elemento.text)

    for elemento in elementos_conector:
        conectores.append(elemento.text)

    for elemento in elementos_distancia:
        distancias.append(elemento.text)

    for elemento in elementos_avaliacoes:
        avaliacoes.append(elemento.text)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
# %%

print("Nomes Locais:", nomes_locais)
print("Tipos:", tipos)
print("Endereços:", enderecos)
print("Usos Restritos:", usos_restritos)
print("Estações:", estacoes)
print("Conectores:", conectores)
print("Distâncias:", distancias)
print("Avaliações:", avaliacoes)