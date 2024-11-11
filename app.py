from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello_aaron():

    blessings = [
        "May your cup overflow with joy unending",
        "May the Lord bless your journey with light and peace",
        "May your days be filled with the strength of the Almighty",
        "May the good Lord grant you wisdom beyond measure",
        "May your home be a haven of love and laughter",
        "May your faith move mountains in the face of trials",
        "May your soul find rest in the arms of the Savior",
        "May the light of His mercy guide your path",
        "May the Lord bless your hands to prosper in all you do",
        "May you find comfort in the shadow of His wings",
        "May the Lord bless you with a heart full of gratitude",
        "May His grace cover you like a river overflowing",
        "May your prayers be like incense rising to heaven",
        "May you stand firm on the rock of His promises",
        "May the Lord grant you peace that surpasses understanding",
        "May your spirit be refreshed like a garden in spring rain",
        "May you always walk in the favor of the Lord",
        "May you have strength like the eagle and patience like the saints",
        "May the Lord bless you with dreams that soar and visions that prevail",
        "May your days be bathed in the glow of His goodness",
        "May the Lord anoint your steps and direct your path",
        "May His love be the anchor in every storm",
        "May you be blessed with faith as strong as the cedar",
        "May your heart sing with the joy of His salvation",
        "May the Lord make His face shine upon you always",
        "May your spirit be nourished by His living word",
        "May His blessings flow to your children and their children",
        "May you be rooted and grounded in His love",
        "May your heart be steadfast, trusting in the Lord",
        "May you be blessed with a double portion of His favor",
        "May you walk in the spirit and not grow weary",
        "May the Lord bless you with the peace of green pastures",
        "May the Lord's mercy be new every morning in your life",
        "May your soul rejoice in His goodness all your days",
        "May you find rest in the shadow of the Almighty",
        "May your faith be a beacon in times of darkness",
        "May you be blessed with a harvest of righteousness",
        "May the Lord be your fortress and your shield",
        "May your heart be still and know that He is God",
        "May you be clothed with the garment of praise",
        "May His word be a lamp to your feet and a light to your path",
        "May you be blessed with eyes to see and ears to hear His will",
        "May the Lord's grace be sufficient in every season",
        "May your spirit be lifted on wings of worship",
        "May the Lord's blessings chase you down and overtake you",
        "May the love of God surround you like a mighty fortress",
        "May you dwell in the secret place of the Most High",
        "May you be blessed with the courage of David and the wisdom of Solomon",
        "May your heart overflow with the joy of His presence",
        "May His faithfulness sustain you through every trial",
        "Strong you are, but patience you must have",
        "Only you can prevent the wildfires of the soul",
        "Wisdom comes, when still you are",
        "May you find peace like a quiet forest grove",
        "Trust the Force, you must, and peace you shall find",
        "Mind your steps, the path is narrow but true",
        "Deep roots, you must grow, to weather the storm",
        "In the stillness, the answers you seek will come",
        "Protect the flame of your spirit, for only you can",
        "May the forest guide you to the still waters of wisdom"
    ]
    
    images = [
        "https://drx-danwins.us-east-1.linodeobjects.com/drx-danwins/new_file11112024_51_47aaron.png",
        "https://drx-danwins.us-east-1.linodeobjects.com/drx-danwins/new_file11112024_40_33aaron4.png",
        "https://drx-danwins.us-east-1.linodeobjects.com/drx-danwins/new_file11112024_40_42aaron2.png"
    ]

    image = random.choice(images)

    blessing = random.choice(blessings)

    return render_template("index.html", blessing=blessing, image=image)

