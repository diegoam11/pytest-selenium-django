import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options

@pytest.fixture
def browser():
    """Configuración del navegador para las pruebas."""
    options = Options()
    options.add_argument("--headless")  # Ejecuta el navegador en modo headless
    driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)
    yield driver
    driver.quit()

def test_calculadora_suma(browser, live_server):
    """Prueba que verifica la funcionalidad de suma."""
    browser.get(f"{live_server.url}/")

    # Localizar los elementos de entrada y botones
    num1_input = browser.find_element(By.NAME, "num1")
    num2_input = browser.find_element(By.NAME, "num2")
    sumar_button = browser.find_element(By.XPATH, "//button[@value='sumar']")

    # Realizar una suma
    num1_input.send_keys("10")
    num2_input.send_keys("5")
    sumar_button.click()

    # Verificar que el resultado sea correcto
    resultado_text = browser.find_element(By.TAG_NAME, "h2").text
    assert "Resultado: 15.0" in resultado_text

def test_calculadora_resta(browser, live_server):
    """Prueba que verifica la funcionalidad de resta."""
    browser.get(f"{live_server.url}/")

    # Localizar los elementos de entrada y botones
    num1_input = browser.find_element(By.NAME, "num1")
    num2_input = browser.find_element(By.NAME, "num2")
    restar_button = browser.find_element(By.XPATH, "//button[@value='restar']")

    # Realizar una resta
    num1_input.send_keys("10")
    num2_input.send_keys("5")
    restar_button.click()

    # Verificar que el resultado sea correcto
    resultado_text = browser.find_element(By.TAG_NAME, "h2").text
    assert "Resultado: 5.0" in resultado_text

def test_calculadora_multiplicacion(browser, live_server):
    """Prueba que verifica la funcionalidad de multiplicación."""
    browser.get(f"{live_server.url}/")

    # Localizar los elementos de entrada y botones
    num1_input = browser.find_element(By.NAME, "num1")
    num2_input = browser.find_element(By.NAME, "num2")
    multiplicar_button = browser.find_element(By.XPATH, "//button[@value='multiplicar']")

    # Realizar una multiplicación
    num1_input.send_keys("10")
    num2_input.send_keys("5")
    multiplicar_button.click()

    # Verificar que el resultado sea correcto
    resultado_text = browser.find_element(By.TAG_NAME, "h2").text
    assert "Resultado: 50.0" in resultado_text

def test_calculadora_division(browser, live_server):
    """Prueba que verifica la funcionalidad de división."""
    browser.get(f"{live_server.url}/")

    # Localizar los elementos de entrada y botones
    num1_input = browser.find_element(By.NAME, "num1")
    num2_input = browser.find_element(By.NAME, "num2")
    dividir_button = browser.find_element(By.XPATH, "//button[@value='dividir']")

    # Realizar una división
    num1_input.send_keys("10")
    num2_input.send_keys("5")
    dividir_button.click()

    # Verificar que el resultado sea correcto
    resultado_text = browser.find_element(By.TAG_NAME, "h2").text
    assert "Resultado: 2.0" in resultado_text

def test_calculadora_division_por_cero(browser, live_server):
    """Prueba que verifica el manejo de división por cero."""
    browser.get(f"{live_server.url}/")

    # Localizar los elementos de entrada y botones
    num1_input = browser.find_element(By.NAME, "num1")
    num2_input = browser.find_element(By.NAME, "num2")
    dividir_button = browser.find_element(By.XPATH, "//button[@value='dividir']")

    # Intentar dividir entre cero
    num1_input.send_keys("10")
    num2_input.send_keys("0")
    dividir_button.click()

    # Verificar que se muestre el mensaje de error
    error_text = browser.find_element(By.TAG_NAME, "h2").text
    assert "Error: No se puede dividir entre cero." in error_text
