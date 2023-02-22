# noxfile.py
import nox


locations = ".", "noxfile.py"
@nox.session(python=["3.10"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-import-order")
    session.run("flake8", *args)