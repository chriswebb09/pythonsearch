from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

data = {
    "1": {
        "title": "In Moscow's Shadows 60: Ukraine: Nuclear Options, National Morale, and How Kyiv Can Save Moscow",
        "description": "What can one say about the unfolding horror in Ukraine. In this podcast I alight on a few specific issues: Putin's nuclear signalling (at least I hope that's all it is), the idiocy of 'No Fly Zones' in this context, Russian morale, and how, if Putin is re-booting the Brezhnev franchise, this could in the long-term let Russia finally complete its reform process.",
        "podcast_name": "In Moscow's Shadows",
        "id": 1,
        "date": "02/27/2022",
        "url": "https://www.buzzsprout.com/1026985/10152168-in-moscow-s-shadows-60-ukraine-nuclear-options-national-morale-and-how-kyiv-can-save-moscow.mp3",
        "related_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "2": {
        "title": "What Putin Wants",
        "description": "Russia's newly-belligerent stance has rocked the democratic West on its heels, from the annexation of the Crimea to the sponsoring of extremist digital disinformation to - almost certainly - the stacking of elections in the US and UK. And it all stems from the paranoid, Machiavellian, espionage-steeped mindset of one man: Vladimir Putin. On this edition, Arthur talks to exiled journalists, foreign correspondents including Luke Harding of The Guardian and Russia analysts to unpick the question that baffles even Russians themselves: What does Putin want? Пожалуйста, наслаждайтесь нашим подкастом. Спасибо! 'There was no liberal Putin. There was no white album.'- LUKE HARDING 'Russia is the world champion at national suicide. It's a deeply, deeply self-destructive country.' - PETER POMERANTSEV 'Putin doesn't even see Ukraine as a country… They think, this was always ours, what is the US doing interfering?' - ARTYOM LISS 'The plan is to make Russia great again… Neither London nor Washington nor Paris has come up with an adequate way to deal with him.' - LUKE HARDING",
        "podcast_name": "Doomsday Watch with Arthur Snell",
        "id": 2,
        "date": "11/23/2021",
        "url": "https://traffic.megaphone.fm/PMO1944155127.mp3?updated=1637063647",
        "related_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    },
    "3": {
        "title": "It's not about Russia. It's about Putin",
        "description": "Since December, the biggest question facing foreign policymakers in the US and Europe has been as simple as it has been hard to really believe: Is Russia going to invade Ukraine? Russian President Vladimir Putin has ordered massive numbers of troops, tanks, artillery, and more to the border with Ukraine, as well as in Crimea (a region that Russia seized from Ukraine in 2014) and in Belarus (a close ally of Russia and northern neighbor of Ukraine). He has also issued demands that Ukraine not be admitted into NATO, and that NATO not deploy forces to member states close to Russia like Poland and the Baltic states. These are bold demands that some view as designed for Ukraine and the West to reject, allowing Putin to claim that diplomacy has failed and an invasion is necessary. For the moment, though, diplomatic efforts between the US, EU members, Ukraine, and Russia continue, and some experts are more optimistic that the situation can resolve without what could be Europe's first major land war in decades. One of them is Mark Galeotti, director of Mayak Intelligence, a professor at University College London, and an expert on Russian security affairs. We spoke on Zoom recently for an episode of Vox’s podcast The Weeds. A transcript, heavily truncated and edited for length and clarity, follows.",
        "podcast_name": "The Weeds",
        "id": 3,
        "date": "02/6/2022",
        "url": "https://www.podtrac.com/pts/redirect.mp3/pdst.fm/e/chtbl.com/track/524GE/traffic.megaphone.fm/VMP8280337054.mp3",
        "related_episodes": ["https://www.buzzsprout.com/1026985/10107958-in-moscow-s-shadows-59-imagining-a-ukrainian-peace-deal", "https://www.buzzsprout.com/1026985/10070465-in-moscow-s-shadows-58-ukrainian-thoughts-welcome-to-stagnation-and-more-2022-predictions"]
    }
}

# ROUTES

def search_data(term):
    results = []
    for (key, item) in data.items():
        title = item["title"].lower()
        title = re.sub('[!,*)@#%(&$_?.^]', '', title)
        print(title)
        print(term)
        if term in title:
            results.append(item)
    return results

@app.route('/')
def home():
    display = [data["1"], data["2"], data["3"]]
    return render_template('home.html', data=display)

@app.route('/detail/<id>')
def detail(id=None):
    item = data[id]
    return render_template("detail.html", data=item)

@app.route('/search/<term>')
def search(term: None):
    term = re.sub('[!,*)@#%(&$_?.^]', '', term)
    results = search_data(term)
    print(results)
    return render_template('search.html', data=results, search=term)

if __name__ == '__main__':
    app.run(debug = True)
