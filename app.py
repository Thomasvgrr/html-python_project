from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salutation', methods=['POST'])
def salutation():
    nom = request.form['nom']
    message = f'Bonjour, {nom} !'
    return render_template('welcome.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
