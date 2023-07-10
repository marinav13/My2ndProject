 <!-- GETTING STARTED -->
## About the Evictions in MA project

<h1>What I aimed to accomplish:</h1>

<p>I wanted to see whether evictions are on the rise in Massachusetts. I also wanted to learn how to scrape from Tableau visualizations in cases where it's otherwise not possible to download the data. </p>

<br>
<br>
<h1>Short description of your findings</h1>
<p> I found that evictions have spiked in MA this year. Hard-hit communities include Fall River, Holyoke, Springfield, Pittsfield and New Bedford, where evictions and money order judgments are disproptionately high. </p>

<br>
<br>
<h1>Summary of the data collection process, with links</h1>
<p> I used <a href="https://github.com/bertrandmartel/tableau-scraping">a wonderful Tableau scraping tool created by Bertrandmartel to download .CSV files from Tableau visualizations maintained by the Massachusetts state trial court system. The trial court system has refused to simply allow the public to download data from its public Tableau visualization. I have requested the data but have only received partial data for another visualization. The state trial court system has correctly stated that the judiciary is exempt from the public records access law. </a> </p>
<p> I used the following data sets for the state of Massachusetts:</p>

<p><a href="https://public.tableau.com/shared/4RPS78R3R?:display_count=n&:origin=viz_share_link">2020-2023 eviction orders</a></p>

<p><a href="https://public.tableau.com/shared/8S6Q53TYD?:display_count=n&:origin=viz_share_link">by location eviction orders since 2020</a></p>

<p><a href="https://public.tableau.com/shared/F8Q5B97KS?:display_count=n&:origin=viz_share_link">#by location eviction orders since 2022</a></p>

<br>
<br>
<h1>Overview of the data analysis process</h1>
<p>I used Tableauscraper and for loops to go through the data, get worksheet names and then save the .csv files to a folder. I then analyzed the data using Excel pivot tables for the simple analysis of finding communities with the biggest counts of eviction orders and money judgments. I added <a href="https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-cities-and-towns.html"> Census population data </a>, cleaned the data and used V Lookup to match communities with populations. I was unable to match every community with population data -- partly because the state data had a breakdown for Boston neighborhoods.

<br>
<br>
<h1>A section about what new skills, approaches, etc you used, or where you grew the most during the project</h1>
<p> I gained new skills in web scrapign and working in Github to find tools created by other users and modifying them to suit my own purposes. I have gained more confidence in how to use for loops to iterate through data and find what I need. I'll be able to use this code to scrap data from other Tableau visualizations. </p>

<br>
<br>
<h1>A section about things you tried to do or wanted to do but did not have the skills/time (but if you have more time you might do)</h1>
<p> I want to use MySQl or R to analyze and clean the data next time. I used Excel because I thought it would be straightforward, but I think I would have saved more time using SQL. I'd like to scrape data from Apartments.com for reporting on the rental market in MA next.
</p>


<p>Link to Github project: <a href="https://marinav13.github.io/MyProject/">here</a></p>
