from setuptools import setup

setup(name='pypatent',
      version='1.0.1',
      description='Search and retrieve USPTO patent data',
      url='http://github.com/daneads/pypatent',
      author='Dan Eads',
      author_email='24708079+daneads@users.noreply.github.com',
      license='GNU GPLv3',
	  classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Topic :: Internet', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 'Programming Language :: Python :: 3'],
	  keywords=['patent', 'uspto', 'scrape', 'scraping'],
      packages=['pypatent'],
	  install_requires=['bs4', 'requests'],
	  python_requires='>=3',
      zip_safe=False)