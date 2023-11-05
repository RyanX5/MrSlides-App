from flask import Flask, render_template, redirect
import slides
import audio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/record')
def auth():
    
    audio_obj = audio.audio()
    result = audio_obj.process()
    slide = slides.slides()
    result = slide.main()
    if result == "DONE":
        return redirect("/done")

    

@app.route('/login')
def log():
    return render_template("main.html")

@app.route('/done')
def done():
    return render_template("done.html")

@app.route('/process')
def process():
    
    return render_template("processing.html")



if __name__ == '__main__':
    app.run(debug=True)
