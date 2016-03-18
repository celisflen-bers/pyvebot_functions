#!/usr/bin/python
# Carlos Celis Flen-Bers

import sys, getopt
import xmlrpclib
import file functions
pypi_base_url = "https://pypi.python.org/pypi/"
def package_located(argument):
  info = {}
  info['url'] = str(pypi_base_url + argument)
  
  #https://wiki.python.org/moin/PyPIXmlRpc
  pkg_info = xmlrpclib.ServerProxy(pypi_base_url)
  
  rel = pkg_info.package_releases(argument)
  info['lastest_rel'] = rel[0]
  
  pkg_data = pkg_info.release_data(argument, info['lastest_rel'])
  info['name'] = pkg_data['name']
  info['summary'] = pkg_data['summary']

  return info
    
def main(argv):
  package = ''
  try:
    opts, args = getopt.getopt(argv,"h")
  except getopt.GetoptError:
    print 'mybot.py <package>'
    sys.exit(2)
  for opt in argv:
      if opt == '-h':
        print 'mybot.py <package>'
        sys.exit()
      else:
        package = opt
        print 'info ', package_located(package)
  print 'Package "', package, '"'

if __name__ == "__main__":
  main(sys.argv[1:])
