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
  info = {}

  pkg_info = srv_conn()
  rel = pkg_info.package_releases(pkg)
  info['lastest_rel'] = rel[0]

  pkg_data = pkg_info.release_data(pkg, info['lastest_rel'])
  info['name'] = pkg_data['name']
  info['summary'] = pkg_data['summary']
  info['url'] = str(pypi_base_url + pkg)
  info['home_page'] = pkg_data['home_page']
  return info


def simplesearch(pkg):
  print pkg


def xmlrpcsearch(pkg, spec='name'):
  pkg_info = srv_conn()
  return pkg_info.search({spec:pkg}, {'_pypi_ordering': True})
