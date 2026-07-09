from flask import Flask, render_template

app = Flask(__name__)

# TASK 1: Add two routes to your webpage 
# (use Bootstrap if you want it to look nice)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cat")
def cat():
    return render_template("cat.html")

# CHALLENGE 1: Create an html page that 
# displays all of the items
# in a list of your choice. You can put  
# whatever you want in this list, 
# below is an example
favourite_animals = ["dogs", "cats", "parrots", "ferret"]

# TASK 2: Use Jinja2 to add custom content to an HTML page
# CHALLENGE 2: Use {% block content %} 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
