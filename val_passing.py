from flask import Flask, render_template

app=Flask(__name__)

@app.route('/prof/<username>')
def prof(username):
    return render_template('new.html',username=username, new_var=False)

app.run(debug=True)