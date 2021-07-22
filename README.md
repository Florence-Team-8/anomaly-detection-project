## Detecting Anomolous Network Access Project

Hello,

Welcome to the README file for our "Anomaly Detection Project".


_________________

## Planning Process

The TRELLO board used for the planning process can be found on this link: [Trello](https://trello.com/b/LA6GxLOI/anomaly-detection)


_________________

Program ID Codes
1 - Full stack PHP
2 - Java
3 - Data Science
4 - Front End Program


#### 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

> - 1 (Full Stack PHP) - javascript-i    1144 page views
> - 2 (Java) -  javascript-i 19383 views
> - 3 (Data Science) - classification/overview     2469 page views

Javascript-i had the most traffic for both the Full Stack PHP & Java programs. This makes sense since JavaScript is a highly used programming language for web developers because it allows users to interact with web pages.  While the most accessed for Data Science was the classification overview.  The Classification Methodology is the most used for Supervised Learning.

#### 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
- Most of the pings are either towards the end of the program, or immediately the day after
- Some have a lot of pings at the beginning of the program start and stop once it hits two weeks
- about a third only ping the day of the program start or after

>There are a few possible explanations for this.  Perhaps the user unenrolled, or they changed their github user status. What is interesting is that some users only pinged towards the end of the program, the others pinged for the first two weeks. My assumption is that it could be a staff member pinging the system or it's people that left after two weeks

>Users 49,64, 278, 812, and 832 accessed the curriculum towards the end of the program

>Users 487, 1060 and 1065 accessed the curriculum within two weeks of the start date

>889 and 1059 access the database over a week or two and then stops.

#### 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
>DS students ping the system the most after graduation. Mostly fundamentals looking at general info about pipeline. 

>The fifth through eleventh most pinged sites for graduates is web dev style looking at creating files and navigating the file system. 

> Both groups are looking at lessons that are at the beginning of the lessons. 

> Graduates pinging early lessons makes sense.
#### 7. Which lessons are least accessed?

The below endpoints have 34 page views each

> - 1 (Full Stack PHP) 
>   • content/php_iv/classes-and-objects-ii
>   • slides/object_oriented_programming
> - 2 (Java)
>   •  2.02.03_Power_Analysis    
>   •  3-sql/6.4-limit                           
>   •  8-clustering/5.1-kmeans-part-1                                 
>   •  Univariate_Regression_Excel                                     
> - 3 (Data Science)
>   • 13-advanced-topics/3.8-json-responses
>   • 2-storytelling/3.5-creating-dashboards
>   • advanced-topics/developing-data-products 


Program 4 (Front End Program) was not used in the responses for the most and least accessed endpoints since it was a test group. Full Stack PHP & Java did not have similar low accessed endpoints as they did for the most accessed endpoints. There least accessed included some Data Science pages while the lows for Data Science were lessons that are least used in Data Science.

### Reproduce Our Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>The curriculum access log data was acquired from the txt file provided. 

The cohort data from the SQL database and information provided by Mr Zach Gulde. 

- [ ] The full cohort data needed to reproduce this notebook can be found [here](https://docs.google.com/spreadsheets/d/11g_qJf7VD989pvzOZIYkVZZc7xip4L5Cysifx_V6dIk/edit?usp=sharing) and needs to be downloaded as a csv to your working directory. 
- [ ] Ensure you have both the txt file named `anonymized-curriculum-access-07-2021.txt` and the csv named `full_cohort_list.csv` in order for the acquire to go smoothly.
- [ ] Nulls were filled in with 0s for the purpose of this exploration.
