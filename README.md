# JobScraper

```
job-scraper-app/
├── backend/                # Backend code (FastAPI)
│   └── ...
├── frontend/               # Frontend code (React + Vite)
│   └── ...
└── README.md               # High-level documentation
```

```
backend/
├── app/
│   ├── __init__.py         # Makes this directory a Python package
│   ├── main.py             # Entry point of the FastAPI application
│   ├── routes.py           # Contains API route definitions
│   ├── scraper.py          # Logic for scraping jobs from Wellfound
│   ├── models.py           # Define data models and schemas (if needed)
│   ├── utils.py            # Utility functions (optional)
│   └── config.py           # Configuration settings (optional)
├── requirements.txt        # Python dependencies
├── README.md               # Documentation for backend setup and usage
└── .env                    # Environment variables (if needed)
```

```
frontend/
├── public/
│   ├── index.html          # Main HTML file
│   └── favicon.ico         # Favicon for the app
├── src/
│   ├── components/         # Reusable UI components
│   │   ├── JobTable.jsx    # Component to display job data
│   │   └── SearchBar.jsx   # Component for keyword input and search button
│   ├── pages/              # Main pages of the app
│   │   └── Home.jsx        # Homepage containing the main logic
│   ├── services/           # API service for Axios calls
│   │   └── api.js          # Handles API requests
│   ├── App.jsx             # Main App component
│   ├── main.jsx            # Application entry point
│   └── index.css           # Global styles
├── package.json            # Node.js dependencies
├── vite.config.js          # Vite configuration
└── README.md               # Documentation for frontend setup and usage
```
