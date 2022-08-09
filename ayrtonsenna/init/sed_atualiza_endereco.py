# from bs4 import BeautifulSoup
from utils import WDShorcuts
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
import os
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


def press_key_b4(key: str):
    from keyboard import is_pressed
    """
    Só dá break quando uma tecla específica é pressionada, e então, continua o código
    :param key:
    :return:
    """

    while True:
        #
        if is_pressed(key):
            if is_pressed(key):
                return True
        else:
            ...


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


# df = pd.read_excel("C:\\Users\\sbferreira\\Desktop\\silas\\__TURMAS.xlsx")
df = pd.read_excel(
    "C:\\Users\\sbferreira\\Desktop\\H\init\\data_files\\infantil.xlsx")


def get_campos(campo): return df[campo].to_list()


PATH = r"C:\Users\sbferreira\Documents\_TURMAS_PENDENTES"
# arqs = [os.path.join(PATH, p) for p in os.listdir(
#     PATH) if not os.path.isdir(os.path.join(PATH, p))]

# enable_download_in_headless_chrome(PATHUSED)
# ALUNO	NASCIMENTO	RA
narq = None
for nome_arq in os.listdir(PATH):
    for nome, nasc, ra in zip(get_campos("ALUNO"), get_campos("NASCIMENTO"), get_campos("RA")):
        narq = str(os.path.splitext(nome_arq)[0])
        file_fullname = os.path.join(PATH, nome_arq)
        print(nome, narq)
        if narq.upper().strip() == str(nome.upper().strip()):
            driver = webdriver.Chrome(service=service, options=options)
            driver.maximize_window()
            wds = WDShorcuts(driver)
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

            # campo_busca = driver.find_element(By.ID, "txtNumeroClasse")
            select_tipo_filtro.select_by_value('1')
            driver.find_element(By.ID, 'txtRa').send_keys(ra[:-1])
            driver.find_element(By.ID, "btnPesquisar").click()
            sleep(3.5)
            driver.execute_script("""
            document.querySelector("#tabelaDados > tbody > tr > td:nth-child(8) > a > i").click()
            """)
            sleep(5)
            el = driver.find_element(By.ID, "aba2")
            wds.click_ac_elementors(el)
            sleep(2)
            try:
                driver.find_element(By.ID, "btnUploadEndereco").click()
            except:
                driver.find_element(
                    By.ID, "btnVisualizarUploadEndereco").click()
            sleep(2)
            flsk = driver.find_element(By.ID, "fileComprovanteEndereco")
            flsk.send_keys(file_fullname)
            driver.find_element(By.ID, "btnSalvarUpload").click()

            clicked = driver.find_element(
                By.XPATH, '//*[@id="sedUiModalWrapper_1"]/div/div/div[3]/button[1]')
            sleep(2)
            # wds.send_keys_anywhere(Keys.ENTER)
            # wds.click_ac_elementors(clicked)
            press_key_b4("F9")
            driver.close()
            driver.quit()
            break
