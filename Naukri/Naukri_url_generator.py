def generate_naukri_job_url():
    """Generates a Naukri.com job search URL based on user input."""
    base_url = "https://www.naukri.com/"
    
    keyword = input("Enter job keyword: ").strip().replace(" ", "-")
    location = input("Enter job location: ").strip().replace(" ", "-")
    
    experience_map = {f"{i} years": str(i) for i in range(1, 31)}
    wfhtype_map = {"work from office": "0", "hybrid": "3", "remote": "2"}
    ctcfilter_map = {"3": "0to3", "6": "3to6", "10": "6to10", "15": "10to15", "25": "15to25", "50": "25to50"}
    
    job_age = input("Enter job age (in days, leave blank if not needed): ").strip()
    experience = experience_map.get(input("Enter experience (in years, leave blank if not needed): ").strip().lower(), "")
    wfhtype = wfhtype_map.get(input("Enter work type (work from office, hybrid, remote, leave blank if not needed): ").strip().lower(), "")
    
    ctc_filters = input("Enter salary ranges (in LPA, separated by commas, leave blank if not needed): ").strip().lower().split(",")
    ctc_filters = [ctcfilter_map.get(ctc.strip(), "") for ctc in ctc_filters if ctcfilter_map.get(ctc.strip(), "")]
    
    query_params = [f"{keyword}-jobs-in-{location}"]
    base_url=f"{base_url}{'/'.join(query_params)}"
    query_params = []
   
    if job_age: query_params.append(f"jobAge={job_age}")
    if experience: query_params.append(f"experience={experience}")
    if wfhtype: query_params.append(f"wfhType={wfhtype}")
    for ctc in ctc_filters:
        query_params.append(f"ctcFilter={ctc}")
    if(query_params is not None):
        naukri_url = f"{base_url}?{'&'.join(query_params)}"
    else:
        naukri_url = base_url
    print(naukri_url)
    return naukri_url
