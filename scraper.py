from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# =====================
# EDGE DRIVER AYARLARI
# =====================
EDGE_DRIVER_PATH = "drivers/msedgedriver.exe"

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=options)

# =====================
# N11 HESABINA GİRİŞ YAP
# =====================
print("=== N11 Hesabına Giriş ===\n")
kullanici_adi = input("N11 E-posta veya Kullanıcı Adı: ").strip()
sifre = input("Şifre: ").strip()

# N11 giriş sayfasına git
driver.get("https://www.n11.com/login")
time.sleep(3)

try:
    # E-posta/Kullanıcı adı alanını doldur
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(kullanici_adi)
    
    # Şifre alanını doldur
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(sifre)
    
    # Giriş yap butonuna tıkla
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Giriş sonucunu bekle
    time.sleep(5)
    print("✓ Giriş işlemi tamamlandı.\n")
    
except Exception as e:
    print(f"✗ Giriş hatası: {e}\n")
    driver.quit()
    exit()

# =====================
# KULLANICIDAN PARÇA ADI AL
# =====================
parca_adi = input("Aramak istediğin parça adı: ").strip()
search_query = parca_adi.replace(" ", "+")

url = f"https://www.n11.com/arama?q={search_query}"
driver.get(url)

# Sayfanın yüklenmesini bekle
time.sleep(5)

print("\n--- N11 Arama Sonuçları ---\n")

# =====================
# ÜRÜNLERİ ÇEK
# =====================
products = driver.find_elements(By.CSS_SELECTOR, "li.column")

if not products:
    print("Ürün bulunamadı.")
else:
    for i, product in enumerate(products[:5], start=1):
        try:
            name = product.find_element(By.CSS_SELECTOR, "h3.productName").text
            price = product.find_element(By.CSS_SELECTOR, "span.newPrice").text
            print(f"{i}. Ürün: {name}")
            print(f"   Fiyat: {price}\n")
        except:
            continue

# =====================
# TARAYICIYI KAPAT
# =====================
driver.quit()
