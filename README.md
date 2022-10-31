## SwachBin Flask API

## Get Started

Clone the repo:

```bash
git clone https://github.com/Dhaan-Zero-Hunger/DhaanAPI.git
```

Install the project dependencies:

```bash
npm i
```

## Set Up Dhaan APP

### Step 1: Adding Auth0 configuration variables to Node.js

Under the project directory, create a hidden file called `.env` to store configuration variables and secrets that your app needs:

```bash
touch .env
```

Add the following to `.env`:

```bash
AUTH0_CLIENT_ID=
AUTH0_DOMAIN=
AUTH0_CLIENT_SECRET=
SESSION_SECRET=
AUTH0_CALLBACK_URL=http://localhost:3000/callback
```

- `AUTH0_DOMAIN` is your **Domain** value from the "Settings".

- `AUTH0_CLIENT_ID` is your **Client ID** from the "Settings".

- `AUTH0_CLIENT_SECRET` is your **Client Secret** from the "Settings".

Execute the following command to generate a suitable string for the session secret:

```bash
node -e "console.log(crypto.randomBytes(32).toString('hex'))"
```

Copy and paste the output of the command above as the value for `SESSION_SECRET` in `.env`.

**Make sure to add this `.env` file to `.gitignore` so that it isn't committed to version control**.

## Run the Express Web App with Live Reload

Run the server using `nodemon` under the hood:

```bash
npm run dev
```

In a separate terminal window, serve the client from a static server using Browsersync under the hood:

```bash
npm run ui
```

> Browsersync proxies the server running on port `8000` with `nodemon`. Check out the npm script commands present in `package.json` for more details.

To see the app in action, visit [`http://localhost:3000`](http://localhost:3000) on your browser.

