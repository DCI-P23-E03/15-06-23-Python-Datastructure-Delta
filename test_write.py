database = {
    "Germany": {
        "Information": "Rich history, vibrant cities, and a cool climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "Japan": {
        "Information": "A blend of tradition and modernity with pleasant temperatures",
        "Climate": 4,
        "Price": 3,
        "Safety": 4
    },
    "Australia": {
        "Information": "Stunning landscapes, diverse wildlife, and a sunny climate",
        "Climate": 5,
        "Price": 5,
        "Safety": 5
    },
    "Canada": {
        "Information": "Breathtaking nature, friendly locals, and a cold climate",
        "Climate": 2,
        "Price": 4,
        "Safety": 4
    },
    "Italy": {
        "Information": "Art, culture, and delicious cuisine with a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 3
    },
    "Brazil": {
        "Information": "Beautiful beaches, vibrant festivals, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Thailand": {
        "Information": "Exotic temples, stunning islands, and a hot climate",
        "Climate": 4,
        "Price": 2,
        "Safety": 3
    },
    "South Africa": {
        "Information": "Safari adventures, diverse landscapes, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "United States": {
        "Information": "Iconic cities, natural wonders, and a cold climate",
        "Climate": 2,
        "Price": 4,
        "Safety": 4
    },
    "France": {
        "Information": "Romantic atmosphere, world-class cuisine, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "China": {
        "Information": "Great Wall, ancient history, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 3
    },
    "India": {
        "Information": "Rich culture, diverse traditions, and a hot climate",
        "Climate": 5,
        "Price": 1,
        "Safety": 2
    },
    "Egypt": {
        "Information": "Ancient pyramids, Nile River, and a hot climate",
        "Climate": 5,
        "Price": 2,
        "Safety": 3
    },
    "Mexico": {
        "Information": "Colorful culture, stunning beaches, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Russia": {
        "Information": "Vast landscapes, rich history, and a cold climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "United Kingdom": {
        "Information": "Historic landmarks, charming villages, and a cold climate",
        "Climate": 2,
        "Price": 3,
        "Safety": 4
    },
    "Greece": {
        "Information": "Mythology, picturesque islands, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Turkey": {
        "Information": "Cultural heritage, stunning coastlines, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 3
    },
    "Argentina": {
        "Information": "Tango, Patagonia, and a varied climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 3
    },
    "New Zealand": {
        "Information": "Adventure sports, breathtaking landscapes, and a moderate climate",
        "Climate": 3,
        "Price": 4,
        "Safety": 4
    },
    "Malaysia": {
        "Information": "Rainforests, stunning beaches, and a hot climate",
        "Climate": 4,
        "Price": 2,
        "Safety": 3
    },
    "Sweden": {
        "Information": "Scenic beauty, cultural heritage, and a cold climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 4
    },
    "Spain": {
        "Information": "Vibrant festivals, beautiful beaches, and a hot climate",
        "Climate": 4,
        "Price": 3,
        "Safety": 4
    },
    "South Korea": {
        "Information": "K-pop, traditional palaces, and a moderate climate",
        "Climate": 3,
        "Price": 3,
        "Safety": 4
    },
    "Seychelles": {
        "Information": "Idyllic beaches, turquoise waters, and diverse marine life",
        "Climate": 5,
        "Price": 4,
        "Safety": 4
    }
}

with open("database.txt","wt") as f:
   string=""
   for i,j in database.items():
      
      string+=i+"\n\t"
      for k in j.values():
         string+=str(k)+"\n\t"
      string+="\n"
      
      #print(type(i),type(j),"\n")  
   f.write(string)
   #print(readcontent)
