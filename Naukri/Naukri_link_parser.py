from bs4 import BeautifulSoup

def extract_rating(rating_a):
    if rating_a is None or rating_a.find('span', class_="main-2") is None:
        return "None"
    else:
        return rating_a.find('span', class_="main-2").text


def parse_job_data_from_soup(page_jobs):
    print("********PAGE_JOBS***********")
    for job in page_jobs:
        job = BeautifulSoup(str(job), 'html.parser')
        row1 = job.find('div', class_="row1")
        row2 = job.find('div', class_="row2")
        row3 = job.find('div', class_="row3")
        row4 = job.find('div', class_="row4")
        row5 = job.find('div', class_="row5")
        row6 = job.find('div', class_="row6")
        
        job_title = row1.a.text
        company_name = row2.span.a.text
        rating_a = row2.span
        rating = extract_rating(rating_a)
        
        job_details = row3.find('div', class_="job-details")
        ex_wrap = job_details.find('span', class_="exp-wrap").span.span.text
        location = job_details.find('span', class_="loc-wrap ver-line").span.span.text

        # min_requirements = row4.span.text

        all_tech_stack = []
        ul_tag = row5.find("ul", class_="dot-gt tag-li")  # Ensure correct class name
        if ul_tag:
            for tech_stack in row5.ul.find_all('li', class_="dot-gt tag-li"):
                tech_stack = tech_stack.text
                all_tech_stack.append(tech_stack)

        print(f"Job Title : {job_title}")
        print(f"Company Name : {company_name}")
        print(f"Rating : {rating}")
        print(f"Experience : {ex_wrap}")
        print(f"Location : {location}")
        # print(f"Minimum Requirements : {min_requirements}")
        print(f"All Tech Stack : {all_tech_stack}")
        print("***************END***************")
    print("********PAGE_JOBS END***********")
