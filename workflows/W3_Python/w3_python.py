# @begin ic_violation_check_workflow
# @in cleaned_data.csv 
# @out normalized_cleaned_data.csv 

# @begin load_data @desc load CSV into DataFrame
# @in cleaned_data.csv @desc the cleaned data
# @out dataframe
print('do load data')
# @end load_data

# @begin normalize_points @desc Normalize points into the range 0-10
# @in dataframe 
# @out normalized_dataframe
print('do normalize points')
# @end normalize_points

# @begin reset_index @desc Reset the index of the dataframe
# @in normalized_dataframe 
# @out resetted_normalized_dataframe
print('do normalize points')
# @end reset_index

# @begin save_data @desc save DataFrame as CSV
# @in resetted_normalized_dataframe
# @out normalized_cleaned_data.csv 
print('do load data')
# @end save_data

# @end data_clean_overall_workflow