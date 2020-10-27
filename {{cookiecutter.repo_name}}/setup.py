import os
from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except:
    long_description = None

setup(
    name="{{cookiecutter.repo_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    url="{{cookiecutter.repo_url}}",
    license="GPLv3",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
[barman.plugin]
{{cookiecutter.module_name}}={{cookiecutter.module_name}}:BarmanPluginMeta
""",
)
