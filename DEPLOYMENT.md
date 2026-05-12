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
