import pandas as pd
import json
import os

# Run this once to create the label mapping file
def create_label_mapping(csv_path='test.csv'):
    """Create a JSON file with the mapping between numeric indices and aircraft categories"""
    df = pd.read_csv(csv_path)
    
    categories = df['Labels'].astype('category')
    
    # Create mapping from numeric index to aircraft category (Classes column)
    label_mapping = {}
    for index, row in df.drop_duplicates('Labels').iterrows():
        label_value = row['Labels']
        class_name = row['Classes']  # Get the actual aircraft class name
        label_code = categories.cat.categories.get_loc(label_value)
        label_mapping[str(label_code)] = class_name
    
    # Save to JSON
    with open('airplane_classification/label_mapping.json', 'w') as f:
        json.dump(label_mapping, f, indent=4)
    
    print(f"Label mapping saved to label_mapping.json with {len(label_mapping)} classes")
    print(f"Sample mapping: {list(label_mapping.items())[:3]}")

if __name__ == "__main__":
    create_label_mapping('airplane_classification/test.csv')