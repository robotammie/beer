"""
    >>> st_bernardus = Beer('St. Bernardus', .1, 9.5, 250)
    >>> Evil_Twin = Beer('evil twin', .12, 8, 250)
    >>> North_Coast_PranQster = Beer('North Coast PranQster', .076, 6.5, 330)
    >>> Sur_Simcoe = Beer('Sur Simcoe', .045, 9, 250)
    >>> Speziale_Hell_Festbier = Beer('Speziale Hell Festbier', .059, 6.5, 330)
    >>> Russian_River_Damnation = Beer('russian river damnation', .0775, 7.75, 330)
    >>> Russian_River_Happy_Hops = Beer('Russian River Happy Hops', .054, 7, 473)
    >>> Shacksbury_cider = Beer('Shacksbury Cider', .062, 6.25, 250)
    >>> St_Feuillien_Triple = Beer('St Feullien Triple', .085, 9.5, 250)
    >>> Mikkeller_SD_Brett_IPA = Beer('Mikkeller SD Brett IPA', .058, 6, 330)
    >>> Allagash_Saison = Beer('Allagash Saison', .061, 6, 330)
    >>> Cellarmaker_Party_Ghoast = Beer('Cellarmaker Party Ghoast', .066, 7, 473)
    >>> Allagash_White_Ale = Beer('Allagash White Ale', .05, 7.5, 400)
    >>> Moonlight_Reality_Czech_Pils = Beer('Moonlight Reality Czech Pils', .048, 6.75, 473)
    >>> Mikkeller_Mexas_Ranger = Beer('Mikkeller Mexas Ranger', .066, 9, 250)
    >>> AmagerCigar_City_Orange_Crush = Beer('AmagerCigar City Orange Crush', .05, 8.5, 250)
    >>> Petrus_Aged_Pale = Beer('Petrus Aged Pale', .073, 8.5, 250)
    >>> North_Coast_Old_Rasputin = Beer('North Coast Old Rasputin', .09, 6.75, 250)
    >>> Founders_All_Day_IPA = Beer('Founders All Day IPA', .047, 6, 473)
    >>> De_Ranke_Noir_de_Dottianies = Beer('De Ranke Noir de Dottianies', .09, 8, 250)
    >>> Square_Root_225_Saison = Beer('Square Root 225 Saison', .06, 10.5, 250)
    >>> Alesmith_Speedway_stout = Beer('ale speedway stout', .12, 7, 250)
    >>> Jopen_Hoppen_bier = Beer('Jopen Hoppen Bier', .068, 7, 250)
    >>> Wired_Farmhouse_pale = Beer('wired farmhouse pale', .05, 9, 250)

    >>> all_beers = [st_bernardus, Evil_Twin, North_Coast_PranQster, Sur_Simcoe, Speziale_Hell_Festbier, Russian_River_Damnation, Russian_River_Happy_Hops, Shacksbury_cider, St_Feuillien_Triple, Mikkeller_SD_Brett_IPA, Allagash_Saison, Cellarmaker_Party_Ghoast, Allagash_White_Ale, Moonlight_Reality_Czech_Pils, Mikkeller_Mexas_Ranger, AmagerCigar_City_Orange_Crush, Petrus_Aged_Pale, North_Coast_Old_Rasputin, Founders_All_Day_IPA, De_Ranke_Noir_de_Dottianies, Square_Root_225_Saison, Alesmith_Speedway_stout, Jopen_Hoppen_bier, Wired_Farmhouse_pale]

    >>> drunkify_sophia(all_beers)
    [<Beer Founders All Day IPA, 473ml>,
     <Beer evil twin, 250ml>,
     <Beer North Coast PranQster, 330ml>,
     <Beer ale speedway stout, 250ml>,
     <Beer Cellarmaker Party Ghoast, 473ml>]


"""

from pprint import pprint


class Beer(object):
    def __init__(self, name, abv, price, vol, ibu=50):
        self.name = name
        self.abv = abv
        self.price = price
        self.vol = vol
        self.ibu = ibu

    def __repr__(self):
        """define how model displays."""
        return "<Beer %s, %dml>" % (self.name, self.vol)


def drunkify_sophia(beers):
    """Determine the beer that offers Sophia the most alcohol density for her hard-earned money"""
    beer_hash = {}
    for beer in beers:
        ratio = (beer.vol * beer.abv) / beer.price
        beer_hash[ratio] = beer_hash.get(ratio, [])
        beer_hash[ratio].append(beer)
    ratios = beer_hash.keys()
    ratios.sort()
    top_five = []
    for ratio in ratios[-5:]:
        top_five.append((beer_hash[ratio][0]))
    pprint(top_five)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** NIKE\n"
