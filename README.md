## Project Name: **JobScraper**

---

**JobScraper** is a web application that allows users to search for job listings with specific keywords. The application scrapes data from various job boards and presents it in an easy-to-read format. It consists of a Flask backend for scraping job data and a React frontend for displaying the data in a user-friendly UI.

## Features
- Scrape job listings from a job board (e.g., Remote OK).
- Search for jobs by keyword.
- Display job title, company name, and other relevant job details.
- Dynamic data fetching and display via React.
- Fully responsive design to support multiple screen sizes.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x or higher
- Node.js (with npm or yarn)
- Flask
- React (Vite)
- Dependencies for both Flask and React (will be installed automatically)

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jobscraper.git
cd jobscraper
```

### 2. Setup Flask Backend

#### a. Install Python dependencies

Navigate to the backend folder (`backend`) and create a virtual environment (optional but recommended):

```bash
cd job-scraper-backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### b. Install Flask and other required packages

```bash
pip install -r requirements.txt
```

- `Flask`: For the backend API.
- `requests`: For making HTTP requests.
- `BeautifulSoup`: For scraping job listings.
- `Flask-CORS`: To handle Cross-Origin Resource Sharing (CORS).

#### c. Run Flask Backend

```bash
flask run
```

This will start the Flask server at `http://127.0.0.1:5000/`.

### 3. Setup React Frontend

#### a. Install dependencies

Navigate to the frontend folder (`frontend`) and install the necessary packages:

```bash
cd job-scraper-frontend
npm install  # or use yarn install
```

#### b. Start the React Development Server

```bash
npm run dev  # or use yarn dev
```

This will start the React app at `http://localhost:5173/`.

### 4. Ensure Both Servers are Running

- Flask API should be running at `http://127.0.0.1:5000/`.
- React frontend should be running at `http://localhost:5173/`.

---

## How to Use the App

1. Open the React frontend in your browser (`http://localhost:5173/`).
2. Enter a job keyword (e.g., "developer", "designer", etc.) into the search input.
3. Press the "Fetch Jobs" button.
4. View the list of job titles and company names that match your keyword.
5. The data is fetched dynamically from the backend, which scrapes job listings from job boards.

---

## Folder Structure

```plaintext
JobScraper/
├── backend/
│   ├── app.py               # Flask API to scrape data and handle requests
│   ├── requirements.txt     # Python dependencies
│   └── ...                  # Other backend-related files
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── index.css        # Styles for the frontend
│   │   └── ...              # Other frontend-related files
│   ├── package.json         # Frontend dependencies and scripts
│   └── ...                  # Other frontend-related files
└── README.md                # Project documentation
```

---

## Notes

- The backend scrapes data from a job board (e.g., Remote OK) and returns job titles and company names in JSON format.
- The frontend provides a simple interface where users can search for jobs and view the results in a table.
- For any issues related to CORS (Cross-Origin Resource Sharing), make sure you have `Flask-CORS` configured correctly in the backend.
