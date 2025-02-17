from bs4 import BeautifulSoup
import time
# from Indeed.Ineed_driver_setup import setup_driver
from Ineed_driver_setup import setup_driver

def scrape_indeed_jobs(url):
    driver = setup_driver()
    driver.get(url)

    # Wait for the page to load (adjust the sleep time if needed)
    time.sleep(5)

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()  # Close the browser

    # Find the job listings container
    allData = soup.find("div", {"class": "mosaic-provider-jobcards"})

    if allData is None:
        print("Could not find the job listings container. The HTML structure might have changed.")
        return []

    # Extract job listings
    job_listings = []
    alllitags = allData.find_all("li", {"class": "eu4oa1w0"})

    for job in alllitags:
        job_info = {}
        try:
            job_info["Job Title"] = job.find("a").find("span").text.strip()
        except:
            job_info["Job Title"] = "N/A"

        try:
            job_info["Company"] = job.find("span", {"data-testid": "company-name"}).text.strip()
        except:
            job_info["Company"] = "N/A"

        try:
            job_info["Location"] = job.find("div", {"data-testid": "text-location"}).text.strip()
        except:
            job_info["Location"] = "N/A"

        try:
            job_link = job.find("a", href=True)["href"]
            job_info["Job Link"] = f"https://in.indeed.com{job_link}"
        except:
            job_info["Job Link"] = "N/A"

        try:
            date_posted = job.find("span", {"class": "date"}).text.strip()
            job_info["Date Posted"] = date_posted
        except:
            job_info["Date Posted"] = "N/A"

        job_listings.append(job_info)

    return job_listings
