# Lecture


### Types of projects
* benchmarking new techniques
* new use-case for existing technique


### At LHL
* one mini project in pairs, midterm project in pairs, final project is open-ended 
* feature engineering and dimensionality reduction... 

* when in pairs - different sub-tasks, and files

### Code
* define functions/classes whenever possible
* persist model - set global variable - save trained  model and only retain when needed 

* save results of a GET
* each cell should have clearly defined goal
* revisit and clean up code 

### Version Control
* git pulls merges with current 
* git clone when pulling for the first time

### Presentation structure:
* motivation, task, modeling, results, conclusions


-----
# mini project help
```
url = "https://api.tfl.gov.uk/Journey/Meta/Modes"
r = re.get(url)
json = r.json()
modes = list(set([item.get('modeName') for item in json]))
print('Planned duration:')
for m in modes:
    if m.lower() in ["bus", "tube"]:
        r = re.get(f'https://api.tfl.gov.uk/Journey/JourneyResults/51.4700%2C%20-0.4543/to/51.5055%2C%20-0.0754?mode={m}')
        json = r.json()

        if r.status_code == 200:

            journeys = json['journeys']
            durations = []
            for j in journeys:
                durations.append(j.get('duration'))

            print(f'{m.capitalize()}: {min(durations)} minutes')

        else:
            print(f"{m.capitalize()}: {json['message']}")
```