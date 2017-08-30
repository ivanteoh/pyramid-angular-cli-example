from setuptools import setup

REQUIRES = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]

setup(name='backend',
      install_requires=REQUIRES,
      entry_points="""\
      [paste.app_factory]
      main = backend:main
      """,
)
