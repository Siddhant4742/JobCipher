# from Linkedin.linkedin import linkedin
# # from Indeed.indeed import indeed
# from Naukri.naukri_selenium import naukri
# keyword=""
# location=""
# experience=""
# job_type=""
# remote=""
# date_posted=""
# company=""
# industry=""
# ctc_filters=""
# # def user_input():
# #     global keyword,location,experience,job_type,remote,date_posted,company,industry,ctc_filters
# keyword = input("Enter job keyword: ").strip()
# location = input("Enter job location: ").strip()
# experience = input("Enter experience level (In years put 1 for entry level): ")
# job_type = input("Enter job type (Full-time, Part-time, Contract, Internship): ").strip().lower()
# remote = input("Enter remote work type (On-site, Hybrid, Remote): ").strip().lower()
# date_posted = input("Enter date posted filter (24 hours, 1 week, 1 month): ").strip().lower()
# company = input("Enter company ID (optional, leave blank if not needed): ").strip()
# industry = input("Enter industry filter (Software, Finance, Education): ")
# ctc_filters = input("Enter salary ranges (in LPA, separated by commas, leave blank if not needed): ").strip().lower().split(",")



# linkedin(keyword,location,experience,job_type,remote,date_posted,company,industry)
# naukri(keyword,location,experience,remote,ctc_filters,date_posted)
# # indeed(keyword,location,date_posted)

import threading
from Linkedin.linkedin import linkedin
from Naukri.naukri_selenium import naukri

# User Inputs
keyword = input("Enter job keyword: ").strip()
location = input("Enter job location: ").strip()
experience = input("Enter experience level (In years, put 1 for entry level): ").strip()
job_type = input("Enter job type (Full-time, Part-time, Contract, Internship): ").strip().lower()
remote = input("Enter remote work type (On-site, Hybrid, Remote): ").strip().lower()
date_posted = input("Enter date posted filter (24 hours, 1 week, 1 month): ").strip().lower()
company = input("Enter company ID (optional, leave blank if not needed): ").strip()
industry = input("Enter industry filter (Software, Finance, Education): ").strip()
ctc_filters = input("Enter salary ranges (in LPA, separated by commas, leave blank if not needed): ").strip().lower().split(",")

# Creating Threads
linkedin_thread = threading.Thread(target=linkedin, args=(keyword, location, experience, job_type, remote, date_posted, company, industry))
naukri_thread = threading.Thread(target=naukri, args=(keyword, location, experience, remote, ctc_filters, date_posted))

# Starting Threads
linkedin_thread.start()
naukri_thread.start()

# Wait for both threads to finish
linkedin_thread.join()
naukri_thread.join()

print("Both job searches completed!")
