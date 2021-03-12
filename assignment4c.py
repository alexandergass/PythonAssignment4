from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

root = Element( 'movielist' )

entry = SubElement( root, 'movieid1' )
title = SubElement(entry, "title")
title.text = "The Wolf of Wallstreet"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Martin Scorsese"
actor = SubElement(entry, "actor")
actor.text = "Leonardo DiCaprio"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0993846/"
year = SubElement(entry, "year")
year.text = "2013"
genre = SubElement(entry, "genre")
genre.text = "Biography/Crime/Drama"

entry = SubElement( root, 'movieid2' )
title = SubElement(entry, "title")
title.text = "War Dogs"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BMjEyNzQ0NzM4MV5BMl5BanBnXkFtZTgwMDI0ODM2OTE@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Todd Phillips"
actor = SubElement(entry, "actor")
actor.text = "Jonah Hill"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt2005151/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "2016"
genre = SubElement(entry, "genre")
genre.text = "Biography/Crime/Drama"

entry = SubElement( root, 'movieid3' )
title = SubElement(entry, "title")
title.text = "Guardians of the Galaxy"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "James Gunn"
actor = SubElement(entry, "actor")
actor.text = "Chris Pratt"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt2015381/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "2014"
genre = SubElement(entry, "genre")
genre.text = "Action, Adventure, Comedy"

entry = SubElement( root, 'movieid4' )
title = SubElement(entry, "title")
title.text = "The Nightmare Before Christmas"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BNWE4OTNiM2ItMjY4Ni00ZTViLWFiZmEtZGEyNGY2ZmNlMzIyXkEyXkFqcGdeQXVyMDU5NDcxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Tim Burton"
actor = SubElement(entry, "actor")
actor.text = "Henry Selick"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0107688/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "1993"
genre = SubElement(entry, "genre")
genre.text = "Animation, Family, Fantasy"

entry = SubElement( root, 'movieid5' )
title = SubElement(entry, "title")
title.text = "Shaun of the Dead"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BMTg5Mjk2NDMtZTk0Ny00YTQ0LWIzYWEtMWI5MGQ0Mjg1OTNkXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Edgar Wright"
actor = SubElement(entry, "actor")
actor.text = "Simon Pegg"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0365748/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "2013"
genre = SubElement(entry, "genre")
genre.text = "Biography/Crime/Drama"

entry = SubElement( root, 'movieid6' )
title = SubElement(entry, "title")
title.text = "The Shining"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Stanley Kubrick"
actor = SubElement(entry, "actor")
actor.text = "Jack Nicholson"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0081505/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "1980"
genre = SubElement(entry, "genre")
genre.text = "Drama/Horror"

entry = SubElement( root, 'movieid7' )
title = SubElement(entry, "title")
title.text = "Hot Fuzz"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BMzg4MDJhMDMtYmJiMS00ZDZmLThmZWUtYTMwZDM1YTc5MWE2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Edgar Wright"
actor = SubElement(entry, "actor")
actor.text = "Simon Pegg"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0425112/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "2007"
genre = SubElement(entry, "genre")
genre.text = "Action, Comedy, Mystery"

entry = SubElement( root, 'movieid8' )
title = SubElement(entry, "title")
title.text = "Pirates of the Caribbean Curse of the Black Pearl"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BNGYyZGM5MGMtYTY2Ni00M2Y1LWIzNjQtYWUzM2VlNGVhMDNhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Gore Verbinski"
actor = SubElement(entry, "actor")
actor.text = "Johnny Depp"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0993846/"
year = SubElement(entry, "year")
year.text = "2003"
genre = SubElement(entry, "genre")
genre.text = "Action, Adventure, Fantasy"

entry = SubElement( root, 'movieid9' )
title = SubElement(entry, "title")
title.text = "The Ring"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BNDA2NTg2NjE4Ml5BMl5BanBnXkFtZTYwMjYxMDg5._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Gore Verbinski"
actor = SubElement(entry, "actor")
actor.text = "Naomi Watts"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt0298130/?ref_=nv_sr_2?ref_=nv_sr_2"
year = SubElement(entry, "year")
year.text = "2002"
genre = SubElement(entry, "genre")
genre.text = "Horror, Mystery"

entry = SubElement( root, 'movieid10' )
title = SubElement(entry, "title")
title.text = "Horrible Bosses"
image = SubElement(entry, "image")
image.text = "https://m.media-amazon.com/images/M/MV5BNzYxNDI5Njc5NF5BMl5BanBnXkFtZTcwMDUxODE1NQ@@._V1_UX182_CR0,0,182,268_AL_.jpg"
director = SubElement(entry, "director")
director.text = "Seth Gordon"
actor = SubElement(entry, "actor")
actor.text = "Jason Bateman"
imdb = SubElement(entry, "imdb")
imdb.text = "https://www.imdb.com/title/tt1499658/?ref_=nv_sr_1?ref_=nv_sr_1"
year = SubElement(entry, "year")
year.text = "2011"
genre = SubElement(entry, "genre")
genre.text = "Comedy, Crime"

output_file = open( 'fav_movies.xml', 'w' )
# This line triggered only error in validator, duplicated xml version line
# output_file.write( '<?xml version="1.0"?>' )
output_file.write( prettify(root))
output_file.close()