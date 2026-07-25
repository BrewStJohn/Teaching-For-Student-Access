from flask import Flask, render_template

app = Flask(__name__)

# TASK 1: Add two routes to your webpage 
# (use Bootstrap if you want it to look nice)

# CHALLENGE 1: Create an html page that 
# displays all of the items
# in a list of your choice. You can put  
# whatever you want in this list, 
# below is an example
favourite_animals = ["dogs", "cats", "parrots", "ferret"]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cat")
def cat():
    return render_template("cat.html")

# TASK 2: Use Jinja2 to add custom content 
# to an HTML page
# CHALLENGE 2: Use {% block content %} 

# EXTRA CHALLENGE: Use jinjas template inheritance
# So that all pages on your website use the same
# generic template.

# TASK 3:
# Create a simple userID form.
# When the user submits the form and sets 
# the userID (username), the page should
# remember the user IF they visit the page
# within 2 minutes. 

# Then, send them to a new page that displays 
# their name using the stored cookie information.

# CHALLENGE 3: if they revisit the page 
# (or refresh) after 2 minutes have passed, 
# then you will be required to login again 
# (because the cookie will be expired by then)

# TASK 4: Form Validation

# Client-side verification: When the user tries to login, 
# validate their login. Here are some examples of things you can verify:
# a) Username and password fields are filled in
# b) Username and password length requirements
# display to the user when they have an invalid login 
# (change the HTML and CSS)

# Server-side verification: 
# check to see if the user is a 'verified user' 
# on your page. If the username is 'admin' and 
# password is 'pass123', return a template thats
# a landing page. Otherwise, return to them
# a message saying wrong username / password.

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
