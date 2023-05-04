# Django + Vite + Alpine.js + Pico.css + rest framework

My boilerplate to quickstart all my projects.

## Installation

-   Create a virtual enviornment and activate it
-   Clone the project

Type below command to install npm+pip packages

```
npm run setup
```

-   Change the **SECRET_KEY** in **core/settings.py** to your own, you can use https://djecrety.ir/

Start Vite

```
npm run dev
```

Start Django

```
npm run server
```

Navigate to **127.0.0.1:8000** in browser

![alt text](https://i.imgur.com/X02eIjo.png)

Done!

## Updating Pico CSS

To import the latest css files into your django project install gulp-cli globally

```
npm install --global gulp-cli
```

Update pico

```
npm update @picocss/pico
```

Copy files

```
gulp copy-pico
```

## Building for production

```
npm run build
```

All your files will be in **static/dist**

<hr>

That's it! have fun making websites. 🙂
