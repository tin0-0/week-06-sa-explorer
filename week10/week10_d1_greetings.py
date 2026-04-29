from flask import Flask, request, abort

app = Flask(__name__)
PROVINCES = {
    "Gauteng": {"capital": "Johannesburg", "pop_millions": 15.5, "area_km2": 18176},
    "Western Cape": {"capital": "Cape Town", "pop_millions": 7.2, "area_km2": 129462},
    "KwaZulu-Natal": {"capital": "Pietermaritzburg", "pop_millions": 11.5, "area_km2": 94361},
    "Eastern Cape": {"capital": "Bhisho", "pop_millions": 6.7, "area_km2": 168966},
    "Limpopo": {"capital": "Polokwane", "pop_millions": 5.9, "area_km2": 125754},
    "Mpumalanga": {"capital": "Mbombela", "pop_millions": 4.7, "area_km2": 76495},
    "North West": {"capital": "Mahikeng", "pop_millions": 4.1, "area_km2": 104882},
    "Free State": {"capital": "Bloemfontein", "pop_millions": 2.9, "area_km2": 129825},
    "Northern Cape": {"capital": "Kimberley", "pop_millions": 1.3, "area_km2": 372889},
}
@app.route("/")
def greet():
    return "<h1>Dumelang</h1>" 

@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route("/user/<id>")
def show_user(id):
    #<int
    return f"<h1> User #{id}</h1><p>This is of type {type(id).__name__}</p>"

@app.route("/province/<name>")
def  province(name):
    name - name.title()
    if name not in PROVINCES:
        abort(404)
        P = PROVINCES[name]
        return f"<h1>{name}</h1><p>Capital: {P['capital']}</p><p>Population: {P['pop_millions']} million</p><p>Area: {P['area_km2']} km2</p>"

        return f"<h1> SA Provinces</h1><p>{', '.join(PROVINCES)}/p>"


@app.route("/search")
def search():
    q = request.args.get("q", "")
    return f"<h1>Searching for '{q}'</h1>"





if __name__ == "__main__":
    app.run(debug = True)