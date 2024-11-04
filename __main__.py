import pandas as pd
import sys
import os

def split_csv_into_batches(input_file, batch_size=100):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Get the base file name and extension
    base_name, _ = os.path.splitext(os.path.basename(input_file))
    input_dir = os.path.dirname(input_file)

    # Create output directory
    output_dir = os.path.join(input_dir, f"{base_name}_batches")
    os.makedirs(output_dir, exist_ok=True)

    # Determine the number of batches
    total_records = len(df)
    num_batches = (total_records // batch_size) + (1 if total_records % batch_size != 0 else 0)
    
    for batch_number in range(num_batches):
        # Calculate start and end indices for the current batch
        start_index = batch_number * batch_size
        end_index = start_index + batch_size
        
        # Slice the DataFrame to get the current batch
        batch_df = df[start_index:end_index]
        
        # Create the output file name
        output_file = os.path.join(output_dir, f"{base_name}_{batch_number + 1:04d}.csv")
        
        # Save the batch to a new CSV file
        batch_df.to_csv(output_file, index=False)
        print(f"Created: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python split_csv.py <input_file.csv> [<batch_size>]")
        sys.exit(1)
    
    input_csv_file = sys.argv[1]
    batch_size = int(sys.argv[2]) if len(sys.argv) == 3 else 100
    split_csv_into_batches(input_csv_file, batch_size)
