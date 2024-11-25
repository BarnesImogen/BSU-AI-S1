import pandas as pd

# Load the dataset
df = pd.read_csv('application_record.csv')

# Data Cleanup
df['AGE_YEARS'] = df['DAYS_BIRTH']/-365.2425
df.drop('DAYS_BIRTH', axis=1, inplace=True)

df['YEARS_EMPLOYED'] = df['DAYS_EMPLOYED']/-365.2425
df.drop('DAYS_EMPLOYED', axis=1, inplace=True)


# Define functions for backward chaining rules
def applicant_approved(row):
    # Check if applicant meets criteria for approval
    if applicant_eligible(row) and row['YEARS_EMPLOYED'] > 5:
        return True
    return False

def applicant_eligible(row):
    # Check if applicant meets criteria for eligibility
    if row['AMT_INCOME_TOTAL'] > 80000 and row['NAME_EDUCATION_TYPE'] in ['Higher education', 'Academic degree']:

        return True


# Apply backward chaining to determine approval status
def backward_chain(row):
    return "Approved" if applicant_approved(row) else "Rejected"

# Apply backward chaining to each row in the dataset
df['APPLICATION_STATUS'] = df.apply(backward_chain, axis=1)

# Display the results or save to a file
print(df[['ID', 'AMT_INCOME_TOTAL', 'AGE_YEARS', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE', 'OCCUPATION_TYPE', 'APPLICATION_STATUS']])
df.to_csv("credit_card_application_results_backward.csv", index=False)


