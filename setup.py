from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='project_euler',
      version='0.1',
      description='Solutions to Project Euler problems',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: BSD License'
      ],
      url='http://github.com/FranklinChen/project-euler-python',
      author='Franklin Chen',
      author_email='franklinchen@franklinchen.com',
      license='BSD3',
      packages=['project_euler'],
      zip_safe=False,
      scripts=[
          'bin/answer1'
      ]
    )
