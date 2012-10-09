from distutils.core import setup
from sh import pandoc

setup(
    name='cardscript',
    version='0.6',
    description="A scriptable card game processing engine.",
    author="Charles Nelson",
    author_email="cnelsonsic@gmail.com",
    url="https://github.com/cnelsonsic/cardscript",
    packages=['cardscript', 'cardscript.cards'],
    license='AGPLv3+',
    long_description='\n'.join(pandoc('README.md', t='rst')),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Games/Entertainment :: Board Games',
        ],
)

