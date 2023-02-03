# FastAPI + TailwindCSS Example

A YouTube tutorial I've made can be found [here](https://youtu.be/yrEKYkIK-Fw).

Feel free to contact me if you have any questions.

The steps I followed are the following

## Instructions

### 1.- Setup your FastAPI

You need to install

**FastAPI**

```sh
pip install fastapi
```

**ASGI Server**

```sh
pip install "uvicorn[standard]"
```

**Templating Engine**

For this example we will be using Jinja2

```sh
pip install Jinja2
```

### 2.- Return HTML from your FastAPI route

**Create a "templates" folder in your project**

Inside this folder create a "base.html" file

**Add the TemplateResponse to your route response**

```sh
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates=Jinja2Templates(directory="templates")

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("base.html",{"request":request})
```

### 3.- Create a "tailwindcss" folder on your project

Here we will be adding the TailwindCSS files

### 4.- Install TailwindCSS

Start a new terminal inside your project folder and run the following command

```sh
npm install tailwindcss
```

### 5.- Create a "tailwind.config.js" file

This file will be used to configure TailwindCSS, and make sure you include in content the path to your templates folder

```sh
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

### 6.- Create a new folder "styles" inside your tailwindcss folder

Here we will be adding our custom styles, by creating a new file "styles.css" and adding the base directives

```sh
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 7.- Run the TailwindCSS CLI build process

This proccess will generate a "app.css" file inside a new "static/css" folder.

The "--watch" flag will make sure that the styles are updated every time you make a change in your files.

```sh
npx tailwindcss -i ./styles/app.css -o ../static/css/app.css --watch
```

### 8.- Add the TailwindCSS stylesheet to your base.html file

**Mount the static folder**

In order to mount this folder we need to add the following lines to our main.py file

Import the static files

```sh
from fastapi.staticfiles import StaticFiles
```

Add the static folder to your app

```sh
app.mount("/static", StaticFiles(directory="static"), name="static")
```

Now we can add the stylesheet to our base.html file

```sh
<link href="{{url_for('static',path='/css/app.css')}}" rel="stylesheet">
```

### 9.- Serving compressed files with the GZip middleware

In order to serve compressed files we need to import the middleware

```sh
from fastapi.middleware.gzip import GZipMiddleware
```

add the middleware to your app

```sh
app.add_middleware(GZipMiddleware)
```

## Script for running the TailwindCSS CLI build process

We can create a script inside your package.json file to run the TailwindCSS CLI build process

```sh
"scripts": {
    "dev": "npx tailwindcss -i ./styles/app.css -o ../static/css/app.css --watch"
},
```
