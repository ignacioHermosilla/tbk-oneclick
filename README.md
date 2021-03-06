# Transbank Oneclick
Python implementation of transbank-oneclick API SOAP

## Disclaimer

This library is based on [python-oneclick](https://github.com/cornershop/python-oneclick) (I was the main contributor to this library). **tbk-oneclick** is a "slim" version of python-oneclick, removing the dependency on old and "problematic" cryptographic libraries (C wrappers). That allows the use of this library on environments like **Heroku** or **AWS lambda**.

## Install

Setup:

  ```
  pip install tbk-oneclick
  ```

  or manually:

  ```
  python setup.py develop
  ```

## Usage

First set environment variable for commerce

```
import os
os.environ['TBK_COMMERCE_KEY'] = "KEY"  # path/to/certificate/certificate.key
os.environ['TBK_COMMERCE_CRT'] = "CERTIFICATE"  # path/to/certificate/certificate.crt
```

The default behavior is to use the transbank production environment. If you want to use the Transbank testing environment (with your testing certificates), you need to indicate this on initialization:

```
from oneclick import OneClick
oneclick = OneClick(testing_mode=True)  # use library with Transbank testing environment
```

otherwise (production certificates):

```
from oneclick import OneClick
oneclick = OneClick()  # Transbank production environment
```

Init Inscription

```
#  request
oneclick = OneClick()
resp = oneclick.init_inscription(email='your@email.com', 
                                 redirect_url='http://your_domain.com',
                                 username='your_username')
#  response example
resp.is_valid()  # True
resp.token  # e7665f871fa39e6c05549eeddd1ff07a520a769fa84cc6994465cdb06cbb4b
resp.urlWebpay  # https://webpay3g.orangepeople.cl/webpayserver/bp_inscription.cgi
```
Finish Inscription

```
oneclick = OneClick()
#  Transbank send the TBK_TOKEN to the redirect_url given on init_inscription
resp = oneclick.finish_inscription(token=params['TBK_TOKEN'])
#  response example
resp.is_valid()  # True
resp.authCode  # 1234
resp.creditCardType  # Visa
resp.last4CardDigits  # 6623
resp.tbkUser  # d2f27f36-b038-4937-8aa6-182b3de38cfd
```
Authorize

```
oneclick = OneClick()
#  request
resp = oneclick.authorize(amount_to_charge=10000, 
                          tbk_user='d2f27f36-b038-4937-8aa6-182b3de38cfd',
                          username='your_username', 
                          buy_order='20150820155538859')
#  response example
resp.is_valid()  # True
resp.authorizationCode  # 1213
resp.transactionId  #  71498
resp.creditCardType  #  Visa
resp.last4CardDigits  #  6623
```
Reverse

```
oneclick = OneClick()
#  request
resp = oneclick.reverse(buy_order='20150820155538859')
#  response example
resp.is_valid()  # True
resp.reverseCode  # 3619160862457231902
resp.reversed  # True
```
Remove user

```
oneclick = OneClick()
#  request
resp = oneclick.remove_user(tbk_user='d2f27f36-b038-4937-8aa6-182b3de38cfd', 
                            username='your_username')
#  response example
resp.is_valid()  # True
resp.removed  # True
```

## Errors

The method -> is_valid() always returns False when something was wrong. Additionally, 3 params are returned: 
* error: error token
* error_msg: error description
* extra: raw error

example:

```
oneclick = OneClick()
#  request
resp = oneclick.authorize(amount_to_charge=10000, 
                          tbk_user='d2f27f36-b038-4937-8aa6-182b3de38cfd',
                          username='your_username', 
                          buy_order='20150820155538859')
#  response example
resp.is_valid()  # False
resp.error  # AuthorizeError
error.error_msg  #  limites Oneclick, máximo monto de pago excedido
error.extra  #  <responseCode>-98</responseCode>
```

## Tests

  ```
  python setup.py test
  ```

  ```
  nosy
  ```  

## Contributors
This library is based on python-oneclick (https://github.com/cornershop/python-oneclick).

You can contribute by forking the project, adding the contributions and creating the PRs, or just file an issue and we will try to solve it ASAP.


## License

The MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
