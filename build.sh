rm dist/*
pip3 install -r requirements.txt
python3 setup.py sdist
python3 setup.py bdist_wheel
twine upload dist/*
