import os, sys, qrcode, io, flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('qrcode', __name__, url_prefix='/qrcode')

@bp.route('/generator', methods=('GET', 'POST' ))
def genQR():
    if request.method == 'POST':
        img = ''
        data = request.form['data']
        error = None
        if not data:
            error = "Please enter a URL or similar."
            flash(error)
        elif error == None:
            qr = qrcode.QRCode(version=1,

                                box_size=10,
                                border=4)

            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image()

            img_buf=io.BytesIO()

            img.save(img_buf)
            img_buf.seek(0)

            data = ''

            #return (render_template('qrCode/qrcode.html', code = finalCode))
            return(flask.send_file(img_buf, mimetype='image/png'))

    return render_template('qrCode/qrcode.html')
