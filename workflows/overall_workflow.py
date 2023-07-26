# @begin data_clean_overall_workflow
# @in original_data.csv @desc the original dirty data
# @out normalized_cleaned_data.csv @desc Greeting displayed to user.

# @begin data_profiling @desc Using Python
# @in original_data.csv @desc the original dirty data
# @out data_quality_problems @desc data quality problems found
print('do data profiling')
# @end data_profiling

# @begin data_cleaning @desc Using OpenRefine
# @in original_data.csv @desc the original dirty data
# @in data_quality_problems @desc data quality problems found
# @out cleaned_data.csv
print('do data cleaning')
# @end data_cleaning

# @begin ic_violation_check @desc Using Python
# @in cleaned_data.csv @desc the cleaned data
# @out normalized_cleaned_data.csv
print('do data cleaning')
# @end ic_violation_check

# @end data_clean_overall_workflow