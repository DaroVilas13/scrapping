
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from telegram_bot import TelegramBot
from mongodb import MongoDB
from dotenv import load_dotenv
import os
from capmonster_python import RecaptchaV2Task

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_driver = webdriver.Chrome(options=options)
load_dotenv()
API_KEY=os.getenv("API_KEY")
WEBSITE_KEY=os.getenv("WEBSITE_KEY")
bot=TelegramBot()
db = MongoDB()
matrix_ruc=[
    "0992362316001"

]
for t in matrix_ruc:
    print(chrome_driver.title)
    chrome_driver.get("https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc")
    busca_ruc=chrome_driver.find_element(By.ID,"busquedaRucId")
    busca_ruc.send_keys(t)
    #busqueda por xpath
    #element_boton=chrome_driver.find_element(By.XPATH,'//*[@id="sribody"]/sri-root/div/div[2]/div/div/sri-consulta-ruc-web-app/div/sri-ruta-ruc/div[2]/div[1]/div[6]/div[2]/div/div[2]/div/button/span[1]')
    #busqueda por selector
    element_boton=chrome_driver.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div.col-sm-12.ng-star-inserted > div:nth-child(7) > div.col-sm-6 > div > div:nth-child(2) > div > button > span.ui-button-text.ui-clickable')
    #resuelve el capchat
    capmonster = RecaptchaV2Task(API_KEY)
    task_id = capmonster.create_task("https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc", WEBSITE_KEY, no_cache=True)
    result = capmonster.join_task_result(task_id).get("gRecaptchaResponse")
    chrome_driver.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = " f"'{result}';")
    chrome_driver.find_element(By.ID, "ngrecaptcha-0").click()
    element_boton.click()
    respuesta_contenedor=chrome_driver.find_element(By.CLASS_NAME,'container')
    #ruc_respuesta=(respuesta_contenedor.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div:nth-child(1) > sri-mostrar-contribuyente > div:nth-child(1) > div.col-sm-4 > div:nth-child(2) > div > span')).text
    ruc_texto=(respuesta_contenedor.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div:nth-child(1) > sri-mostrar-contribuyente > div:nth-child(1) > div.col-sm-4 > div:nth-child(2) > div > span')).text
    bot.send_tg_message(ruc_texto)
    razon_social_texto=(respuesta_contenedor.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div:nth-child(1) > sri-mostrar-contribuyente > div:nth-child(1) > div.col-sm-8 > div:nth-child(2) > div > span')).text
    bot.send_tg_message(razon_social_texto)
    representante_legal_texto=(respuesta_contenedor.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div:nth-child(1) > sri-mostrar-contribuyente > div:nth-child(1) > div:nth-child(4) > div > div.col-sm-8.ng-star-inserted > span > div > div.col-sm-12 > div > div.col-sm-12.ng-star-inserted > div > div:nth-child(2)')).text
    bot.send_tg_message(representante_legal_texto)
    representante_legal_ci_texto=(respuesta_contenedor.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div:nth-child(1) > sri-mostrar-contribuyente > div:nth-child(1) > div:nth-child(4) > div > div.col-sm-8.ng-star-inserted > span > div > div.col-sm-12 > div > div.col-sm-12.ng-star-inserted > div > div:nth-child(4)')).text
    bot.send_tg_message(representante_legal_ci_texto)
    db.insert_sri_consulta(text=ruc_texto,text1=razon_social_texto,text2=representante_legal_texto,text3=representante_legal_ci_texto)
    time.sleep(4)
print("fin")
chrome_driver.close()
