import time
from selenium import webdriver
host = input("Enter host name: ");
time.sleep(0.2);
user = input("Enter user name: ");
time.sleep(0.2);
msg = input("Enter message: ");
time.sleep(0.2);
nsend = int(input("Enter sends number: "))
time.sleep(0.2);
url='https://'+host+'/'+user
time.sleep(0.2)
driver = webdriver.Chrome('<driver>')
for x in range(nsend):
    driver.get(url);
    time.sleep(3)
    search_box = driver.find_element_by_name('<text_area>')
    time.sleep(1)
    span = driver.find_element_by_xpath("<path>")
    btn = driver.find_element_by_xpath("<path>")
    time.sleep(1)
    span.click()
    time.sleep(1)
    search_box.send_keys(msg)
    time.sleep(1)
    btn.click()
    time.sleep(5)
driver.quit()
