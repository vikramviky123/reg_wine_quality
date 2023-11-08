from setuptools import setup, find_packages

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()


__VERSION__ = "0.0.0"

REPO_NAME = "reg_wine_quality"
AUTHOR_USER_NAME = "vikramviky123"
SRC_REPO = "mlflow"
AUTHOR_EMAIL = "vikram_viky2001@yahoo.com"


setup(
    name=SRC_REPO,
    version=__VERSION__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for mlflow",
    long_description=long_description,

    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
