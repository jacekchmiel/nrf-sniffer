from setuptools import setup, find_packages

setup(name='pykonnekt',
      description='Konnekt python libraries',
      author='Jacek Chmiel',
      author_email='chmieljj@gmail.com',
      packages=['nrf_sniffer'],
      install_requires=['pyserial'],
      use_scm_version=True,
      setup_requires=['setuptools_scm'])
