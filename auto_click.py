# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

#Ler arquivo TXT com URL
arq = open('urls.txt', 'r')
texto = arq.readlines()
driver = webdriver.Chrome(ChromeDriverManager().install())
#Loop
for linha in texto :
    #URL inserida no navegador
    driver.get(linha)
    # Texto do Botão - um nome do botão
    element = driver.find_element_by_link_text("NOME DO BOTÃO TEXTO")
    #Tempo de aguarda
    time.sleep(10)
    # click no botão
    element.click()
    time.sleep(10)
#sair do arquivo
arq.close()  
#sair do navegador
driver.quit()
