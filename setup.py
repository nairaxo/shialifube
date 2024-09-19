from setuptools import setup, find_packages

setup(
    name='shialifube',
    version='0.1.2',
    description='Transliteration of Comorian into Arabic Script',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abdou Mohamed Naira',
    author_email='naira.abdoumohamed@gmail.com',
    url='https://github.com/nairaxo',
    packages=find_packages(),
    install_requires=[
        # Liste des dépendances, par exemple :
        # 'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
