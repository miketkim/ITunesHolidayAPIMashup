import requests, json, pprint
import unittest


CACHE_FNAME = 'cache.txt'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def getWithCaching(Holiday):
    BASE_URL = 'https://itunes.apple.com/search'
    # full_url = requestURL(BASE_URL, params={'term': Holiday, 'media': 'music', 'entity': 'song'})
    full_url = requestURL(BASE_URL, params={'term': Holiday, 'media': 'movie'})
    if full_url in CACHE_DICTION:
        print 'using cache'
        # use stored response
        response_text = CACHE_DICTION[full_url]
    else:
        print 'fetching'
        # do the work of calling the API
        response = requests.get(full_url)
        # store the response
        CACHE_DICTION[full_url] = response.text
        response_text = response.text

        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()
    return response_text
def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url


try:
    cache_file = open("holidayapi.txt", 'r')
    CACHE_DICTION = json.loads(cache("US"))
    cache_file.write(json.dumps(CACHE_DICTION))
    cache_file.close()
except:
    CACHE_DICTION = {}

def cache(country):
    baseurl= "https://holidayapi.com/v1/holidays?"
    params={'key' : '3332fa9e-1d89-458e-a44d-3f867f8879ed', 'country' : country, 'year' : '2015',  'month' : '12', 'public' : True}
    holiday= requestURL(baseurl, params=params)
    data = requests.get(holiday)
    new_text = data.text
    return new_text
    # holiday1= json.loads(holiday.text)
    if holiday in CACHE_DICTION:
        print 'working'
        # use stored response
        new_text= CACHE_DICTION[holiday]
    else:
        print 'other method'
        # do the work of calling the API
        response = requests.get(holiday)
        # store the response
        CACHE_DICTION[holiday] = response.text
        new_text = response.text

        cache_file = open(CACHE_LNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()
    return new_text




def GetaDecemberHoliday(year):
    files = open("holidayapi.txt", 'r')
    jsons = json.load(files)
    datakeys= jsons.values()[1][0]["name"]
    datakeys1=jsons.values()[1][1]['name']
    b= str(datakeys)
    c =str(datakeys1)
    if year > 0:
        return b + "      " + c

print GetaDecemberHoliday(int(raw_input("Enter a year: ")))

def GetMovies(holiday):
    myfile = open("cache.txt",'r')
    myjson = json.load(myfile) 
    datakeys = json.loads(myjson[myjson.keys()[0]]).keys()
    lst=[]
    for movie in json.loads(myjson[myjson.keys()[0]])[datakeys[1]]:
        if holiday in movie['longDescription']:
            lst.append(movie["trackName"])
    return lst
x= GetMovies(raw_input("Type in Christmas to see a list of movies about it:  "))
print x

def shortestDescriptionsFirst(movie):
    myfile = open("cache.txt",'r')
    myjson = json.load(myfile) 
    datakeys = json.loads(myjson[myjson.keys()[0]]).keys()
    for x in json.loads(myjson[myjson.keys()[0]])[datakeys[1]]:
        if movie in x["trackName"]: 
            return len(x['longDescription'])
            
newlist= sorted(x, reverse= True, key= shortestDescriptionsFirst)
print newlist


class Holiday():
    def __init__(self, movie, country, cost):
        """User must choose between the two holidays: Christmas and New Year's Eve."""
        self.movie = movie  
        self.country = country
        self.cost = cost 
    def __str__(self):
         return "You are choosing the movie {} which is from the {} and you want to pay a maximum of ${}".format(self.movie, self.country, self.cost)

    def getGenre(self):
        myfile = open("cache.txt",'r')
        myjson = json.load(myfile) 
        datakeys = json.loads(myjson[myjson.keys()[0]]).keys()
        for movie in json.loads(myjson[myjson.keys()[0]])[datakeys[1]]:
            if self.movie in movie["trackName"]: 
                return str(movie['primaryGenreName'])
        
    def getPrice(self):
        myfile = open("cache.txt",'r')
        myjson = json.load(myfile) 
        datakeys = json.loads(myjson[myjson.keys()[0]]).keys()     
        for movie in json.loads(myjson[myjson.keys()[0]])[datakeys[1]]:
            if self.cost > movie["trackPrice"]:
                return (self.movie, movie['trackPrice'])
            else:
                return "This movie is too expensive! Try another movie."
    


blah= Holiday("Elf (2003)", "USA", 5.00)
print blah


genre = blah.getGenre()
print genre


price = blah.getPrice()
print price





class Problem1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(type(x), type([]))
    def test_2(self):
        self.assertEqual(len(newlist), 24)
    def test_3(self):
        self.assertEqual(type(cache_file), file)
    def test_4(self):
        self.assertEqual(type(genre), type(""))
    def test_5(self):
        self.assertEqual(type(newlist), type([]))
    def test_6(self):
        self.assertEqual(type(CACHE_FNAME), str)

unittest.main(verbosity=2) # Run all the tests in this file, with info about why they're failing







