# vue-meta-info

This project provides a sample front-end for examining meta information from a Flask-RESTful-DBBase based application.

The point of Flask-RESTful-DBBase derives from introspection of Python database models created with SQLAlchemy. By using the structure of the models, the constraints and relationships, a set of tools help validate, serialize/deserialize and document a web API.

Because the output of the API is all JSON, it can be presented via a front-end application such as this.

![Sample Screenshot](public/screenshot.png)

## Project setup

Getting setup to use the sample is a two-part problem. There must be a functioning Flask server with Flask-RESTful-DBBase installed.  A sample app is found in the flask_app directory. Once that is started the Vue project can be run.

# Installation of Flask Sample API.

```
cd flask_app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

```
# Installation Vue-Meta-Info
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your unit tests
```
npm run test:unit
```

### Run your end-to-end tests
```
npm run test:e2e
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
