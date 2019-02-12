from flask import Flask, render_template as render, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('friendsdb')
    query = "select * from friends;"
    all_friends = mysql.query_db(query)
    print(type(all_friends[0]))


    return render("index.html", friends = all_friends)

@app.route("/add_friend", methods=["POST"])
def add_friend():

    mysql = connectToMySQL('friendsdb')
    query = "insert into friends (first_name, last_name, occupation, created_at, updated_at) values ("+'"'+request.form["fname"]+'","'+request.form["lname"]+'","'+request.form["occupation"]+'",'+"NOW(), NOW());"

    # insert into friends (first_name, last_name, occupation, created_at, updated_at) values ("Peter", "Parker", "Superhero", NOW(), NOW());

    print(query)

    mysql.query_db(query)

    return redirect("/")







if __name__ == "__main__":
    app.run(debug=True)
