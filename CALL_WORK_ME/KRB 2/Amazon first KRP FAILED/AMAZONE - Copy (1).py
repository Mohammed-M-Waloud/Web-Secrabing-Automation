from telnetlib import EC
import names, os, random, string, phonenumbers, warnings
from captcha_solver import CaptchaSolver
from selenium.webdriver import Keys
clear = lambda: os.system('cls')
clear()
from threading import Thread
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random_address
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import phone_iso3166.country as countries

warnings.filterwarnings("ignore", category=DeprecationWarning)
global url1, url2
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options = uc.ChromeOptions()
    with open('vpn.txt', 'r') as e:
        proxy = e.readline()
        e.close()
    with open('vpn.txt', 'r') as e:
        data = e.read().splitlines(True)
        e.close()
    with open('vpn.txt', 'w') as e:
        e.writelines(data[1:])
        e.close()
    with open('vpn.txt', 'a') as e:
        e.write(proxy)
        e.close()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    print(Fore.RED + 'proxy : ' + Fore.GREEN + proxy)
    # chrome_options.experimental_options["prefs"] = {
    #     "profile.managed_default_content_settings.images": 2,
    #     "profile.managed_default_content_settings.stylesheets": 2,
    #     # "profile.managed_default_content_settings.javascript": 2,
    #     "profile.managed_default_content_settings.geolocation": 2,
    #     "profile.default_content_setting_values.notifications": 2,
    # }
    if headless == 0:
        chrome_options.add_argument("--headless")
    # chrome_options.add_extension('so.crx')
    # chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--clear-token-service")
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument("--aggressive-cache-discard")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-offline-load-stale-cache")
    chrome_options.add_argument("--disable-3d-apis")
    chrome_options.add_argument("--disable-gpu-shader-disk-cache")
    chrome_options.add_argument("--media-cache-size=0")
    chrome_options.add_argument("--disk-cache-size=0")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    # chrome_options.add_argument("--user-agent= Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=700,700")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--silent")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    # driver = uc.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.delete_all_cookies()
    return driver


def readEmail():
    with open('Emails.txt', 'r') as e:
        EmailData = e.readline()
        e.close()
    with open('Emails.txt', 'r') as e:
        data = e.read().splitlines(True)
        e.close()
    with open('Emails.txt', 'w') as e:
        e.writelines(data[1:])
        e.close()

    return EmailData


def readNumber():
    with open('Number.txt', 'r') as e:
        Number = e.readline()
        e.close()
    with open('Number.txt', 'r') as e:
        data = e.read().splitlines(True)
        e.close()
    with open('Number.txt', 'w') as e:
        e.writelines(data[1:])
        e.close()
    return Number


def readExtension():
    with open('Extension.txt', 'r') as e:
        Extension = e.readline()
        e.close()
    with open('Extension.txt', 'r') as e:
        data = e.read().splitlines(True)
        e.close()
    with open('Extension.txt', 'w') as e:
        e.writelines(data[1:])
        e.close()
    with open('Extension.txt', 'a') as e:
        e.write(Extension)
        e.close()
    return Extension


def expand_shadow_element(element, driver):
	shadow_root=driver.execute_script('return arguments[0].shadowRoot', element)
	return shadow_root


def StartLogin(driver, EmailData):
    try:
            url1 = random.choice(list(open('URL1.txt', 'r').readlines()))
            url2 = random.choice(list(open('URL2.txt', 'r').readlines()))
            Email, Pass = str(EmailData).split('|')
            driver.get(url1)
            # WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located)
            if 'ap_password' in driver.page_source:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='email')).send_keys(
                    Email)
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass, Keys.RETURN)

            else:
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='email')).send_keys(
                    Email, Keys.RETURN)
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass, Keys.RETURN)
            sleep(0.3)
            if "auth-warning-message-box" in driver.page_source or "auth-captcha-image-container" in driver.page_source or 'alt="CAPTCHA"' in driver.page_source:
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(3))
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass)
                sleep(0.2)
                with open(f"trash/{result_str}.png", "ab") as file:
                    captcha_img = WebDriverWait(driver, 100).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, "#auth-captcha-image"))
                    file.write(captcha_img.screenshot_as_png)
                with open("captcha code.txt", "r") as c:
                    cap = c.readline()
                    solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                    raw_data = open(f"trash/{result_str}.png", 'rb').read()
                solving_captcha = solver.solve_captcha(raw_data)
                WebDriverWait(driver, 100).until(lambda driver: driver.find_element("id", "auth-captcha-guess")).send_keys(
                    solving_captcha)
                sleep(0.1)
                WebDriverWait(driver, 100).until(lambda driver: driver.find_element("id", "signInSubmit")).click()
                sleep(0.1)
                os.remove(f'trash/{result_str}.png')

            sleep(0.3)
            if "auth-warning-message-box" in driver.page_source:
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(3))
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass)
                sleep(0.2)
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass)
                with open(f"trash/{result_str}.png", "ab") as file:
                    captcha_img = WebDriverWait(driver, 100).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, "#auth-captcha-image"))
                    file.write(captcha_img.screenshot_as_png)
                with open("captcha code.txt", "r") as c:
                    cap = c.readline()
                    solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                    raw_data = open(f"trash/{result_str}.png", 'rb').read()
                solving_captcha = solver.solve_captcha(raw_data)
                WebDriverWait(driver, 100).until(lambda driver: driver.find_element("id", "auth-captcha-guess")).send_keys(
                    solving_captcha)
                sleep(0.1)
                WebDriverWait(driver, 100).until(lambda driver: driver.find_element("id", "signInSubmit")).click()
                sleep(0.2)
                os.remove(f'trash/{result_str}.png')
            sleep(0.3)
            if "auth-error-message-box" in driver.page_source or "forgotpassword/reverification?" in driver.current_url:
                print(
                    Fore.LIGHTRED_EX + "[!] Invalid Login, Check Your Email or Password or maybe Account Bloced!" + Fore.RESET)
                driver.quit()
            sleep(0.3)
            try:
                driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[5]/div/a").click()
            except:
                pass

            if 'Select a Merchant and Marketplace'in driver.page_source:
                sleep(0.5)
                driver.find_element(By.XPATH,
                                    '//*[@id="picker-container"]/div/div[2]/div/div[3]/div/div[1]/button').click()
                sleep(0.3)
                driver.find_element(By.XPATH,
                                    '//*[@id="picker-container"]/div/div[3]/div/button').click()
                sleep(0.2)
                driver.get(url2)
                numofcall=open('numOfCall.txt','r').read()
                for i in range(0,int(numofcall)):
                    if 'Internal failure'in driver.page_source:
                        break
                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#root > div > form > div > div.hill-primary-input-container > div > kat-textarea'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    letters = string.ascii_lowercase
                    for i in range(0, 5):
                        r = random.randint(5, 12)
                        result_str = ''.join(random.choice(letters) for i in range(r))
                        shadow_root1.find_element(By.ID, value='textarea-2').send_keys(
                            result_str)
                        shadow_root1.find_element(By.ID, value='textarea-2').send_keys(" ")

                    Number = readNumber()
                    country = countries.phone_country('+' + Number)
                    countryCode = phonenumbers.country_code_for_region(country)
                    callNum = Number.split(str(countryCode), 1)[1]
                    # print(country)
                    # print(countryCode)
                    # print(callNum)

                    WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="root"]/div/form/div/div[3]/kat-tabs/kat-tab/kat-box/div[2]/div[1]/div/div[2]/span[3]/kat-dropdown')).click()
                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#root > div > form > div > div.hill-contact-methods > kat-tabs > kat-tab > kat-box > div.hill-form-fields-container.hill-phone-fields > div.hill-form-fields-container.hill-phone-input > div > div.inputs > span.country-selector > kat-dropdown'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    # try:
                    if countryCode == 1:
                        with open('countryUSA.txt', 'r') as co:
                            country = co.read()

                    shadow_root1.find_element(By.CSS_SELECTOR, value=f"kat-option[value='{country}']").click()
                    # shadow_root1.find_element(By.CSS_SELECTOR, value=f"kat-option[value='US']").click()

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='div.inputs > span.phone-number > span.phone-number-input > div > kat-input'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    shadow_root1.find_element(By.CSS_SELECTOR, value="#input-3").send_keys(callNum)

                    ext = readExtension()
                    if ext == "" or ext == " ":
                        pass
                    else:
                        element = WebDriverWait(driver, 20).until(
                            lambda driver:
                            driver.find_element(
                                by=By.CSS_SELECTOR,
                                value='span.phone-number-extension > div > kat-input'))
                        shadow_root1 = expand_shadow_element(element, driver)
                        shadow_root1.find_element(By.CSS_SELECTOR, value="#input-4").send_keys(ext)
                        element = WebDriverWait(driver, 20).until(
                            lambda driver:
                            driver.find_element(
                                by=By.CSS_SELECTOR,
                                value='#katal-id-11'))
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        driver.execute_script("arguments[0].click();", element)
                    sleep(0.5)
                    letters = string.ascii_lowercase
                    result_str = ''.join(random.choice(letters) for i in range(3))
                    with open(f"trash/{result_str}.png", "ab") as file:
                        f=0
                        while f==0:
                            try:
                                captcha_img = WebDriverWait(driver, 100).until(
                                    lambda driver: driver.find_element(By.CSS_SELECTOR, "div.captcha-image > img"))
                                file.write(captcha_img.screenshot_as_png)
                                f=1
                            except:
                                f=0
                    with open("captcha code.txt", "r") as c:
                        cap = c.readline()
                        solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                        raw_data = open(f"trash/{result_str}.png", 'rb').read()
                    solving_captcha = solver.solve_captcha(raw_data)

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='div.hill-captcha-container > div.captcha-input > div > kat-input'))

                    shadow_root1 = expand_shadow_element(element, driver)

                    shadow_root1.find_element(By.ID, value='input-5').send_keys(
                        solving_captcha)
                    os.remove(f'trash/{result_str}.png')

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#call-me-now-button'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    element = shadow_root1.find_element(By.CSS_SELECTOR, value="button")

                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    driver.execute_script("arguments[0].click();", element)

                    sleep(0.3)
                    if 'cancel-call-button' in driver.page_source:
                        print(Fore.GREEN+'Success Call >>> '+str(callNum))

                    driver.refresh()
                    sleep(1)
                driver.quit()
            elif 'Not Authorized' in driver.page_source:
                driver.quit()
                print(22222222)
            else:
                driver.get(url2)
                numofcall = open('numOfCall.txt', 'r').read()
                for i in range(0, int(numofcall)):

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#root > div > form > div > div.hill-primary-input-container > div > kat-textarea'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    letters = string.ascii_lowercase
                    for i in range(0, 5):
                        r = random.randint(5, 12)
                        result_str = ''.join(random.choice(letters) for i in range(r))
                        shadow_root1.find_element(By.ID, value='textarea-2').send_keys(
                            result_str)
                        shadow_root1.find_element(By.ID, value='textarea-2').send_keys(" ")

                    Number = readNumber()
                    country = countries.phone_country('+' + Number)
                    countryCode = phonenumbers.country_code_for_region(country)
                    callNum = Number.split(str(countryCode), 1)[1]
                    # print(country)
                    # print(countryCode)
                    # print(callNum)
                    WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="root"]/div/form/div/div[3]/kat-tabs/kat-tab/kat-box/div[2]/div[1]/div/div[2]/span[3]/kat-dropdown')).click()
                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#root > div > form > div > div.hill-contact-methods > kat-tabs > kat-tab > kat-box > div.hill-form-fields-container.hill-phone-fields > div.hill-form-fields-container.hill-phone-input > div > div.inputs > span.country-selector > kat-dropdown'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    # try:
                    if countryCode == 1:

                        with open('countryUSA.txt', 'r') as co:
                            country = co.read()
                    shadow_root1.find_element(By.CSS_SELECTOR, value=f"kat-option[value='{country}']").click()
                    # shadow_root1.find_element(By.CSS_SELECTOR, value=f"kat-option[value='US']").click()

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='div.inputs > span.phone-number > span.phone-number-input > div > kat-input'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    shadow_root1.find_element(By.CSS_SELECTOR, value="#input-3").send_keys(callNum)

                    ext = readExtension()
                    if ext == "" or ext == " ":
                        pass
                    else:
                        element = WebDriverWait(driver, 20).until(
                            lambda driver:
                            driver.find_element(
                                by=By.CSS_SELECTOR,
                                value='span.phone-number-extension > div > kat-input'))
                        shadow_root1 = expand_shadow_element(element, driver)
                        shadow_root1.find_element(By.CSS_SELECTOR, value="#input-4").send_keys(ext)
                        element = WebDriverWait(driver, 20).until(
                            lambda driver:
                            driver.find_element(
                                by=By.CSS_SELECTOR,
                                value='#katal-id-11'))
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        driver.execute_script("arguments[0].click();", element)
                    sleep(0.5)
                    letters = string.ascii_lowercase
                    result_str = ''.join(random.choice(letters) for i in range(3))
                    with open(f"trash/{result_str}.png", "ab") as file:
                        captcha_img = WebDriverWait(driver, 100).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR, "div.captcha-image > img"))
                        file.write(captcha_img.screenshot_as_png)
                    with open("captcha code.txt", "r") as c:
                        cap = c.readline()
                        solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                        raw_data = open(f"trash/{result_str}.png", 'rb').read()
                    solving_captcha = solver.solve_captcha(raw_data)

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='div.hill-captcha-container > div.captcha-input > div > kat-input'))

                    shadow_root1 = expand_shadow_element(element, driver)

                    shadow_root1.find_element(By.ID, value='input-5').send_keys(
                        solving_captcha)
                    os.remove(f'trash/{result_str}.png')

                    element = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.CSS_SELECTOR,
                            value='#call-me-now-button'))
                    shadow_root1 = expand_shadow_element(element, driver)
                    element = shadow_root1.find_element(By.CSS_SELECTOR, value="button")

                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    driver.execute_script("arguments[0].click();", element)

                    sleep(0.3)
                    if 'cancel-call-button' in driver.page_source:
                        print(Fore.GREEN + 'Success Call >>> ' + str(callNum))
                    sleep(5)
                    driver.refresh()
                    sleep(1)
                    if 'Internal failure'in driver.page_source:
                        break
                driver.quit()
    except:
        pass

def main():
    while True:
        try:
            driver = get_driver()
            EmailData = readEmail()
            StartLogin(driver, EmailData)
        except:
            pass


def cls(): os.system('cls' if os.name == 'nt' else 'clear')


def logo():
    cls()
    print(Fore.WHITE + '''

                            ────────────────────────────────────────────────────────────
                            ─██████──████████────████████████████──────██████████████───
                            ─██░░██──██░░░░██────██░░░░░░░░░░░░██──────██░░░░░░░░░░██───
                            ─██░░██──██░░████────██░░████████░░██──────██░░██████░░██───
                            ─██░░██──██░░██──────██░░██────██░░██──────██░░██──██░░██───
                            ─██░░██████░░██──────██░░████████░░██──────██░░██████░░████─
                            ─██░░░░░░░░░░██──────██░░░░░░░░░░░░██──────██░░░░░░░░░░░░██─
                            ─██░░██████░░██──────██░░██████░░████──────██░░████████░░██─
                            ─██░░██──██░░██──────██░░██──██░░██────────██░░██────██░░██─
                            ─██░░██──██░░████────██░░██──██░░██████────██░░████████░░██─
                            ─██░░██──██░░░░██────██░░██──██░░░░░░██────██░░░░░░░░░░░░██─
                            ─██████──████████────██████──██████████────████████████████─
                            ────────────────────────────────────────────────────────────
    \n\n\n''')


if __name__ == '__main__':
    logo()
    # This code won't run if this file is imported.
    print("[+] pleas enter number of threads..")
    number_of_threads = input()
    # print("[+] if you need change language enter >> 1 ")
    # try:
    #     AskLang = int(input())
    # except:
    #     AskLang = 0
    print("[+] to non headless enter >> 1 ")
    try:
        headless = int(input())
    except:
        headless = 0


    def func():
        main()


    for number in range(int(number_of_threads)):
        t = Thread(target=func)
        t.start()
        sleep(1)

