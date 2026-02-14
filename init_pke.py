from flask import Flask, render_template, request, redirect, url_for
from main import app

@app.route('/Showdown/Pokédex/Scalpereur')
def Scalpereur():
    return render_template('/pokedex/Scalpereur.html')
