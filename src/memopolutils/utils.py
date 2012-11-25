# -*- coding: utf-8 -*-

import urllib
import json

DOMAIN = 'http://memopol.lqdn.fr'
BASE_URL_COUNTRY = '/api/v1/mepcountry/'
BASE_URL_COUNTRY_MEP = '/api/v1/mepcountrymep/'
BASE_URL_MEP = '/api/v1/mepmep' # MEP = Member of European Parliament

def loadJson(resource_uri, offset=None, limit=None, domain=DOMAIN):
    """ Load JSON data for a given URL, using an offset and a limit (see 
        Tastypie documentation) """
    sep = '?' in resource_uri and '&' or '?'
    resource_uri = '%s%s%sformat=json' % (domain, resource_uri, sep)
    if offset is not None:
        resource_uri += '&offset=%d' % offset
    if limit is not None:
        resource_uri += '&limit=%d' % limit
    
    f = urllib.urlopen(resource_uri)
    datas = json.load(f)
    return datas

def getCountries():
    """ Return the list of available countries (Tastypie result) """
    return loadJson(BASE_URL_COUNTRY, limit=0)['objects']

def getCountriesInfos():
    """ Return list of (code, name, resource_uri) for available countries """
    countries = getCountries()
    return [(country['code'], country['name'], country['resource_uri'])
             for country in countries]

def getCountry(code=None, resource_uri=None):
    """ Return a country from his code (like u'FR' for France) or from his
        resource URI (like u'/api/v1/mepcountry/280/' for France
        (Tastypie result) """
    country = None
    
    if resource_uri is not None:
        country = loadJson(resource_uri)
    
    elif code is not None:
        countries = getCountries()
        for c in countries:
            if c['code'] == code:
                country = c
                break
    
    return country

def getMeps(country_uri):
    """ Return a country's MEP list (Tastypie result) """
    country = getCountry(resource_uri=country_uri)

    meps_uris = []
    meps = []
    
    for countrymep_uri in country['countrymep_set']:
        try:
            countrymep = loadJson(countrymep_uri)
        except ValueError:
            # ?? : The model '' has an empty attribute 'party' and doesn't
            # allow a null value.
            continue
        
        mep_uri = countrymep['mep']
        if countrymep['mep'] not in meps_uris:
            meps_uris.append(countrymep['mep'])
            mep = loadJson(mep_uri)
            if mep['active'] == True:
                meps.append(mep)
    
    return meps

def getMepsInfos(country_uri):
    """ Return list of meps (total_scrore, full_name, ...) for a given 
        country uri. """
    meps = [(mep['total_score'], mep['full_name'])
            for mep in getMeps(country_uri)]
    meps.sort()
    meps.reverse()
    return meps