from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecret-sa-key" # Required for flash messages!

# This is our "Database" for now. 
# Each task is a dictionary: {'id': 1, 'task': 'Buy Milk', 'done': False}
tasks = []

@app.route("/")
def index():
    # This says: "Go to the templates folder and find index.html"
    # We also send our 'tasks' list to the HTML so it can show them.
    return render_template("index.html", all_tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, flash 



# PROVINCES = {
#     "Gauteng": {"capital": "Johannesburg", "pop_millions": 15.5, "area_km2": 18176},
#     "Western Cape": {"capital": "Cape Town", "pop_millions": 7.2, "area_km2": 129462},
#     "KwaZulu-Natal": {"capital": "Pietermaritzburg", "pop_millions": 11.5, "area_km2": 94361},
#     "Eastern Cape": {"capital": "Bhisho", "pop_millions": 6.7, "area_km2": 168966},
#     "Limpopo": {"capital": "Polokwane", "pop_millions": 5.9, "area_km2": 125754},
#     "Mpumalanga": {"capital": "Mbombela", "pop_millions": 4.7, "area_km2": 76495},
#     "North West": {"capital": "Mahikeng", "pop_millions": 4.1, "area_km2": 104882},
#     "Free State": {"capital": "Bloemfontein", "pop_millions": 2.9, "area_km2": 129825},
#     "Northern Cape": {"capital": "Kimberley", "pop_millions": 1.3, "area_km2": 372889},
# }

# SA_PROVINCES = ["Gauteng", "Western Cape", "KwaZulu-Natal", "Eastern Cape", "Limpopo", "Mpumalanga", "North West", "Free State", "Northern Cape"]
# app = Flask(__name__)
# app.SECRET_KEY = "mysecretkey"
# @app.route("/hello/<name>")
# def hello(name):
#     return render_template("hello.html", name=name, age =30, city="New York")

# @app.route("/provinces")
# def provinces():
#     return render_template("province.html", provinces = PROVINCES)

# @app.route("/contact", methods =["GET", "POST"])
# def contact():
#     errors = []
#     name = ""
#     message = ""
#     if request.method == "POST":
#         name = request.form.get("name", "").strip()
#         message = request.form.get("message", "").strip()
#         if not name:
#             errors.append("Name is required")
#         if len(message) < 10:
#             errors.append("Message should be at least 10 characters long")
        
#         if not errors:
#             print (f"FROM {name}: {message}") #in real life this would be sent to an email address
#             return render_template("contact_thanks.html", name = name)
#     return render_template("contact.html")

# @app.route("/feedback", methods=["GET", "POST"])
# def feedback():
#     errors = []
#     data = {"name": "", "province": "", "feedback": ""}

#     if request.method == "POST":
#         data["name"] = request. form.get("name", "").strip() 
#         data["province"] - request. form.get("province","").strip()
#         data[ "feedback"] - request. form.get("feedback", "").strip()

#         if len (data["name"]) < 2:
#             errors. append("Name must be at least 2 characters")

#         if data ["province"] not in SA_PROVINCES:
#             errors.append ("Please select a valid province!")

#         if len(data["feedback"]) < 10:
#             errors. append ("Feedback must be at least 10 characters!")

#         if not errors:
#             return render_template("feedback_thanks.html", data = data)
#     return render_template("feedback.html", data = data, errors = errors)

# @app.route ("/me")
# def me():
#     return redirect

# if __name__ == "__main__":
#     app.run(debug=True)
