from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

data = {
    "1": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "id": 1,
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "2": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "id": 2,
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "3": {
        "title": "It's not about Russia. It's about Putin",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "The Weeds",
        "id": 3,
        "date": "02/27/2022",
        "url": "https://open.spotify.com/episode/4MDiImcnFuE8xbOdmjoB7L?go=1&sp_cid=50e62089aedddad9df281fa05b647427&utm_source=embed_player_p&utm_medium=desktop&nd=1",
        "recent_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    }
}

# ROUTES

def search_data(term):
    results = []
    for (key, item) in data.items():
        if term in item["title"]:
            results.append(item)
    return results

@app.route('/')
def home():
    display = [data["1"], data["2"], data["3"]]
   # print(display)
    return render_template('home.html', data=display)

@app.route('/detail/<id>')
def detail(id=None):
    item = data[id]
    return render_template("detail.html", data=item)

@app.route('/search/<term>')
def search(term: None):
    results = search_data(term)
    print(results)
    return render_template('search.html', data=results, search=term)

if __name__ == '__main__':
    app.run(debug = True)
