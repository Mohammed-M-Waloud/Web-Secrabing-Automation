import names ,os,random,string,phonenumbers,warnings
clear = lambda: os.system('cls')
clear()
from threading import Thread
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import phone_iso3166.country as countries
warnings.filterwarnings("ignore", category=DeprecationWarning)
global url1, Domain, url2, IssueNumber, SubIssueNumber
Domain = open('Domain.txt', 'r').read()
url1 = f"https://advertising.amazon.{Domain}/advertisingAccounts/registration/create?ref_=a20m_us_rgstr_opnreg_us"
url2 = f"https://advertising.amazon.{Domain}/contactus?entityId"
numcalestooneAccount=open('numcalestooneAccount.txt', 'r').read()
NumfailedCall=open('NumfailedCall.txt', 'r').read()

def getIssue():
    IssueNumber = open('IssueNumber.txt', 'r').read()
    if IssueNumber == " " or IssueNumber == "":
        IssueNumber = random.randint(1, 12)
    return str(IssueNumber)

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
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
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
    with open('Emails.txt', 'a') as e:
        e.write(EmailData)
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
    with open('Number.txt', 'a') as e:
        e.write(Number)
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

def StartLogin(driver, EmailData):
    Email, Pass = str(EmailData).split('|')
    driver.get(url1)
    WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.NAME,
            value='email')).send_keys(Email)

    WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.NAME,
            value='password')).send_keys(Pass)

    LoginBtn = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.ID,
            value='signInSubmit'))
    try:
        LoginBtn.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass
    try:
        NameInput = WebDriverWait(driver, 200).until(
            lambda driver:
            driver.find_element(
                by=By.ID,
                value='amzn-adam:self-reg-account-name-input'))
        fname = names.get_first_name()
        lname = names.get_last_name()
        fullname = fname + " " + lname
        for i in fullname:
            NameInput.send_keys(i)
    except:
        try:
            NameInput = WebDriverWait(driver, 200).until(
                lambda driver:
                driver.find_element(
                    by=By.ID,
                    value='amzn-adam:self-reg-account-name-input'))
            fname = names.get_first_name()
            lname = names.get_last_name()
            fullname = fname + " " + lname
            for i in fullname:
                NameInput.send_keys(i)
        except:
            pass
    # AddCountries=WebDriverWait(driver, 20).until(
    #     lambda driver:
    #     driver.find_element(
    #         by=By.CSS_SELECTOR,
    #         value='td:nth-child(2) > button'))
    # AddCountries.click()
    # # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    #
    # CheckBoxes=WebDriverWait(driver, 20).until(
    #     lambda driver:
    #     driver.find_elements(
    #         by=By.CLASS_NAME,
    #         value='sc-storm-ui-20024340__sc-1gskqay-0 frmhhe'))
    # for i in CheckBoxes:
    #     i.click()

    Accept_and_continue_Btn = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.XPATH,
            value='//*[@id="app"]/div/div/div[7]/div[2]/button[2]'))
    try:
        Accept_and_continue_Btn.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass

    while "sc-storm-ui-20024340__sc-b4z2xs-0 bTflwP sc-storm-ui-20024340__sc-b4z2xs-13 styles__PageTitle-sc-ftjnpc-7 jAvtNJ" in driver.page_source:
        sleep(0.5)

def prrpareToCall(driver):
    driver.get(url2)
    IssueDropdown = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.NAME,
            value='IssueDropdown'))
    try:
        IssueDropdown.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass
    IssueNumber=getIssue()
    IssueSelect = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.CSS_SELECTOR,
            value=f'#portal > div > div > button:nth-child({IssueNumber})'))
    try:
        IssueSelect.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass
    SubIssueDropdown = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.NAME,
            value='SubIssueDropdown'))
    try:
        SubIssueDropdown.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass
    SubIssueDropdownl = {
        '1': '5',
        '2': '2',
        '3': '3',
        '4': '3',
        '5': '9',
        '6': '9',
        '7': '9',
        '8': '4',
        '9': '5',
        '10': '9',
        '11': '10',
        '12': '7',
        '13': '7'
    }
    SubIssueNumber = SubIssueDropdownl[IssueNumber]
    SubIssueNumber2 = random.randint(1, int(SubIssueNumber))
    SupIssueSelect = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_element(
            by=By.CSS_SELECTOR,
            value=f'#portal > div > div > button:nth-child({SubIssueNumber2})'))
    try:
        SupIssueSelect.click()
        # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    except:
        pass

    SelectPhoneContact = WebDriverWait(driver, 20).until(
        lambda driver:
        driver.find_elements(
            by=By.XPATH,
            value='//button[@class="sc-storm-ui-20022551__sc-1vzueig-0 jFMLlA toggle type-toggle"]'))
    # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
    c=0
    for i in SelectPhoneContact:
        try:
            if c==1:
                i.click()
            c+=1
        except:
            pass
    # pass
    if AskLang==1:
        try:
            SelectLang=WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='//button[@class="sc-storm-ui-20022551__sc-1vzueig-0 jFMLlA toggle with-spacing lang-button"]'))
            SelectLang.click()
            # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
        except:
            pass
    letters = string.ascii_lowercase

    inps = driver.find_elements(
            by=By.XPATH,
            value='//input[@class="sc-storm-ui-20022551__sc-1sj9x5i-0 dSZuBE"]')
    for i in inps:
        valu=i.get_attribute("value")
        if '+' in valu :
            break
        else:
            Text = ''.join(random.choice(letters) for i in range(10))
            i.send_keys(Text)
    Text = ''.join(random.choice(letters) for i in range(5))
    Text2 = ''.join(random.choice(letters) for i in range(6))
    Text3 = ''.join(random.choice(letters) for i in range(7))
    Text4 = ''.join(random.choice(letters) for i in range(12))
    str = Text + " " + Text2 + " " + Text3 + " " + Text4
    try:
        inp = WebDriverWait(driver, 20).until(
            lambda driver:driver.find_element(
            by=By.TAG_NAME,
            value='textarea'))
        inp.send_keys(str)
    except:
        pass

def StartCall(driver):
    failedCall=0
    for i in range(0,int(numcalestooneAccount)):
        prrpareToCall(driver)
        if "AbstractFlyoverStyles__AbstractFlyoverContainer-sc-o91v4z-1 imRmgb react-draggable" in driver.page_source:
            push = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.CSS_SELECTOR,
                    value='i.sc-storm-ui-20023587__sc-1vzu9xb-0:nth-child(2)'))
            try:
                push.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass

        SelectCoubtryDropDawnList = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value='//button[@class="sc-storm-ui-20022551__sc-d3w8xm-0 gyLbNV sc-storm-ui-20022551__sc-amnlzo-2 kAixWd country-dropdown"]'))
        try:
            SelectCoubtryDropDawnList.click()
            # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
        except:
            pass
        Number = readNumber()
        country = countries.phone_country('+' + Number)
        countryCode = phonenumbers.country_code_for_region(country)
        # print(countryCode)
        callNum = Number.split(str(countryCode), 1)[1]
        SelectCoubtry = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.XPATH,
                value=f'//button[@value="{country.lower()}"]'))
        try:
            SelectCoubtry.click()
            # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
        except:
            pass

        phoneNumberInput = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.NAME,
                value='phoneNumber'))
        try:
            for i in callNum:
                phoneNumberInput.send_keys(i)
            # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
        except:
            pass
        Extension = readExtension()
        if Extension != "":
            ExtensionInput = WebDriverWait(driver, 20).until(
                lambda driver:
                driver.find_element(
                    by=By.CSS_SELECTOR,
                    value='div.ext-number > div > div > input'))
            try:
                ExtensionInput.send_keys(Extension)
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass

        callButton = WebDriverWait(driver, 20).until(
            lambda driver:
            driver.find_element(
                by=By.NAME,
                value='callButton'))
        for i in range(8):
            try:
                callButton.click()
                # driver.execute_script("arguments[0].scrollIntoView();", LoginBtn)
            except:
                pass
            sleep(0.3)
        if 'sc-storm-ui-20022551__sc-b4z2xs-3 eiNyQO sc-storm-ui-20022551__sc-b4z2xs-13 fbrQYt' in driver.page_source:
            print(Fore.GREEN + "Success Call >>" + Number)
        else:
            if 'sc-storm-ui-20022551__sc-1jwbhbz-1 cLYPMW something-went-wrong' in driver.page_source:
                print(Fore.RED + "Failed Call >>" + Number)
                failedCall +=1
        if failedCall==int(NumfailedCall):
            driver.quit()
            break
        driver.refresh()

    # sleep(999)

def main():
    while True:
        try:
            driver = get_driver()
            EmailData = readEmail()
            StartLogin(driver, EmailData)
            StartCall(driver)
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
    print("[+] if you need change language enter >> 1 ")
    try:
        AskLang= int(input())
    except:
        AskLang=0
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

