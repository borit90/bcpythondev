# Deployment Guide to Render.com

## Prerequisites
- A GitHub account (for linking your repository)
- A Render.com account (free)
- Gmail account with app-specific password enabled

## Step-by-Step Deployment

### 1. Set Up Gmail App Password
   - Go to your Google Account: https://myaccount.google.com/
   - Enable 2-Factor Authentication if not already enabled
   - Go to App passwords: https://myaccount.google.com/apppasswords
   - Select Mail → Windows Computer
   - Copy the 16-character password

### 2. Push Code to GitHub
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/borit90/mysite.git
   git push -u origin main
   ```

### 3. Deploy on Render.com
   1. Go to https://render.com and sign up/log in
   2. Click "New +" → "Web Service"
   3. Select "Deploy an existing repository"
   4. Connect your GitHub and select your repository
   5. Configure:
      - **Name**: mysite
      - **Environment**: Python 3
      - **Build Command**: `pip install -r requirements.txt`
      - **Start Command**: `gunicorn main:app`
      - **Plan**: Free

### 4. Set Environment Variables
   In Render dashboard for your service:
   1. Go to "Environment"
   2. Add the following variables:
      - `SECRET_KEY`: Generate a random string (use `python -c "import secrets; print(secrets.token_hex(32))"`)
      - `MAIL_USERNAME`: Your Gmail address
      - `MAIL_PASSWORD`: Your Gmail app password
      - `MAIL_DEFAULT_SENDER`: Your Gmail address
      - `FLASK_ENV`: `production`

### 5. Deploy
   - Click "Deploy Web Service"
   - Wait for build and deployment to complete
   - Your site will be live at: `https://mysite.onrender.com`

## Updating Your Site
   Simply push changes to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```
   Render will automatically redeploy with the latest code.

## Troubleshooting
- Check Render logs if deployment fails
- Verify all environment variables are set correctly
- Ensure `requirements.txt` includes all dependencies
- Test locally with `python main.py` before pushing

## Railway Deployment

Follow these steps to deploy the Flask app on Railway (recommended for backend deployments):

1. Create a Railway project
   - Go to https://railway.app and log in
   - Click "New Project" → "Deploy from GitHub"
   - Connect your GitHub account and select the repository

2. Configure the service
   - Choose the repo and branch to deploy
   - Set the environment to `Python`
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn main:app` (or Railway will honor the `Procfile` added to this repo)

3. Add required Environment Variables
   In your Railway project, open the service and go to the **Variables** (or **Environment**) tab and add:

   - `SECRET_KEY` — generate locally with:

     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```

   - `MAIL_USERNAME` — your Gmail address
   - `MAIL_PASSWORD` — your Gmail app password (16-character app password created after enabling 2FA)
   - `MAIL_DEFAULT_SENDER` — your Gmail address
   - `FLASK_ENV` — `production` (optional)

   Notes:
   - Railway sets a `PORT` environment variable for the runtime; `Procfile` and `gunicorn` will use it automatically.
   - Keep `MAIL_SERVER`, `MAIL_PORT`, and `MAIL_USE_TLS` as configured in `main.py` unless you need a different SMTP provider.

4. Gmail app password (if using Gmail SMTP)
   - Ensure your Google account has 2-Step Verification enabled
   - Create an App Password for Mail (follow Google's docs) and use it as `MAIL_PASSWORD`

5. Deploy and verify
   - Save variables and trigger a deploy (Railway redeploys automatically when variables change)
   - Watch build logs for `pip` and `gunicorn` output
   - Check runtime logs for Flask startup and any `mail.send()` warnings or errors

6. Confirm contact form route
   - Make sure you visit the backend route (`/contact`) served by Flask — the repo contains both a static `contact.html` and the backend template; static-hosting can serve the root static file instead of the Flask route if misconfigured. We updated the static `contact.html` to POST to `/contact` so the backend receives submissions.

Example local test commands

```bash
# create a virtualenv
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
export SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
export MAIL_USERNAME="your@gmail.com"
export MAIL_PASSWORD="your-app-password"
export MAIL_DEFAULT_SENDER="your@gmail.com"
python main.py
``` 

If you prefer Railway CLI, you can also set variables via the CLI after installing the Railway toolbelt (check Railway docs for exact commands).

## Final notes
- The app now includes basic mail error handling so missing SMTP credentials will not crash the service; check logs for delivery errors and ensure mail-related env vars are correct.
- If you want to disable email sending entirely in production, set the mail vars to empty and the app will flash a message instead of attempting to send.
