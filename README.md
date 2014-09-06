There's a Job for That
======================

A tool to guide job seekers, in plain language, to the jobs or careers that match their skills, goals, and needs. We see this as a supplementary tool that could be embedded on a larger job-seeking site.

Ideated at the White House Data Jam on 21st Century Jobs.

Synopsis (DRAFT):


This app will help job seekers find jobs or careers that match their skills, goals, and needs. We are especially focused on people who are unemployed or are looking for a new job. Our focus on searching for low- to middle-skilled jobs -- occupations that often require an associates degree or industry certificate. The challenge is that the language that job-seekers use often does not match well to the language of the career databases (or the language in job ads). 

Examples include: returning veterans looking to make use of skills learned in the military, people who do not know how ot explain their skills well or do not know what sorts of jobs might match, people looking to change jobs (for example, looking for ideas of what industries might have appropriate jobs for them, and people with strong soft skills (personable, customer service oriented, etc.).

This app will help people match their own explanations of their skills to those jobs, and (indirectly) teach them some of the jobs-related "resume jargon" they might use to write their own resume, fill out a job application, or use in an interview. 

Data analysis issues
We are considering developing a schema / metadata model (or algorithm) that makes such matches easier / more accurate than what's currently out there (lots of erroneous matches).

Extensions of the idea:
This work could also lead to:
1. A tool to help employers write job descriptions more accurately and in a way that helps them tap into the broadest appropriate pool of aplicants. 
2. Support for a resume-writing applications





This repository holds
---------------------

1. Original ideation materials: from the June 25th, 2014, White House session on 21st Century Jobs
2. User stories
3. Wireframes
4. Data memos: Documenting usage of datasets and algorithms, as well as needs for data sharing
5. API documentation: sources, intended calls
6. Skeleton Python/Flask app code: for simple use in demonstrating the click-through/swipe-through.




Python_Flask app code
---------------------
The Python/Flask app is deployed on Heroku as a tool for showing the user's click/swipe-through workflow as design evolves.

Visit the app at: 
http://theres-a-job-for-that.herokuapp.com

A Postgres database drives the app.

An original API constructed for the backend:
- Accepts: keywords and question responses
- Returns: job titles and questions 
