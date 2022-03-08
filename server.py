from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "1": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "2": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "3": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    }
}

# ROUTES

@app.route('/')
def home():
    display = [data["1"], data["2"], data["3"]]
    print(display)
    return render_template('home.html', data=display)

@app.route('/detail/<id>')
def detail(id=None):
    item = data[id]
    return render_template("detail.html", data=item)

@app.route('/search/<term>')
def search(term: None):
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug = True)
