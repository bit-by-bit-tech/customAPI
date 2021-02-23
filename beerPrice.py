import os, sys, qrcode, io, flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('drink-prices', __name__, url_prefix='/drink-prices')

@bp.route('/comparison', methods=('GET', 'POST' ))
def compareDrinks():
    if request.method == 'POST':
        drink_1_size = float(request.form['drink_1_size'])
        drink_1_price = float(request.form['drink_1_price'])
        drink_2_size = float(request.form['drink_2_size'])
        drink_2_price = float(request.form['drink_2_price'])

        drink_1_avg = (drink_1_price / drink_1_size)#reduce the zeroes to 2
        drink_2_avg = (drink_2_price / drink_2_size)#reduce the zeroes to 2

        drink_1_avg ='%.2f' % drink_1_avg
        drink_2_avg ='%.2f' % drink_2_avg
        if drink_1_avg < drink_2_avg:
            answer = "Drink 1"
        else:
            answer = "Drink 2"

        return (render_template('beerPrices/beerPrices.html', d1avg=drink_1_avg, d2avg=drink_2_avg, answer=answer))

    return render_template('beerPrices/beerPrices.html')
