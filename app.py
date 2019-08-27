from flask import Flask, request, url_for, render_template, session
#from flask_session import Session
import requests, logging, werwolf

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/setup', methods = ['GET','POST'])
def setup():
    return render_template('setup.html')


@app.route('/setup/numberOfPlayers', methods = ['GET','POST'])
def setPlayerNumber():
    numberOfPlayers = request.form.get('num')
    with open('no_of_players.txt', 'w+') as file:
        file.write(str(numberOfPlayers))
    werwolf.createDict()
    return(render_template('success.html', players = numberOfPlayers))


@app.route('/spieler', methods = ['GET','POST'])
def get_data():
    if request.method =='GET':
        return('Please submit the form')
    else:
        if request.method == "POST":
            name = request.form.get("name")
            #werwolf.game(name)
            file = open('no_of_players.txt')
            num = file.read()
            operator = werwolf.deduct()
            return render_template('user.html', players = num, name = name, operator = operator)



if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0')
