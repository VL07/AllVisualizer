from flask import Flask, redirect, render_template, url_for, request, jsonify
import random
import string
import json
# from replit import db

app = Flask(__name__)

visualizers = {"bar": "Bar", "line": "Line", "pie": "Pie", "doughnut": "Doughnut"}

# URL IMPORTANT
URL = "http://127.0.0.1:5001"
# SET TO TRUE IF IN REPLIT.COM (OR REPL.IT) IMPORTANT
# Boath need to be true to create fake db and work
RUNSINREPLIT = True
CREATEFAKEDB = True
# Replit project url
REPLITURL = "#"

# creats a fake db if not running in replit
if CREATEFAKEDB:
    db = {}

def randomUniceKey(l=8):
    s = ''.join(random.choice(string.ascii_letters + str(string.digits)) for i in range(l))
    return str(s)


# 404
@app.errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")



#index
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/visualizer/<thing>/")
@app.route("/visualizer/<thing>")
def visualizer(thing):

    if CREATEFAKEDB:
        global db

    if thing in visualizers.keys():
        if thing == "bar":

            url = randomUniceKey()
            while url in list(db.keys()):
                url = randomUniceKey()

            #adds to db
            db[url] = {"data": {"values": [], "labels": [], "label": ""}, "type": "bar"}

            editurl = randomUniceKey()

            db[url + editurl] = {"type": "bar", "data": {"values": [], "labels": [], "label": ""}}
            
            # purl = url # sets urls to anoutehr var that tont change
            # url = str(url_for("sharedVisualiser") + "/" + url + "/")
            # editurl = str(url_for("sharedVisualiser") + "/" + purl + editurl + "/")

            print(url, editurl)

            return render_template("visualizer_bar.html", visualizer=thing, url=url, editurl=editurl, surl=url_for('sharedVisualiser', _external=True))

        elif thing == "line":
            url = randomUniceKey()
            while url in list(db.keys()):
                url = randomUniceKey()

            #adds to db
            db[url] = {"data": {"values": [], "labels": [], "label": "", "tension": 0}, "type": "line"}

            editurl = randomUniceKey()

            db[url + editurl] = {"type": "line", "data": {"values": [], "labels": [], "label": "", "tension": ""}}
            
            print(url, editurl)

            return render_template("visualizer_line.html", visualizer=thing, url=url, editurl=editurl, surl=url_for('sharedVisualiser', _external=True))

        elif thing == "pie":

            url = randomUniceKey()
            while url in list(db.keys()):
                url = randomUniceKey()

            #adds to db
            db[url] = {"data": {"values": [], "labels": [], "label": ""}, "type": "pie"}

            editurl = randomUniceKey()

            db[url + editurl] = {"type": "pie", "data": {"values": [], "labels": [], "label": ""}}
            
            print(url, editurl)

            return render_template("visualizer_pie.html", visualizer=thing, url=url, editurl=editurl, surl=url_for('sharedVisualiser', _external=True))

        elif thing == "doughnut":
            url = randomUniceKey()
            while url in list(db.keys()):
                url = randomUniceKey()

            #adds to db
            db[url] = {"data": {"values": [], "labels": [], "label": ""}, "type": "doughnut"}

            editurl = randomUniceKey()

            db[url + editurl] = {"type": "doughnut", "data": {"values": [], "labels": [], "label": ""}}
            
            print(url, editurl)

            return render_template("visualizer_doughnut.html", visualizer=thing, url=url, editurl=editurl, surl=url_for('sharedVisualiser', _external=True))


        else:
            return render_template("visualizernotfound.html", visualizer=thing, valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))
            
    else:
        return render_template("visualizernotfound.html", visualizer=thing, valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))

@app.route("/s")
@app.route("/s/")
@app.route("/s/<key>/")
@app.route("/s/<key>")
@app.route("/s/<key>/<keytwo>/")
@app.route("/s/<key>/<keytwo>")
def sharedVisualiser(key=None, keytwo=None):

    if CREATEFAKEDB:
        global db

    if key == None:
        key = request.args.get("key")
    
    if key == None:
        return render_template("errors/notvalidkey.html", key="")

    if RUNSINREPLIT:
        
        if key in db.keys():
            # VALID KEY

            # checks for key 2

            if keytwo:
                
                if key + keytwo in db.keys():
                    typeofchart = db[key + keytwo]["type"]

                    # Checks what type of chart it is
                    if typeofchart == "bar":
                        # if it's a bar
                        data = db[key + keytwo]["data"]

                        # url sets in html file
                        url = key
                        editurl = keytwo

                        thing = typeofchart

                        values = data["values"]
                        labels = data["labels"]
                        label = data["label"]
                        
                        print(values)
                        print(labels)
                        print(label)
                        return render_template("visualizer_bar.html", visualizer=thing, url=url, editurl=editurl, labels=labels, values=values, label=label, surl=url_for('sharedVisualiser', _external=True))

                    elif typeofchart == "line":
                        data = db[key + keytwo]["data"]

                        # url sets in html file
                        url = key
                        editurl = keytwo

                        thing = typeofchart

                        values = data["values"]
                        labels = data["labels"]
                        label = data["label"]
                        tension = data["tension"]
                        
                        print(values)
                        print(labels)
                        print(label)
                        return render_template("visualizer_line.html", visualizer=thing, url=url, editurl=editurl, labels=labels, values=values, label=label, surl=url_for('sharedVisualiser', _external=True), tension=tension)

                    elif typeofchart == "pie":
                        data = db[key + keytwo]["data"]

                        # url sets in html file
                        url = key
                        editurl = keytwo

                        thing = typeofchart

                        values = data["values"]
                        labels = data["labels"]
                        label = data["label"]
                        
                        print(values)
                        print(labels)
                        print(label)
                        return render_template("visualizer_pie.html", visualizer=thing, url=url, editurl=editurl, labels=labels, values=values, label=label, surl=url_for('sharedVisualiser', _external=True))


                    elif typeofchart == "doughnut":
                        data = db[key + keytwo]["data"]

                        # url sets in html file
                        url = key
                        editurl = keytwo

                        thing = typeofchart

                        values = data["values"]
                        labels = data["labels"]
                        label = data["label"]
                        
                        print(values)
                        print(labels)
                        print(label)
                        return render_template("visualizer_pie.html", visualizer=thing, url=url, editurl=editurl, labels=labels, values=values, label=label, surl=url_for('sharedVisualiser', _external=True))


                    else:
                        #not a valid type
                        # so we delete it so it don't take space on the db
                        # because it's corrupt
                        # and unfixable

                        s = json.dumps(db[key + keytwo])

                        del db[key + keytwo]
                        del db[key]

                        return "<h1>Data was corrupt</h1><p>Please report this on this projects <a herf='https://github.com/VL07/All_Visualizer/issues'>Github</a> page</p><code>" + s + "</code>"


            else:
                # return only see version
                

                print(db[key]["data"]["values"])
                print(json.dumps(db[key]["data"]["values"]))
                if db[key]["type"] == "line":
                    return render_template("embed/embed.html", label=db[key]["data"]["label"], values=db[key]["data"]["values"], labels=db[key]["data"]["labels"], type=db[key]["type"], tension=db[key]["data"]["tension"])

                return render_template("embed/embed.html", label=db[key]["data"]["label"], values=db[key]["data"]["values"], labels=db[key]["data"]["labels"], type=db[key]["type"], tension=0)

        else:
            return render_template("errors/notvalidkey.html", key=key)

    else:
        return render_template("errors/notinreplit.html", replitURL=REPLITURL)

    return render_template("errors/notvalidkey.html", key=key)


@app.route("/saveToDb/<key>/<keytwo>/")
def saveToDb(key=None, keytwo=None):
    print("got save request")
    if CREATEFAKEDB:
        global db

    print(request.args.get("labels"))
    print(request.args.get("values"))
    print(request.args.get("label"))

    if request.args.get("labels") == "" or request.args.get("values") == "" or request.args.get("label") == "" or request.args.get("labels") == None or request.args.get("values") == None or request.args.get("label") == None:
        return "no data"


    labels = request.args.get("labels").split(",")
    values = request.args.get("values").split(",")
    label = request.args.get("label")

    if not key or not keytwo or not labels or not values or not label:
        return "error not enouth data"
    

    if not str(key + keytwo) in list(db.keys()):
        return "not valid keys"
    
    print(db[key]["type"])
    print(db[key]["data"])
    data = {"type": db[key]["type"], "data": {}}
    data2 = {"type": db[key]["type"], "data": {}}
    print(request.args.get("tension"))
    if db[key]["type"] == "line":
        tension = request.args.get("tension")
        print("saving line")
        if tension == "" or tension == None:
            print("error saving tension ")
            return "missing value tension"
        data["data"]["tension"] = tension
        data2["data"]["tension"] = tension

    print(labels)
    data["data"]["labels"] = labels
    print(data["data"]["labels"])
    print(data["data"])
    data["data"]["values"] = values
    data["data"]["label"] = label

    
    data2["data"]["labels"] = labels
    data2["data"]["values"] = values
    data2["data"]["label"] = label

    db[key] = data
    db[key + keytwo] = data2

    print("saved to db")
    print(type(db[key]))


    return "success"

@app.route("/visualizer")
@app.route("/visualizer/")
def vislist():
    return render_template("visualizernotfound.html", visualizer="", valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))


@app.route("/help")
@app.route("/help/")
def help():
    return render_template("help.html")

@app.route("/embed")
@app.route("/embed/")
@app.route("/embed/<data>")
@app.route("/embed/<data>/")
def embed(data=""):

    return redirect(url_for("/"))
    
    if not data:
        data = request.args.get("data")
    
    if not data:
        return render_template("embed/embed_error.html")

    return render_template("embed/embed.html", data=json.parse(data))

@app.route("/github")
@app.route("/github/")
@app.route("/source")
@app.route("/source/")
@app.route("/github/<page>")
@app.route("/source/<page>")
@app.route("/github/<page>/")
@app.route("/source/<page>/")
def source(page=""):
    if not page:
        page = request.args.get("page")
    
    if not page:
        return redirect("https://github.com/VL07/All_Visualizer")

    return redirect("https://github.com/VL07/All_Visualizer/" + page)

@app.route("/wiki")
@app.route("/wiki/")
def wiki():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

