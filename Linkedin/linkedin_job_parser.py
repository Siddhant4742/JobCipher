from bs4 import BeautifulSoup
from datetime import datetime


def parse_all_job_details(file_path):
    count=0
    # Open and read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all job listings (assuming each job entry is in a div with a specific class)
    job_cards = soup.find_all("div", class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")

    # Keep track of processed job listings using a set of tuples (company_name, location, company_link, time_posted)
    processed_jobs = set()

    # Loop through all job listings and extract details
    for job_card in job_cards:
        # Extract company name and company link
        company_name_tag = job_card.find("a", class_="hidden-nested-link")
        company_name = company_name_tag.text.strip() if company_name_tag else "No company name"
        company_link = company_name_tag['href'] if company_name_tag else "No company link"

        # Skip job listing if company name contains '*'
        if '*' in company_name:
            continue

        # Extract location
        location = job_card.find("span", class_="job-search-card__location")
        location = location.text.strip() if location else "No location"

        # Extract time posted (getting the datetime attribute)
        time_posted_tag = job_card.find("time", class_="job-search-card__listdate")
        time_posted = time_posted_tag['datetime'] if time_posted_tag else None

        # Calculate how long ago the job was posted
        if time_posted:
            time_posted_datetime = datetime.strptime(time_posted, "%Y-%m-%d")
            current_time = datetime.now()
            time_diff = current_time - time_posted_datetime

            # Format time difference (in days, weeks, etc.)
            if time_diff.days < 1:
                time_posted = "Posted today"
            elif time_diff.days == 1:
                time_posted = "Posted 1 day ago"
            else:
                time_posted = f"Posted {time_diff.days} days ago"
        else:
            time_posted = "No time posted"

        # Extract job posting link (correcting the class)
        job_posting_tag = job_card.find("a", class_="base-card__full-link")
        job_posting_link = job_posting_tag["href"] if job_posting_tag else "No job posting link"

        # Create a tuple of the job details to check for duplicates
        job_details = (company_name, location, company_link, time_posted, job_posting_link)

        # Skip this job listing if it has already been processed
        if job_details in processed_jobs:
            continue

        # Add the job details to the processed set
        processed_jobs.add(job_details)

        # Print the extracted details for the first instance of each unique job listing
        print(f"Company: {company_name}")
        print(f"Company Link: {company_link}")
        print(f"Location: {location}")
        print(f"Time Posted: {time_posted}")
        print(f"Job Posting Link: {job_posting_link}")
        count+=1
        print("-" * 50)  # Separator between job listings
    print(count)
    


