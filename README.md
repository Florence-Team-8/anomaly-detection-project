![image](https://user-images.githubusercontent.com/80718680/126676948-7fc31166-47a0-4153-98b1-2877955ac0e1.png)



Hello,

Welcome to the README file for our "Detecting Anomalous Network Access Project".


_________________

## Planning Process

The TRELLO board used for the planning process can be found on this link: [Trello](https://trello.com/b/LA6GxLOI/anomaly-detection)

_________________


## Data Dictionary
-  Please use this data dictionary as a reference for the variables used within in the data set.


| Column Name  | Description                                                                                  | Type                                               |
|--------------|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| `date`       | Date and time request was made                                                               | object (transformed to dateteime for some section) |
| `endpoint`   | Address of endpoint requested                                                                | object                                             |
| `user_id`    | Assigned id of person making request                                                         | int64                                              |
| `cohort_id`  | Numeric ID of cohort user belongs to. Key for `name`                                         | float64                                            |
| `source_id`  | IP address request was made from                                                             | object                                             |
| `name`       | Name (as string) of cohort user belongs to                                                   | object                                             |
| `start_date` | The cohort start date                                                                        | object (transformed to datetime for some sections) |
| `end_date`   | The cohort end date                                                                          | object (transformed to datetime for some sections) |
| `program_id` | Numeric ID to represent what program the cohort belongs to                                   | float64                                            |
| `is_active`  | Boolean value of whether or not the student was active in a cohort when the request was made | int64 (boolean)                                    |
| `pings`      | Numeric column for aggregating active and inactive pings                                     | int64                                              |

**Program ID Codes** 

1 - Full stack PHP

2 - Java

3 - Data Science

4 - Front End Program

---- 
#### Which lesson appears to attract the most traffic consistently across cohorts (per program)?

> Javascript-i had the most traffic for both the Full Stack PHP & Java programs. This makes sense since JavaScript is a highly used programming language for web developers because it allows users to interact with web pages.  While the most accessed for Data Science was the classification overview.  The Classification Methodology is the most used for Supervised Learning.

#### Which lessons are least accessed?

> Full Stack PHP & Java did not  have similar low accessed endpoints as they did for the most accessed endpoints. The lowest accessed for Full stack program was classes and objects lessons and object oriented programming. For the Java program, it was a Power analysis lesson. 

> The lowest accessed pages for Data Science included the storytelling creating dashboards lesson, and several pages in the advanced topics section (developing data products). 
Program 4 (Front End Program) was not used in the responses for the most and least accessed endpoints since it was a test group.

#### Is there a cohort that referred to a lesson significantly more, that other cohorts seemed to gloss over?

> Data Science cohorts (program ID 3), at first glance, appear to be viewing different lessons more often. But based on the knowledge of how the curriculum has changed over time, this seems reasonable. While all cohorts (minus Darden) had some version of the intro to data science lesson on there, Darden's lower view count on this could be explained by the curriculum changing during their tenure). Early cohorts (Bayes and Curie) viewed the regression overview lesson much more than the other cohorts, while from Darden onward the Classification Overview lesson was by far the most viewed. The change in the curriculum (to teaching classification first before regression) could be the cause of this as well. 

> Web development students (program ID 2) appear to be accessing the same several lessons over and over across the cohorts (Java i, ii, iii, html-css, jquery, and spring). This may be due to the program and curriculum, being more established by this point. This suggests that these lessons are consistently valuable to the web dev students.

#### Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
- Most of the pings are either towards the end of the program, or immediately the day after
- Some have a lot of pings at the beginning of the program start and stop once it hits two weeks
- about a third only ping the day of the program start or after

>There are a few possible explanations for this.  Perhaps the user unenrolled, or they changed their github user status. What is interesting is that some users only pinged towards the end of the program, the others pinged for the first two weeks. My assumption is that it could be a staff member pinging the system or it's people that left after two weeks
>Users 49,64, 278, 812, and 832 accessed the curriculum towards the end of the program
>Users 487, 1060 and 1065 accessed the curriculum within two weeks of the start date
>889 and 1059 access the database over a week or two and then stops.

#### What topics are grads continuing to reference after graduation and into their jobs (for each program)?
>DS students ping the system the most after graduation. Mostly fundamentals looking at general info about pipeline. 
>The fifth through eleventh most pinged sites for graduates is web dev style looking at creating files and navigating the file system. 
> Both groups are looking at lessons that are at the beginning of the lessons. 
> Graduates pinging early lessons makes sense. Codeup programs range from 4-6 months, and the top accessed lessons are earlier lessons. Perhaps alumni needed to look up something that they learned very early on. 
> Both types of lessons accessed contain material that would be used quite frequently in a career.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce Our Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>The curriculum access log data was acquired from the txt file provided. 

The cohort data from the SQL database and information provided by Mr Zach Gulde. 

- [X] Read this README.md
- [ ] The full cohort data needed to reproduce this notebook can be found [here](https://docs.google.com/spreadsheets/d/11g_qJf7VD989pvzOZIYkVZZc7xip4L5Cysifx_V6dIk/edit?usp=sharing) and needs to be downloaded as a csv to your working directory. 
- [ ] Ensure you have both the txt file named `anonymized-curriculum-access-07-2021.txt` and the csv named `full_cohort_list.csv` in order for the acquire to go smoothly.
- [ ] Clone this repo
- [ ] Run the ad_project_final_notebook.ipynb
