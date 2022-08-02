# import necessary libraries
from bs4 import BeautifulSoup as bs
import requests
import re
import pickle




move_dict = {}
pokem_dict = {}

# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)
    # response will be provided in JSON format
    return response.text

# assign required credentials
# assign URL
url_to_scrape = "https://pokemondb.net/move/all"
# create document
html_document = getHTMLdocument(url_to_scrape)
# create soap object
soup = bs(html_document, 'html.parser')
# find all the anchor tags with "ent-name" 
# attribute starting with "/move/(whatevermove)"

for link in soup.find_all('a',
                            attrs={'href': re.compile("/move/")}):
    # display the actual urls?????????
    links = (link.get('href'))
    listOfLinks =( "https://pokemondb.net" + links)
    ##print(listOfLinks)
  
    # load webpage content
    r = requests.get(listOfLinks)

    #convert to a bsoup object
    soup = bs(r.content)
    #print html
    #print(soup)
    #searchs page for the body stuff
    body = soup.find('body')
    #searchs the body for examples of the a tag with the class ent-name. This gives us the names of hte pokemon that can learn the move
    pokeNames = body.find_all('a', {'class':'ent-name'})

    if pokeNames == []: continue
    move_name = links[6:]
    print(move_name)

    move_dict[move_name] = set()

    for title in pokeNames:
        # the_end = (links[6:] + " " + title.text)
        move_dict[move_name].add(title.text)

        pokemon_name = title.text
        if pokem_dict.get(pokemon_name) == None: # make initial empty list for each new pokemon
            pokem_dict[pokemon_name] = []

        if move_name not in pokem_dict[pokemon_name]: # need to avoid duplicate moves
             pokem_dict[pokemon_name].append(move_name)


    with open('moves.pkl', 'wb+') as file:
        pickle.dump(pokem_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    



    