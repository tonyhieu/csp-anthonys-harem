from flask import Blueprint, render_template, request, json
import requests

ethan_bp = Blueprint('ethan', __name__,
                       url_prefix='/ethan',
                       template_folder='templates',
                       static_folder='static', static_url_path='static/ethan')

@ethan_bp.route("/")
def ethan_index():
    return render_template("ethanIndex.html")

@ethan_bp.route("/textAdventureEthan")
def text_adventure():
    return render_template("textAdventureEthan.html")

@ethan_bp.route("/videogamesApiEthan")
def videogamesApiEthan():

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        'accept': "application/json",
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': "f843e28f92mshd3de980258688f8p118a28jsn305a11f8326b"
    }

    response = requests.request("GET", url, headers=headers)

    output = json.loads(response.text)
    return render_template("videogamesApiEthan.html", haha=output)