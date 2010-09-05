from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonInstallableProducts
from Products.CMFPlone.interfaces import INonInstallable as INonInstallableProfiles

from erico.site.policy.config import PRODUCTS

def nonInstallableProducts(products):
    ''' Given a list of product tuples formated as
        (name,locked,hidden,install,profile,runProfile)
        we return a list of names to be used by HiddenProducts
    '''
    pNames = [name for (name,locked,hidden,install,profile,runProfile) in products 
                   if hidden]
    pOldStyle = [name.replace('Products.','') for name in pNames 
                                              if name.startswith('Products.')]
    pNames = pOldStyle + pNames
    return pNames

def nonInstallableProfiles(products):
    ''' Given a list of product tuples formated as
        (name,locked,hidden,install,profile,runProfile)
        we return a list of names to be used by HiddenProfiles
    '''
    pNames = [profile for (name,locked,hidden,install,profile,runProfile) in products 
                   if hidden]
    return pNames

class HiddenProducts(object):
    implements(INonInstallableProducts)
    
    def getNonInstallableProducts(self):
        return nonInstallableProducts(PRODUCTS)

class HiddenProfiles(object):
    implements(INonInstallableProfiles)
    
    def getNonInstallableProfiles(self):
        return nonInstallableProfiles(PRODUCTS)
