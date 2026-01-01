from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-video")
def get_video():
    return '''
            <video autoplay muted loop playsinline class="absolute inset-0 w-full h-full object-cover opacity-100 transition-opacity duration-500 z-0">
                <source src="/static/assets/joaolive.MOV" type="video/mp4">
            </video>
        '''

if __name__ == "__main__":
    app.run(debug=True)