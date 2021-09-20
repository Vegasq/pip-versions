import setuptools

setuptools.setup(
    name="pip-versions",
    version="0.1.2",
    author="Nick Yakovliev",
    author_email="mail@mkla.dev",
    py_modules=['pip_versions'],
    entry_points={"console_scripts": [
        "pip-versions = pip_versions.versions:main",
        "pip-plugin-versions = pip_versions.versions:main_plugin",
    ]},
    packages=[
        "pip_versions",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pip",
    ],
)
