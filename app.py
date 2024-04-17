from flask import Flask
from forms import MyForm
from flask import render_template, redirect

app=Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
