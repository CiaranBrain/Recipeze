# Validation Testing

## HTML and CSS

I used the W3c validator on my HTML and CSS files.  Please see results below:


### HTML

| File | URL | Screenshot | Notes |
|--------|--------|--------|--------|
| Home (not logged in) | https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com | ![Screenshot]() | Document checking completed. No errors or warnings to show |
| Home (logged in) | https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com | ![Screenshot]() | Document checking completed. No errors or warnings to show |
| About | https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com%2Fabout | ![Screenshot]() | Document checking completed. No errors or warnings to show |
| Add Recipe | https://validator.w3.org/nu/?doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com%2Frecipes%2Fadd_recipe%2F#textarea | ![Screenshot]() | Document checking completed. No errors or warnings to show |
| Edit Recipe | https://validator.w3.org/nu/#textarea| ![Screenshot]() | The form will be submitted to the same view that renders it, leaving the action attribute empty (action="") is a common practice in Django |
| Register | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com%2Faccounts%2Fsignup%2F | ![Screenshot]() | Error within AllAuth |
| Sign In | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com%2Faccounts%2Flogin%2F | ![Screenshot]() | Document checking completed. No errors or warnings to show |
| sign Out | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecipeze-da8be575c94f.herokuapp.com%2Faccounts%2Flogout%2F | ![Screenshot]() | Document checking completed. No errors or warnings to show |   


### CSS

| File |  URL | Screenshot | Notes |
|--------|--------|--------|--------|
| style.css | https://jigsaw.w3.org/css-validator/validator#css | ![Screenshot]() | No Error Found |


### PYTHON

I used the CI Python Linter https://pep8ci.herokuapp.com/# on all my .py files. Please see results below.
| File | Screenshot |
|--------|--------|
| config urls.py |  |
| config setting.py | |
| admin.py | |
| forms.py |  |
| models.py |  |
| recipe urls.py |  |
| views.py |  |

Due to the nature of the code and the need to accommodate complex expressions, I encountered difficulties in complying with the PEP8 standards, particularly regarding line length. While adhering to the guidelines is important, in certain cases, maintaining readability and clarity took precedence.
