from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")

# Preencher campos do formulário de exemplo
driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[3]/div/form/input[1]").send_keys("João")
driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[3]/div/form/input[2]").send_keys("Silva")

time.sleep(3)
# Enviar o formulário (simulado, pois não há backend real)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[1]/div[1]/div[3]/div/form/input[3]").click()

driver.quit()