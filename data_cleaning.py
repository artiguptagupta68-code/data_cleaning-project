import pandas as pd
#Load the original dataset
df=pd.read_csv('marketing_campaign.csv', sep="\t")

print("origional data shape:" ,df.shape)

print ("\n first 5 rows")

print (df.head())

print("\nMissing values before cleaning:")
print(df.isnull().sum())

#Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

#Remove duplicate rows
df = df.drop_duplicates()

print("\nDuplicates removed.")
# Standardize column names
df.columns = (
df.columns
.str.strip()
.str.lower()
.str.replace(" ", "_")
)
#Standardize text values
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# Handle missing values
#Fill numerical columns with their median
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values with the most frequent value
for column in text_columns:
    if df[column].isnull().any():

        mode_value = df[column].mode()

        if not mode_value.empty:
            df[column] = df[column].fillna(mode_value[0])

# Convert date columns to datetime
df["dt_customer"] = pd.to_datetime(
    df["dt_customer"],
    format="%d-%m-%Y",
    errors="coerce"
)
#  Fix data types

if "year_birth" in df.columns:
    df["year_birth"] = pd.to_numeric(
        df["year_birth"], errors="coerce"
    ).astype("Int64")

if "income" in df.columns:
    df["income"] = pd.to_numeric(
        df["income"], errors="coerce"
    ).round().astype("Int64")

print("Dataset shape before saving:", df.shape)
print(df.head())

df.to_csv("cleaned_dataset.csv", index=False)

print("File saved successfully!")
#Display cleaning summary
print("\nCleaning completed!")
print("Cleaned dataset shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned data types:")
print(df.dtypes)

print("\nCleaned dataset saved as cleaned_dataset.csv")