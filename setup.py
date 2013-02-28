import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name = 'project_euler',
      version = '0.1',
      description = 'Solutions to Project Euler problems',
      long_description = readme(),
      classifiers = [
          'License :: OSI Approved :: BSD License'
      ],
      url = 'http://github.com/FranklinChen/project-euler-python',
      author = 'Franklin Chen',
      author_email = 'franklinchen@franklinchen.com',
      license = 'BSD3',
      packages = find_packages(exclude = ["tests"]),
      keywords = "Project Euler",
      entry_points = {
        'console_scripts': {
            'project_euler_answer1 = project_euler.problem_1:print_answer',
        }
      }
    )
