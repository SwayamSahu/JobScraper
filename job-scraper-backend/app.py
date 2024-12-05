from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import threading

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Global variable to store job results
job_results = []

# Function to scrape data from RemoteOK
def scrape_jobs(keyword):
    global job_results
    job_results.clear()  # Clear previous results before scraping

    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all job listings based on the structure you provided
        job_listings = soup.find_all('td', class_='company position company_and_position')

        # Loop through each job listing and extract job title and company name
        for job in job_listings:
            job_title = job.find('h2', itemprop='title').text.strip() if job.find('h2', itemprop='title') else None
            company_name = job.find('h3', itemprop='name').text.strip() if job.find('h3', itemprop='name') else None
            
            if job_title and company_name:
                job_results.append({
                    'company_name': company_name,
                    'job_title': job_title
                })
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching job listings: {e}")

# Define the route to scrape jobs
@app.route('/scrape', methods=['GET'])
def scrape():
    keyword = request.args.get('keyword')  # Get the keyword from query params
    if not keyword:
        return jsonify({"error": "Keyword is required!"}), 400

    # Create and start the scraping thread
    scrape_thread = threading.Thread(target=scrape_jobs, args=(keyword,))
    scrape_thread.start()

    # Wait for the scraping thread to finish
    scrape_thread.join()

    # Return the scraped results as JSON
    return jsonify(job_results)

# Define the root route
@app.route('/')
def home():
    return "Welcome to the job scraping API. Use '/scrape?keyword=<keyword>' to scrape jobs."

if __name__ == '__main__':
    app.run(debug=True)
