
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from telegram_bot import TelegramBot


chrome_driver = webdriver.Chrome()
bot=TelegramBot()
matrix_ruc=[
    "0992362316001"

]
for t in matrix_ruc:
    chrome_driver.get("https://srienlinea.sri.gob.ec/sri-en-linea/SriRucWeb/ConsultaRuc/Consultas/consultaRuc")
    print(chrome_driver.title)
    busca_ruc=chrome_driver.find_element(By.ID,"busquedaRucId")
    busca_ruc.send_keys(t)
    #busqueda por xpath
    #element_boton=chrome_driver.find_element(By.XPATH,'//*[@id="sribody"]/sri-root/div/div[2]/div/div/sri-consulta-ruc-web-app/div/sri-ruta-ruc/div[2]/div[1]/div[6]/div[2]/div/div[2]/div/button/span[1]')
    #busqueda por selector
    element_boton=chrome_driver.find_element(By.CSS_SELECTOR,'#sribody > sri-root > div > div.layout-main > div > div > sri-consulta-ruc-web-app > div > sri-ruta-ruc > div.row.ng-star-inserted > div.col-sm-12.ng-star-inserted > div:nth-child(7) > div.col-sm-6 > div > div:nth-child(2) > div > button > span.ui-button-text.ui-clickable')
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
    time.sleep(4)
print("fin")
chrome_driver.close()
