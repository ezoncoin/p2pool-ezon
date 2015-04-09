from distutils.core import setup, Extension

ezoncoin_module = Extension('ezoncoin_subsidy', sources = ['ezoncoin_subsidy.cpp'])

setup (name = 'ezoncoin_subsidy',
       version = '1.0',
       description = 'Subsidy function for EzonCoin',
       ext_modules = [ezoncoin_module])
