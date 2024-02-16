from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clicar_em_ver_todas_avaliacoes(driver):
    wait = WebDriverWait(driver, 10)

    # XPath do link "Ver todas as avaliações"
    xpath_ver_todas_avaliacoes = '//label[@class="sc-kOHTFB brGmaU" and text()="Ver todas as avaliações"]'

    try:
        # Aguarde até que o link seja visível e clicável
        ver_todas_avaliacoes = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_ver_todas_avaliacoes)))

        # Clique no link "Ver todas as avaliações"
        ver_todas_avaliacoes.click()

        # Aguarde até que a URL mude, indicando a navegação para a página de comentários
        wait.until(EC.url_changes(driver.current_url))
    except:
        print("Click realizado: 'Ver todas as avaliações'.")
        
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
        print("Click realizado: 'Ver mais avaliações'.")
