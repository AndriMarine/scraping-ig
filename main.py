import time
import excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

try:
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(executable_path=r"C:\Users\Telkom\Downloads\scraping-ig-mark\Drivers\geckodriver.exe", options=options)
    driver.get('https://www.instagram.com/')

    element = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.NAME,"username")))
    driver.find_element(By.NAME,"username").send_keys("input user")
    driver.find_element(By.NAME,"password").send_keys("input password")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(3)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(3)
    driver.get('https://www.instagram.com/p/Cdc46gopgm3/')

    i = 1
    while i < 3:
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button'))).click()
        time.sleep(2)
        i += 1
    
    user_names = []
    user_comments = []

    #meminta webdriver untuk menemukan elemen kolom komentar
    comment = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul")

    #mengambil data username dan komentar
    for c in comment:
        i = 1
        while i < 5:
            index = "ul["+ str(i) +"]"
            container = c.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/" + index)
            name = container.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/"+ index +"/div/li/div/div/div[2]/h3").text
            content = container.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/"+ index +"/div/li/div/div/div[2]/div[1]/span").text
            content = content.replace('\n', ' ').strip().rstrip()
            user_names.append(name)
            user_comments.append(content)
            i += 1
    
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div"))).click()
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[5]/div/div/div/div/div/div"))).click()
    
    user_names.pop(0)
    user_comments.pop(0)
    excel.export(user_names, user_comments)
    
finally:
    print("Finished")