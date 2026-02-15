from flask import Flask, render_template, request, redirect, url_for
import tweepy
from init_pke import *

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('Accueil.html')

@app.route('/Showdown')
def Showdown():
    return render_template('Showdown.html')

@app.route('/Showdown/news')
def display_tweets():
    return render_template('news.html')


@app.route('/Showdown/Pokédex')
def Pokedex():
    return render_template('Pokedex.html')

@app.route('/Showdown/Replays')
def Replays():
    return render_template('Replays.html')

@app.route('/Showdown/Replays/OU 9G/double_regen_001')
def double_regen_001():
    return render_template('/Replays/OU 9G/double_regen_001.html')

@app.route('/Showdown/Replays/Random_bat')
def Random_bat():
    return render_template('Replays/randombat_9G/random_bat.html')

@app.route('/Showdown/Teams')
def Teams():
    return render_template('Teams.html')

@app.route('/Showdown/Teams/ou9g')
def OU_Team():
    return render_template('formats/ou9g.html')

@app.route('/Showdown/Teams/ou9g/double_regen')
def double_regen():
    return render_template('/teams/OU 9G/double_regen.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)