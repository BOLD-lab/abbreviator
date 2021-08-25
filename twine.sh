# docker run --rm -it -v $(pwd):/vol python bash

pip install --upgrade twine
python setup.py sdist bdist_wheel
twine upload dist/*