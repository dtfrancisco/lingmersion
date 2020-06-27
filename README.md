# lingmersion
Lingmersion is a language-based flashcard app. Users can create and edit flashcards in a list. They can also other view other user lists. This app is built with Vue in the frontend and Flask in the backend.

## Npm and Vue setup
To run this project, you will need to install Vue. Vue can be installed through npm or used by downloading and including it in a script tag or by using the latest version with a CDN and including it in a script tag.

Npm is the recommended way to install Vue by the Vue official docs https://vuejs.org/v2/guide/installation.html. ```npm install``` will install the Node package manager. Use the ```npm run serve``` command to compile the app and have live reloads or run the ```vue ui``` command and use the popped up window at http://localhost:8000/ to compile the project. The vue ui command allows developers to easily add plugins like Vuex, manage dependencies, and view statistics. The app is ran on http://localhost:8080/.

Some more npm commands are available below.

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
### Customize Vue configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Python and Flask setup
This project also needs to have Python and Flask installed. Python can be installed from https://www.python.org/ and Flask can be installed with the ```pip install flask``` command. Pip will be installed automatically when Python is installed. The backend is ran on http://localhost:5000/.

## Python packages used
Look at backend/requirements.txt for a complete list of packages with their corresponding version numbers installed.

## How to use
When the app is started, the user is taken to the home page. The home page contains a list of flashcards that have already been created. New lists can be added to the home page. Clicking a link to a list of flashcards will take the user to an editable screen where they can change the properties (name, author, and cards). New cards can be added to the list. The terms of each card will fetch a MP3 from the ForvoAPI.

## Run for development

To run the frontend server, navigate to the frontend folder and run the ```npm run serve``` command to compile the app. Once the app has finished compiling, the terminal will tell you the local and network URLs the app is running at. To run the backend server, activate your virtual environment where Flask is installed, enter the ```export FLASK_APP=[*Insert name of Python file where Flask app is launched*].py``` command and the ```flask run ``` command. Alternatively, save the FLASK_APP information in a .env file if you do not want to repeat this process every time you run the backend server. Additionally, this program expects the FORVO_API_KEY field to be read from a .env file. This is where you provide your Forvo API key.