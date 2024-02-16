from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from navegacao import clicar_em_ver_todas_avaliacoes, clicar_em_ver_mais_avaliacoes
from extracao import extrair_comentarios, extrair_informacoes_produto
from manipulacao_dados import tokenizacao, tokens_mais_frequentes, processar_comentarios

# Configuração do serviço
servico = Service(GeckoDriverManager().install())

# Configuração das opções do Firefox (opcional, dependendo das configurações desejadas)
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--ignore-certificate-errors')

# Inicialização do navegador com opções e serviço
navegador = webdriver.Firefox(service=servico, options=firefox_options)

# Abrir a página desejada
url = "https://www.magazineluiza.com.br/apple-iphone-13-128gb-meia-noite-tela-61-12mp/p/234661800/te/ip13/"
navegador.get(url)

# Clicar em "Ver mais avaliações" várias vezes para navegar por diferentes páginas
clicar_em_ver_todas_avaliacoes(navegador)
for _ in range(7):  # Modifique o número conforme necessário
    clicar_em_ver_mais_avaliacoes(navegador)

# Extrair comentários após a navegação
comentarios = extrair_comentarios(navegador)
produto = extrair_informacoes_produto(navegador)
# Manipulação de dados
processar_comentarios(comentarios, produto)

# Fechar o navegador no final do script
navegador.quit()
