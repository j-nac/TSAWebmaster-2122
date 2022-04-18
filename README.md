# TSAWebmaster-2122

An entry for the TSA Webmaster HS 2021-2022 competition by students at Mountlake Terrace High School.

## Installation

All instructions are for Windows

### Prerequisites

- [ ] Clone the repo
- [ ] Install Python

### Flask and Python Setup

1. Create a virtual environment in the project root directory (`cd ../..` if you're coming from the last step) with the command `python -m venv .venv`
2. Activate with the command `.venv\Scripts\activate`. Terminal should now show (.venv) on the left - you deactivate with the command `deactivate`
3. Install requirements with command `pip install -r requirements.txt`
4. Any new packages installed with pip can be saved to the requirements with the command `pip freeze > requirements.txt`
5. \[Optional] Configure python interpreter in your text editor selecting using the virtual environment

### Running the app

1. Set proper environment variables
2. From the project root, run the website with command `python run.py`
3. You can see the website on http://localhost:5000/

## Developing

This website uses flask for the backend with a basic package file structure.
The \_\_init\_\_.py file creates the flask app object, views.py is where all the routes (code to render pages) goes, html files go in templates folder, everything else (css, js, and images) go in the static folder. Remember to use url_for which is imported from flask to reference all files or pages in the project.
