# binary-categorical-classifier
Research project to determine if Q-analysis is capable of classifying binary and categorical data. It compares Q-analysis to KNN.

## You need to have
* Python 3.10
* Pip3 22.2.1
* virtualenv 20.16.3
* Node.js 16.16.0

## How to run
### Q-analysis and KNN backend
1. Create a virtual environment with virtualenv inside the root directory of _q-analysis_ or _knn_
2. Activate the virtual environment
3. Install the Python dependecies with `pip install -r requirements.txt`
4. Run backend with `python -m flask run --host=0.0.0.0`

### Frontend
1. Go to the _frontend_ directory
2. Install all dependencies with `npm install`
3. Run frontend with `npm run serve`
