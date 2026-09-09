import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProcesoDeConfiguracion:
	def __init__(self, plataforma, navegador):
		self.navegador = navegador
		self.plataforma = plataforma

		if self.navegador == "webdriver.Chrome()":
			self.proceso_con_chrome()
			print("Proceso finalizado.")

		elif self.navegador == "webdriver.Firefox()":
			print("Proceso no definido.")
		
		elif self.navegador == "webdriver.Chrome()":
			print("Proceso no definido.")

	def proceso_con_chrome(self):		
		driver = webdriver.Chrome()
		nombre_navegador = driver.capabilities['browserName']
		print(f"Iniciado {nombre_navegador}...", end=" ")
		print(f"Hecho.")
	
		print(f"Ingresando a {self.plataforma}", end=" ")
		driver.get(self.plataforma)
		print(f"Hecho.")
		time.sleep(0.5)

		print(f"Ingresando usuario...", end=" ")
		username = driver.find_element(By.ID, "username")
		username.send_keys("Admin")
		print("Hecho.")
		time.sleep(0.5)
		
		print(f"Ingresando usuario...", end=" ")
		password = driver.find_element(By.ID, "password")
		password.send_keys("12345")
		print("Hecho.")
		time.sleep(0.5)

		print("Ingresando a al panel de control...", end=" ")
		entrar = driver.find_element(By.ID, "btn-login")
		entrar.click()
		print("Hecho.")
		time.sleep(0.5)

		registros = driver.find_elements(By.CLASS_NAME, "btn-delete")
		print(f"Total de registros encontrados: {len(registros)}")
		contador = 0

		while True:
			eliminar_registros = driver.find_elements(By.CLASS_NAME, "btn-delete")

			if not eliminar_registros:
				break
			
			eliminar_registros[0].click()
			print("Registro eliminado...")
			contador += 1
			time.sleep(0.5)

		print(f"Total de registros eliminados: {contador}")

		print("Agregando un nuevo registro...")
		agregar_registro = driver.find_element(By.ID, "btn-open-add-modal")
		agregar_registro.click()
		agregar_ip_de_camara = driver.find_element(By.ID, "modal-cam-ip")
		agregar_ip_de_camara.send_keys("192.168.1.20")
		usuario_de_camara = driver.find_element(By.ID, "modal-cam-user")
		usuario_de_camara.send_keys("MB-1223")
		password_de_camara = driver.find_element(By.ID, "modal-cam-pass")
		password_de_camara.send_keys("password")
		guardar_registro = driver.find_element(By.ID, "btn-save-camera")
		guardar_registro.click()
		time.sleep(10)
		print("Nuevo registro agregado.")


def seleccion_de_web_driver():
	while True:
		web_driver = input("navegador> ")

		if web_driver == "1":
			web_driver = "webdriver.Chrome()"
			return web_driver
			break

		elif web_driver == "2":
			web_driver = "webdriver.Firefox()"
			return web_driver
			break

		elif web_driver == "3":
			web_driver = "webdriver.Edge()"
			return web_driver
			break


def guardar_config_opcion():
	while True:
		seleccion = input("¿Desea guardar ésta configuración? [Y/n]")

		if seleccion == "Y" or seleccion == "y" or seleccion == "s" or seleccion == "S":
			return seleccion
			break
		elif seleccion == "n" or seleccion == "N":
			return seleccion
			break
		else:
			print("Opcion no valida!")
		

def guardar_config(guardar_configuracion, web_driver_final):
	if guardar_configuracion == "Y" or guardar_configuracion == "y" or guardar_configuracion == "s" or guardar_configuracion == "S":
		with open("config.txt", "w", encoding="utf-8") as archivo:
			archivo.write(web_driver_final)

	elif guardar_configuracion == "n" or guardar_configuracion == "N":
		print("No se guardó ninguna configuración para sesiones futuras.")

	else:
		guardar_config()

def proceso(web_driver_final):
	inicio_del_proceso = ProcesoDeConfiguracion("https://jaco-deb.github.io/Laboratorio-Selenium/HVR_Laboratorio.html", web_driver_final)

if Path("config.txt").is_file():
	with open("config.txt", "r", encoding="utf-8") as archivo:
	    web_driver_txt = archivo.read()
	    
	proceso(web_driver_txt)

else:
	print("""
Seleccione el número del navegador que desea utilizar:
	1. Chrome
	2. Firefox
	3. Edge
		""")

	seleccion_de_driver = seleccion_de_web_driver()
	guardar_o_no_guardar = guardar_config_opcion()
	guardar_config(guardar_o_no_guardar, seleccion_de_driver)
	proceso(seleccion_de_driver)
	
	