# Creating a blog with Cookiecutter-Django & deploying it to Heroku

> Learn to jumpstart a production-ready blog using the Cookiecutter-Django framework and how to deploy it to Heroku

![screenshot](./screenshots/blog-home.png)

Additional description about the project and its features.

## Built With

- Python,
- Cookiecutter-Django,
- Bootstrap 4.5, Bootstwatch Darkly

## Live Demo

[Live Demo Link](https://quiet-citadel-68595.herokuapp.com/)


## Getting Started

**This is an example of how you may give instructions on setting up your project locally.**
**Modify this file to match your project, remove sections that don't apply. For example: delete the testing section if the currect project doesn't require testing.**


To get a local copy up and running follow these simple example steps.

### Prerequisites

Python 3.8
virtual environment
PostgreSQL.
Redis, if using Celery
Cookiecutter
Heroku
AWS/GCP for static assets
Git

### Setup

Install cookiecutter

`$ python -m pip install "cookiecutter>=1.7.2"`

Install cookiecutter-django

`$ cookiecutter https://github.com/pydanny/cookiecutter-django`

Create a virtual environment

`$ virtualenv <name_of_environment>`

Activate/Run PostgreSQL

### Usage

`$ cookiecutter https://github.com/pydanny/cookiecutter-django` - run the cookiecutter-django command
`$ source <name_of_environment>/bin/activate` - create a virtual environment
`$ python -m pip install -r requirements/local.txt` - install local dev dependencies
`$ createdb <what you have entered as the project_slug at setup stage> -U postgres --password <password>` - create a postgreSQL db
`$ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>` - export database_url

### Run tests

For unit tests, run:

`$ python manage.py test`

### Deployment

Complete deployment instructions are at: https://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html


## Authors

👤 **Vicente G. Reyes**

- Github: [@reyesvicente](https://github.com/reyesvicente)
- Twitter: [@highcenburg](https://twitter.com/highcenburg)
- Facebook: [highcenbugtv](https://facebook.com/highcenbugtv)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Cookiecutter
- Cookiecutter-django
- Learnetto
- Bootswatch

## 📝 License

This project is [MIT](https://github.com/reyesvicente/cookiecutter-blog-tutorial-learnetto/blob/master/LICENSE) licensed.

https://www.buymeacoffee.com/highcenburg
