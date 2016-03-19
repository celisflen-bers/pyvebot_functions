#!/usr/bin/python
# -*- coding: utf8
# Carlos Celis Flen-Bers

import sys, getopt

from functions import *

help_msg = "Exec\n" + sys.argv[0] + " <package>"

def usage():
  print help_msg

def about():
  print "Programa de ejecución"

def pysearch(pkg='pypi'):
# En representación del bot
  res = xmlrpcsearch(pkg)
  for i in res:
    print '  -' + i['name'] + ': ' + i['version'] + '\n    ' + i['summary']
  print ' end'

def pypi(pkg='pypi'):
# En representación del bot
  res = package_located(pkg)
  print '  ' + res['name'] + ': ' + res['lastest_rel']
  print '    ' + res['summary']
  print '  Visite ' + res['url'] + ' para ver paquete pypi'
  print '  Visite ' + res['home_page'] + ' para más info'

def main(argv):
  package = ''
  try:
    opts, args = getopt.getopt(argv,"hs:p:",["help", "about", "pysearch=", "pypi="])
  except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt == '--about':
      about()
      sys.exit()
    elif opt in ("-s", "--pysearch"):
      print "buscar paquetes por: " + arg
      pysearch(arg)
    elif opt in ("-p", "--pypi"):
      print "buscar paquete: " + arg
      pypi(arg)

if __name__ == "__main__":
  main(sys.argv[1:])
