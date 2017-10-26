from setuptools import setup

setup(name='pypatent',
      version='1.0.0',
      description='Search and retrieve USPTO patent data',
      url='http://github.com/dan457/pypatent',
      author='Dan Eads',
      author_email='4708079+dan457@users.noreply.github.com',
      license='GNU GPLv3',
	  classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Topic :: Internet', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)', 'Programming Language :: Python :: 3'],
	  keywords=['patent', 'uspto', 'scrape', 'scraping'],
      packages=['pypatent'],
	  install_requires=['bs4', 'requests', 're'],
	  python_requires='>=3',
      zip_safe=False)