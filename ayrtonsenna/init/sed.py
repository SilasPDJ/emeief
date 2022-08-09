# from bs4 import BeautifulSoup
from utils import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
# import pandas as pd
import pandas as pd
options = webdriver.ChromeOptions()
# Path to your chrome profile"
options.add_argument(
    "user-data-dir=C:\\Users\\sbferreira\\Desktop\\H\\_\\profile")

service = Service(ChromeDriverManager().install())


PATHUSED = os.path.join(os.path.dirname(__file__), "data_files")
# input(os.path.exists(PATHUSED))

# f'\\{os.listdir(pathinit)[0]}'


def enable_download_in_headless_chrome(download_dir):
    """
    :param download_dir: where do you want to download it?
    :return: change download_dir any moment during driver execution
    """
    download_dir = download_dir.replace('/', '\\')
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {
        'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)


def logar_sed():
    # login inicio
    login = "rg180581612sp"
    senha = "secretaria2022"
    sleep(3)
    campo_login = driver.find_element(By.ID, "name")
    campo_senha = driver.find_element(By.ID, "senha")
    campo_login.send_keys(login)
    campo_senha.send_keys(senha)
    driver.find_element(By.ID, "botaoEntrar").click()
    sleep(4)
    # -------- fim login

# logar_sed()


def search_menu(searched):
    dmft = driver.find_element(By.ID,
                               "decorMenuFilterTxt")
    dmft.send_keys(searched)
    dmft.send_keys(Keys.ENTER)


df = pd.read_excel("C:\\Users\\sbferreira\\Desktop\\silas\\__TURMAS.xlsx")
def get_campos(campo): return df[campo].to_list()


for cod, turma in zip(get_campos("Códigos"), get_campos("Turmas")):
    driver = webdriver.Chrome(service=service, options=options)
    enable_download_in_headless_chrome(PATHUSED)
    driver.get("https://sed.educacao.sp.gov.br/Inicio")
    try:
        logar_sed()
    except NoSuchElementException:
        pass
    search_menu("Ficha aluno")
    driver.implicitly_wait(30)
    select_tipo_filtro_options = {1: "RA", 2: "Nome Fonético", 3: "Nome Completo", 4: "Escola",
                                  5: "Número da Classe", 6: "Filiação 1", 7: "Filiação 2", 8: "Documento", 11: "Responsável"}
    select_tipo_filtro = Select(
        driver.find_element(By.ID, "TipoConsultaFichaAluno"))

    campo_busca = driver.find_element(By.ID, "txtNumeroClasse")
    select_tipo_filtro.select_by_value('5')
    campo_busca.send_keys(cod)
    print(cod)
    driver.find_element(By.ID, "btnPesquisar").click()

    def contains_title(item): return driver.find_element(
        By.XPATH, f'//*[contains(text(),"{item}")]')

    contains_title(" Gerar Excel").click()
    sleep(1)
    contains_title("Arquivo CSV").click()
    from pathlib import Path
    sleep(10)
    files = [os.path.join(PATHUSED, x) for x in os.listdir(
        PATHUSED) if x.endswith(".csv")]
    last_file = max(files, key=os.path.getctime)
    # os.rename

    # [print(last_file) for i in range(10)]

    os.rename(last_file, turma+".csv")
    driver.close()
    driver.quit()