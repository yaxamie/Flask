'''Flask is pretty cool!  Who knows where this will go?!'''

from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)
app.secret_key = '5\xb2\x9e\xf4\xc5\xca\x8c\xb7 vE\x86\xd5\xa6\xd1m\xf2\x90\xd5\xe4\\m?\xbe'


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', name=escape(session['username']))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
