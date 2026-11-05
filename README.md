Data Cleaning Steps
1. Load the DatasetThe original dataset is loaded into a Pandas DataFrame.

2. Handle Missing Values
Missing values are identified using:
df.isnull().sum()
Numerical missing values are filled using the median, while missing text values are filled using the most frequent value.

3. Remove Duplicate Records
Duplicate rows are removed using:
df.drop_duplicates()

4. Standardize Column Names
Column names are converted to lowercase, and spaces are replaced with underscores.
Example:
Year Birth → year_birth

5. Standardize Text Values
Leading and trailing spaces are removed from text columns.

6. Convert Data Types
Customer dates are converted into datetime format.
Birth years are converted into integer format.
Income values are converted into integer format.

7. Export the Cleaned Dataset
The cleaned dataset is saved as:
cleaned_dataset.csv


