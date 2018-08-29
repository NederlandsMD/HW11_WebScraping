from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_and_beyond = mongo.db.collection.find()
    return render_template("index.html", marsdata = mars_and_beyond)

@app.route("/scrape")
def mars_scraper():
    mongo.db.collection.remove({})

    mars_data = scrape_mars.scrape()

    # news_title, news_p, featured_image_url, mars_weather, df, Mars_Hem

    news = {'news_title': mars_data[0],
            'news_lede': mars_data[1]}
    mongo.db.collection.insert_one(news)

    img = {"feat_img": mars_data[2]}
    mongo.db.collection.insert_one(img)

    weather = {"current_weather": mars_data[3]}
    mongo.db.collection.insert_one(weather)
    
    table = {"Mars_table": mars_data[4]}
    mongo.db.collection.insert_one(table)

    hemispheres = {"Mars_Hemispheres": mars_data[5]}
    mongo.db.collection.insert_one(hemispheres)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True) 
