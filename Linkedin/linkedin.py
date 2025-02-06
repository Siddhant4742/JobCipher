from linkedin_url_generator import generate_linkedin_job_url
from linkedin_job_fetcher import fetchAndSave
from linkedin_job_parser import parse_all_job_details
# Function to parse the HTML file and extract details for multiple jobs



# Example usage
# Generate LinkedIn job search URL
url = generate_linkedin_job_url()
print("Generated LinkedIn URL:", url)
file_path = "data/text_3.html"
fetchAndSave(url, file_path)



# Call the function to parse and display the details for all job listings
parse_all_job_details(file_path)
