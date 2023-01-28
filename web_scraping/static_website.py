import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Find by ID
results = soup.find(id='ResultsContainer')

# Show html page
# print(results.prettify())

# Find all Elements by HTML Class Name
job_elems = results.find_all('div', class_='card-content')

# Job elements
print("Job elements: ", len(job_elems))
print("Show all job elements")
for job_elem in job_elems:
    # Each job_element is another BeautifulSoup() object
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('h3', class_='company')
    location_elem = job_elem.find('p', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    # You can add .text to a Beautiful Soup object to return only the text content of the HTML elements
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# Filter using a keyword
print("--------------")
print("Show Python Jobs")
# Looks for that string exactly
# python_jobs = results.find_all("h2", string="Python")
# You can pass functions as arguments,
# The lambda function looks at the text of each <h2> element,
# converts it to lowercase, and checks whether the substring "python" is found anywhere
python_jobs = results.find_all('h2',
                               string=lambda text: "python" in text.lower())

# for p_job in python_jobs:
#     link = p_job.find('a')['href']
#     print(p_job.text.strip())
#     print(f"Apply here: {link}\n")

# Access to third parent to retrieve information (card-content)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())
