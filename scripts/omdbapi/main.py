import omdb

def movie_info(movie):
    try:
        a = omdb.get(title=movie[0], year=movie[1])
        print(a["country"])
    except:
        print("An exception occurred")

omdb.set_default('apikey', "5fe52aac")

movie_list = [
    ["Shutter Island","2010"],
    ["Inception","2010"],
    ["Gone Girl","2014"]
]

for movie in movie_list:
    movie_info(movie)