import sys

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
import undetected_chromedriver as uc
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import phone_iso3166.country as countries

warnings.filterwarnings("ignore", category=DeprecationWarning)
global url1
url1="https://sellercentral-europe.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsellercentral-europe.amazon.com%2Fsw%2Famazon-pay%2Fonboarding%2FSIGNUP%2Fstep%2FAgreements%3FsolutionProviderId%3DAW93DIZMWSDWS%26regRedirection%3D%3FsolutionProviderId%3DAW93DIZMWSDWS%26marketplaceId%3DAZAJMM36N6WQL%26solutionProviderToken%3DAAAAAQAAAAEAAAAQTJIz7PQwoGxK6PyIcUFbKQAAAHAbQ3wOHLAOzrcmfURnsRkLLcVpsjI6PQ%2BvTaHaSKIuWsocRuABLQGCvNa%2Bh7Rq2FhvDE65APdoy7pu8RtO4XDjDvIE%2BE0JeBBZbSVwbJLGHxPiaECqrjGBuRgNWz8xuA2W542LO6r7j%2FDWdqQGcLVz%26solutionProviderOptions%3Dlwa%3Bmws-acc%3B%26redirectToSCORE%3D0%26passthrough%252Faccount%3Dpyop%26productTier%3DPYOP_BASIC%26language%3Den_GB%26passthrough%252FsuperSource%3DOAR%26passthrough%252F*Version*%3D1%26passthrough%252FmarketplaceID%3DAZAJMM36N6WQL%26simplifiedLogin%3D2%26passthrough%252FwaiveFee%3D1%26passthrough%252Fld%3D1%257CSPUNGBAPAAW93DIZMWSDWSSWIPE%26registrationId%3DAW93DIZMWSDWS_948-9051427-7762404%26passthrough%252Fsource%3Dinternal-landing-select%26passthrough%252Fiswba2%3D0%26passthrough%252F*entries*%3D0%26productType%3DAmazonPayments%26passthrough%252FsimplifiedLogin%3D2&prevRID=03MDQTP563AJDR0VCX38&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_ap_onboarding_eu&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&language=en_GB&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=APOnboarding-UK&disableLoginPrepopulate=1&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
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
    proxy = readProxy()
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
    with open('FailedEmailEurope.txt', 'r') as e:
        e.seek(int(position))
        EmailData = e.readline()
        if EmailData=="" or EmailData==" " :
            position=0
            sys.exit("End Crate")
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
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.CSS_SELECTOR, value="span > button")).click()
            sleep(0.1)
            os.remove(f'trash/{result_str}.png')


        if "For your security, approve the notification sent to:" in driver.page_source or "Customise the Amazon Pay experience" in driver.page_source:
            if "Customise the Amazon Pay experience" in driver.page_source:
                with open('SuccessEmailEurope.txt', 'a') as f:
                    f.write(Email + "|" + Pass)
            else:
                with open('celer center.txt', 'a') as f:
                    f.write(Email + "|" + Pass)
            driver.quit()

        # try:
        # sleep(3)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="POC_KYC_Attributes_BC"]/div/form/div/div/div/div/div[2]/div/div/label/input'))
        # # driver.execute_script("arguments[0].scrollIntoView();", Submit)
        # # sleep(0.3)
        #
        # driver.execute_script("arguments[0].click();", Submit)
        #
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="IsLegalRepOptiontrue"]'))
        # # driver.execute_script("arguments[0].scrollIntoView();", Submit)
        # # sleep(0.3)
        # driver.execute_script("arguments[0].click();", Submit)


        index = random.randint(1, 25)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[1]/div/div[2]/div/span'))
        # Submit.click()
        Submit = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value=f'//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[1]/div/div[2]/div/span/select/option[{index}]'))
        Submit.click()


        index = random.randint(1, 25)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[2]/div/div[2]/div/span'))
        # Submit.click()
        Submit = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value=f'//*[@id="BC_EU_POC_ENTITY_SELLER_INFO"]/div/form/div[3]/div[2]/div/div[2]/div/span/select/option[{index}]'))
        Submit.click()


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

        firstchick = WebDriverWait(driver, 200).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='//*[@id="POC_KYC_Attributes_BC"]/div/form/div/div/div/div/div[2]/div/div/label/input'))
        driver.execute_script("arguments[0].click();", firstchick)
        dateOfBirth = WebDriverWait(driver, 200).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/form/div[3]/div[2]/div[2]/div[2]/div/input'))
        driver.execute_script("arguments[0].click();", dateOfBirth)
        for i in date:
            sleep(0.1)

            dateOfBirth.send_keys(i)

        # sleep(999)
        # sleep(999)
        # sleep(999)

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
        for i in date:
            sleep(0.1)
            dateOfBirth.send_keys(i)


        num=((str(4)+(''.join(str(random.randint(0,9)) for i in range(8)))))
        for i in num:
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/div/form/div[3]/div[3]/div[2]/div[2]/div[2]/input')).send_keys(i)

        last = WebDriverWait(driver, 200).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='//*[@id="sc-content-container"]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/label/input'))
        driver.execute_script("arguments[0].click();", last)
        # sleep(3)
        Submit = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/div/div/form/div[2]/div[4]/div[1]/div[1]/div/div/div/div/label/input'))
        driver.execute_script("arguments[0].scrollIntoView();", Submit)
        driver.execute_script("arguments[0].click();", Submit)
        sleep(0.2)
        try:
            sleep(2)
            Submit = WebDriverWait(driver, 5).until(
                lambda driver:
                driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="sc-content-container"]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/span/span/input'))
            driver.execute_script("arguments[0].click();", Submit)
        except:
            pass
        sleep(10)
        # driver.refresh()
        #
        #
        # sleep(3)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="POC_KYC_Attributes_BC"]/div/form/div/div/div/div/div[2]/div/div/label/input'))
        # driver.execute_script("arguments[0].click();", Submit)
        #
        #
        # sleep(3)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='//*[@id="IsLegalRepOptiontrue"]'))
        # driver.execute_script("arguments[0].scrollIntoView();", Submit)
        # driver.execute_script("arguments[0].click();", Submit)
        # sleep(3)
        # Submit = WebDriverWait(driver, 20).until(
        #     lambda driver:
        #     driver.find_element(
        #         by=By.XPATH,
        #         value='/html/body/div[1]/div[2]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[4]/div/div/div/form/div[2]/div[4]/div[1]/div[1]/div/div/div/div/label/input'))
        # driver.execute_script("arguments[0].scrollIntoView();", Submit)
        # driver.execute_script("arguments[0].click();", Submit)
        # sleep(0.2)
        # try:
        #     sleep(2)
        #     Submit = WebDriverWait(driver, 5).until(
        #         lambda driver:
        #         driver.find_element(
        #             by=By.XPATH,
        #             value='//*[@id="sc-content-container"]/div[1]/div/div[5]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/span/span/input'))
        #     driver.execute_script("arguments[0].click();", Submit)
        # except:
        #     pass
        #
        #
        # # sleep(999)
        if 'Enter the URL of your privacy policy' not in driver.page_source:
            # driver.refresh()
            # sleep(999)
            with open('FailedEmailEurope.txt', 'a') as f:
                f.write(Email + "|" + Pass)
            driver.quit()
        else:
            with open('SuccessEmailEurope.txt','a')as f:
                f.write(Email+"|"+Pass)
            driver.quit()
    except:

        try:
            driver.quit()
        except:
            pass






    # except:
    #     try:
    #         driver.quit()
    #     except:
    #         pass
def main():
    while True:
        try:
            driver = get_driver()
            EmailData = readEmail()
            StartLogin(driver, EmailData)
        except:
            try:
                driver.quit()
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

