# Robotiic

Robotiic is a Streamlit application for visualizing the results of genetic algorithms, showcasing eight queens with backtracking, and for the MCV / MRV heuristic. Inspired from "Artificial Intelligence: A Modern Approach 3rd Edition", by Stuart Russell, Peter Norvig.

Check out the `Heroku` depliyment [here](robotiic.herokuapp.com/).

## Streamlit

Checking if Streamlit was installed properly,

```bash
streamlit hello
```

Starting the streamlit application,

```bash
streamlit run app.py
```

## Heroku

Logging,

```bash
heroku logs --tail -a robotiic
```

## Autopep8

Formatting,

```bash
autopep8 --in-place --aggressive --aggressive [filename]
```

## Pip

Installing,

```bash
pip install package_name
```

Moving to `requirements.txt,

```bash
pip freeze > requirements.txt
```

## Pipenv

Activating,

```bash
pipenv shell
```

Updating `Pipfile`, by moving dependencies from `requirements.txt` to `Pipfile`,

```bash
pip freeze > requirements.txt
pipenv install -r requirements.txt
```

Updating `pipfile.lock`,

```bash
pipenv lock --pre --clear
```

## References

- [NetworkX - Colored graphs](https://stackoverflow.com/questions/27030473/how-to-set-colors-for-nodes-in-networkx)
- [NetworkX - Label With Edges](https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python)