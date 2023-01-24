import os

ENV = "DEV"
#ENV = "PROD"

# Server
host = "0.0.0.0"
port = int(os.environ.get("Port", 5000))

# Info
app_name = "Undergraduate Snapshot"
fontawesome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/fount-awesome.min.css"
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

about = "Move the sliders to a relevant value and you will get a snapshot of what your week may look like on your journey at MSU. Feel free to hover over the titles for more information."
disclaimer = "The purpose of this Dashboard is to provide students with insights into how their time at MSU Denver may be allocated.\
It gives the student a snapshot of the hours in a week and how they will be spent based on the student input.\n\n\
*Note: This Dashboard utilizes certain assumptions that students should be aware of:\n\
1) Calulations are based on students seeking an undergraduate degree that requires 120 credit hours. These credit hours are earned by taking\
 classes specific to the degree they are seeking. Students should always consult an academic advisor when planning for graduation.\
Students should utilize the Degree Progress Report and the MSU Denver Academic Advisor page that are linked above.\n\
2) Calculations are based on a student taking only the fall and spring semesters. Taking classes during the summer may help a student\
 graduate in a shorter time frame than predicted by this dashboard.*"

progress = "https://degreeworks.msudenver.edu/Dashboard"
advisors = "http://msudenver.edu/advising"
sleep = "https://learningcenter.unc.edu/tips-and-tools/sleeping-to-succeed/"
study = "https://www.collegiateparent.com/academics/student-study-time-matters/"
stress = "https://www.bestcolleges.com/resources/balancing-stress/"

image = "data:image/png;base64,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"