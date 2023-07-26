import pandas as pd

# check null, n/a, (blank)
def check_empty_values(df):
    print('-----check_empty_values-----')
    columns = ['country', 'points', 'price', 'taster_name', 'taster_twitter_handle', 'variety']
    for col in columns:
        blank_count = df[col].isnull().sum()
        null_count = (df[col].astype(str).str.lower() == 'null').sum()
        na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
        print(f'column "{col}": blank={blank_count}, null={null_count}, n/a={na_count}')

# check points and prices are numeric
def convert_to_numeric_columns(df):
    print('-----check_numeric_value-----')
    columns = ['points', 'price']
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        non_numeric_count = df[col].isna().sum()
        n_min, n_max = df[col].min(), df[col].max()
        print(f'column "{col}": non_numeric={non_numeric_count}, min={n_min}, max={n_max}')


# normalize points to range 0-10
def normalize_points(df):
    print('-----normalize_points-----')
    col = 'points'
    n_min, n_max = df[col].min(), df[col].max()
    df['normalized_points'] = (df[col] - n_min) / (n_max - n_min) * 10
    print('done')


# each twitter handle should belong to exactly one person
def check_twitter_handle(df):
    print('-----check_twitter_handle-----')
    c1 = 'taster_twitter_handle'           #one
    c2 = 'taster_name'                     #multi
    df = df[[c1,c2]]
    ic_violations = df.groupby(c1)\
        .filter(lambda x: x[c2].nunique() > 1)\
        .groupby([c1, c2]).size().to_dict()
    print(ic_violations)


def main():
    input_path = './data/winemag-data-130k-v2.csv'
    save_path = 'output.csv'
    df = pd.read_csv(input_path, header=0)

    print('-----input data-----')
    print(df.head()) 
    check_empty_values(df)
    convert_to_numeric_columns(df)
    normalize_points(df)
    check_twitter_handle(df)

    print('-----cleaned data-----')
    print(df.head())

    df.to_csv(save_path, index=False)
    print('saved to', save_path)



if __name__ == '__main__':
    main()

