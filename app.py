from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "madlibsstuff"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """creates prompt form as homepage"""
    prompts = story.prompts
    return render_template('homepage.html', prompts=prompts)

@app.route('/my-story')
def get_story():
    """generates story with answers provided in form"""
    text = story.generate(request.args)
    return render_template('story.html', text=text)