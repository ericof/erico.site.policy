# -*- coding: utf-8 -*-
from zope import component
import logging
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import interfaces as gsinterfaces
from Products.GenericSetup.upgrade import listUpgradeSteps

from Products.ZCatalog.ProgressHandler import ZLogHandler

from erico.site.policy.config import PRODUCTS

def upgrade0to1(context):
    ''' Upgrade to version 1.0
    '''
    setup = getToolByName(context, 'portal_setup')
    migration = getToolByName(context,'portal_migration')
    catalog = getToolByName(context,'portal_catalog')
    portal_properties = getToolByName(context,'portal_properties')
    qi = getToolByName(context,'portal_quickinstaller')

    # Install dependencies for this upgrade
    # List package names
    packages = [
                 #'beyondskins.site.policy',
               ]
    # (name,locked,hidden,install,profile,runProfile)
    dependencies = [(name,locked,hidden,profile) for name,locked,hidden,install,profile,runProfile in PRODUCTS if ((name in packages) and install)]
    
    for name,locked,hidden,profile in dependencies:
        qi.installProduct(name, locked=locked, hidden=hidden, profile=profile)
    
    # If we have blob and imaging installed
    # uncomment lines bellow
    # profiles = ['profile-plone.app.blob:file-replacement',
    #            'profile-plone.app.blob:image-replacement',
    #            ]
    # for profile in profiles:
    #     setup.runAllImportStepsFromProfile(profile)
