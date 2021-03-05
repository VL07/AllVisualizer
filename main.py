from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

visualizers = {"text": "Text", "graf": "Graf"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/visualizer/<thing>")
def visualizer(thing):
    if thing in visualizers.keys():
        return render_template("visualizer.html", visualizer=thing)
    else:
        return render_template("visualizernotfound.html", visualizer=thing, valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))

@app.route("/visualizer/")
def vislist():
    return render_template("visualizernotfound.html", visualizer="", valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))

if __name__ == "__main__":
    app.run()

