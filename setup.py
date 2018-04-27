from setuptools import setup

setup(name='pysbatch',
      version='0.1.1.dev1',
      description='Submit slurm job in python',
      url='https://github.com/luptior/pysbatch',
      author='Gan Xu',
      author_email='luptior@gmail.com',
      license='MIT',
      packages=['pysbatch'],
      zip_safe=False,
      classifiers=[
          # How mature is this project?
          'Development Status :: 2 - Pre-Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',

          # Pick your license as you wish (should match "license" above)
           'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',],
      keywords='slurm batch job submit',
      python_requires='>=3'
     )
