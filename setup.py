# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("erico", "site", "policy", "version.txt")).read().strip()

setup(name='erico.site.policy',
      version=version,
      description="Policy for my personal Plone site",
      long_description=open(os.path.join("erico", "site", "policy", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['erico', 'erico.site'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.disqus==0.3.0',
          'collective.simplesocial==1.3',
          'collective.siterss==0.4',
          'collective.ui.ie6nomore==1.0',
          'collective.portlet.keywordmatches==1.2',
          'Products.contentmigration==2.0',
          'Products.LinguaPlone==4.0a1',
          'Products.PlonePopoll==2.7.3b1',
          'sc.contentrules.groupbydate==1.0',
          'collective.blogging==1.1',
          'collective.js.jquery==1.3.2.1dev-r84292',
          'collective.js.jqueryui==1.8.4.1',
          'erico.site.theme',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

