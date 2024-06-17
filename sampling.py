# Import libraries 
import pandas as pd
import openpyxl

if __name__ == "__main__":
    # 1. Import excel file named <input_file> and create a dataframe from it
    input_file = 'input_file.xlsx' # TODO: Update this with your input file name
    data = pd.read_excel(input_file)
    data = pd.DataFrame(data)
    
    # 2. Calculate number of messages to sample based on the unique value from <key_column> and convert into dictionary
    key_column = 'Channel Name' # TODO: Update this with the name of the column you want to sample based on  
    percent = 0.2 # TODO: Update this with the percent of messages you want to sample for each value from <key_column>
    count_dict = ((data.groupby(key_column).size()) * percent).astype(int).to_dict()
    print(count_dict)
    
    # 3. Sample <percent> of messages from each unique value from <key_column>
    output_data = pd.DataFrame()
    for channel_name, num in count_dict.items():
        current_sample = data[data[key_column] == channel_name].sample(n = num)
        output_data = pd.concat([output_data, current_sample])
        
    # 4. Randomly shuffle rows
    output_data = output_data.sample(frac=1).reset_index(drop=True)

    # 5. Check to see how many total number of messages has been sampled 
    len(output_data)
    
    # 6. Export (Comment out line depending on what output file you want)
    output_file_name = 'output_file.xlsx' # TODO: Update this!
    # Export as a CSV
    # output_data.to_csv(output_file_name, index=False)
    # Export as an Excel spreadsheet
    output_data.to_excel(output_file_name, index=False)