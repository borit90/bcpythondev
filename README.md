# BC Python Developer Website

A professional portfolio website for BC Python Developer, built with Flask and Bootstrap.

## Features

- **Home Page**: Introduction and overview of services
- **About Me**: Personal background and expertise
- **Services**: Detailed list of offered services
- **Portfolio**: Showcase of completed projects
- **Contact**: Contact form and information

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome (via CDN)

## Installation

This repository now includes a static website build that is ready for GitHub Pages hosting. The static pages are served from the repository root, and the existing Flask application is preserved for local or backend-based deployments.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bc-python-developer-website
   ```

2. If you want to run the Flask application locally:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python main.py
   ```

3. Visit the static site locally by opening `index.html` in your browser, or use the Flask app at `http://localhost:5000`.

## Project Structure

```
bc-python-developer-website/
├── index.html              # Static home page for GitHub Pages
├── about.html              # Static about page
├── services.html           # Static services page
├── portfolio.html          # Static portfolio page
├── contact.html            # Static contact page
├── 404.html                # Static 404 error page
├── main.py                 # Flask application (local/backend use)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── templates/              # Flask templates (optional backend version)
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── portfolio.html
│   └── contact.html
└── static/                 # Static files
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/             # Place your images here
```

## Customization

### Adding Images
Place your images in the `static/images/` directory. The following images are referenced in the templates:

- `python-logo.png`: Python logo for the home page
- `profile.jpg`: Profile picture for the about page
- `project1.jpg` through `project6.jpg`: Project screenshots for the portfolio page

You can replace these with your own images or use placeholder images from services like Lorem Picsum.

### Changing Content
Edit the HTML templates in the `templates/` directory to update content, or modify the Flask routes in `main.py` for dynamic content.

### Styling
Modify `static/css/style.css` to customize the appearance of the website.

## Deployment

### GitHub Pages

The site is now compatible with GitHub Pages as a static website. The HTML pages are located in the repository root, and the static assets stay under `static/`.

To deploy with GitHub Pages:

1. Push the repository to GitHub.
2. Open the repository Settings > Pages.
3. Select the `main` branch (or your default branch) and the `/ (root)` folder.
4. Save and visit the published URL.

### Flask / Backend Deployment

The Flask app still exists in `main.py` for local development or backend deployment, but GitHub Pages will only host the static HTML and assets.

- **Heroku**: Use gunicorn as the WSGI server
- **AWS/GCP/Azure**: Deploy as a containerized application
- **PythonAnywhere**: Direct deployment of Flask apps

## Contact

For questions or collaborations, contact BC at contact@bcpythondeveloper.com

## License

This project is open source and available under the [MIT License](LICENSE).