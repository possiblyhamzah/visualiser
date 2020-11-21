from distutils.core import setup
setup(
  name = 'visualiser',   
  packages = ['visualiser'],
  version = '0.1',
  license='MIT',
  description = 'A terminal visualiser.',
  author = 'possiblyhamzah',
  author_email = 'possiblyhamzah@gmail.com',
  url = 'https://github.com/probablyhamzah/visualiser',
  download_url = 'https://github.com/probablyhamzah/visualiser/archive/v_01.tar.gz',
  keywords = ['visualiser', 'terminal'],
  install_requires=[
          'twine',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)