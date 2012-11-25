memopolutils
====================

Python utils for accessing memopol.lqdn.fr datas using his REST API

Requirements : Python 2.6+

Examples : 

>>> from memopolutils import utils as memopolutils
>>> import pprint
>>> pp = pprint.PrettyPrinter(indent=4)
>>> pp.pprint(memopolutils.getCountriesInfos())
>>> pp.pprint(memopolutils.getCountry(resource_uri=u'/api/v1/mepcountry/280/'))
>>> pp.pprint(memopolutils.getCountry(code=u'FR'))
>>> pp.pprint(memopolutils.getMepsInfos('/api/v1/mepcountry/280/'))

