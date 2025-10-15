from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        sex = request.form['sex']
        status = request.form['status']
        location = request.form['location']
        return render_template('profile.html', firstname=firstname, lastname=lastname, sex=sex, status=status, location=location)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
