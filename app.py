#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, request, url_for, redirect
from webpay import WebPay
from webpay.errors import InvalidRequestError

app = Flask(__name__)
app.config.from_object(__name__)
WEBPAY_PUB_KEY = 'test_public_19DdUs78k2lV8PO8ZCaYX3JT'
WEBPAY_PRI_KEY = 'test_secret_eHn4TTgsGguBcW764a2KA8Yd'
WEBDB_PRICE = 1554


@app.route('/')
def index():
    return render_template('index.html', webpay_pubkey=WEBPAY_PUB_KEY)


@app.route('/purchase', methods=['POST'])
def purchase():
    webpay = WebPay(WEBPAY_PRI_KEY)
    try:
        charge = webpay.charges.create(
            amount=WEBDB_PRICE,
            currency='jpy',
            card=request.form.get('webpay-token'))
        return render_template('purchased.html', charge=charge)
    except InvalidRequestError:
        e = sys.exc_info()[1]  # noqa
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
