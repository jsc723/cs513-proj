import pandas as pd
import pandasql as ps
from sys import argv

def main():
    input_path = argv[1]
    df = pd.read_csv(input_path, header=0)

    print('-----input data-----')
    print(df.head()) 
    # filter only US wines
    df = ps.sqldf('''SELECT * FROM df WHERE country ="US"''')
    print(df)

    review_count_df = ps.sqldf('''SELECT taster_name, count(*) as num_of_reviews FROM df GROUP BY taster_name ORDER BY num_of_reviews DESC''')
    print(review_count_df)
    most_significant_reviewer = review_count_df['taster_name'][0]
    num_of_reviews = review_count_df['num_of_reviews'][0]
    print(f'most_significant_reviewer: "{most_significant_reviewer}", num_of_reviews: {num_of_reviews}')

    result_df = ps.sqldf(f'''SELECT variety, count(*) as num_of_reviews, avg(normalized_points) as avg_points, min(price) as min_price, max(price) as max_price
             FROM df WHERE taster_name = "{most_significant_reviewer}" GROUP BY variety''')

    print(result_df.to_string(index=False))




if __name__ == '__main__':
    main()