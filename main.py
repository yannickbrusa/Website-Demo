from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("Welche Aktie willst du traden?")
print("Gebe das Kürzel für Aktie 1 ein:")
stock1_name = input()
print("Gebe das Kürzel für Aktie 2 ein:")
stock2_name = input()
print("Du tradest ab jetzt den Kurs von " + stock1_name + " zu " + stock2_name)
#driver = webdriver.Chrome()
#driver.get("https://de.finance.yahoo.com/gainers")
#driver.find_element_by_name("agree").click()
#test1 = driver.find_element_by_xpath("//th[4]/span[1]").click()
#test1.click()