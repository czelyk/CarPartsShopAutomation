from selenium import webdriver
from selenium.webdriver.common.by import By

# Driver yolunu belirt
driver_path = "./drivers/chromedriver.exe"  # Windows için

driver = webdriver.Chrome(executable_path=driver_path)

# Siteyi aç
driver.get("https://www.ornek-parca-sitesi.com")

# Arama kutusuna parça yaz
search_box = driver.find_element(By.ID, "search-input")
search_box.send_keys("debriyaj seti")
search_box.submit()

# Fiyatı çek
price_element = driver.find_element(By.CLASS_NAME, "price")
price = float(price_element.text.replace("TL", "").replace(",", ""))
print(f"Alış fiyatı: {price} TL")

driver.quit()