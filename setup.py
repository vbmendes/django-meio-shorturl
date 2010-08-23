from setuptools import setup, find_packages

setup(
    name = "django-shorturl",
    version = "1.0",
    url = 'http://github.com/vbmendes/django-shorturl',
    license = 'BSD',
    description = "Short URL handling in Django apps.",
    author = 'Vinicius Mendes',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
