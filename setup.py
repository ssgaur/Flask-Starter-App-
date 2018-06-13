from setuptools import setup
from setuptools.command.test import test as TestCommand
import HtmlTestRunner
import unittest
import StringIO

def readme():
    with open('README.md') as f:
        return f.read()

class PlivoTests(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):

        runner = HtmlTestRunner.HTMLTestRunner(
                output="Reports"
                )
        test_suite = unittest.TestLoader().discover("tests", pattern='*_tests.py')
        runner.run(test_suite)

setup(name='flask-app',
      version='1.0',
      description='App Description',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='App Keywords',
      author='Shailendra',
      author_email='shailendra.singh.knp@gmail.com',
      packages=["config", "app", "tests"],
      test_suite="tests",
      cmdclass={"test": PlivoTests},
      install_requires=[
          'Flask',
          'requests',
          'pymongo',
          'flask_cors',
          'flask_sqlalchemy'
      ],
      include_package_data=True,
      zip_safe=False)