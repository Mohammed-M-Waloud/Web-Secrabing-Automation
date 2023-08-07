import os
from threading import Thread
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By

companies = [['CompanyName','CompanyWebsite', 'Telephones']]
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.delete_all_cookies()
    return driver


def print_warning(string):
    print(Fore.YELLOW + f"         [Warning] {string}")


def print_error(string):
    print(Fore.RED + f"         [Error] {string}")


def print_success(string):
    print(Fore.GREEN + f"         [Success] {string}")


def PrepereLinks(driver,url):
    AllLinks = list()
    print_success(">>>>> Start Open Website <<<<<")
    try:
        driver.get(url)
        driver.implicitly_wait(30)
    except Exception as e:
        print_error("Can't Open Url")
        print_error(str(e))
        return


    multy_pages = False
    if "next page-numbers" in driver.page_source:
        multy_pages = True
    if multy_pages:
        while multy_pages:
            AllLinksSelector = "body > div.mainContentWrap > div > div > div > div > div.row > div > div > a"
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            AllLinksElements = soup.select(AllLinksSelector)
            for link_element in AllLinksElements:
                href = link_element.get('href')
                AllLinks.append(href)
                # print(AllLinks)
            element = driver.find_element(By.CSS_SELECTOR , value="a.next.page-numbers")
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("arguments[0].click();", element)

            if "next page-numbers" not in driver.page_source:
                multy_pages = False
    else:
        AllLinksSelector = "body > div.mainContentWrap > div > div > div > div > div.row > div > div > a"
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        AllLinksElements = soup.select(AllLinksSelector)
        for link_element in AllLinksElements:
            href = link_element.get('href')
            AllLinks.append(href)
            # print(AllLinks)
    return AllLinks


def FetchData(driver):
    AllDataList = list()

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    section = soup.select('section.section.article_wrapper')[0].text.strip()
    import re
    # Remove non-breaking space characters and other whitespace characters
    cleaned_text = re.sub(r'\s+', ' ', section).strip()
    section = cleaned_text.splitlines()
    # print(section)

    try:
        company_name_element = section[0].split("النوع",1)[0]
        AllDataList.append(company_name_element.split(":",1)[1])
        print(company_name_element.split(":")[1])
    except:
        AllDataList.append(" ")
    # sleep(999)

    try:
        company_website_element = soup.select('a:contains("اضغط هنا")')
        company_website = company_website_element[0]['href']
        AllDataList.append(company_website)
    except:
        AllDataList.append(" ")



    try:
        company_telephon_elements = section[0]
        phone_pattern = r'\+?\d[\d -]+\d'

        # Find all phone numbers in the text
        phone_numbers = re.findall(phone_pattern, company_telephon_elements)
        AllDataList.append(phone_numbers[0])
    except:
        AllDataList.append(" ")


    print_success(f"AllDataList {AllDataList} \n")
    return AllDataList

def StartOpenLinks(driver, AllLinks):
    for Url in AllLinks:
        try:
            driver.get(Url)
            driver.implicitly_wait(30)
        except Exception as e:
            print_error("Can't Open Url")
            print_error(str(e))
            return
        AllDataList = FetchData(driver)
        companies.append(AllDataList)
    driver.quit()
    return  companies
def main(url):
    clear_screen()
    with get_driver() as driver:
        AllLinks = PrepereLinks(driver,url)
        companies = StartOpenLinks(driver, AllLinks)
        # Create a DataFrame from the 'companies' list
        df = pd.DataFrame(companies)
        # Save the DataFrame to an Excel file
        filename_excel = 'DataCompanies.xlsx'
        df.to_excel(filename_excel, index=False )
        print_success(">>>>> Done Fetch Data <<<<<")

if __name__ == '__main__':
    urls = ["https://coavira.com/category/%d9%85%d9%83%d8%a9/","https://coavira.com/category/%d8%a7%d9%84%d8%b8%d9%87%d8%b1%d8%a7%d9%86/",
            "https://coavira.com/category/%d8%a7%d9%84%d8%b7%d8%a7%d8%a6%d9%81/","https://coavira.com/category/%d8%a7%d9%84%d8%ae%d8%a8%d8%b1/",
            "https://coavira.com/category/%d8%a7%d9%84%d8%af%d9%85%d8%a7%d9%85/","https://coavira.com/category/%D8%AC%D8%AF%D8%A9/",
            "https://coavira.com/category/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/"]
    threads = []
    for url in urls:
        t = Thread(target=main,args=(url,) )
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()