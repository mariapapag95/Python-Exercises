from flask import Flask, render_template, request, session, redirect
from model import User, Data

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        return render_template('homepage.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm = request.form['confirm']
        u = User(username)
        users_balance = 100000
        if u.signup(username, password, confirm):    
            return render_template('dashboard.html', users_balance=users_balance)
        else:
            return render_template('signup.html')
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        u = User(username)
        users_balance = u.user_balance()
        users_orders_info = u.user_orders()
        users_holdings_info = u.user_holdings()
        if u.login(password):
            return render_template('dashboard.html',users_orders_info=users_orders_info,users_holdings_info=users_holdings_info,users_balance=users_balance)
        else:
            return render_template('login.html')

@app.route('/lookup', methods=['GET','POST'])    
def lookup():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        ticker_symbol = request.form['ticker_symbol']
        data = Data()
        lookup_results = data.lookup(ticker_symbol)
        return render_template('dashboard.html', lookup_results=lookup_results)

@app.route('/quote', methods=['GET','POST'])
def quote():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        ticker_symbol = request.form['ticker_symbol']
        trade_volume = int(request.form['trade_volume'])
        data = Data()
        quote_results = data.quote(ticker_symbol,trade_volume)
        return render_template('dashboard.html', quote_results=quote_results)

@app.route('/buy', methods=['GET','POST'])
def buy():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        ticker_symbol = request.form['ticker_symbol']
        trade_volume = request.form['trade_volume']
        username = request.form['username']
        with User(username) as u:
            if u.buy(ticker_symbol,trade_volume):
                return render_template('success.html')
            else:
                return render_template('error.html')

@app.route('/sell', methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        return render_template('homepage.html')
    elif request.method == 'POST':
        ticker_symbol = request.form['ticker_symbol']
        trade_volume = request.form['trade_volume']
        username = request.form['username']
        user = User(username)
        if user.sell(ticker_symbol,trade_volume):
            return render_template('success.html')
        else:
            return render_template('error.html')

@app.route('/close_account', methods=['GET','POST'])
def abort():
    if request.method == 'GET':
        return render_template('close.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        u = User(username)
        if u.delete_user(username):
            return render_template('byeforever.html')
        else: 
            return render_template('error.html')

@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    if request.method == 'GET':
        return render_template('adminlogin.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        adminkey = request.form['adminkey']
        d = Data()
        users = d.users()
        holdings = d.holdings()
        orders = d.orders()
        leaderboard = d.leaderboard()
        u = User(username)
        if u.admin(password,adminkey):
            return render_template('admindashboard.html',users=users,holdings=holdings,orders=orders,leaderboard=leaderboard)
        else:
            return render_template('adminlogin.html')

@app.route('/super', methods=['GET','POST'])
def superuser():
    if request.method == 'GET':
        return render_template('secretlogin.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        superkey = request.form['superkey']
        d = Data()
        users = d.users()
        holdings = d.holdings()
        orders = d.orders()
        leaderboard = d.leaderboard()
        super_balance = 10000000000000
        u = User(username)
        if u.superuser(password,superkey):
            return render_template('superuser.html',users=users,holdings=holdings,orders=orders,leaderboard=leaderboard,super_balance=super_balance)
        else:
            return render_template('secretlogin.html')


if __name__ == '__main__':
    app.secret_key = 'maria'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug = True)