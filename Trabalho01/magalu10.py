from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clicar_em_ver_mais_avaliacoes(driver):
    wait = WebDriverWait(driver, 10)

    # XPath do link "Ver mais avaliações"
    xpath_ver_mais_avaliacoes = '//a[@data-testid="pagination-button"]'

    try:
        # Aguarde até que o link seja visível e clicável
        ver_mais_avaliacoes = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_ver_mais_avaliacoes)))

        # Clique no link "Ver mais avaliações"
        ver_mais_avaliacoes.click()

        # Aguarde até que a URL mude, indicando a navegação para a próxima página
        wait.until(EC.url_changes(driver.current_url))
    except:
        print("Não foi possível encontrar o elemento 'Ver mais avaliações'.")

# Configuração do serviço
servico = Service(GeckoDriverManager().install())

# Configuração das opções do Firefox (opcional, dependendo das configurações desejadas)
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--ignore-certificate-errors')

# Inicialização do navegador com opções e serviço
navegador = webdriver.Firefox(service=servico, options=firefox_options)

# Abrir a página desejada
navegador.get("https://www.magazineluiza.com.br/review/ecadg9ee4f/colchao-magnetico-queen-bio-massageador-eco-prince-eco-new-colchoes/CO/CCBQ/")

# Clicar em "Ver mais avaliações" várias vezes para navegar por diferentes páginas
for _ in range(3):  # Modifique o número conforme necessário
    clicar_em_ver_mais_avaliacoes(navegador)


