from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


def main():
    driver = webdriver.Chrome(executable_path='C:\\Users\\yschlakm\\Desktop\\chromedriver_win32\\chromedriver.exe')
    driver.get("https://levnet.jct.ac.il/Login/Login.aspx")
    if "login" not in str.lower(driver.current_url):
        print("error: not on login page.")
        return
    username = driver.find_element_by_id("username")
    username.clear()
    username.send_keys("yschlakm")
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("12345dror")
    password.send_keys(Keys.RETURN)

    time.sleep(1)
    driver.get("https://levnet.jct.ac.il/Student/WeeklySchedule.aspx")
    time.sleep(5)
    print(len(driver.find_elements_by_xpath("/html/body/form/section[2]/div/div[1]/div[1]/a")))
    courseListBtn = driver.find_elements_by_xpath("/html/body/form/section[2]/div/div[1]/div[1]/a")[0]
    courseListBtn.click()
    # /html/body/form/section[2]/div/div[1]/div[3]/div/div/div[1]/a
    time.sleep(1000)
    driver.close()


if __name__ == "__main__":
    main()