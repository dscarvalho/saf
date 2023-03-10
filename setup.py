from distutils.core import setup

setup(
    name='saf',
    version='0.12',
    packages=['saf', 'saf.test', 'saf.constants', 'saf.importers', 'saf.importers.tokenizers', 'saf.annotators',
              'saf.data_model', 'saf.formatters', 'saf.serializers'],
    url='',
    license='',
    author='Danilo S. Carvalho',
    author_email='danilo@jaist.ac.jp',
    description='Simple Annotation Framework',
    install_requires=[
        'nltk',
        'regex'
    ]
)
