import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cr0wg4n",
    version="0.0.1",
    author="Mauricio Matias Conde",
    author_email="mcm.crw@gmail.com",
    description="this is an API mapping library for Kibana API to generate visualizations and dashboards automatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cr0wg4n/kibana-api",
    project_urls={
        "Bug Tracker": "https://github.com/cr0wg4n/kibana-api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='elasticsearch, kibana, development',
    packages=["kibana_dashboard_api"],
    install_requires=[
        "requests",
        "multipledispatch"
    ],
    python_requires=">=3.0",
)