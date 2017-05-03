#from distutils.core import setup
#from distutils.core import setup
from setuptools import setup
setup(
  name = 'apolloMusicPlayer',
  packages = ['apolloMusicPlayer'], # this must be the same as the name above
  version = '0.1',
  description = 'The music player for Apollo',
  author = 'Erik Beitel',
  author_email = 'erik.beitel@gmail.com',
  url = 'https://github.com/ebber/apolloRipper', # use the URL to the github repo
  download_url = 'https://github.com/ebber/apolloMusicRipper/archive/0.1.tar.gz', # I'll explain this in a second
  install_requires=[
   "logging"
    ],
  keywords = ['audio', 'music player'], # arbitrary keywords
  classifiers = [],
)
