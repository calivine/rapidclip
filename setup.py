from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='rapidclip',
      version='0.1',
      description='video editing cli',
      long_description=readme(),
      keywords='video editing editor',
      author='Alex C',
      author_email='a.calog@protonmail.com',
      url='https://github.com/calivine/rapidclip',
      include_package_data=True,
      install_requires=['moviepy'],
      entry_points={
            'console_scripts': ['rapid=rapidclip.command_line:main'],
      })
