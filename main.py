import json #allows the importing of json data

def process_data(data): #function for the data
    processed_data = []
    for user in data:
        submissions = sorted(user["submissions"], key=lambda x: x["score"], reverse=True)[:24] 
        total_score = sum(submission["score"] for submission in submissions) #sum fuction used to create a total score
        if len(submissions) >= 3: #len/length function in a if statement so that only people with more than 3 submissions will count
            processed_data.append({"name": user["name"], "score": total_score, "submissions": submissions})
    return sorted(processed_data, key=lambda x: x["score"], reverse=True) #returns scores in decending order

with open("scores.json", "r") as file: #opening the score json file in read mode
    data = json.load(file) #loading it
processed_data = process_data(data) #putting it into an variable

with open("processed_data.json", "w") as file: #opening the output json file in write mode
    json.dump(processed_data, file, indent=6) #put the file as an argument, with indent for presentebility

def get_leaderboard(): # function used to put the output data in read mode and what will be displayed on the webpage
    with open("processed_data.json", "r") as file:
        leaderboard = json.load(file)
    return leaderboard

leaderboard = get_leaderboard()

#flask framework

from flask import Flask, render_template #render so i can upload the data using a html file

app = Flask(__name__)

@app.route("/") #decoration
def leaderboard_page():
    return render_template("index.html", leaderboard=leaderboard)

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate) #allowed me to use the enumerate built in function

if __name__ == '__main__':
    #app.debug = True #refreshed the webpage if anything changes
    #app.run(host = '0.0.0.0', port = 8080) #allows me to create a http file to run and test code locally
    app.run(debug=false, host = '0.0.0.0')



