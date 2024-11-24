import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configurar el navegador Edge para las pruebas
@pytest.fixture
def driver():
   edge_options = Options()
   edge_options.add_argument("--start-maximized")
   driver = webdriver.Edge(options=edge_options)
   yield driver
   driver.quit()

# Crear carpeta 'imagenes' si no existe
@pytest.fixture(scope="session", autouse=True)
def create_images_folder():
   if not os.path.exists("imagenes"):
      os.makedirs("imagenes")

# Función para esperar un elemento
def esperar_elemento(driver, by, value, timeout=10):
   return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# Prueba 1: Login vacío (sin credenciales)
def test_login_fallido(driver):
   url = "https://bondelic.netlify.app"
   driver.get(url)

   
   email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
   password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
   password_field.send_keys(Keys.RETURN) 

   
   driver.save_screenshot("imagenes/login_fallido.png")

# Prueba 2: Login con credenciales válidas
def test_login_con_credenciales(driver):
   url = "https://bondelic.netlify.app"
   driver.get(url)

   
   email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
   password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
   email_field.clear()
   password_field.clear()
   email_field.send_keys("keury@example.com") 
   password_field.send_keys("369") 

   
   driver.save_screenshot("imagenes/login_con_credenciales_1.png")

   
   password_field.send_keys(Keys.RETURN)

   time.sleep(2)

   
   driver.save_screenshot("imagenes/login_con_credenciales_2.png")

# Prueba 3: Hacer scroll down hasta el final de la página de inicio y tomar una captura
def test_scroll_inicial(driver):
   url = "https://bondelic.netlify.app"
   driver.get(url)
   time.sleep(2)

   
   email_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
   password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
   email_field.clear()
   password_field.clear()
   email_field.send_keys("keury@example.com") 
   password_field.send_keys("369") 
   password_field.send_keys(Keys.RETURN)
   time.sleep(5)

   
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
   
   time.sleep(3)

   
   driver.save_screenshot("imagenes/inicio_scroll.png")

# Prueba 4: Ir a la página de productos y tomar una captura
def test_pagina_productos(driver):
   url = "https://bondelic.netlify.app"
   driver.get(url)

   
   email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
   password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
   email_field.clear()
   password_field.clear()
   email_field.send_keys("keury@example.com") 
   password_field.send_keys("369")  
   password_field.send_keys(Keys.RETURN)

   
   productos_button = esperar_elemento(driver, By.LINK_TEXT, "Nuestros productos")
   productos_button.click()

   
   driver.save_screenshot("imagenes/pagina_productos.png")

# Prueba 5: Ir a la página del formulario y tomar una captura
def test_pagina_formulario(driver):
   url = "https://bondelic.netlify.app"
   driver.get(url)

   
   email_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='text']")
   password_field = esperar_elemento(driver, By.CSS_SELECTOR, "input[type='password']")
   email_field.clear()
   password_field.clear()
   email_field.send_keys("keury@example.com") 
   password_field.send_keys("369")
   password_field.send_keys(Keys.RETURN)

   
   formulario_button = esperar_elemento(driver, By.LINK_TEXT, "Registrate")
   formulario_button.click()

   
   driver.save_screenshot("imagenes/pagina_formulario.png")
