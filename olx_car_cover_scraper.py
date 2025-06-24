
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Selenium options
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://www.olx.in/items/q-car-cover")

# Wait for content to load
time.sleep(5)

titles = []
prices = []
locations = []
links = []

ads = driver.find_elements(By.XPATH, '//li[contains(@class, "EIR5N")]')

for ad in ads:
    try:
        title = ad.find_element(By.TAG_NAME, "h6").text
        price = ad.find_element(By.TAG_NAME, "span").text
        location = ad.find_element(By.CLASS_NAME, "_2tW1I").text
        link = ad.find_element(By.TAG_NAME, "a").get_attribute("href")

        titles.append(title)
        prices.append(price)
        locations.append(location)
        links.append(link)
    except:
        continue

driver.quit()

# Save to CSV
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Location": locations,
    "Link": links
})
df.to_csv("car_covers_olx.csv", index=False)
print("Data saved to car_covers_olx.csv")
