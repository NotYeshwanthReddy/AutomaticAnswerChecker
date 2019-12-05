from setuptools import setup

setup(
	name=='AutomaticAnswerChecker'
	version='1.0'
	description=''
	licence="NONE"
	author="Yeshwanth Reddy"
	author_email="peddamalluyeshwanth1999@gmail.com"
	url="yeshwanth-reddyy.github.io"
	packages=['AutomaticAnswerChecker']
	install_requirements=['flask', 'gunicorn', 'requests', 'fuzzywuzzy', 'numpy', 'Pyrebase', 'pandas', 'scikit_learn']
)