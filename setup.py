from distutils.core import setup

version = '0.1.1'

setup(
    name='kurma',         # How you named your package folder
    # Chose the same as "name"
    packages=['kurma', 'kurma.structure_order', 'kurma.lmps'],

    # package_dir={'': 'kurma'},
    # packages=find_packages(where='kurma'),

    version=version,      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Library to do simple manipulation of md=trajectory from lammps.',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    author='Ravinder Bhattoo',                   # Type in your name
    author_email='',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/ravinderbhattoo/kurma',
    # I explain this later on
    download_url='https://github.com/ravinderbhattoo/kurma/archive/{}.tar.gz'.format(
        version),
    keywords=['Molecular Dynamics', 'Trajectory', 'PDF', 'RDF',
              'Coordination Number'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'numpy',
        'pandas',
        'matplotlib',
        'scipy',
        'jax'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 5 - Production/Stable',
        # Define that your audience are developers
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
