from flask import Flask, render_template,redirect, url_for, request
import json

'''Key Learning Goals
1. Defining routes and navigation between routes
2. Jinjas2 templating
3. Processing data from forms
4. Simple data storage using json
5. Build a fully functional app

Overview:
- Backend for login
- Backend for signup
- Backend for home page
- Backend for task entry page
- Rendering for home page
- Rendering for index page
- 22 items to complete
'''

app=Flask(__name__)

'''Allows users to go to the index page'''
@app.route("/")
def index():
    #TODO:(4) Show different template renderings using name
    name="Ryan"
    return render_template("index.html",name=name)

'''Allows users to login'''
@app.route("/login")
def login():
    return render_template("login.html")

'''Allows users to sign up'''
@app.route("/signup")
def signup():
    return render_template("signup.html")

'''Allows entries into the Todo List'''
@app.route("/entry")
def entry():
    #TODO:(2) Return the correct template
    return render_template("entry.html")

#TODO:(4) Render the correct template for the "home" page with tasks=tasks and name=name
#TODO:(12) Add permissions for post requests
@app.route("/home",methods=["GET","POST"])
def home():
    #TODO:(5) Inject the below list of tasks and name into the correct template
    #Data that will be injected into the template
    tasks = ["Cleaning the dishes", "Walking the dog", "Cooking dinner", "Playing basketball", "Practicing piano"]
    name=""

    # TODO:(22) Update the tasks with the ones from the "tasks.json" file

    #TODO:(13) Check post request
    #TODO:(14) Get the entered username
    #TODO:(15) Check if the username and password match
    #TODO:(16) If there is a match, re-render the "home" page with the tasks and the username

    return render_template("home.html")

#TODO:(17) Check post request
#TODO:(18) Create an empty list for tasks
#TODO:(19) Get all of the tasks from the form and store in a var
#TODO:(20) Add all tasks to the task list
#TODO:(21) Write all of the tasks to the "tasks.json" file
@app.route("/confirm-entry",methods=["POST","GET"])
def confirm_entry():
    return render_template("confirm-entry.html")

#TODO:(1) Make a new route whose name is "confirm-signup"
#TODO:(3) Make the new route render the "confirm-signup" page
#TODO:(6) Allow post and get for the confirmation page

    '''Inside method'''
    #TODO:(7) Check post request form data
    #TODO:(8) Create variables from the posted data
    #TODO:(9) Store data in the "user" dictionary
    #TODO:(10) Store data in json file
    #TODO:(11) Server side redirect to "login" page

if __name__=="__main__":
    app.run(debug=True) #Never run as debug=True in a production environment


