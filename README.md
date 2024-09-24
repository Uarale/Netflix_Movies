# Netflix: A Journey Through the 90s!

## Table of Contents
1. [Project Overview](#project-overview)
2. [Motivation](#motivation)
3. [Challenges](#challenges)
4. [Technology Used](#technology-used)
5. [Process](#process)
6. [The Data](#the-data)
7. [Conclusion](#conclusion)
8. [Credit](#credit)

## Project Overview
Netflix, founded in 1997 as a DVD rental service, has since grown into one of the largest entertainment and media companies in the world. With its extensive library of movies and TV shows, Netflix offers a great opportunity for applying exploratory data analysis (EDA) and gaining insights into the entertainment industry.

In this project, I analyzed Netflix’s movie catalog, focusing specifically on films released in the 1990s. Through this analysis, I aimed to uncover trends, patterns, and key insights about the movies from this memorable decade.

## Motivation
This project came about as part of my journey to earn a Data Analyst certificate. I downloaded the dataset from DataCamp’s "Data Analyst with Python" career track, and this was my very first project within that track. I also took a GitHub crash course on DataCamp to learn best practices for using the platform effectively.

## Challenges
One of the main challenges I faced was ensuring that each line of code was correct. I had to make sure it didn't return any errors while also effectively answering the questions I was trying to explore. It was a valuable learning experience that helped me refine my coding skills.

## Technology Used
- **Python**: The programming language i  used for data analysis.
- **PyCharm**: The integrated development environment (IDE) where I wrote and executed the code for this project.
- **Pandas**: A powerful library for data manipulation and analysis, allowing me to easily work with the dataset.
- **Matplotlib**: Used for data visualization to illustrate findings and trends.

These technologies were chosen for their robustness and community support, which greatly aided in the data analysis process.

## Process
1. **Data Collection**: The analysis began with the collection of the `netflix_data.csv` dataset, containing various details about Netflix’s movie collection.
2. **Data Exploration**: I explored the dataset to understand its structure and contents.
3. **Data Cleaning**: I performed data cleaning tasks to handle any missing values or inconsistencies within the dataset.
4. **Exploratory Data Analysis (EDA)**: This involved analyzing the data to discover patterns and insights related to 1990s movies, such as trends in genres, directors, and release years.
5. **Visualization**: I created visualizations to represent findings effectively, making it easier to communicate insights derived from the data.
6. **Conclusion**: Summarized the key findings and insights gained from the analysis.

## The Data: `netflix_data.csv`

| Column        | Description                           |
|---------------|---------------------------------------|
| `show_id`     | The ID of the show                    |
| `type`        | Type of show                          |
| `title`       | Title of the show                     |
| `director`    | Director of the show                  |
| `cast`        | Cast of the show                      |
| `country`     | Country of origin                     |
| `date_added`  | Date added to Netflix                 |
| `release_year`| Year of Netflix release               |
| `duration`    | Duration of the show in minutes       |
| `description` | Description of the show               |
| `genre`       | Show genre                            |



## Conclusion
Here are the insights gained from my analysis of Netflix movies from the 1990s, written from my perspective:

---

### Insights Gained from My Netflix Movies Analysis

1. **Understanding Movie Durations**:
   - By filtering the dataset for movies released in the 1990s, I was able to create a clear picture of how long these films typically were. The histogram I generated highlighted the distribution of movie durations, showing me which lengths were most common during that decade. It was fascinating to see where most films landed—if the peak was around 90 minutes, it might suggest that shorter films were the norm back then, aligning with audience preferences for quick, engaging stories.

2. **Exploring Short Action Movies**:
   - I dug deeper into the action genre, specifically counting how many short action movies (under 90 minutes) were released in the 1990s. The final count gave me insight into trends within this genre. A low number of short action films might indicate that filmmakers were opting for longer, more detailed narratives during this time, possibly to create more complex characters and storylines. It also made me think about how audience expectations for action films have evolved since then.

3. **Trends in 1990s Filmmaking**:
   - Overall, this analysis allowed me to glean insights about the filmmaking trends of the 1990s. Understanding the preferences for movie lengths can help inform modern production choices, especially for those of us interested in creating nostalgic content. If shorter films were preferred back then, it might be worth considering how that plays into what audiences want to see today.

4. **The Importance of Data Cleaning**:
   - Throughout this project, I learned a lot about the importance of data cleaning. Converting duration data from strings to integers was a crucial step that ensured my analysis was based on accurate information. This experience reinforced for me how vital it is to prepare and clean data properly to get meaningful insights.


## Credits
- **DataCamp**: For providing the dataset through the "Data Analyst with Python" career track, which made this project possible.
- **DataCamp**: For the GitHub crash course that helped me learn best practices for using the platform and effectively managing my project.

