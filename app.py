from flask import Flask,render_template,request,redirect,session
from flask_session import Session
from DB_FUNCTIONS.db_functions import CreateUser,ListUsers,deleteUser,AllMoviesCart,findCartItems


app = Flask(__name__)

# This sets the session to be non-permanent, meaning it will be cleared when the browser is closed.
app.config['SESSION_PERMANENT'] = False 
# This sets the session type to use the file system for storage.
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)


if app == "__main__":
    app.run(debug=True, use_reloader=True)


PLAYERS = {}
SPORTS = ['football','soccerr','basketball','baseball','tennis']


# @app.route("/")
# def hello_world():
#     if "name" in request.args:
#         msg = request.args['name']
#     else:
#         msg = "world"

#     return render_template('index.html',placeholder=msg)


# Another way of doing this
@app.route("/")
def hello_world():
    if not session.get('name'):
        return redirect('/login')
    # msg = request.args.get('name','world')
    # return render_template('index.html',placeholder=msg)
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['name'] = None
    session['cart'] = None
    return redirect('/')


@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/post-form",methods=['GET','POST'])
def postForm():
    if request.method == "GET":
        return render_template('postform.html')
    
    # For POST Request, we use request.form.get() instead of request.args.get()
    elif request.method == "POST":
        return render_template('greet.html',name=request.form.get('name','fake'),email=request.form.get('email','fake@fake.com'),message=request.form.get('message','Fake message'))
        # return redirect(url_for('/greet',name=request.form.get('name','fake'),email=request.form.get('email','fake@fake.com'),message=request.form.get('message','Fake message')))


@app.route("/greet")
def greet():
    return render_template('greet.html',name=request.args.get('name','fake'),email=request.args.get('email','fake@fake.com'),message=request.args.get('message','Fake message'))


@app.route("/sportform",methods=['GET','POST'])
def sport():
    if request.method == 'GET':
        return render_template('sportform.html')
    
    elif request.method == 'POST':
        name = request.form.get('name')
        sport = request.form.get('sport')
        
        # From List
        # if name in PLAYERS and sport not in SPORTS:
        #     return "You are not registered! Hacker!"
        # else:
        #     # PLAYERS[name] = sport
        #     # return render_template('players.html',players=PLAYERS)

        # From DB
        CreateUser(name=name,sport=sport)
        return redirect('/players')
    

@app.route('/players',methods=['GET','POST'])
def players():
    
    if request.method == 'POST':
        id = request.form.get('degenerate')
        # print('id is ',id)
        deleteUser(id)

    Users = ListUsers()
    return render_template('players.html',players=Users)


@app.route('/shop',methods=['GET','POST'])
def shop():
    if not session.get('name'):
        return redirect('/')
    
    # if not session.get('cart'):
    if not session.get('name'):
        session['cart'] = []
    
    if request.method == 'POST':
        id = request.form.get('movie_id')
        session['cart'].append(id)
        return redirect('/cart')
            
    movies = AllMoviesCart()
    return render_template('/shop.html',movies=movies)



@app.route('/cart')
def cart():
    if not session.get('name'):
        return redirect('/') 
    if not session.get('cart'):
        return redirect('/shop')
    print('session cart app: ',session['cart'])
    return render_template('/cart.html',cart=findCartItems(session['cart']))


