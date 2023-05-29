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
global url1
url1 = "https://sellercentral.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral.amazon.com%2Fsw%2Famazon-pay%2Fonboarding%2FSIGNUP%2Fstep%2Fsignup%3FmarketplaceId%3DAGWSWK15IEJJ7%26solutionProviderId%3D%26regRedirection%3D%26redirectToSCORE%3D0%26passthrough%252Faccount%3Dpyop%26productTier%3DPYOP_BASIC%26language%3Den_GB%26passthrough%252FsuperSource%3DOAR%26passthrough%252F*Version*%3D1%26passthrough%252FmarketplaceID%3DAGWSWK15IEJJ7%26simplifiedLogin%3D2%26passthrough%252FwaiveFee%3D1%26registrationId%3DEMPTY_SP_ID_621-1608262-2428635%26passthrough%252Fsource%3Dinternal-landing-select%26passthrough%252Fiswba2%3D0%26passthrough%252F*entries*%3D0%26productType%3DAmazonPayments%26passthrough%252FsimplifiedLogin%3D2&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_ap_onboarding_na&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=APOnboarding-na&disableLoginPrepopulate=1&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

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

def StartLogin(driver, EmailData):
    try:
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
        sleep(1)
        if "What’s the address of your website?" in driver.page_source:
            driver.quit()
        else:

            for i in range(0,3):
                sleep(3)
                if 'displayNameField' in driver.page_source:
                    break
            try:
                NameInput = WebDriverWait(driver, 200).until(
                    lambda driver:
                    driver.find_element(
                        by=By.NAME,
                        value='displayNameField'))
                letters = string.ascii_lowercase

                fullname = ''.join(random.choice(letters) for i in range(12))

                for i in fullname:
                    NameInput.send_keys(i)
            except:
                pass
            try:
                NameInput = WebDriverWait(driver, 200).until(
                    lambda driver:
                    driver.find_element(
                        by=By.NAME,
                        value='web-url'))
                fname = names.get_first_name()
                lname = names.get_last_name()
                fullname = fname + lname+".com"
                for i in fullname:
                    NameInput.send_keys(i)
            except:
                pass


            index=random.randint(0,29)
            select = Select(driver.find_element(By.ID, 'businessCategory'))
            select.select_by_index(index)

            index=random.randint(1,4)
            select = Select(driver.find_element(By.ID, 'annualSalesVolume'))
            select.select_by_index(index)

            postal=random.choice(open("postal.txt",'r').readlines())
            daaresss=random_address.real_random_address_by_postal_code(postal)
            address1=daaresss.get('address1')
            # {'address1': '711 Tashanna Lane', 'address2': '', 'city': 'Southport', 'state': 'FL', 'postalCode': '32409', 'coordinates': {'lat': 30.41437699999999, 'lng': -85.676568}}
            WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.NAME,
                    value='address_line1')).send_keys(address1)
            WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.NAME,
                    value='pincode')).send_keys(postal)
            ph=''.join(str(random.randint(0,9)) for i in range(10))
            WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.NAME,
                    value='phoneno')).send_keys(ph)
            sleep(0.3)
            Submit=WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="a-autoid-2"]/span/input'))
            driver.execute_script("arguments[0].scrollIntoView();", Submit)
            sleep(0.3)
            Submit.click()
            sleep(1)
            bTypeSelect=WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.ID,
                    value='bTypeSelect'))
            bTypeSelect.click()

            Type=WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.ID,
                    value='individualType{'))
            Type.click()

            try:
                NameInput = WebDriverWait(driver, 200).until(
                    lambda driver:
                    driver.find_element(
                        by=By.NAME,
                        value='ln_first_name'))
                fname = names.get_first_name()
                # lname = names.get_last_name()
                # fullname = fname + "" + lname + ".com"
                for i in fname:
                    NameInput.send_keys(i)
            except:
                pass
            sleep(0.2)
            try:
                NameInput = WebDriverWait(driver, 200).until(
                    lambda driver:
                    driver.find_element(
                        by=By.NAME,
                        value='ln_last_name'))
                # fname = names.get_first_name()
                lname = names.get_last_name()
                # fullname = fname + "" + lname + ".com"
                for i in lname:
                    NameInput.send_keys(i)
            except:
                pass

            # sleep(999)
            usPersonOptionNo=WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="BC_NA_NLX_TAX_INFO"]/div/form/div/div[1]/div[2]/div[1]/div[2]/label'))
            driver.execute_script("arguments[0].scrollIntoView();", usPersonOptionNo)
            sleep(0.3)
            usPersonOptionNo.click()


            # get random month
            month = random.randint(1, 12)
            if month <= 9:
                month = '0' + str(month)
            print(month)
            # get random day
            day = random.randint(1, 28)
            if day <= 9:
                day = '0' + str(day)
            print(day)
            # get random year
            year = random.randint(1980, 2000)
            print(year)
            date = str(month) + str(day) + str(year)
            # try:
            print(date)
            # sleep(999)
            dateOfBirth = WebDriverWait(driver, 200).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="SIV_Identity_Individual_Auth_Rep_DOB_NLX"]/div/div/form/div[2]/input'))
            for i in date:
                dateOfBirth.send_keys(i)
            # NameInput.send_keys(str(day))
            # NameInput.send_keys(str(year))
            # except:
            #     pass
            # sleep(999)

            Submit=WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.NAME,
                    value='Submit'))
            Submit.click()

            sleep(0.5)
            Accept_and_continue_Btn = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="a-popover-4"]/div/div[2]/span[2]/span/input'))
            try:
                Accept_and_continue_Btn.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass
            # index = random.randint(0, 29)
            # select = Select(driver.find_element(By.ID, 'bTypeSelect'))
            # select.select_by_index()
            # # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            #
            # CheckBoxes=WebDriverWait(driver, 20).until(
            #     lambda driver:
            #     driver.find_elements(
            #         by=By.CLASS_NAME,
            #         value='sc-storm-ui-20024340__sc-1gskqay-0 frmhhe'))
            # for i in CheckBoxes:
            #     i.click()
            sleep(0.5)
            Accept_and_continue_Btn = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="successButton"]/span/input'))
            try:
                Accept_and_continue_Btn.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass

            sleep(0.5)
            Accept_and_continue_Btn = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="deferralSectionBottom"]'))
            try:
                Accept_and_continue_Btn.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass

            sleep(3)

            try:
                Accept_and_continue_Btn = WebDriverWait(driver, 1).until(
                    lambda driver:
                    driver.find_element(
                        by=By.XPATH,
                        value='//*[@id="a-autoid-2"]/span/input'))
                driver.execute_script("arguments[0].scrollIntoView();", Accept_and_continue_Btn)
                Accept_and_continue_Btn.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                Accept_and_continue_Btn = WebDriverWait(driver, 1).until(
                    lambda driver:
                    driver.find_element(
                        by=By.XPATH,
                        value='//*[@id="a-autoid-5"]/span/input'))
                driver.execute_script("arguments[0].scrollIntoView();", Accept_and_continue_Btn)
                Accept_and_continue_Btn.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
                # pass

            sleep(3)
            Accept_and_continue_Btn = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="successButton"]/span/input'))
            driver.execute_script("arguments[0].scrollIntoView();", Accept_and_continue_Btn)
            try:
                Accept_and_continue_Btn.click()
            except:
                sleep(2)
                Accept_and_continue_Btn.click()
                pass
            while 'What’s the address of your website?'not in driver.page_source:
                sleep(1)
            with open('SuccessEmail.txt','a')as f:
                f.write(Email+"|"+Pass)
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

