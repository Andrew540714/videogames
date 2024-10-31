from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/money")
def render_page1():
    return render_template('money.html')

@app.route("/information")
def render_page2():
    value5 = list()
    return render_template('graph.html', value22=value5)
    
def list():
    with open('video_games.json') as name5:
        value = json.load(name5)
    value5=[]
    for v in value:
        value5.append(v["Title"])
    options=""
    for z in value5:
       options += Markup("<option value=\"" + z + "\">" + z + "</option>")
    return options
    
if __name__=="__main__":
    app.run(debug=True)