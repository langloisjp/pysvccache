from setuptools import setup

setup(name='httpcache',
      version='0.1',
      description='HTTP cache with invalidation protocol',
      url='http://github.com/langloisjp/httpcache',
      author='Jean-Philippe Langlois',
      author_email='jpl@globalsign.com',
      license='GPL',
      py_modules=['httpcache', 'lrucache'],
      install_requires=['memcache', 'requests'],
      zip_safe=True)
