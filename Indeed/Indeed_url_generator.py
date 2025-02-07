import urllib.parse

def generate_indeed_url_india(job_role, location, date_posted=None):
    base_url = "https://in.indeed.com/jobs?"
    query_params = {
        "q": job_role,  # Job role
        "l": location,  # Location
        "fromage": date_posted if date_posted else "",  # Date posted filter (e.g., "1" for last day)
    }
    # Encode the query parameters
    encoded_params = urllib.parse.urlencode(query_params)
    return base_url + encoded_params
