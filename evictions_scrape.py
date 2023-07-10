from tableauscraper import TableauScraper as TS
import pandas as pd

#2020-2023 eviction orders
#url = 'https://public.tableau.com/shared/4RPS78R3R?:display_count=n&:origin=viz_share_link'

#by location eviction orders since 2020
#url = 'https://public.tableau.com/shared/8S6Q53TYD?:display_count=n&:origin=viz_share_link'

#by location eviction orders since 2022
url = 'https://public.tableau.com/shared/F8Q5B97KS?:display_count=n&:origin=viz_share_link'

#url = 'https://public.tableau.com/views/MassachusettsTrialCourtSummaryProcess/SummaryProcess?:language=en-US&:display_count=n&:origin=viz_share_link'
#url = 'https://public.tableau.com/views/MassachusettsTrialCourtSummaryProcessTier1andTier2Events/Tier1EventDashboard?:language=en-US&:display_count=n&:origin=viz_share_link'
#url = 'https://public.tableau.com/views/MassachusettsTrialCourtSummaryProcessExecutionsIssued/ExecutionsIssd_byWeekMonth?:language=en-US&:display_count=n&:origin=viz_share_link'


ts = TS()
ts.loads(url)
wb = ts.getWorkbook()


for t in wb.worksheets:
    print(f"worksheet name : {t.name}") #show worksheet name
    ws = ts.getWorksheet(t.name)
    data = ws.data
    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)
    file_path = f'/PATH/{t.name}.csv'
    # Save DataFrame to a CSV file
    df.to_csv(file_path, index=False)

# Save DataFrame to a CSV file
#df3.to_csv(f'{name3}.csv', index=False)


#worksheet name : Lee TIER 1 (county)
#worksheet name : Lee TIER 1 (total - continued)
#worksheet name : Lee TIER 1 (total - held)
#worksheet name : Lee TIER 1 (total - not held)
#worksheet name : Lee TIER 1 (total - resolved)
#worksheet name : Lee TIER 1 (total - total)
#worksheet name : Lee TIER 1 (week)
#worksheet name : Sheet 25