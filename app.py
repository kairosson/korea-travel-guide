from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/day-trip")
def day_trip():
    return render_template("day_trip.html")


@app.route("/gangneung-2d1n")
def gangneung_2d1n():
    return render_template("gangneung_2d1n.html")


@app.route("/sokcho-2d1n")
def sokcho_2d1n():
    return render_template("sokcho_2d1n.html")


@app.route("/3-days")
def full_3d2n():
    return render_template("full_3d2n.html")


@app.route("/culture/abai-village")
def abai_village():
    return render_template("abai_village.html")


@app.route("/culture/ojukheon")
def ojukheon():
    return render_template("ojukheon.html")


@app.route("/food")
def food_guide():
    return render_template("food_guide.html")


@app.route("/seoraksan")
def seoraksan():
    return render_template("seoraksan.html")


@app.route("/stories")
def stories():
    return render_template("stories.html")


# ---- Busan (second region) ----

@app.route("/busan")
def busan_index():
    return render_template("busan/busan_index.html")


@app.route("/busan/day-trip")
def busan_day_trip():
    return render_template("busan/busan_day_trip.html")


@app.route("/busan/2d1n")
def busan_2d1n():
    return render_template("busan/busan_2d1n.html")


@app.route("/busan/culture")
def busan_culture():
    return render_template("busan/busan_culture.html")


@app.route("/busan/food")
def busan_food():
    return render_template("busan/busan_food.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
