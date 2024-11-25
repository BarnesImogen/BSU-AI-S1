import pandas as pd

# Load the dataset
df = pd.read_csv('application_record.csv')

# Data Cleanup
df['AGE_YEARS'] = df['DAYS_BIRTH']/-365.2425
df.drop('DAYS_BIRTH', axis=1, inplace=True)

df['YEARS_EMPLOYED'] = df['DAYS_EMPLOYED']/-365.2425
df.drop('DAYS_EMPLOYED', axis=1, inplace=True)




# Define a function to evaluate the forward-chaining rules
def forward_chain(row):
    facts = {}  # Store inferred facts

    # Apply Rule 1
    if row['AMT_INCOME_TOTAL'] > 80000 and row['AGE_YEARS'] < 25:
        facts['eligible'] = True
    else:
        facts['eligible'] = False

    # Apply Rule 2 (if Rule 1 was satisfied)
    #My original code
    # if facts.get('eligible') and row['OCCUPATION_TYPE'] == 'Managers' or row['OCCUPATION_TYPE'] == 'High skill tech staff' or row['OCCUPATION_TYPE'] == 'Accountants' or row['OCCUPATION_TYPE'] == 'Private service staff' or row['OCCUPATION_TYPE'] == 'Secretaries':
    # CHATGPT Cleaned up this line to get the new code
    if facts.get('eligible') and row['OCCUPATION_TYPE'] in ['Managers', 'High skill tech staff', 'Accountants', 'Private service staff', 'Secretaries']:
        facts['approved'] = True
    else:
        facts['approved'] = False

    return "APPROVED" if facts.get('approved') else "REJECTED"


# Apply forward chaining to each row in the dataset
df['APPLICATION_STATUS'] = df.apply(forward_chain, axis=1)


# Display the results or save to a file
print(df[['ID', 'AMT_INCOME_TOTAL', 'AGE_YEARS', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE', 'OCCUPATION_TYPE', 'APPLICATION_STATUS']])
df.to_csv("credit_card_application_results_forward.csv", index=False)
