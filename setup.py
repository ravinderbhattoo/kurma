from distutils.core import setup
version = '0.1.0'

setup(
    name = 'kurma',         # How you named your package folder
    packages = ['kurma'],   # Chose the same as "name"
    version = version,      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Library to do simple manipulation of md=trajectory from lammps.',   # Give a short description about your library
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    author = 'Ravinder Bhattoo',                   # Type in your name
    author_email = '',      # Type in your E-Mail
    url = 'https://github.com/ravinderbhattoo/kurma',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/ravinderbhattoo/kurma/archive/{}.tar.gz'.format(version),    # I explain this later on
    keywords = ['Molecular Dynamics', 'Trajectory', 'PDF', 'RDF', 'Coordination Number'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
            'numpy',
            'pandas',
            'matplotlib',
            'scipy',
            'jax'
        ],
    classifiers=[
      'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
      'Intended Audience :: Science/Research',      # Define that your audience are developers
      'License :: OSI Approved :: MIT License',   # Again, pick a license
      'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
