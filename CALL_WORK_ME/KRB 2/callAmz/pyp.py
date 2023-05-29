import string
import time
from random import random

import requests
from captcha_solver import CaptchaSolver

with requests.session() as ss:
    response = ss.get('https://sellercentral.amazon.com/performance/account/health/contact-us?formid=7951')
    # response = ss.get('https://sellercentral.amazon.com/hill/website/form/7951?hill_locale=')
    print(response)
    headers = {
    'authority': 'sellercentral.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'signin-sso-state-us=b43cc4f3-fe17-41e8-837b-2570a9e18116; session-id=143-9750581-3290726; ubid-main=134-2186155-9856521; session-token="JiyGINTFuaMdXTehv21AAGjjrr6zFPmE3yS9C0NWrWAVClq/fbtM00NVG8WOb7KnrV0RjQ1pn6zOmxootsc9YiIVtm/N1f67u2zd6L3vSHLrxBYCNZauP63AmFxrZlxPn3esJviLSrvZUQz+BP2HjQoXy7Txxt9UpSMmNsWNQbXehdjE3V9etzzy9v7+FGUQ8T7zjIfRv/wVQLRf81AKJ+ve3rKlVXISd6AMWqIckhs="; session-id-time=2304390051l; csm-hit=tb:47JGNP53T7YYKG25BXPF+s-4PVW8HZP6R2AQ9SP2S6X|1673670078945&t:1673670078945&adb:adblk_no',
    'origin': 'https://sellercentral.amazon.com',
    'referer': 'https://sellercentral.amazon.com/ap/signin',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}

    data = {
    'appActionToken': '8EvpP9CxnOkbIgv26CxWOupAucEj3D',
    'appAction': 'SIGNIN',
    'metadata1': 'ECdITeCs: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',
    'openid.return_to': 'ape:aHR0cHM6Ly9zZWxsZXJjZW50cmFsLmFtYXpvbi5jb20vcGVyZm9ybWFuY2UvYWNjb3VudC9oZWFsdGgvY29udGFjdC11cz9mb3JtaWQ9Nzk1MQ==',
    'prevRID': 'ape:NFBWVzhIWlA2UjJBUTlTUDJTNlg=',
    'workflowState': 'eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.SkRXhxhE4n-b5Xkky6w-XBvw2Jy0_k6IY7ryfDcW81zp0QDqIgqDDw.rt1cPxNGuORWbhfX.fsA_2GkwhcSOTEv9gQMb54KTx2niyD5BT6XXlRP-03YiqWqX282eZU_K3rGRmguH51eSACWGDncXAILOyOne7r3AJAEOk-JJWoDoSFZcW5rvsvHgzFbhr3zD29LgfuHyjRp9dBhmW2_NfWXShCUVb5EWx6LTebswfc0qHwrWz2_31mzOLxm2OUwdi4xKCuQzqh7GYUKYHUWY1u9yjWaoJEjM1reDs3GMNq5Otw0aECAawQq2aiwuWm1ot8gjWWbd9Upv0h2miv4FaWFnOqZnfrQlnDVJMtpuglztOuqwjnRJK9ah9_mjaKJDA13hZGeDrNtzFzridibRm9Iyhx8KZ9e0hYqE2aP56EA-37XSMGryrQ-VJw2pjPZ3SfRuG8A25R6_UmqlbHq7zSxLfBY1WsrJGKR9g6T-wYkEByfERncqKwFzZABmP-Evxfsoo2pLRhPDKQnM92FK9rdzjo94wSlZefwB0M6reGXcVvp1wjsU7BH4JkaUnkYo4BL4ULvnB97NDuAZq_lXK3qw0tOwOHQoWHVZoFzXLGfvcWp8jdVrZqK1GfmLietCqwNDCNONmEC1bYdKD1Xv3asEWpOmik2wsnifaDwm1jB1z9fp87H3BGdPXo7EAiN9-Eyflzm4LtcYt0DcfM3Q7HEvBo7Bz_NxmGm_OMVlQ9lZPaZaHqRdrvY__-QHcuhH734op4SC9DZq5qJyZWkX9kaFgs1XsU2wn1JQVJTp__1mFFAmyYeo79Cu9qJQfEsdEFeDNQOraFbe6vEu46oInubYI9sGWqXnOspa7WgpL8orQUYNs_yB32ABhCu6g9ByqpcdBI6AFVO4JpWDUyi2T4bdtVwHinyDLb6KFZ5tGwQ0xbAvv_5dykQ6eXaWR3SzGthUqgQjFIKntXVldP8.p8RvYJeZM9wLF246jWoliw',
    'email': 'michaelstuart8377@hotmail.com',
    'create': '0',
    'encryptedPwd': 'AYAAFNrsP1SioolC4O43byz24KsAAAABAAZzaTptZDUAIDU2ZDE0ZWRjZThlMmNiNmM2ODQyYzU5ZGRhZWU0MjZlAQB9p6oETBK4iWbYR5fPp7Rn90qmstVNZ7wKzWFuI/Vi0PO6wlKLexAeMbJ3RHxlGAfZyjwmb4J6Ciunx9kZnD7rJ81XSlrMMCNM53c7wJSQYssebvB87Jli7f4oVt6lFM9m10cwREMeYulMYrOrddy761UT3iQZlmYeWMA81pRPGFBxu9o5SQt9aE69YW96jJpWh/mCO3NWCQtIaO/qTEYigoKKtRS0UqCium7lzsDPqhJx7fT0Xa7RA7z24N5JiWH7VsGbzZO48grrMA0W1dWvxuG89ri5vwIGuZ0OHa7/5VOmae8879YzehwlhRlltk/eKUW0pXfgAsGgT8QdqWFOAgAAAAAMAAAAHgAAAAAAAAAAAAAAAJSzAkUr99+3eA5BfkiVHkn/////AAAAAQAAAAAAAAAAAAAAAQAAAB2S+/+VA+4yo+ZPz4H9e1wiJe3k4I7S+tYuOpK+wsa0UuqkuOyxr+ubzjh7VXg=',
    'encryptedPasswordExpected': '',
    'rememberMe': 'true',
    'aaToken': '{"uniqueValidationId":"13c762fe-927b-458f-ac82-f36641f7ec62"}'
    }

    response = ss.post('https://sellercentral.amazon.com/ap/signin', headers=headers, data=data)

    print(response)


    # time.sleep(88)
    headers = {
    'authority': 'sellercentral.amazon.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'session-id=259-7960896-4717126; ubid-acbuk=260-5306863-6523218; session-id-time=2304390806l; x-acbuk="kdc5kuFhux?qzJmEPzO88blVicDk5UAWkjdyE2rzsHJuex9xf8XQ8SdbxBf2WwVL"; at-acbuk=Atza|IwEBIATEudMKlbm79j002VNopKMiuswid9tsauRtxPrJaSidX1Ml-Pm8h1qBC7sx8aaypp7XUWfi2VllHYcWZH8uY_AJEzV_AWg7NNyHv9qAXxXNBG8G8ZOqu7KA5rKZI1CdGRgAKYlOei9DXdxl6MydYOPIvk75t7LHPB03dJOuRbmvSBVBqu7KVBu5KUBiX8CffiWaAVOGaVGI5s2Iejqp145YmyUAPoNlZSa9sELXnkORWu-D4iG6-XIDtYwJm6qQV0U; sess-at-acbuk="WOp8WoPnHh4foioJY4sFb6PPEW0+ulIo8TAVdSm3fvs="; sst-acbuk=Sst1|PQGna70jzHuET58_NR6VDn9aCVDzRBp-nDU3YsMCxu4b-NurB7NNre-BLcgUbELYzepBdZKjJwH9X2e-0yJkrpdnvWW0p5g68ffZSOGuWY4VE1NhggQanJYdNDedYqoPdcSHOQH1PKc8gQTZh5xnQ2xf6nD_9JtRe7BkNSJ1FWgdRJSVO-e9lu8nBbU4_cgELhaq8Ap8Odb_rAWJLFqzXcD83O8tqPbG63N3O15y_aQG6lg_AlUHeKaubLV3zeBbtukxWBHMl4m0xzyO4IW_DtF2DRRQc0pj8LDJv-WZ3_AAA2o; __Host-mselc=H4sIAAAAAAAA/6tWSs5MUbJSSsytyjPUS0xOzi/NK9HLT85M0XM0Ngr0NTZyNjYMCXX2VNJRykVSmZtalJyRCFKKRV02ssICkJIoRy9fX2MzP7PwQB+lWgDj0Sc7dQAAAA==; session-token=iMKvDkJkqIMI/uz77kHEkSq923vOgfFuKe5GErjzsMO3GA0PJm1/xAT2IVwALLgO8bzPoB4ah19isA4HEATCIvgQcC2tKrI+iZgx8lhK334LSCxeaF0F7uAECirkMqK5k6mpsgwWY3PIhs2dzTCaxZzMeCpACnSWLDeohVNv+3pvCqCCyA5lz/UHmWp8z6kcNCLpP9cEEmao5J1W+gEHef4b17ljE07FL1IgRXX32KXikDi4j1/npmjOkpq/SRdv',
    'referer': 'https://sellercentral.amazon.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = (
    ('formid', '7951'),
    ('mons_sel_dir_mcid', 'amzn1.merchant.d.AAJF75ISPTABAOJWWYJJY2P2YJVQ'),
    ('mons_sel_mkid', 'AZAJMM36N6WQL'),
    ('mons_sel_dir_paid', 'amzn1.pa.d.ACAZ7EKIQJUZE3JHFNECC6FRPCGA'),
    ('ignore_selection_changed', 'true'),
    ('mons_redirect', 'change_domain'),
    )

    response = ss.get('https://sellercentral.amazon.co.uk/performance/account/health/contact-us', headers=headers, params=params)
    print(response.text)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://sellercentral.amazon.co.uk/performance/account/health/contact-us?formid=7951&mons_sel_dir_mcid=amzn1.merchant.d.AAJF75ISPTABAOJWWYJJY2P2YJVQ&mons_sel_mkid=AZAJMM36N6WQL&mons_sel_dir_paid=amzn1.pa.d.ACAZ7EKIQJUZE3JHFNECC6FRPCGA&ignore_selection_changed=true&mons_redirect=change_domain', headers=headers)


    time.sleep(999)
    headers = {
        'authority': 'sellercentral.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-encoding': 'amz-1.0',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'session-id=141-6535596-3046816; ubid-main=132-0958466-6019967; csm-hit=tb:JKH4CMP6HTQT5D2YE7R2+s-JKH4CMP6HTQT5D2YE7R2|1673630455980&t:1673630455980&adb:adblk_no; session-id-time=2304350457l; x-main="LvyW@VHWEUzlZlohnRlfWGPunl8xcVWUhe9@@BFTeaCaiff@eLQOG0TbVA8lPIKv"; at-main=Atza|IwEBIGjbcBYB-eh6_dvOlxw-O4E56mq82SlftjfhpzR--eo9I0aJTz6_MFYyJ0zIrk9gYuYPURT5e5INVmG7EHrzCbRWj8Umx8JXV2u6ncH_mTWIzZDFCMOF_9rd_YcO5WnQKbVsVu67Dmo_jSrC-7xqsqOXotUKzxrUQRvckMPp2Si9bZRvGf8bxKbg5-jOKw0cQ2ygDlLTSboDm3CySvGMt82a; sess-at-main="J6xm3NwcOwaFFCvSHe/ne9HAwSSB58hevopd1zfpztM="; sst-main=Sst1|PQGt-J0xvP_x4-_dQQdpGq9YCS-Xdb1YdD5lRx3zHO5aF-LHjngWqipRMNu4CvFrCf0N_YhXZKYqb0eafz3rTbtdtAO-ggzDOsN9bBw7mJAqfs5kTKpAEUk6yPo2juk6UeL2FT-lT2m_8NsYCbXye-VRhpMMCjs1z1x-AEaNMQeC6kXzR-Tu3Fdt6DpX_W0LHkwxrADzw4p4OMUNnMu36t_LfxGX28XKPQ0OhzFmn9USCdDwFMgn4kV-z0_QHPUSR2nZMey_A1-rIYI0DiMOq1Idl-1bZVW-kgLrSwOoR2MBNTs; __Host-mselc=H4sIAAAAAAAA/6tWSs5MUbJSSsytyjPUS0xOzi/NK9HLT85M0XM09vUJMnX28zByNjdyU9JRykVSmZtalJyRCFKKRV02ssICkBL38OBwb0NTT1cvL3OlWgDZeBvqdQAAAA==; session-token=Dx5WgnP3pwNijWHxkNM7ZMw0Je3jvOc9UEAqVpORti//LMWmkqoc9z0AFasdxEnnPsmRhjgpGCJ8F5BmQnEYa1eqH3O33mbIzupPiulnnIV/0hUWtF/FPdcB3wPKDBirM41znkiDcEdH15MDtjIZA0ZfEKbcx6G6xMVvuE0Jxv0DGtXYpgjIoS6og6aELDQwubOYAYs+lat4/GBOdea1/G0ARQNiVzsUHFYffktRswGrVs9iznZeVHsa9R9j6Nff',
        'referer': 'https://sellercentral.amazon.com/hill/website/form/7951',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-amz-target': 'com.amazon.hillservice.HillService.GetCaptcha',
    }

    response = ss.get('https://sellercentral.amazon.com/hill/hillservice/mons-api/GetCaptcha', headers=headers).json()
    tokenCap=response['token']
    ImgUrl=response['imageSrc']
    cap='b2272aaaa227fccf49f866b46997cced'

    import urllib.request
    urllib.request.urlretrieve(ImgUrl, "local-filename.png")
    solver = CaptchaSolver('2captcha', api_key=f'{cap}')
    # time.sleep(5)
    raw_data = open(f"local-filename.png", 'rb').read()
    solveText = solver.solve_captcha(raw_data)
    print(solveText)
    print(ImgUrl)


    headers = {
        'authority': 'sellercentral.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'anti-csrftoken-a2z': 'hFoDKwq8Cdld6QagzaWGOjA/0110oGGaUXpgg6fDK+Z/AAAAAGPBk51jMmEyOGFiMS1jNGYxLTQ5MzktYWU2NS1jNzg0ZDY4M2QxZWM=',
        'content-encoding': 'amz-1.0',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'session-id=141-6535596-3046816; ubid-main=132-0958466-6019967; csm-hit=tb:JKH4CMP6HTQT5D2YE7R2+s-JKH4CMP6HTQT5D2YE7R2|1673630455980&t:1673630455980&adb:adblk_no; session-id-time=2304350457l; session-token=44ZAYaNnGwb3ZCAEbU6vaBfWilKAOwh2pjGbW8d3v49RiPmwVFcu7JajYGGWvJ1sJb8JEgLsfcHXaTPOJCnOuNXsOhAvkeyNQ0OMB1KfukcaagYZ3FC0V4yXEUO1vaw92rQoCh6+iV7krwJ44KotODN4tourZYhrej5u3grFMerZ/yvK7xy3rUrw/Y9l72bV8IcFV6IMtKQkkTS9cKbgcOGwqpeGbTQ98XtPeFOcVjAolNl7gBvykAW8NhMGmGt5; x-main="LvyW@VHWEUzlZlohnRlfWGPunl8xcVWUhe9@@BFTeaCaiff@eLQOG0TbVA8lPIKv"; at-main=Atza|IwEBIGjbcBYB-eh6_dvOlxw-O4E56mq82SlftjfhpzR--eo9I0aJTz6_MFYyJ0zIrk9gYuYPURT5e5INVmG7EHrzCbRWj8Umx8JXV2u6ncH_mTWIzZDFCMOF_9rd_YcO5WnQKbVsVu67Dmo_jSrC-7xqsqOXotUKzxrUQRvckMPp2Si9bZRvGf8bxKbg5-jOKw0cQ2ygDlLTSboDm3CySvGMt82a; sess-at-main="J6xm3NwcOwaFFCvSHe/ne9HAwSSB58hevopd1zfpztM="; sst-main=Sst1|PQGt-J0xvP_x4-_dQQdpGq9YCS-Xdb1YdD5lRx3zHO5aF-LHjngWqipRMNu4CvFrCf0N_YhXZKYqb0eafz3rTbtdtAO-ggzDOsN9bBw7mJAqfs5kTKpAEUk6yPo2juk6UeL2FT-lT2m_8NsYCbXye-VRhpMMCjs1z1x-AEaNMQeC6kXzR-Tu3Fdt6DpX_W0LHkwxrADzw4p4OMUNnMu36t_LfxGX28XKPQ0OhzFmn9USCdDwFMgn4kV-z0_QHPUSR2nZMey_A1-rIYI0DiMOq1Idl-1bZVW-kgLrSwOoR2MBNTs; __Host-mselc=H4sIAAAAAAAA/6tWSs5MUbJSSsytyjPUS0xOzi/NK9HLT85M0XM09vUJMnX28zByNjdyU9JRykVSmZtalJyRCFKKRV02ssICkBL38OBwb0NTT1cvL3OlWgDZeBvqdQAAAA==',
        'origin': 'https://sellercentral.amazon.com',
        'referer': 'https://sellercentral.amazon.com/hill/website/form/7951',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-amz-target': 'com.amazon.hillservice.HillService.SubmitForm',
    }

    data = {
        '{"channelType":"Phone","formData":{"formFields":{"describeIssue":"wgegwegewg"},"appointmentData":null,"captchaDetails":{"attempt":'+solveText+',"token":"'+tokenCap+'"},"chatData":null,"emailData":null,"phoneData":{"phoneNumber":{"country":"US","number":"5752550904","extension":null},"subject":"Questions regarding my Account Healtheggw","target":"51fa26f6-5ec8-4922-bb1f-8577cbab6d6b"}},"motivationId":7951,"permissionsToken":"AYADeD6qklkHPIExqLZ O 7TYH0AXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREFqKzV4ZjI4ekE4UVlPamoyOU5LQllxcVhzWTF1MUQzYWhHOEdQVlJlK1htOTNSMURLS05TVUZOSDJ4SzlWbU9xZz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo2NTY4MDU1NjI2NjQ6a2V5Lzc2N2Q1ZjJmLTI2OTAtNDU3Yy05MTY1LWQ4NjVhYWU1MzE1NQC4AQIBAHjKvje4 jP5QZxiYpGZy Zife6tA0D0YjPhWFQ6qAkwLgE51KlCx92l8xZESaK4RTugAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLB5CgMFbWIrgF8ACAgEQgDtL01jXO3Gg5e5utg3NFsBzf5iU8htgZNTjWR/wpHEdnbuJdgPSnjv dDxfOrljGV0xRt2nNoOgnlfGDwIAAAAADAAAEAAAAAAAAAAAAAAAAADWHUAp0EBVE1p1RcFoK7YX/////wAAAAEAAAAAAAAAAAAAAAEAAADfctwT8 EKhL8mhHLEJTlib CgdLiOubB/SpX7agOEfe0gj3DqLsMHs8jAGytSwi eVCXPGxneE4A5O2bweiX89Ui01Zm3jdzJyodPaEyRdbT/pDnMzCg5vXTsEun 6QpqIB4ttFcWocLRtxnY7AeTbtT4aG65fTVD2xhS/DV1k56agDxI2gdBuoRYlVcwfVLcksGLVUGUP s/kvra2VeMJrlqtiSU3qVt3SIUQvJGXcnrGBBZe3bakipM2PlwizYcBUqLP4qelBBtMGUWjQFdpYsDkeZSyzi5Ib 8xvFqrhyGWWHeThqJgtIinTo LXYAZzBlAjEAsgA1m6FjzZxpgye2S52nDpt4dPczoFiRrCyt0VZBFlcqjZuuy8RTGC31RU0YNDpPAjALPk4FfiZapr7WVpEK3G/CmgwkHzqUYaLXiz58DY/LjxjXMiGOtZCUDF6eUaM33uA': '","clientId":null,"locale":"en_US"}'
    }

    response = ss.post('https://sellercentral.amazon.com/hill/hillservice/mons-api/SubmitForm', headers=headers,
                             data=data)
    print(response.content)


    headers = {
        'authority': 'sellercentral.amazon.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'anti-csrftoken-a2z': 'hFoDKwq8Cdld6QagzaWGOjA/0110oGGaUXpgg6fDK+Z/AAAAAGPBk51jMmEyOGFiMS1jNGYxLTQ5MzktYWU2NS1jNzg0ZDY4M2QxZWM=',
        'content-encoding': 'amz-1.0',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'session-id=141-6535596-3046816; ubid-main=132-0958466-6019967; csm-hit=tb:JKH4CMP6HTQT5D2YE7R2+s-JKH4CMP6HTQT5D2YE7R2|1673630455980&t:1673630455980&adb:adblk_no; session-id-time=2304350457l; session-token=44ZAYaNnGwb3ZCAEbU6vaBfWilKAOwh2pjGbW8d3v49RiPmwVFcu7JajYGGWvJ1sJb8JEgLsfcHXaTPOJCnOuNXsOhAvkeyNQ0OMB1KfukcaagYZ3FC0V4yXEUO1vaw92rQoCh6+iV7krwJ44KotODN4tourZYhrej5u3grFMerZ/yvK7xy3rUrw/Y9l72bV8IcFV6IMtKQkkTS9cKbgcOGwqpeGbTQ98XtPeFOcVjAolNl7gBvykAW8NhMGmGt5; x-main="LvyW@VHWEUzlZlohnRlfWGPunl8xcVWUhe9@@BFTeaCaiff@eLQOG0TbVA8lPIKv"; at-main=Atza|IwEBIGjbcBYB-eh6_dvOlxw-O4E56mq82SlftjfhpzR--eo9I0aJTz6_MFYyJ0zIrk9gYuYPURT5e5INVmG7EHrzCbRWj8Umx8JXV2u6ncH_mTWIzZDFCMOF_9rd_YcO5WnQKbVsVu67Dmo_jSrC-7xqsqOXotUKzxrUQRvckMPp2Si9bZRvGf8bxKbg5-jOKw0cQ2ygDlLTSboDm3CySvGMt82a; sess-at-main="J6xm3NwcOwaFFCvSHe/ne9HAwSSB58hevopd1zfpztM="; sst-main=Sst1|PQGt-J0xvP_x4-_dQQdpGq9YCS-Xdb1YdD5lRx3zHO5aF-LHjngWqipRMNu4CvFrCf0N_YhXZKYqb0eafz3rTbtdtAO-ggzDOsN9bBw7mJAqfs5kTKpAEUk6yPo2juk6UeL2FT-lT2m_8NsYCbXye-VRhpMMCjs1z1x-AEaNMQeC6kXzR-Tu3Fdt6DpX_W0LHkwxrADzw4p4OMUNnMu36t_LfxGX28XKPQ0OhzFmn9USCdDwFMgn4kV-z0_QHPUSR2nZMey_A1-rIYI0DiMOq1Idl-1bZVW-kgLrSwOoR2MBNTs; __Host-mselc=H4sIAAAAAAAA/6tWSs5MUbJSSsytyjPUS0xOzi/NK9HLT85M0XM09vUJMnX28zByNjdyU9JRykVSmZtalJyRCFKKRV02ssICkBL38OBwb0NTT1cvL3OlWgDZeBvqdQAAAA==',
        'origin': 'https://sellercentral.amazon.com',
        'referer': 'https://sellercentral.amazon.com/hill/website/form/7951',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-amz-target': 'com.amazon.hillservice.HillService.GetContactRequestStatus',
    }

    data = {
      '{"caseId":"11755917451","channelType":"Phone","contactRequestId":"11755917451:CRQ/u7Pw2kAbT4uZji9lk0o-BQ","permissionsToken":"AYADeO1HVHQhO7L/MJas8Jz2QzgAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREEwb1RxdnBoSjhHUmFYMis3Y2NHNllQMDRKS090L210QmVkSFVCeE9VSmRkU09vS2xWMTgyTHZ1NUZub1RKWC9RZz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo2NTY4MDU1NjI2NjQ6a2V5LzU3MzUxNWE2LTI0ZjktNGY4My05MTk0LWNmZDY1ODAwNTA2MQC4AQIBAHjc1EWg4uVWGg01A1UHbFxj3KfGAoo0rWSvuNQZ8He1pQFwNlSVjU4w6t0kY8RyRDk AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM6ttNB4tqIOdSPOZkAgEQgDtvscMBCZT9ji5Sap7tbSEKGy02rIsZLgKxP0snc3vHE8jPMm1tTp9mvS8HQA1Y6a23xnT3Il70On1qigIAAAAADAAAEAAAAAAAAAAAAAAAAACufkO2qG9uMjM vPAjmT0L/////wAAAAEAAAAAAAAAAAAAAAEAAADsjGikTqjY4ui2le6ucWqCnxUNAy6jJSUdbJB7XRiq8IW/C7nQYocDwhdyQmklrglFRpzskanZTO3GSWeCNogqHrGUYhWRzY8hCBDO9xAUCaZuHmQuctPyBH5EfnRFXJZkwKKA4jX2oZsX2Tdga7rNXUkqQ6UrxoTq7z1nWCWx90h4CXHXhvtRXmgeQIfg8Oc71YZEiNfhYWtqwN6A4dz1UEVAwzY9wlayCXErZCO Phte6k2jUclEyPZlJVB/zxwM/yuJ5fhCg/JHdXOTzq60W udEOJT8mEiYt5VOT6j/RNymC/j7NVN4f2wAcXpqO0m0uJbj6z/L36Y4kJuAGcwZQIwHdskrYtvsjFXp0XcRBdT3kxAUsHIbq2hiA3oDAD73YQIbJVkl uXSF0Pvg8aflzXAjEA/PKL5qst2yPW37YhV5cJTZTtaXF5lcf2nfxrnrMp4UhgyLM48xAdPGFLJ4OTunG1","temporaryFallbackToken":"AYADeEG 60g13OmDVw9Fqo1grpcAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREEwb1RxdnBoSjhHUmFYMis3Y2NHNllQMDRKS090L210QmVkSFVCeE9VSmRkU09vS2xWMTgyTHZ1NUZub1RKWC9RZz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo2NTY4MDU1NjI2NjQ6a2V5LzU3MzUxNWE2LTI0ZjktNGY4My05MTk0LWNmZDY1ODAwNTA2MQC4AQIBAHjc1EWg4uVWGg01A1UHbFxj3KfGAoo0rWSvuNQZ8He1pQFwNlSVjU4w6t0kY8RyRDk AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM6ttNB4tqIOdSPOZkAgEQgDtvscMBCZT9ji5Sap7tbSEKGy02rIsZLgKxP0snc3vHE8jPMm1tTp9mvS8HQA1Y6a23xnT3Il70On1qigIAAAAADAAAEAAAAAAAAAAAAAAAAAAw9EttFlolv0jt9mB17yRW/////wAAAAEAAAAAAAAAAAAAAAEAAAQ5WbHHEuFTGWxC0Ksi3FXGngl2wR dLeNw7pW58fbgRO8IGHESyROXkb6HMeiC3KhxIv/qwLDCvnE3xJuUzNhoIVqrvyc4c9yv4GvR0hkHrKC6bLokmm6FlfI3q41 Csv92z2l0eu68MI1tJyua92StLP1KjMVPOEds11 2ceE3Bl6K5e08HiAPoj17UBNyKqOa5lsU2PaGaIqS6Ca/ycz8DvN4FVoyarQKFe/CrXrcFSYZrWXASBU3H4zjxWvIr86ImZtBQulrCKIKjqSIasFCyyq duwd2UAoIoC5kTkCg0taLkafMqxMHgCO3Gliw0QQzxBx4r8vE2SprPV1LWZAwannSrrOSq7J3DXWUHSYRq kxgcn8VmDjcwAYzGhFboCeJ1Ibem6kFqvrwPj6nZslz04fFQMan9M8Crp1Z8uK87QfOHWmaQzfDN 7i3iUhnednhZwIuYAQS3sSC7t3J0HCp1LGyT4YYEJoK8xU/Os3Nm4HdJ5SSRT8Qnh B6oyYao9kjYHuFyjmZtzNDHPD/Xdfd5G5GWk4YpHYHfyV/kA25tP5c28S0plCckLAYxjI4Zig/SgJfr1V KRoBFOEPyChiWHo4ts03VlGJ4b3UfButriOZ4TCTsI rh4 cYLWGmkpvHnKCrUfV67J3YKpfreJ2DVIIrS4mOsJP6vy hna9ekyPVy68LkO2LKbLRxB3TMXwSFd9KteYkzy2qIplTPrCHz4jkd0mvMgyMbPnmCHiaYDqShZnpCYkZHgzZhPQzKPT2soD3ry4fZAKAs5TAH0pZojBOjGOCsXESkK/S0GVaTaZwcueu4yWSdjq6UX3//lB2fa947x5ej3CXRZXDZ8e9f1 FlPHrC2dhtgZ3nqTtDhnp4M/CfyCcNNvxnO6FAxRBbr6liXH4Cc 6zsXQ6bC5zYCEq0pdZPJah zjdbg5HD1SC4MdQYimbjJhW8dvXRe4vo2wWGjDo0uNwXRtoBiYRHA/DVx4uBxihZ/qGbQg gqmI9zHTcX5mjv0Y/O6vna/uW4MZPz8hYAiaCPUUoTEmBFWbI6Y8eyuvWmbOEuDwPeodiVk/VB/N5AhugRPX neGkZMR1z1F4W68VhIW2Te9KNM0SJZNLzpzSk30aLnXBC3DrLWi0WKpU6Op5T8 WInZ/Bt 5Yl5B4yFYELs 78pircqrF lxn00NGiRG8lkkc9ymcEPM f61UvJh66kmyqZ2kuCcvT4HVB2ntRleiM67bWWLNV/3h1qVqfl5Vhmstfj2brvPlaULol6qjA8aYP0uPmiiVyu5ndxFvJIOrX4VTH264sshSbwvYiyGGJb9UyRn8JmLqjNSngVpKzv0L975MSB2vUY3hZdtadjlnc85k p9vq3XOE7zfBEjhFcBdt23hDqatOp5fU oART3xYWrEW44Eo7 UGIx2VCp/DWJqUQnGPzFRcD0/liCV6oh0UfV7pQAZzBlAjAYfSem6L6axc HiGAQmKSygOyRFTa tfDrp41RKcYJfRoQvQyqZdUHAjZ1i8aF/EkCMQD9gFjV0iVmq/3mj6Cfswe/ IlM nXekm3Mq/ov0TiFWvSXYHI/x5HqnGgoQpYRajY': '"}'
    }

    response = ss.post('https://sellercentral.amazon.com/hill/hillservice/mons-api/GetContactRequestStatus', headers=headers, data=data)
    print(response.content)