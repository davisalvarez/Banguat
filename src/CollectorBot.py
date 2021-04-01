
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "bot/chromedriver.exe"

def starBot(fechaI, fechaF, moneda, dias):
    pagina = webdriver.Chrome(PATH)
    pagina.get('https://www.banguat.gob.gt/cambio/')

    try:
        # Click en moneda
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[2]/td/select/option["+str(moneda)+"]"))
        )
        campo.click()

        # Click en Dia 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/select/option["+fechaI[0]+"]"))
        )
        campo.click()

        # Click en Mes 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/select/option["+fechaI[1]+"]"))
        )
        campo.click()

        # Click en Año 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/select/option["+fechaI[2]+"]"))
        )
        campo.click()


        # Click en Dia 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/select/option["+fechaF[0]+"]"))
        )
        campo.click()

        # Click en Mes 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/select/option["+fechaF[1]+"]"))
        )
        campo.click()

        # Click en Año 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[3]/select/option["+fechaF[2]+"]"))
        )
        campo.click()

        # Click en checkbox excel
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[4]/td/p[1]/input"))
        )
        campo.click()

        #Click en boton Consultar
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[4]/td/p[2]/input"))
        )
        campo.click()

        rate = []
        for ele in range(2, dias, 1):
            dato = WebDriverWait(pagina, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr["+str(ele)+"]/td[2]"))
            )
            try:
                rate.append(float(dato.text))
            except:
                print("No se pudo completar el proceso de extración...")
                pagina.quit()
                return rate
        pagina.quit()
        return rate
    except:
        pagina.quit()
        return []


"""
def starBot(fechaI, fechaF, moneda):
    pagina = webdriver.Chrome(PATH)
    pagina.get('https://www.banguat.gob.gt/cambio/')

    try:
        # Click en moneda
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[2]/td/select/option["+str(moneda)+"]"))
        )
        campo.click()

        # Click en Dia 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]/select/option["+fechaI[0]+"]"))
        )
        campo.click()

        # Click en Mes 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/select/option["+fechaI[1]+"]"))
        )
        campo.click()

        # Click en Año 1
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/select/option["+fechaI[2]+"]"))
        )
        campo.click()


        # Click en Dia 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[1]/select/option["+fechaF[0]+"]"))
        )
        campo.click()

        # Click en Mes 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/select/option["+fechaF[1]+"]"))
        )
        campo.click()

        # Click en Año 2
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/center/div[2]/form[3]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[3]/select/option["+fechaF[2]+"]"))
        )
        campo.click()

        # Click en checkbox excel
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[4]/td/p[1]/input"))
        )
        campo.click()

        #Click en boton Consultar
        campo = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/center/div[2]/form[3]/table/tbody/tr[4]/td/p[2]/input"))
        )
        campo.click()
        
        dato = WebDriverWait(pagina, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[2]"))
        )
        h = input("->")
        return dato.text
    except:
        pagina.quit()
        return -1
"""