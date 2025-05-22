from tmdb_api import enrich_dataframe
import pandas as pd

# Load dataset
input_file = 'netflix_titles.csv'
output_file = 'netflix_titles_updated.csv'

dataframe = pd.read_csv(input_file)
updated_df = enrich_dataframe(dataframe)

# Save the updated dataframe
updated_df.to_csv(output_file, index=False)
print(f"Updated data saved to {output_file}")
