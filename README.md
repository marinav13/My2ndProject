 <!-- GETTING STARTED -->
## About the Pandemic Job Loss in MA project

<h1>What I aimed to accomplish:</h1>

<p>I hoped to see whether the public and private sector has regained jobs lost in the pandemic in MA. I also wanted to zoom in on certain sectors to see if job loss where any job loss has been concentrated. </p>

<br>
<br>
<h1>Short description of your findings</h1>
<p> I found that the private and local government sectors have rebounded in MA. However, the state government sector has yet to regain all jobs lost in the pandemic. Hard-hit sectors include state government hospitals, which lost 1,000 jobs for a 20% drop. The state government education sector also saw a drop -- this sector includes teaching assistants. The hospital sector overall rebounded in the pandemic - but I found that nursing homes have yet to recover. </p>

<br>
<br>
<h1>Summary of the data collection process, with links</h1>
<p> I used an API to look through various Bureau of Labor Statistic series and compare data from May 2023 to May 2019. </p>
<p> I started with <a href="[url](https://beta.bls.gov/dataQuery/find?st=0&r=20&s=popularity%3AD&fq=survey:[sm]&fq=cg:[Geography]&fq=cc:[States+and+Territories]&fq=ccd:[Massachusetts]&fq=mg:[Measure+Published+By]&fq=mg:[Measure+Category]&fq=mg:[Measure+Attributes]&fq=mc:[Employed]&more=0&q=hospitals)">BLS Data Finder.</a> </p>
<p> I used the following data sets for the state of Massachusetts:</p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000000500000001">Total Private</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000009093000001">Local Government</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000009092000001">State Government</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000009092262201">State Government Hospitals</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000009092161101">State Government Educational Services</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000009092200001">Government - State Government Excluding Education</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000006562300001">Nursing and Residential Care Facilities</a></p>

<p><a href="https://beta.bls.gov/dataViewer/view/timeseries/SMU25000006562200001">Hospitals</a></p>


<br>
<br>
<h1>Overview of the data analysis process</h1>
<p>I used for loops to go through the data and get variables to analyze the data. Then I simply subtracted the new minus the old values, then divided over the old to find the percent change. I used if statements to analyze whether May 2023 employment figures were greater than or equal to May 2019 figures. </p>

<br>
<br>
<h1>A section about what new skills, approaches, etc you used, or where you grew the most during the project</h1>
<p> I gained new skills in working with APIs (and getting used to the slowness of APIs) to find the data I want and conduct basic analysis. This code could function as a tracker I could use in future projects. </p>

<br>
<br>
<h1>A section about things you tried to do or wanted to do but did not have the skills/time (but if you have more time you might do)</h1>
<p> It would be interesting to get breakdowns for the state government educational services data (like are these mostly teaching assistants, etc). I had a tough time figuring out how to find the datasets I wanted on the BLS site. I'd like to next do a look at nursing home closures and CMS staffing data to find out which nursing homes have lost the most workers.
</p>


<p>Link to Github project: <a href="https://marinav13.github.io/MyProject/">here</a></p>
