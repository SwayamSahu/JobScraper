import { useState } from 'react';

function JobList() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [keyword, setKeyword] = useState('');
  const [error, setError] = useState(null);

  // Function to fetch the job data from the backend API
  const fetchJobs = async () => {
    if (!keyword) {
      alert("Please enter a keyword to search for jobs.");
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`http://127.0.0.1:5000/scrape?keyword=${keyword}`);
      const data = await response.json();
      if (response.ok) {
        setJobs(data);
      } else {
        setError("Failed to fetch job data. Please try again.");
      }
    } catch (error) {
      setError("Error fetching job data. Please check the backend.");
    }
    setLoading(false);
  };

  return (
    <div>
      <div>
        <input
          type="text"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          placeholder="Enter job keyword"
        />
        <button onClick={fetchJobs}>Fetch Jobs</button>
      </div>

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {jobs.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Job Title</th>
              <th>Company Name</th>
            </tr>
          </thead>
          <tbody>
            {jobs.map((job, index) => (
              <tr key={index}>
                <td>{job.job_title}</td>
                <td>{job.company_name}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default JobList;
