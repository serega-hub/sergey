#Импорт
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/submitinho')
def last():
    return render_template('last.html')

@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_telega = request.form.get('button_telega')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_telega=button_telega , button_python=button_python , button_html=button_html , button_db=button_db)



@app.route('/submit', methods=['POST'])
def last_result_form():
    email = request.form['email']
    text = request.form['text']

    with open('form2.txt', 'a',) as f:
        f.write(email + ' ' + text + ' ' + '\n')

    return render_template('last.html', email=email, text=text)




if __name__ == "__main__":
    app.run(debug=True)