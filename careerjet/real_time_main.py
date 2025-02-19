import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://www.careerjet.co.in/jobs?s=java&l=india"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send GET request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract job listings using correct class names
job_listings = []
for job in soup.find_all("article", class_="job clicky"):
    title_tag = job.find("h2").find("a")
    company_tag = job.find("p", class_="company")
    location_tag = job.find("ul", class_="location").find("li")
    summary_tag = job.find("div", class_="desc")
    url_tag = title_tag["href"] if title_tag and title_tag.has_attr("href") else "N/A"
    
    title = title_tag.get_text(strip=True) if title_tag else "N/A"
    company = company_tag.get_text(strip=True) if company_tag else "N/A"
    location = location_tag.get_text(strip=True) if location_tag else "N/A"
    summary = summary_tag.get_text(strip=True) if summary_tag else "N/A"
    
    job_listings.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Summary": summary,
        "Job URL": "https://www.careerjet.co.in"+url_tag
    })

# Save extracted jobs to CSV
csv_file = "java_jobs.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Company", "Location", "Summary", "Job URL"])
    writer.writeheader()
    writer.writerows(job_listings)

print(f"Jobs saved to {csv_file}")
