from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

visualizers = {"text": "Text", "graf": "Graf", "bar": "Bar"}

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/visualizer/<thing>/")
@app.route("/visualizer/<thing>")
def visualizer(thing):
    if thing in visualizers.keys():
        if thing == "bar":
            return render_template("visualizer_bar.html", visualizer=thing)
        else:
            return render_template("visualizernotfound.html", visualizer=thing, valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))
            
    else:
        return render_template("visualizernotfound.html", visualizer=thing, valid=list(visualizers.values()), links=list(visualizers.keys()), len=len(visualizers))
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

