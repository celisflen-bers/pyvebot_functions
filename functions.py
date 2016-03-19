# Funciones para PyVeBot
# -*- coding: utf8
# Mas info https://github.com/pyve/PyVenezuelaBot

# Creado por Carlos Celis Flen-Bers
# Repo: https://github.com/celisflen-bers/pyvebot_functions

import xmlrpclib

pypi_simple   = "https://pypi.python.org/simple/index.html"
pypi_base_url = "https://pypi.python.org/pypi/"


def srv_conn():
  #https://wiki.python.org/moin/PyPIXmlRpc
  srv_pypi = xmlrpclib.ServerProxy(pypi_base_url)
  return srv_pypi


def package_located(pkg):

  pkg_info = srv_conn()
  rel = pkg_info.package_releases(pkg)
  lastest_rel = rel and rel[0] or None

  pkg_data = pkg_info.release_data(pkg, lastest_rel)
  return pkg_data


def simplesearch(pkg):
  print pkg


def xmlrpcsearch(pkg, spec='name'):
  pkg_info = srv_conn()
  return pkg_info.search({spec:pkg}, {'_pypi_ordering': True})
