# import necessary libraries
from bs4 import BeautifulSoup as bs #used for scraping
import requests #used to send HTTP request
import re #used for regular expression to extract text from webpage
import pickle #used to create a dictionary for all the pokemon and all there moves
 

move_dict = {} #create dict
pokem_dict = {} #create dict


def getHTMLdocument(url):
    '''This function grabs the html document from a given url'''
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
                            attrs={'href': re.compile("/move/")}): #searchs the webpage for the a tag, with href. Then recompiles at the /move/ 
    links = (link.get('href')) #gets all the move names
    listOfLinks =( "https://pokemondb.net" + links) #This takes all the local urls and adds the sites url to create a list of links for the loop to go through

  
    # load webpage content
    r = requests.get(listOfLinks)

    #convert to a bsoup object
    soup = bs(r.content)
    #searchs page for the body stuff
    body = soup.find('body')
    #searchs the body for examples of the a tag with the class ent-name. This gives us the names of the pokemon that can learn the move
    pokeNames = body.find_all('a', {'class':'ent-name'})

    if pokeNames == []: continue #
    move_name = links[6:] #takes the local urls and slices out just the move names themselves
    print(move_name)

    move_dict[move_name] = set()

    for title in pokeNames:
        move_dict[move_name].add(title.text) #gives the pokemon names

        pokemon_name = title.text
        if pokem_dict.get(pokemon_name) == None: # make initial empty list for each new pokemon
            pokem_dict[pokemon_name] = []

        if move_name not in pokem_dict[pokemon_name]: # need to avoid duplicate moves
             pokem_dict[pokemon_name].append(move_name)


    with open('moves.pkl', 'wb+') as file:
        pickle.dump(pokem_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    



    