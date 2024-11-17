from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 7,
        "location": "Marikina",
        "restaurant_name": "Restaurant Seven",
        "status": "Closed",
        "image_url": "https://mk.ca/wp-content/uploads/2024/09/Lacuisine_resto.jpg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },{
        "id": 8,
        "location": "Taguig",
        "restaurant_name": "Restaurant Eight",
        "status": "Open",
        "image_url": "https://smakmagasinet.no/contentassets/64d930c6bbcf49299b6074bf69aac03b/sjoogfloyd-floyd-smak-100221-merci-003-kopi.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 9,
        "location": "Pangasinan",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://www.visittelemark.com/dmsimgs/Terrasse_Merci_2113521831.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 10,
        "location": "Rizal",
        "restaurant_name": "Restaurant Ten",
        "status": "Open",
        "image_url": "https://resizer.otstatic.com/v2/photos/wide-huge/1/69846259.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 11,
        "location": "Cavite",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://d2w1ef2ao9g8r9.cloudfront.net/otl-images/_1600x900_crop_center-center_82_line/Owning-a-Restaurant-Hero-Image-1.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },{
        "id": 12,
        "location": "Laguna",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": "https://www.falconinterior.com/wp-content/uploads/elementor/thumbs/Interior--q99auaxcn3wyk4ui92tlxfn8ilbutnppe1k73loc08.webp?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 13,
        "location": "Batangas",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Closed",
        "image_url": "https://toohotel.com/wp-content/uploads/2022/09/TOO_restaurant_Panoramique_vue_Paris_Seine_Tour_Eiffel_2.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 14,
        "location": "Quezon",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://www.palms.com/sites/default/files/styles/coh_x_large/public/2023-06/VetriCucina-01-1-scaled.jpg?itok=iguHrtbT?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 15,
        "location": "Mindoro",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://cdn.prod.website-files.com/61bcac7b8c69b74b8d5c2b99/654a38bfe3bf7526c162fce0_2%20(15).png?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 16,
        "location": "Aklan",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://media.admiddleeast.com/photos/66a8cd5c062b8b3a02f9430c/16:9/w_2560%2Cc_limit/abu-dhabi-broadway-interior-seating.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 17,
        "location": "Marinduque",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": "https://www.sftravel.com/sites/default/files/styles/hero/public/2024-10/the-vault-garden-downtown.jpg.webp?itok=k4kNQHN9?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 18,
        "location": "Romblon",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://hotelsabovepar.com/wp-content/uploads/2024/07/image-38-2-1024x683.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 19,
        "location": "Palawan",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Closed",
        "image_url": "https://media.cntraveler.com/photos/5b4e39adacc7ce737600877d/master/pass/Del-Mar_2018_Del-Mar-Veranda-.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 20,
        "location": "Isabela",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://cdn-ilanhlf.nitrocdn.com/AzmJrPQohnwWLiYOIRijiymirQDdSgxs/assets/images/optimized/rev-b048aa6/theluxuryeditor.com/wp-content/uploads/2022/12/BlythswoodSquare_Restaurant_BoBirdy_B_SHOT-11_0020_MASTER_F1-1-scaled-1.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 21,
        "location": "Baguio",
        "restaurant_name": "Restaurant Twenty-one",
        "status": "Closed",
        "image_url": "https://www.thetimes.com/imageserver/image/%2Fmethode%2Ftimes%2Fprod%2Fweb%2Fbin%2F7752f990-c56f-11e8-a4a5-a34bea2c1d04.jpg?crop=3176%2C2117%2C0%2C0?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 22,
        "location": "Benguet",
        "restaurant_name": "Restaurant Twenty-two",
        "status": "Open",
        "image_url": "https://resizer.otstatic.com/v2/photos/wide-huge/3/52402153.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 23,
        "location": "Abra",
        "restaurant_name": "Restaurant Twenty-three",
        "status": "Closed",
        "image_url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cmVzdGF1cmFudHxlbnwwfHwwfHx8MA%3D%3D?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 24,
        "location": "Kalinga",
        "restaurant_name": "Restaurant Twenty-four",
        "status": "Open",
        "image_url": "https://daddysdeals.co.za/wp-content/uploads/2023/01/Parkhurst-Restaurants-.jpeg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 25,
        "location": "Antique",
        "restaurant_name": "Restaurant Twenty-five",
        "status": "Closed",
        "image_url": "https://a.storyblok.com/f/116532/1620x1080/ff80c38cfc/level-6-miami.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 26,
        "location": "Zamboanga",
        "restaurant_name": "Restaurant Twenty-six",
        "status": "Open",
        "image_url": "https://publish.purewow.net/wp-content/uploads/sites/2/2024/03/outdoor-restaurants-los-angeles-bar-funke-1272.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 27,
        "location": "Cagayan",
        "restaurant_name": "Restaurant Twenty-seven",
        "status": "Closed",
        "image_url": "https://www.thebayleaf.com.ph/wp-content/uploads/static/intramuros-restaurants-image.webp?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 28,
        "location": "Catanduanes",
        "restaurant_name": "Restaurant Twenty-eight",
        "status": "Open",
        "image_url": "https://www.southernliving.com/thmb/0kV1QqG1sVtlXzXMQ20k23hj8eg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/68ab14_944f9f7baf264e35bbf248a73f33cd92mv2-e31ed149670045ac9224fa66446d8dbd.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 29,
        "location": "Nueva Ecija",
        "restaurant_name": "Restaurant Twenty-nine",
        "status": "Closed",
        "image_url": "https://images.squarespace-cdn.com/content/v1/5f9decf1e529e27a4705d448/1681676661420-MZGRIQXRH7H87EH70AB9/MacBook+Pro+-+22banner-17.png?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 30,
        "location": "Nueva Vizcaya",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://www.jdesigngroup.com/wp-content/uploads/2013/12/bigstock-Luxury-Restaurant-In-European-52461799-1.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 31,
        "location": "Batanes",
        "restaurant_name": "Restaurant Thirty-one",
        "status": "Closed",
        "image_url": "https://lebua.com/wp-content/uploads/2019/04/44-Breeze-Angle-2-1-scaled.jpg?auto=compress&cs=tinysrgb&w=600"
    }, {
        "id": 32,
        "location": "Jolo",
        "restaurant_name": "Restaurant Thirty-two",
        "status": "Open",
        "image_url": "https://thevenuesco.au/wp-content/uploads/2023/01/HBFSF16-1.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 33,
        "location": "Sulu",
        "restaurant_name": "Restaurant Thirty-three",
        "status": "Closed",
        "image_url": "https://www.herenhuis-izegem.be/media/pages/restaurant/3ae549c22d-1666274054/restaurant-1.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 34,
        "location": "Cotabato",
        "restaurant_name": "Restaurant Thirty-four",
        "status": "Open",
        "image_url": "https://images2.alphacoders.com/862/862730.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 35,
        "location": "Bicol",
        "restaurant_name": "Restaurant Thirty-five",
        "status": "Closed",
        "image_url": "https://thelibrary.mgmresorts.com/transform/2PLXswLImUz1/Bellagio-Spago-Patio-Sunset-Crop?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 36,
        "location": "Bohol",
        "restaurant_name": "Restaurant Thirty-six",
        "status": "Open",
        "image_url": "https://hips.hearstapps.com/hmg-prod/images/alchemist-copenhagen-1638394487.png?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 37,
        "location": "Cebu",
        "restaurant_name": "Restaurant Thirty-seven",
        "status": "Closed",
        "image_url": "https://www.toureiffel.paris/sites/default/files/styles/mobile_450_762/public/2023-01/jv_carousel5.jpg?itok=MOIgYN19?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 38,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Thirty-eight",
        "status": "Open",
        "image_url": "https://assets.architecturaldigest.in/photos/657afa3128c355874538a538/16:9/w_2560%2Cc_limit/13%2520(1).jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 39,
        "location": "Masbate",
        "restaurant_name": "Restaurant Thirty-nine",
        "status": "Closed",
        "image_url": "https://noburestaurants.com/assets/New-Orleans/Nobu-New-Orleans-Dining-Pod-2200-x-1100.webp?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 40,
        "location": "Davao",
        "restaurant_name": "Restaurant Fourty",
        "status": "Open",
        "image_url": "https://studioasa.in/wp-content/uploads/2022/01/0_jVseNFhhSAn_id5a.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 41,
        "location": "Siargao",
        "restaurant_name": "Restaurant Fourty-one",
        "status": "Closed",
        "image_url": "https://www.upmenu.com/wp-content/uploads/2022/08/Small-Cafe-Interior-Design.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 42,
        "location": "Zambales",
        "restaurant_name": "Restaurant Fourty-two",
        "status": "Open",
        "image_url": "https://impeccabuild.com.au/wp-content/uploads/2020/10/Inexpensive-Restaurant-Design-Ideas-Restaurant-Fitouts-ImpeccaBuild-12-scaled.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 43,
        "location": "Bulacan",
        "restaurant_name": "Restaurant Fourty-three",
        "status": "Closed",
        "image_url": "https://www.southernliving.com/thmb/yuWnWu5msq32Gutv6MtF7A0rOy8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Screenshot2024-05-06at12.25.45PM-3bc1e12e2b03442eb8ef56a742e33ac4.png?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 44,
        "location": "Albay",
        "restaurant_name": "Restaurant Fourty-four",
        "status": "Open",
        "image_url": "https://static.wanderon.in/wp-content/uploads/2024/01/ryu-rooftop-1-min-1600x900-1.webp?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 45,
        "location": "Leyte",
        "restaurant_name": "Restaurant Fourty-five",
        "status": "Closed",
        "image_url": "https://quark-studio.com/wp-content/uploads/2019/07/DijlahVillage-47.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 46,
        "location": "Samar",
        "restaurant_name": "Restaurant Fourty-six",
        "status": "Open",
        "image_url": "https://quark-studio.com/wp-content/uploads/2019/07/DijlahVillage-32.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 47,
        "location": "Puerto Princesa",
        "restaurant_name": "Restaurant Fourty-seven",
        "status": "Closed",
        "image_url": "https://mir-s3-cdn-cf.behance.net/project_modules/1400/00a5de30604091.562a50137bd81.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 48,
        "location": "Capiz",
        "restaurant_name": "Restaurant Fourty-eight",
        "status": "Open",
        "image_url": "https://b.zmtcdn.com/data/pictures/8/21221268/4b45133d799fdc119626a7787daa0194.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 49,
        "location": "Vigan",
        "restaurant_name": "Restaurant Fourty-nine",
        "status": "Closed",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Barbieri_-_ViaSophia25668.jpg/1200px-Barbieri_-_ViaSophia25668.jpg?auto=compress&cs=tinysrgb&w=600"
    },{
        "id": 50,
        "location": "Cainta",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://images-luxe.outlookindia.com/2024/09/26055054/The-Sactuary-Outdoor.jpg?auto=compress&cs=tinysrgb&w=600"
    },
]



@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)