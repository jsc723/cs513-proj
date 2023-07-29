import pandas as pd
from sys import argv

# check null, n/a, (blank)
def ic_empty_country(df):
    print('-----ic_empty_country-----')
    col = 'country'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

def ic_empty_points(df):
    print('-----ic_empty_points-----')
    col = 'points'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

def ic_empty_price(df):
    print('-----ic_empty_price-----')
    col = 'price'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

def ic_empty_taster_name(df):
    print('-----ic_empty_taster_name-----')
    col = 'taster_name'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

def ic_empty_taster_twitter_handle(df):
    print('-----ic_empty_taster_twitter_handle-----')
    col = 'taster_twitter_handle'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

def ic_empty_variety(df):
    print('-----ic_empty_variety-----')
    col = 'variety'
    blank_count = df[col].isnull().sum()
    null_count = (df[col].astype(str).str.lower() == 'null').sum()
    na_count = (df[col].astype(str).str.lower() == 'n/a').sum()
    print(f'blank={blank_count}, null={null_count}, n/a={na_count}')

# check points are numeric
def ic_points_numeric(df):
    print('-----ic_points_numeric-----')
    col = 'points'
    df[col] = pd.to_numeric(df[col], errors='coerce')
    non_numeric_count = df[col].isna().sum()
    print(f'non_numeric={non_numeric_count}')

# check price are numeric
def ic_price_numeric(df):
    print('-----ic_price_numeric-----')
    col = 'price'
    df[col] = pd.to_numeric(df[col], errors='coerce')
    non_numeric_count = df[col].isna().sum()
    print(f'non_numeric={non_numeric_count}')

# check points are in range 80-100
def ic_points_range(df):
    print('-----ic_points_range-----')
    col = 'points'
    out_of_range_count = ((df[col] < 80) | (df[col] > 100)).sum()
    print(f'out_of_range_count={out_of_range_count}')

# check prices are greater than 0
def ic_price_range(df):
    print('-----ic_price_range-----')
    col = 'price'
    out_of_range_count = (df[col] <= 0).sum()
    print(f'out_of_range_count={out_of_range_count}')

# normalize points to range 0-10
def normalize_points(df):
    print('-----normalize_points-----')
    col = 'points'
    n_min, n_max = df[col].min(), df[col].max()
    df['normalized_points'] = (df[col] - n_min) / (n_max - n_min) * 10
    print('done')

# reset index (the first column) to 1,2,3,...
def reset_index(df):
    print('-----reset_index-----')
    df[df.columns[0]] = range(1, len(df) + 1)
    print('done')


def main():
    input_path = argv[1] 
    save_path = './step2_python/cleaned.csv'
    df = pd.read_csv(input_path, header=0)

    print('-----input data-----')
    print(df.head()) 

    ic_empty_country(df)
    ic_empty_points(df)
    ic_empty_price(df)
    ic_empty_taster_name(df)
    ic_empty_taster_twitter_handle(df)
    ic_empty_variety(df)
    ic_points_numeric(df)
    ic_price_numeric(df)
    ic_points_range(df)
    ic_price_range(df)

    normalize_points(df)
    reset_index(df)

    print('-----cleaned data-----')
    print(df.head())

    df.to_csv(save_path, index=False)
    print('saved to', save_path)



if __name__ == '__main__':
    main()

