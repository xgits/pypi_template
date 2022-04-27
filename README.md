pypi template

https://packaging.python.org/en/latest/tutorials/packaging-projects/

# environment
py -m pip install --upgrade pip

py -m pip install --upgrade build

py -m build

py -m pip install --upgrade twine


# test
py -m twine upload --repository testpypi dist/*

py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

# distribute
twine upload dist/*
