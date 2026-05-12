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

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bc-python-developer-website
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
bc-python-developer-website/
├── main.py                 # Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── portfolio.html
│   └── contact.html
└── static/                # Static files
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/            # Place your images here
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

This Flask application can be deployed to various platforms:

- **Heroku**: Use gunicorn as the WSGI server
- **AWS/GCP/Azure**: Deploy as a containerized application
- **PythonAnywhere**: Direct deployment of Flask apps

## Contact

For questions or collaborations, contact BC at contact@bcpythondeveloper.com

## License

This project is open source and available under the [MIT License](LICENSE).