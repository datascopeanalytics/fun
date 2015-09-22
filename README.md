Datascope fun!

## Want fun? Start here.

Run these steps to start the fun:

1. `mkvirtualenv fun` to create a python virtual environment with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/).
2. `pip install -r requirements.txt` to install required python libraries.
3. Create a `settings.py` file with a variable called `SLACK_TOKEN = '{{bearer_token}}'`. To get a `bearer_token`, click on the "Create token" button on [this page](https://api.slack.com/web) for the team for which you would like to have fun.
4. `python slack_fun.py mstringer` to test our your installation of `fun`. The test is successful if @stringertheory starts giggling like he's watching Dumb and Dumber. He's enjoying the fun!

## Troubleshooting

Did you run the test with `dean` as the argument for `slack_fun.py`? If not, do that.
