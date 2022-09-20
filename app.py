from time import time
from flask import Flask, render_template, request, redirect
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST', 'GET'])
def generate():
    error = None
    if request.method == 'POST':
        url = request.form['url']
        size = request.form['size']
        fillColor = request.form['fillColor']
        backColor = request.form['backColor']

        if url and size or fillColor or backColor:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=size,
                border=4,
            )
            qr.add_data(url)  
            # using the make() function  
            qr.make(fit = True)  
            # using the make_image() function  
            img = qr.make_image(fill_color = (fillColor), back_color = (backColor))
            # saving the QR code image  
            img.save("./qrcodes/" + str(time()) + ".png")  
        else:
            error = 'You must fill out the input'
    else:
        return render_template('index.html')
        
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
