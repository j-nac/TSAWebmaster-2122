# TSAWebmaster-2122

An entry for the TSA Webmaster HS 2021-2022 competition by students at Mountlake Terrace High School.

## Installation

1. Clone the repo
2. Install python
3. Create a virtual environment in the project root directory with the command `python -m venv .venv` (for Windows)
4. Activate with the command `.venv\Scripts\activate`
5. Install requirements with command `pip install -r requirements.txt`
6. \[Optional] Configure python interpreter in your text editor selecting using the virtual environment
7. Run the website with command `python run.py`
8. You can see the website on http://localhost:5000/

## Developing

This website uses flask for the backend with a basic package file structure.
The \_\_init\_\_.py file creates the flask app object, views.py is where all the routes (code to render pages) goes, html files go in templates folder, everything else (css, js, and images) go in the static folder. Remember to use url_for which is imported from flask to reference all files or pages in the project.
