from flask import Flask, render_template

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

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name, age =30, city="New York")

@app.route("/provinces")
def provinces():
    return render_template("province.html", provinces = PROVINCES)

if __name__ == "__main__":
    app.run(debug=True)