import setuptools

setuptools.setup(
    name="packagename",
    version="0.0.1",
    author="LIU Dian",
    author_email="xgits@outlook.com",
    description="pypi template",
    project_urls={
        "Bug Tracker": "https://github.com/xgits/pypitemplate/issues",
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.7",
)