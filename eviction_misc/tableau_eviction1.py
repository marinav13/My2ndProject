from tableauscraper import TableauScraper as TS
import pandas as pd

url = 'https://public.tableau.com/views/MassachusettsTrialCourtSummaryProcessExecutionsIssued/ExecutionsIssd_byWeekMonth?:language=en-US&:display_count=n&:origin=viz_share_link'

ts = TS()
ts.loads(url)
wb = ts.getWorkbook()

#for t in workbook.worksheets:
 #   print(f"worksheet name : {t.name}") #show worksheet name
  #  print(t.data) #show dataframe for this worksheet

#show parameters values / column
#parameters = workbook.getParameters()
#print(parameters)

# set parameters column / value
#workbook = workbook.setParameter("P.League 2", "Ligue 1")

# display worksheets
#for t in workbook.worksheets:
#       print(t.data)


#DB01 Total Cases
#DB02 Cases, Executions Issued
#DB03 County, Executions Issued

##wb = ts.getWorkbook()

#data = wb.getCsvData(sheetName='DB01 Total Cases')

##print(data)

#sheets = workbook.getSheets()
#print(sheets)

# Iterate over each sheet in the workbook
# Iterate over each sheet in the workbook
for sheet_name in wb.worksheets:
    worksheet = wb.getWorksheet(sheet_name)
    data = worksheet.data

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    file_name = f'{sheet_name}.csv'
    df.to_csv(file_name, index=False)
# Convert the data to a pandas DataFrame
#df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
#df.to_csv('scraped_data.csv', index=False)