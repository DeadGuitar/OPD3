from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("main_page.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        deposit = float(request.form.get('deposit'))
        interest = float(request.form.get('interest'))
        time = int(request.form.get('time'))
        ans = deposit
        for payment in range(time):
            ans += round(ans*(interest/1200), 2)
    return render_template("main_page.html", Ans=round(ans, 2), depv=deposit, intv=interest, timev=time)


if __name__ == "__main__":
    app.run(debug=True)
