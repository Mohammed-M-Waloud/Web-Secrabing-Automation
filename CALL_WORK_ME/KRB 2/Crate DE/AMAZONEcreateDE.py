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
url1="https://sellercentral-europe.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral-europe.amazon.com%2Fsw%2Famazon-pay%2Fonboarding%2FSIGNUP%2Fstep%2FAgreements%3FsolutionProviderId%3DA12EXUMYWB7412%26regRedirection%3D%3FsolutionProviderId%3DA12EXUMYWB7412%26marketplaceId%3DA53RDEWN57UU5%26solutionProviderToken%3DAAAAAQAAAAIAAAAQDfBWFdXSPIQUc9IUxYNxKwAAAHDv2FhReGEGRva8SlqDBoG%2FbSsix2n32IGohEhegImA4rWyGalvBCRMg44JFk6%2BbXdrtEQfMadEertYngoTElX%2FQtpbQ9FYMkb%2Fa0%2Bz2ujrWd%2F3qSoDXPoJ2TKqap5eXkFeOMLjVn5bOB3%2FitFsSRQV%26solutionProviderOptions%3Dlwa%3Bmws-acc%3B%26redirectToSCORE%3D0%26passthrough%252Faccount%3Dpyop%26productTier%3DPYOP_BASIC%26language%3Dde_DE%26passthrough%252FsuperSource%3DOAR%26passthrough%252F*Version*%3D1%26passthrough%252FmarketplaceID%3DA53RDEWN57UU5%26simplifiedLogin%3D2%26passthrough%252FwaiveFee%3D1%26passthrough%252Fld%3DELDELPA-sellercentral.amazon.com%257CSPUNDEAPAA12EXUMYWB7412SWIPE%26registrationId%3DA12EXUMYWB7412_862-3629117-8421517%26passthrough%252Fsource%3Dinternal-landing-select%26passthrough%252Fiswba2%3D0%26passthrough%252F*entries*%3D0%26productType%3DAmazonPayments%26passthrough%252FsimplifiedLogin%3D2&prevRID=QH4924JQRRK6QA58Q1KM&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_ap_onboarding_eu&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&language=de_DE&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=APOnboarding&disableLoginPrepopulate=1&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"

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
            print(Fore.LIGHTRED_EX + "[!] Invalid Login, Check Your Email or Password or maybe Account Blocked!" + Fore.RESET)
            with open("AccountBlocked.txt",'a') as f :
                 f.write(Email+"|"+Pass)
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
            if "Geschäftsname" in driver.page_source :
                with open('SuccessEmailDE.txt', 'a') as f:
                    f.write(Email + "|" + Pass)
                print(Fore.GREEN + "[=] Success Email >>> " + Email + Fore.RESET)
                driver.quit()
            else:
                # FIRST STEP
                try:
                    sleep(1)
                    index = random.randint(0, 10)
                    select = Select(driver.find_element(By.ID, 'tableDetailsSelect'))
                    # while  index == 2:
                    #     index = random.randint(0, 10)
                    index=open('CountryNumber.txt','r').readline()
                    select.select_by_index(index)
                    sleep(0.2)
                    index = random.randint(1, 4)
                    select = Select(driver.find_element(By.NAME, 'business-type-dropdown-field'))
                    select.select_by_index(index)
                    try:
                        NameInput = WebDriverWait(driver, 10).until(
                            lambda driver:
                            driver.find_element(
                                by=By.ID,
                                value='ln_legal_name'))
                        fname = names.get_first_name()
                        lname = names.get_last_name()
                        fullname = fname + " " +lname
                        for i in fullname:
                            NameInput.send_keys(i)
                    except:
                        pass

                    Submit = WebDriverWait(driver, 5).until(
                        lambda driver:
                        driver.find_element(
                            by=By.NAME,
                            value='Submit'))
                    driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    sleep(0.3)


                    try:
                        Submit = WebDriverWait(driver, 5).until(
                            lambda driver:
                            driver.find_element(
                                by=By.XPATH,
                                value='//*[@id="a-popover-1"]/div/div[1]/button'))
                        driver.execute_script("arguments[0].scrollIntoView();", Submit)
                        Submit.click()
                        Submit = WebDriverWait(driver, 5).until(
                            lambda driver:
                            driver.find_element(
                                by=By.NAME,
                                value='Submit'))
                        driver.execute_script("arguments[0].scrollIntoView();", Submit)
                        sleep(0.3)
                        Submit.click()
                    except:
                        pass
                except:
                    pass
                # SECOUND STEP
                try:
                    NameInput = WebDriverWait(driver, 12).until(
                        lambda driver:
                        driver.find_element(
                            by=By.NAME,
                            value='web-url'))
                    try:
                        sleep(0.3)
                        NameInput = WebDriverWait(driver, 25).until(
                            lambda driver:
                            driver.find_element(
                                by=By.NAME,
                                value='web-url'))
                        fname = names.get_first_name()
                        lname = names.get_last_name()
                        fullname = fname + lname + ".com"
                        NameInput.clear()
                        for i in fullname:
                            NameInput.send_keys(i)
                    except:
                        pass

                    # random.randint(1,2)
                    volume = WebDriverWait(driver, 10).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value=f'//*[@id="fieldOption"]'))
                    driver.execute_script("arguments[0].scrollIntoView();", volume)
                    sleep(0.3)
                    volume.click()
                    index = random.randint(1, 20)
                    select = Select(driver.find_element(By.XPATH, '//*[@id="business_category"]/div/div[1]/select'))
                    select.select_by_index(index)
                    sleep(0.3)
                    pincode = open('PinCode.txt', 'r').readline()
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value="pincode")).send_keys(pincode)
                    letters = string.ascii_lowercase
                    fullname = ''.join(random.choice(letters) for i in range(10))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="SuggestedAddress"]/div[2]/div[1]/div/div[2]/div[1]/div/input')).send_keys(fullname)
                    sleep(0.3)

                    fullname = ''.join(random.choice(letters) for i in range(8))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="SuggestedAddress"]/div[2]/div[1]/div/div[2]/div[2]/div/input')).send_keys(fullname)
                    sleep(0.3)
                    fullname = ''.join(random.choice(letters) for i in range(8))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="SuggestedAddress"]/div[2]/div[1]/div/div[3]/div[1]/div/div/div/input')).send_keys(fullname)
                    sleep(0.3)

                    fullname = ''.join(random.choice(letters) for i in range(8))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value='CompanyRepresentative')).send_keys(fullname)
                    sleep(0.3)
                    try:
                        fullname = ''.join(random.choice(letters) for i in range(8))
                        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="SuggestedAddress"]/div[2]/div[1]/div/div[3]/div[2]/div/div/div/input')).send_keys(fullname)
                        sleep(0.3)
                    except:
                        pass

                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value='phoneno')).send_keys(''.join(str(random.randint(0,9)) for i in range(9)))
                    fullname = ''.join(random.choice(letters) for i in range(8))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="BC_BusinessEntity"]/div/form/div[1]/div[1]/div/div[3]/div/input')).send_keys(fullname)
                    # sleep(0.3)
                    # WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[4]/div/div[2]/div/div/div/form/div[1]/div[1]/div/div[2]/div/input')).send_keys(''.join(str(random.randint(0,9)) for i in range(8)))
                    # sleep(999)
                    sleep(0.3)
                    fullname = ''.join(random.choice(letters) for i in range(12))
                    # WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[4]/div/div[4]/div/div/form/div/div/div[2]/div/input')).send_keys(''.join(str(random.randint(0,9)) for i in range(10)))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[4]/div/div[4]/div/div/form/div/div/div[2]/div/input')).send_keys(fullname)
                    # fullname = ''.join(random.choice(letters) for i in range(12))
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="cs-phone-id"]')).clear()
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='//*[@id="cs-phone-id"]')).send_keys(''.join(str(random.randint(0,9)) for i in range(9)))


                    # sleep(999)
                    index = random.randint(1, 3)
                    select = Select(driver.find_element(By.NAME, 'title'))
                    select.select_by_index(index)


                    sleep(0.3)
                    fullname = names.get_first_name()
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value='first_name')).send_keys(fullname)
                    sleep(0.3)

                    fullname = names.get_first_name()
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value='middle_name')).send_keys(fullname)
                    sleep(0.3)

                    fullname = names.get_first_name()
                    WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, value='last_name')).send_keys(fullname)

                    # TTT=input("gggggg")
                    sleep(2)
                    Submit = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            # value='//input[@labelledby="a-autoid-1-announce"]'))
                            value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div[3]/div[2]/div[5]/div/span[2]/span/input'))
                    driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    sleep(0.3)
                    # driver.execute_script("arguments[0].click();", Submit)
                    Submit.click()
                except:
                    pass
                sleep(2)
                # sleep(999)
                # THIRD STEP
                try:
                    Submit = WebDriverWait(driver, 12).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="POC_KYC_Attributes_BC"]/div/form/div/div/div/div/div[2]/div/div/label/input'))
                    # driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    # sleep(0.3)
                    driver.execute_script("arguments[0].click();", Submit)

                    sleep(0.5)
                    index = random.randint(1, 20)
                    Submit = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[1]/div/div[2]/div/span'))
                    Submit.click()
                    sleep(0.5)
                    try:
                        Submit = WebDriverWait(driver, 2).until(
                            lambda driver:
                            driver.find_element(
                                by=By.XPATH,
                                value=f'//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[1]/div/div[2]/div/span/select/option[{index}]'))
                        Submit.click()
                    except:
                        pass
                    sleep(0.5)
                    index = random.randint(1, 20)
                    Submit = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[2]/div/div[2]/div/span'))
                    Submit.click()
                    sleep(0.5)
                    try:
                        Submit = WebDriverWait(driver, 2).until(
                            lambda driver:
                            driver.find_element(
                                by=By.XPATH,
                                value=f'//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[2]/div/div[2]/div/span/select/option[{index}]'))
                        Submit.click()
                    except:
                        pass


                    # get random month
                    month = random.randint(1, 11)
                    if month <= 9:
                        month = '0' + str(month)
                    # print(month)
                    # get random day
                    day = random.randint(1, 28)
                    if day <= 9:
                        day = '0' + str(day)
                    # print(day)
                    # get random year
                    year = random.randint(1980, 1999)
                    # print(year)
                    date = str(day) +str(month)  + str(year)
                    # try:


                    # data-ng-swipe-date-picker   data-ng-model  data-ng-if

                    dateOfBirth = WebDriverWait(driver, 200).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/form/div[3]/div[2]/div[2]/div[2]/div/input'))
                    driver.execute_script("arguments[0].click();", dateOfBirth)
                    sleep(0.5)
                    for i in date:
                        sleep(0.1)

                        dateOfBirth.send_keys(i)



                    # get random month
                    month = random.randint(1, 12)
                    if month <= 9:
                        month = '0' + str(month)
                    # print(month)
                    # get random day
                    day = random.randint(1, 28)
                    if day <= 9:
                        day = '0' + str(day)
                    # print(day)
                    # get random year
                    year = random.randint(2024, 2040)
                    # print(year)
                    date = str(day) +str(month)  + str(year)
                    # try:
                    # data-ng-swipe-date-picker   data-ng-model  data-ng-if

                    dateOfBirth = WebDriverWait(driver, 200).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/form/div[3]/div[3]/div[3]/div[2]/div/input'))
                    driver.execute_script("arguments[0].click();", dateOfBirth)
                    sleep(0.5)
                    for i in date:
                        sleep(0.1)
                        dateOfBirth.send_keys(i)


                    num=((str(4)+(''.join(str(random.randint(0,9)) for i in range(8)))))
                    for i in num:
                        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/form/div[3]/div[3]/div[2]/div[2]/div[2]/input')).send_keys(i)

                    Submit = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/div/div/form/div[2]/div[4]/div[1]/div[1]/div/div/div/div/label/input'))
                    driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    # sleep(0.3)
                    driver.execute_script("arguments[0].click();", Submit)
                    sleep(0.2)
                    Submit = WebDriverWait(driver, 20).until(
                        lambda driver:
                        driver.find_element(
                            by=By.XPATH,
                            value='//*[@id="sc-content-container"]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/label/input'))
                    driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    # Submit.click()
                    # # sleep(0.3)
                    driver.execute_script("arguments[0].click();", Submit)



                    # sleep(5)
                    # Submit = WebDriverWait(driver, 5).until(
                    #     lambda driver:
                    #     driver.find_element(
                    #         by=By.XPATH,
                    #         value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/label/input'))
                    # driver.execute_script("arguments[0].scrollIntoView();", Submit)
                    # Submit.click()
                    # # sleep(0.3)
                    # driver.execute_script("arguments[0].click();", Submit)
                    try:
                        sleep(2)
                        Submit = WebDriverWait(driver, 5).until(
                            lambda driver:
                            driver.find_element(
                                by=By.XPATH,
                                value='//*[@id="sc-content-container"]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/span/span/input'))
                        # driver.execute_script("arguments[0].scrollIntoView();", Submit)
                        # Submit.click()
                        # # sleep(0.3)
                        driver.execute_script("arguments[0].click();", Submit)
                    except:
                        pass
                   # c=input("11111")
                    while "Geschäftsname" not in  driver.page_source:
                        sleep(1)
                    with open('SuccessEmailDE.txt', 'a') as f:
                        f.write(Email + "|" + Pass)
                    print(Fore.GREEN + "[=] Success Email >>> " + Email + Fore.RESET)
                    driver.quit()
                    # if 'URL Ihrer Datenschutzrichtlinie eingeben' not in driver.page_source:
                    #     with open('SuccessEmailDE.txt', 'a') as f:
                    #         f.write(Email + "|" + Pass)
                    #     driver.quit()
                    # else:
                    #     with open('FailedEmailDE.txt', 'a') as f:
                    #         f.write(Email+"|"+Pass)
                    #     driver.quit()
                except:
                    try:
                        driver.quit()
                    except:
                        pass

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

