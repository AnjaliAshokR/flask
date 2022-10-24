from flask import Flask, render_template

app=Flask(__name__)

@app.route('/users')
def users():
    user=['Anju', 'Meenu', 'Remi', 'Rahul']
    return render_template('users.html', user=user)

app.run(debug=True)