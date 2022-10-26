# some utilities
from platform import python_branch
import mysql.connector

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect

#Test DB connection
mydb = mysql.connector.connect(
  host="us-cdbr-east-06.cleardb.net",
  user="b9672cfc679037",
  password="54055ecc",
  database="heroku_a503fd3f3d82a0d"
)

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="smarttrash"
# )


# Declare a flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    '''
    Render the main page
    '''
    return render_template('index.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    '''
    Render the main page
    '''
    return render_template('index.html')

@app.route('/trending', methods=['GET'])
def trending():
    '''
    Render the main page
    '''
    return render_template('highchart.html')

@app.route('/classifications', methods=['GET'])
def classifications():
    '''
    Render the main page
    '''
    return render_template('knob-chart.html')

@app.route('/surrounding', methods=['GET'])
def surrounding():
    '''
    Render the main page
    '''
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM smartbin")
    myresult = mycursor.fetchall()
    empty = []
    full=[]
    half=[]
    for x in myresult:
        print(x[3])
        if x[5]==1:
            empty.append(x[3])
        if x[5]==2:
            half.append(x[3])
        if x[5]==3:
            full.append(x[3])

    return render_template('jvectormap.html', empty=empty,full=full,half=half)

@app.route('/displayBins', methods=['GET'])
def displayBins():
    '''
    Render the main page
    '''

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM smartbin")
    myresult = mycursor.fetchall()
    empty = []
    full=[]
    half=[]
    for x in myresult:
        print(x[3])
        if x[5]==1:
            empty.append(x[3])
        if x[5]==2:
            half.append(x[3])
        if x[5]==3:
            full.append(x[3])

    return render_template('displaybins.html', empty=empty,full=full,half=half)

@app.route('/register', methods=['GET'])
def register():
    '''
    Render the main page
    '''
    return render_template('register.html')

@app.route('/registerUser', methods=['POST'])
def registerUser():
    data = request.form
    
    account = "Personal"
    email = request.form.get('name')
    password = request.form.get('password')

    mycursor = mydb.cursor()
    sql = "INSERT INTO users (id, email, password, type) VALUES (%s, %s, %s, %s)"
    val = (NULL, email, password, account)        
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    '''
    Render the main page
    '''
    return render_template('bin.html')
    #return render_template('registerDone.html')

@app.route('/bin', methods=['GET'])
def registerbin():
    '''
    Render the main page
    '''
    return render_template('bin.html')

@app.route('/addBin', methods=['POST'])
def addbin():
    user_id = 1
    name = request.form.get('name')
    location = request.form.get('location')
    geolocation = request.form.get('geolocation')
    mycursor = mydb.cursor()
    sql = "INSERT INTO smartbin (id, name, location, geolocation, user_id) VALUES (%s, %s, %s, %s, %s)"
    val = (NULL, name, location, geolocation, user_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return render_template('index-old.html')

if __name__ == '__main__':
    app.run(port=5000)
    #app.run()
