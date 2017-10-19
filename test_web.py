from perimeter import area_kite
from flask import Flask,render_template,redirect, request

app = Flask (__name__)

@app.route('/')
def home ()-> '302':
    return redirect('/entry')

@app.route('/entry/')
def go_entry()->'html':
    return render_template('entry.html', the_title='Welcome to the form')


@app.route('/calculate/', methods=['POST'])
def calculate ()->'html':
    D = float(request.form['D'])
    d = float(request.form['d'])

    result = area_kite(D,d)
    title = "perimeter kite result.html"
    return render_template('result.html', the_D=D, the_d=d, the_result=result, the_title=title)


app.run(debug=True)
