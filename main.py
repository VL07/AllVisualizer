from flask import Flask, redirect, render_template, url_for, request
import random
import string
import json

app = Flask(__name__)

visualizers = {"text": "Text", "graf": "Graf", "bar": "Bar"}

# URL IMPORTANT
URL = "http://127.0.0.1:5001"
# SET TO TRUE IF IN REPLIT.COM (OR REPL.IT) IMPORTANT
RUNSINREPLIT = False
# Replit project url
REPLITURL = "#"

def randomUniceKey(l=8):
    if RUNSINREPLIT:
        # ADD DATABASE FOR REPLIT
        pass
    else:
        s = ''.join(random.choice(string.ascii_letters + str(string.digits)) for i in range(l))
        return s

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/visualizer/<thing>/")
@app.route("/visualizer/<thing>")
def visualizer(thing):
    if thing in visualizers.keys():
        if thing == "bar":
            return render_template("visualizer_bar.html", visualizer=thing, url=URL+"/"+randomUniceKey()+"/")
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
                        pass
                    else:
                        #not a valid type
                        # so we delete it so it don't take space on the db
                        # because it's corrupt
                        # and unfixable

                        del db[key + keytwo]
                        del db[key]

                        return "<h1>Data was corrupt</h1><p>Please report this on this projects <a herf='https://github.com/VL07/All_Visualizer/issues'>Github</a> page</p><code>" + json.dumps(db[key + keytwo]) + "</code>"


            else:
                # return only see version
                
                return render_template("embed/embed.html", data=json.dumps(db[key]))

        else:
            return render_template("errors/notvalidkey.html", key=key)

    else:
        return render_template("errors/notinreplit.html", replitURL=REPLITURL)

    return render_template("errors/notvalidkey.html", key=key)


@app.route("/visualizer")
@app.route("/visualizer/")
def vislist():
    return render_template("visualizernotfound.html", visualizer="", valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))


@app.route("/help")
@app.route("/help/")
def help():
    return "<h1>Under construction</h1>"

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
    return redirect("https://github.com/VL07/All_Visualizer/wiki")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001")

