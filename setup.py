from setuptools import find_packages, setup

setup(
    name='pabui',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'PyAutoBlockchain'
    ],
    entry_points={
        'console_scripts': [
            "pabui=pabui:run"
        ]
    },
    package_data={
        'pabui': ['static/*', 'templates/*']
    }
)
