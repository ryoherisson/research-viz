import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

platform = 'A100'

MEMORYSIZE_FILENAME = f'data/input/random_memorysize_{platform}.csv'
OUTPUT_FILEPATH = f'data/output/random_memorysize_{platform}.png'

color=['royalblue', 'orange', 'grey', 'limegreen']

sns.set(style="darkgrid")

def read_csv(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename, index_col=0)
    return df

# データをseabornのbarplotのhueを指定できるように整形する
def reshape_df(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    reshaped_df = df.stack().rename_axis(['matrix', 'sparse_matrix_format']).reset_index().rename(columns={0: column_name})
    return reshaped_df

def main():
    memorysize_df = read_csv(MEMORYSIZE_FILENAME)
    memorysize_df = reshape_df(memorysize_df, 'memorysize')

    plt.figure(figsize=(25, 9))

    # barを描画
    sns.barplot(data=memorysize_df, x='matrix', y='memorysize', hue='sparse_matrix_format', palette=color)

    # 文字サイズを大きくする
    plt.title(platform, fontsize=20)

    # y軸の値の文字サイズを大きくする
    plt.yticks(fontsize=16)

    plt.ylabel('Relative Memory Size Over CSR', fontsize=20)
    # x軸のラベルを表示しない
    plt.xlabel('')
    # labelを下部に移動. 枠線を消す
    plt.legend(bbox_to_anchor=(0.5, -0.1), loc='upper center', ncol=4, fontsize=20, frameon=False)


    # 余白を調整
    plt.subplots_adjust(left=0.05, right=0.95, bottom=0.2, top=0.9)

    plt.savefig(OUTPUT_FILEPATH)

if __name__ == '__main__':
    main()
