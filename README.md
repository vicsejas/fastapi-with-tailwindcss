# Updated FastAPI + Tailwind CSS v4.0 Example

A YouTube tutorial for version v4.0 soon.

Deprecated(for V3.0): A YouTube tutorial I've made can be found [here](https://youtu.be/yrEKYkIK-Fw).

Feel free to contact me on [x(twitter)](https://twitter.com/vicsejas). if you have any questions.

## Instructions

### 1.- Setup your FastAPI project

You need to install.

**FastAPI**

```sh
pip install fastapi
```

**ASGI Server**

```sh
pip install "uvicorn[standard]"
```

**Templating Engine**

For this example we will be using Jinja2.

```sh
pip install Jinja2
```

### 2.- Return HTML from your FastAPI route

**Create a "templates" folder in your project**

You need to create a new "templates" folder and create a "base.html" file inside.

```sh
mkdir templates && touch templates/base.html
```

now we will add some basic html.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>
```

**Add the TemplateResponse to your route response**

Now we need setup Jinja2Templates with our "templates" folder and return a TemplateResponse in our index route.

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
```

### 3.- Create a "tailwindcss" folder on your project

Here we will be adding the TailwindCSS files.

```sh
mkdir tailwindcss
```

### 4.- Install TailwindCSS

Start a new terminal inside your project folder and change the working directory to the "tailwindcss" folder.

```sh
cd tailwindcss
```

and then run the following command, with the package manager you'd like to use.

#### npm

```sh
npm install -D tailwindcss @tailwindcss/cli 
```

#### pnpm

```sh
pnpm install -D tailwindcss @tailwindcss/cli 
```

#### yarn

```sh
yarn add -D tailwindcss @tailwindcss/cli
```

### 5.- Create a new folder "styles" inside your tailwindcss folder

Here we will be adding our custom styles.

For that we need to create a new "styles" folder inside our "tailwindcss" folder.

```sh
mkdir styles
```

now we need to create a new file "app.css" inside this folder.

```sh
touch styles/app.css
```

then add the following directives.

```css
@import "tailwindcss";
@source "../../templates";
```

### 6.- Run the TailwindCSS CLI build process

This proccess will generate a "app.css" file inside a new "static/css" folder.

The "--watch" flag will make sure that the styles are updated every time you make a change in your files.

```sh
npx @tailwindcss/cli -i ./styles/app.css -o ../static/css/app.css --watch
```

### 7.- Add the TailwindCSS stylesheet to your base.html file

**Mount the static folder**

In order to mount this folder we need to add the following lines to our main.py file.

Import the static files.

```python
from fastapi.staticfiles import StaticFiles
```

Add the static folder to your app.

```python
app.mount("/static", StaticFiles(directory="static"), name="static")
```

Now we can add the stylesheet to our base.html file.

```html
<link href="{{url_for('static',path='/css/app.css')}}" rel="stylesheet" />
```

### 8.- Serving compressed files with the GZip middleware

In order to serve compressed files we need to import the middleware.

add the middleware to your app.

```python
app.add_middleware(GZipMiddleware)
```

## Script for running the TailwindCSS CLI build process

We can create a script in the package.json file to run the TailwindCSS CLI build process.

```js
"scripts": {
    "dev": "npx @tailwindcss/cli -i ./styles/app.css -o ../static/css/app.css --watch"
},
```

And then simply run.

#### npm

```sh
npm run dev
```

#### pnpm

```sh
pnpm dev
```

#### yarn

```sh
yarn dev
```

to run the Tailwind CSS build process.

Now you have Tailwind CSS v4.0 set up in your FastAPI project.
