from time import sleep
import os
clear = lambda: os.system('cls')
import sys
from colorama import Fore
from playwright.sync_api import sync_playwright
from firebase_admin import credentials,initialize_app,db
import threading
# import phone_iso3166.country as countries
# import phonenumbers

def getfullnameofcountry(shortname):
    data = {"AF": "Afghanistan",
            "AX": "Aland Islands",
            "AL": "Albania",
            "DZ": "Algeria",
            "AS": "American Samoa",
            "AD": "Andorra",
            "AO": "Angola",
            "AI": "Anguilla",
            "AQ": "Antarctica",
            "AG": "Antigua and Barbuda",
            "AR": "Argentina",
            "AM": "Armenia",
            "AW": "Aruba",
            "AU": "Australia",
            "AT": "Austria",
            "AZ": "Azerbaijan",
            "BS": "Bahamas",
            "BH": "Bahrain",
            "BD": "Bangladesh",
            "BB": "Barbados",
            "BY": "Belarus",
            "BE": "Belgium",
            "BZ": "Belize",
            "BJ": "Benin",
            "BM": "Bermuda",
            "BT": "Bhutan",
            "BO": "Bolivia, Plurinational State of",
            "BQ": "Bonaire, Sint Eustatius and Saba",
            "BA": "Bosnia and Herzegovina",
            "BW": "Botswana",
            "BV": "Bouvet Island",
            "BR": "Brazil",
            "IO": "British Indian Ocean Territory",
            "BN": "Brunei Darussalam",
            "BG": "Bulgaria",
            "BF": "Burkina Faso",
            "BI": "Burundi",
            "KH": "Cambodia",
            "CM": "Cameroon",
            "CA": "Canada",
            "CV": "Cape Verde",
            "KY": "Cayman Islands",
            "CF": "Central African Republic",
            "TD": "Chad",
            "CL": "Chile",
            "CN": "China",
            "CX": "Christmas Island",
            "CC": "Cocos (Keeling) Islands",
            "CO": "Colombia",
            "KM": "Comoros",
            "CG": "Congo",
            "CD": "Congo, The Democratic Republic of the",
            "CK": "Cook Islands",
            "CR": "Costa Rica",
            "CI": "Côte d'Ivoire",
            "HR": "Croatia",
            "CU": "Cuba",
            "CW": "Curaçao",
            "CY": "Cyprus",
            "CZ": "Czech Republic",
            "DK": "Denmark",
            "DJ": "Djibouti",
            "DM": "Dominica",
            "DO": "Dominican Republic",
            "EC": "Ecuador",
            "EG": "Egypt",
            "SV": "El Salvador",
            "GQ": "Equatorial Guinea",
            "ER": "Eritrea",
            "EE": "Estonia",
            "ET": "Ethiopia",
            "FK": "Falkland Islands (Malvinas)",
            "FO": "Faroe Islands",
            "FJ": "Fiji",
            "FI": "Finland",
            "FR": "France",
            "GF": "French Guiana",
            "PF": "French Polynesia",
            "TF": "French Southern Territories",
            "GA": "Gabon",
            "GM": "Gambia",
            "GE": "Georgia",
            "DE": "Germany",
            "GH": "Ghana",
            "GI": "Gibraltar",
            "GR": "Greece",
            "GL": "Greenland",
            "GD": "Grenada",
            "GP": "Guadeloupe",
            "GU": "Guam",
            "GT": "Guatemala",
            "GG": "Guernsey",
            "GN": "Guinea",
            "GW": "Guinea-Bissau",
            "GY": "Guyana",
            "HT": "Haiti",
            "HM": "Heard Island and McDonald Islands",
            "VA": "Holy See (Vatican City State)",
            "HN": "Honduras",
            "HK": "Hong Kong",
            "HU": "Hungary",
            "IS": "Iceland",
            "IN": "India",
            "ID": "Indonesia",
            "IR": "Iran, Islamic Republic of",
            "IQ": "Iraq",
            "IE": "Ireland",
            "IM": "Isle of Man",
            "IL": "Israel",
            "IT": "Italy",
            "JM": "Jamaica",
            "JP": "Japan",
            "JE": "Jersey",
            "JO": "Jordan",
            "KZ": "Kazakhstan",
            "KE": "Kenya",
            "KI": "Kiribati",
            "KP": "Korea, Democratic People's Republic of",
            "KR": "Korea, Republic of",
            "KW": "Kuwait",
            "KG": "Kyrgyzstan",
            "LA": "Lao People's Democratic Republic",
            "LV": "Latvia",
            "LB": "Lebanon",
            "LS": "Lesotho",
            "LR": "Liberia",
            "LY": "Libia",
            "LI": "Liechtenstein",
            "LT": "Lithuania",
            "LU": "Luxembourg",
            "MO": "Macao",
            "MK": "Macedonia, Republic of",
            "MG": "Madagascar",
            "MW": "Malawi",
            "MY": "Malaysia",
            "MV": "Maldives",
            "ML": "Mali",
            "MT": "Malta",
            "MH": "Marshall Islands",
            "MQ": "Martinique",
            "MR": "Mauritania",
            "MU": "Mauritius",
            "YT": "Mayotte",
            "MX": "Mexico",
            "FM": "Micronesia, Federated States of",
            "MD": "Moldova, Republic of",
            "MC": "Monaco",
            "MN": "Mongolia",
            "ME": "Montenegro",
            "MS": "Montserrat",
            "MA": "Morocco",
            "MZ": "Mozambique",
            "MM": "Myanmar",
            "NA": "Namibia",
            "NR": "Nauru",
            "NP": "Nepal",
            "NL": "Netherlands",
            "NC": "New Caledonia",
            "NZ": "New Zealand",
            "NI": "Nicaragua",
            "NE": "Niger",
            "NG": "Nigeria",
            "NU": "Niue",
            "NF": "Norfolk Island",
            "MP": "Northern Mariana Islands",
            "NO": "Norway",
            "OM": "Oman",
            "PK": "Pakistan",
            "PW": "Palau",
            "PS": "Palestinian Territory, Occupied",
            "PA": "Panama",
            "PG": "Papua New Guinea",
            "PY": "Paraguay",
            "PE": "Peru",
            "PH": "Philippines",
            "PN": "Pitcairn",
            "PL": "Poland",
            "PT": "Portugal",
            "PR": "Puerto Rico",
            "QA": "Qatar",
            "RE": "Réunion",
            "RO": "Romania",
            "RU": "Russian Federation",
            "RW": "Rwanda",
            "BL": "Saint Barthélemy",
            "SH": "Saint Helena, Ascension and Tristan da Cunha",
            "KN": "Saint Kitts and Nevis",
            "LC": "Saint Lucia",
            "MF": "Saint Martin (French part)",
            "PM": "Saint Pierre and Miquelon",
            "VC": "Saint Vincent and the Grenadines",
            "WS": "Samoa",
            "SM": "San Marino",
            "ST": "Sao Tome and Principe",
            "SA": "Saudi Arabia",
            "SN": "Senegal",
            "RS": "Serbia",
            "SC": "Seychelles",
            "SL": "Sierra Leone",
            "SG": "Singapore",
            "SX": "Sint Maarten (Dutch part)",
            "SK": "Slovakia",
            "SI": "Slovenia",
            "SB": "Solomon Islands",
            "SO": "Somalia",
            "ZA": "South Africa",
            "GS": "South Georgia and the South Sandwich Islands",
            "ES": "Spain",
            "LK": "Sri Lanka",
            "SD": "Sudan",
            "SR": "Suriname",
            "SS": "South Sudan",
            "SJ": "Svalbard and Jan Mayen",
            "SZ": "Swaziland",
            "SE": "Sweden",
            "CH": "Switzerland",
            "SY": "Syrian Arab Republic",
            "TW": "Taiwan, Province of China",
            "TJ": "Tajikistan",
            "TZ": "Tanzania, United Republic of",
            "TH": "Thailand",
            "TL": "Timor-Leste",
            "TG": "Togo",
            "TK": "Tokelau",
            "TO": "Tonga",
            "TT": "Trinidad and Tobago",
            "TN": "Tunisia",
            "TR": "Turkey",
            "TM": "Turkmenistan",
            "TC": "Turks and Caicos Islands",
            "TV": "Tuvalu",
            "UG": "Uganda",
            "UA": "Ukraine",
            "AE": "United Arab Emirates",
            "GB": "United Kingdom",
            "US": "United States",
            "UM": "United States Minor Outlying Islands",
            "UY": "Uruguay",
            "UZ": "Uzbekistan",
            "VU": "Vanuatu",
            "VE": "Venezuela, Bolivarian Republic of",
            "VN": "Viet Nam",
            "VG": "Virgin Islands, British",
            "VI": "Virgin Islands, U.S.",
            "WF": "Wallis and Futuna",
            "YE": "Yemen",
            "ZM": "Zambia",
            "ZW": "Zimbabwe"}
    return data[shortname]


def main(ref2):
    while True:


        with open("Path.txt", "r") as f:
            path=f.readline()
        with open('NumbberOfCalles.txt', 'r') as f:
            NumbberOfCalles = f.readline()
        data2 = ref2.get()
        if user not in data2:
            print(
                Fore.LIGHTGREEN_EX + "*********************************************" + Fore.LIGHTRED_EX + "Sorry Baby" + Fore.LIGHTGREEN_EX + "*********************************************")
            sys.exit()
        with sync_playwright() as p:
            # READ proxy from file
            with open('vpn.txt', 'r') as fin:
                proxy = fin.readline()
            with open('vpn.txt', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('vpn.txt', 'w') as fout:
                fout.writelines(data[1:])
            print(Fore.RED + 'proxy : ' + Fore.GREEN + proxy)

            # driver = p.firefox.launch(headless=headless ,proxy={"server":proxy}) # ,proxy={"server":"socks5://usa.rotating.proxyrack.net:9000"})
            driver = p.firefox.launch(headless=headless) # ,proxy={"server":"socks5://usa.rotating.proxyrack.net:9000"})
            context = driver.new_context()

            page = context.new_page()

            try:

                url = 'https://www.youtube.com/verify?pli=1'
                page.goto(url)
            except Exception:
                print("      [+]  Time out Error ")
            # print(Fore.LIGHTBLUE_EX + "    [+]  Start >>> " + self.gmail)
            with open("email.txt", "r") as f:
                userdata = f.readline()
            with open('email.txt', 'r') as u:
                data = u.read().splitlines(True)
            with open('email.txt', 'w') as w:
                w.writelines(data[1:])
            email, passw, recvery = userdata.split('|')
            print(Fore.LIGHTBLUE_EX + "Start >>>  " + email)

            page.wait_for_load_state('domcontentloaded')
            onpemail='id=identifierId'
            btn = '//*[@id="identifierNext"]/div/button'
            inbpass = '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
            # inbpass = '#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'
            btnpass = '#passwordNext > div > button'
            page.is_visible(onpemail)
            if (page.is_visible(onpemail)) == True:
                page.fill(onpemail, email)
            sleep(0.1)
            if (page.is_visible(btn)) == True:
                page.click(btn)
            sleep(0.4)
            page.locator(inbpass).wait_for()
            page.locator(inbpass).fill(passw)
            sleep(0.2)
            page.is_visible(btnpass)
            if (page.is_visible(btnpass)) == True:
                page.click(btnpass)
            sleep(0.9)
            # if "Your password was changed less than an hour ago" in page.inner_html("*") or "تم تغيير كلمة مرورك قبل أقل من ساعة واحدة" in page.inner_html("*")  or "Wrong password. Try again or click ‘Forgot password’ to reset it." in page.inner_html("*"):
            #     print(Fore.RED+"Somthing Wrong With Password")
            #     with open("FailePass.txt", "a") as f:
            #         f.write(email + '|' + passw + '|' + recvery)
            #
            #     page.close()

            try:
                page.wait_for_timeout(7000)
                if "Verify your identity" in page.inner_text("*") \
                        or "Enter a phone number to get a text message with a verification code Phone number" in page.inner_html(
                    "*"):
                    print(Fore.YELLOW + "Yellow Email")
                    # with open("Yellow.txt", "a") as f:
                    #     f.write(email + '|' + passw + '|' + recvery)

                    page.close()
                if "Your account has been disabled" in page.inner_text(
                        "*") or "Your account has been disabled" in page.inner_html(
                        "*")\
                    or "تم إيقاف حسابك" in page.inner_text(
                        "*") or "تم إيقاف حسابك" in page.inner_html(
                        "*"):
                    try:
                        print(Fore.RED + "      [+]  Your account has been disabled  >>> " +email)

                        # with open("disabledAccount.txt", "a") as f:
                        #     f.write(email+'|'+passw+'|'+recvery)
                        page.close()
                    except Exception as e:
                        pass

                if "Confirm your recovery phone number" in page.inner_html("*") or "Confirm your recovery phone number" in page.inner_text("*") or "تأكيد رقم هاتف الاسترداد" in page.inner_html("*") or "تأكيد رقم هاتف الاسترداد" in page.inner_text("*") :
                    page.click(
                        '#view_container > div > div > div.pwWryf.bxPAYd > div > div.WEQkZc > div > form > span > section > div > div > div > ul > li:nth-child(4) > div')
                    sleep(2)
                    page.fill("#phoneNumberId", value=recvery)
                    page.click(
                        '#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')

                elif "Confirm your recovery email" in page.inner_html("*") or "يجب إثبات هويتك" in page.inner_html("*"):
                    page.click('li.JDAKTe:nth-child(3) > div:nth-child(1)')

                    if "Verify it’s you" in page.inner_html("*") or "Verify it’s you" in page.inner_text("*") or "Verify that it’s you" in page.inner_html("*") or "Verify that it’s you" in page.inner_text("*") :
                        sleep(3)
                        print(Fore.LIGHTGREEN_EX + "recovery email  " + recvery)
                        page.fill('#knowledge-preregistered-email-response',recvery)
                        page.click(
                            '#view_container > div > div > div.pwWryf.bxPAYd > div > div.zQJV3 > div > div.qhFLie > div > div > button')
                else:
                    pass

                    page.wait_for_timeout(7000)

                    if "Couldn’t sign you in" in page.inner_text("*") or  "تعذر تسجيل دخولك" in page.inner_text("*"):
                        print(Fore.YELLOW + "Couldn’t sign you in Email")
                        # with open("Yellow.txt", "a") as f:
                        #     f.write(email + '|' + passw + '|' + recvery)

                        page.close()
                    elif "Verify your identity" in page.inner_text("*") or  "يجب إثبات هويتك" in page.inner_text("*")\
                            or "Enter a phone number to get a text message with a verification code Phone number" in page.inner_html(
                        "*"):
                        print(Fore.YELLOW + "Yellow Email")
                        # with open("Yellow.txt", "a") as f:
                        #     f.write(email + '|' + passw + '|' + recvery)

                        page.close()
                    if "Your account has been disabled" in page.inner_text(
                            "*") or "Your account has been disabled" in page.inner_html(
                        "*") \
                            or "تم إيقاف حسابك" in page.inner_text(
                        "*") or "تم إيقاف حسابك" in page.inner_html(
                        "*"):
                        try:
                            print(Fore.RED + "      [+]  Your account has been disabled  >>> " + email)

                            # with open("disabledAccount.txt", "a") as f:
                            #     f.write(email+'|'+passw+'|'+recvery)
                            page.close()
                        except Exception as e:
                            pass
                    page.wait_for_timeout(1000)
                if "أنت في وضع تسجيل الدخول" in page.inner_html('*') or 'ليس الآن' in page.inner_html(
                        '*') or "You’re signed in" in page.inner_text('*') or"You’re signed in" in page.inner_html('*') or 'Not now' in page.inner_html(
                        '*') or "You’re signed in" in page.inner_text('*'):
                    notnow = '#yDmH0d > c-wiz > div > div > div > div.L5MEH.Bokche.ypEC4c > div.lq3Znf > div:nth-child(1) > button'
                    # sleep(0.3)
                    page.click(notnow)
                else:
                    pass
                page.wait_for_timeout(3000)
                while "اختيار قناة" not in page.inner_html("*") and "اختيار قناة" not in page.inner_text("*")\
                        and"إثبات ملكية رقم الهاتف (الخطوة 1 من 2)" not in page.inner_html("*") \
                        and "إثبات ملكية رقم الهاتف (الخطوة 1 من 2)" not in page.inner_text("*")\
                        and "Select a channel" not in page.inner_html("*") and "Select a channel" not in page.inner_text("*")\
                        and"Phone verification (step 1 of 2)" not in page.inner_html("*") \
                        and "Phone verification (step 1 of 2)" not in page.inner_text("*"):
                    sleep(1)
                # We're sorry...
                if "اختيار قناة" in page.inner_html("*") or "اختيار قناة" in page.inner_text("*")or"Select a channel" in page.inner_html("*") or "Select a channel" in page.inner_text("*"):
                    try:
                        notnow = '#contents > ytd-account-item-renderer:nth-child(1) > tp-yt-paper-icon-item'
                        page.click(notnow)
                    except:
                        notnow = 'ytd-account-item-renderer.style-scope:nth-child(1) > tp-yt-paper-icon-item:nth-child(1) > tp-yt-paper-item-body:nth-child(2) > yt-formatted-string:nth-child(1)'
                        page.click(notnow)
                else:
                    sleep(1)
            except:
                pass
            try:
                sleep(999)
                for i in range(int(NumbberOfCalles)):
                    page.click('#input-2 > input')
                    page.click(path)
                    # read number and delet it
                    with open('numbers.txt', 'r') as numbers:
                        callsonenum1 = numbers.readline()
                    with open('numbers.txt', 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open('numbers.txt', 'w') as fout:
                        fout.writelines(data[1:])
                    print(Fore.RED + 'use this  Number: ' + Fore.BLUE + callsonenum1)
                    try:
                        page.locator(
                            'tp-yt-paper-radio-button.radio:nth-child(2) > div:nth-child(2) > yt-formatted-string:nth-child(1)').click()
                    except:
                        pass
                    try:
                        page.fill('//*[@id="input-1"]/input', value=callsonenum1)
                    except:
                        pass

                    try:
                        page.click('//*[@id="send-code-button"]/yt-button-renderer')
                    except:
                        pass

                    try:
                        sleep(1)
                        if "إدخال رمز التحقق المؤلف من 6 أرقام" in page.inner_html(
                                "*") or "إدخال رمز التحقق المؤلف من 6 أرقام" in page.inner_text("*")\
                            or"Enter your 6-digit verification code" in page.inner_html(
                                "*") or "Enter your 6-digit verification code" in page.inner_text("*"):
                            print(Fore.LIGHTBLUE_EX + ' >>>>>>>>>> Success Call')
                            page.click('//*[@id="back-button"]/yt-button-renderer')
                        else:
                            print(Fore.LIGHTRED_EX + ' >>>>>>>>>> Failed Call')
                            page.reload()
                            sleep(2)
                        if f"There was a problem sending a verification code to {callsonenum1}. Please enter a different phone number." in page.inner_html("*")\
                            or f"There was a problem sending a verification code to {callsonenum1}. Please enter a different phone number." in page.inner_text("*"):
                            print(Fore.LIGHTRED_EX + ' >>>>>>>>>> Failed Call')
                            page.reload()
                            sleep(2)
                    except:
                        pass
                page.close()
            except:
                pass



json={
  "type": "service_account",
  "project_id": "smsusers-15097",
  "private_key_id": "8c0138091f9843b7d392a0312dcff6253c18bbde",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCyUPNkCAD+YR/h\nY2OEBJfpM2EPLI/E8tYLJ1Ril8To80iyTCaqU44QR+IhJEb4pCwJa4y9L41pdcIS\n/qHI0nOcjJdeqPamBVALA2rotuZ7j0roTEhh6kHKlrgTHRjNiRP1GXwJPa6xjBaL\n++Mz0IH2hcaEJpH1b2oUMOfcIISkE0x6AVeqvS1MEZt8rwW7bEraIsmV22Ak/X1o\nt/Sj5hxZKkr77FXDsG41Jv2uywA5u8yZqci0W6pmTMvA9hl2e5fN70LTtEo1NU+f\n6fikGcBkSAeuDOrnXtechCK8Kw3648LlwDapyvYCC5cEsYadCPL2uB9GXCH2XktM\nwMHbJQeDAgMBAAECggEADOhBfeulusQSrTC8YC7URNaUaidFGYdPCWFQQToQJaE6\nkWFkE8SBji8jMK1HZTG+WEjh1+3hvruoj9HA/zWF6ykyvxuG4wSTwyr8/u8CUaOm\nfe3LotQfQrKp4gRN/86yKaCDHcjKZOKph890pj2rsp8DUXHYndtHN+1EUzxCraed\nb8FN3UBa9CrmcpbJ1H+tsBbUvlPi97X0JynzlhLGOqhJXE56t6UTnCbABvK6qkXv\n17izcfSEOyst6jLFqzIECy7PojNsKxXSRZoATrl8ZUxIpP2PS2f6sYh4Co4CoUht\nNTvYq3h/cTKnDJYzn+1pTsVXBqUni5+kSQz+8wu6vQKBgQDzTROVHJOA5xBCTg77\nUA8HIshKZ2Ay+BC6zUeF8kMPF6+97s6JHseDX8sj5+rlK0A95qX6xjLfpLi2kMO4\nz/jl23ZcvznvA3ESKt0FZGcjKjpQ3bj8g+Fw6RYKdGgzlso/wG5DuaCGImZXrXt+\nY5hEhNrEpG2SflwulGB9FgHAJwKBgQC7n5BgX1PV+SM0fuKTHV3iUDUwbeszUC+j\nj+TiSP9qCLBcphaYA0dFH0oDwn/adejf9jLcma31RTr7fVjssNpSL1WbT6W3CsTA\nXvkmZ31ql6w9IqYtGPoHCeQRHqVsXjJKp2rU+sURn15J0uu6q4URQzH0btp79qdN\np+kdRkr7RQKBgQCdjTD8I1glZfuyZCfxeANzRIPdIpo6B0eWH+6L/7iLInSMkwMt\n6j+ahELgyoLiyiI8s4qSHRy+lEWE+7OyjwKHnplEMBTNATaMZDNiFYVwUR0YVqw+\n4Qvw+Q9rz7vWhHQN2ofM1Xzsv4P0jQPmcYod/MZKBoxqC+eXxj/BYKnbiwKBgGTD\nnGl1qPPI2rRt1MeHxQ0vYHGDBwdG8F7af+VbqPjMc9M+S/IWCKfB1yFPyxSLsKbf\ndY9uZbPNG5FHT4PGs2niDArearR0bxiVqR+MAxpFHPa0biTYPiebk0XyfItHx6C6\nazC5AS+mtJ/XTEyzo0KTIPgStPpQjKezHwpe3xQ1AoGBALlNsLUrD8Sg65nQ/SZX\n86qTKmlvareGAqHBZuVkRZwUti4bAUXT1MKZkPJ4rICjz/uTofdii8GiEmfgFJU9\nqmY5ub4LVtiiUcXdPrs4DQwXRG2KPVxRpTZdZEBCAdWKI/70fQnhWnW5Pue3Y9Al\nPLw0jzgEUo3HxyZIt901WVuM\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-5126e@smsusers-15097.iam.gserviceaccount.com",
  "client_id": "116249347280035278160",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5126e%40smsusers-15097.iam.gserviceaccount.com"
}


cred=credentials.Certificate(json)
app=initialize_app(cred,{
    'databaseURL':'https://smsusers-15097-default-rtdb.firebaseio.com/'
})
ref=db.reference('/YouTubeCall/')
ref2 = db.reference('/ActiveYouTubeCall/')

data=ref.get()
data2=ref2.get()

with open('UserPass.txt','r') as userpass:
    userpass=userpass.readline()
user,passw=userpass.split('|')

userJson={
            user:passw
        }

import atexit


def fun1():
    ref2.child(user).delete()

atexit.register(fun1)


if user in data2:
    print('Active By Another Person')
    sys.exit()

if user in data:
    if( passw == data[user]):
        ref2.update(userJson)

        print('Welcome..!!!\n')
        print("pleas enter number of threads..")
        number_of_threads = int(input())
        print("pleas enter 1 to non headless  ..")
        try:
            headless=int(input())
        except:
            headless=0
        if headless==1:
            headless=False
        else:
            headless=True
        threads = []
        for j in range(number_of_threads):
            sleep(2)
            t = threading.Thread(target=main, args=[ref2])
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()




