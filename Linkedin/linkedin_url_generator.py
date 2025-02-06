import urllib.parse

# def generate_linkedin_job_url(keyword, location, experience=None, job_type=None, remote=None, date_posted=None):
#     base_url = "https://www.linkedin.com/jobs/search/"

#     params = {
#         "keywords": keyword,
#         "location": location,
#     }

#     # Add optional filters
#     if experience:
#         params["f_E"] = experience  # Example: "1,2" for Internship & Entry-level
#     if job_type:
#         params["f_JT"] = job_type  # Example: "F" for Full-time
#     if remote:
#         params["f_WT"] = remote  # Example: "3" for Remote
#     if date_posted:
#         params["f_TPR"] = date_posted  # Example: "r604800" for past 7 days

#     # Encode the parameters properly
#     query_string = urllib.parse.urlencode(params, safe=",")
#     return f"{base_url}?{query_string}"


def generate_linkedin_job_url():
    """Generates a LinkedIn job search URL based on user input."""
    base_url = "https://www.linkedin.com/jobs/search/?"
    
    experience_map = {"Internship": "1", "Entry-level": "2", "Associate": "3"}
    job_type_map = {"Full-time": "F", "Part-time": "P", "Contract": "C", "Internship": "I"}
    remote_map = {"On-site": "1", "Hybrid": "2", "Remote": "3"}
    date_posted_map = {"24 hours": "r86400", "1 week": "r604800", "1 month": "r2592000"}
    industry_map = {"Software": "4", "Finance": "96", "Education": "142"}
    
    keyword = input("Enter job keyword: ").strip().replace(" ", "%20")
    location = input("Enter job location: ").strip().replace(" ", "%20")
    experience = experience_map.get(input("Enter experience level (Internship, Entry-level, Associate): "), "")
    job_type = job_type_map.get(input("Enter job type (Full-time, Part-time, Contract, Internship): "), "")
    remote = remote_map.get(input("Enter remote work type (On-site, Hybrid, Remote): "), "")
    date_posted = date_posted_map.get(input("Enter date posted filter (24 hours, 1 week, 1 month): "), "")
    company = input("Enter company ID (optional, leave blank if not needed): ").strip()
    industry = industry_map.get(input("Enter industry filter (Software, Finance, Education): "), "")
    
    query_params = [
        f"keywords={keyword}",
        f"location={location}",
        f"f_E={experience}" if experience else "",
        f"f_JT={job_type}" if job_type else "",
        f"f_WT={remote}" if remote else "",
        f"f_TPR={date_posted}" if date_posted else "",
        f"f_C={company}" if company else "",
        f"f_I={industry}" if industry else ""
    ]
    
    linkedin_url = base_url + "&".join(filter(None, query_params))
    return linkedin_url

