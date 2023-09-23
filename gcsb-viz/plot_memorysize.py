import itertools

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matrix = 'florida'
platform = 'titan'

MEMORYSIZE_FILENAME = f'data/input/{matrix}_memorysize_{platform}.csv'
OUTPUT_FILEPATH = f'data/output/{matrix}_memorysize_{platform}.png'

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
    n_matrices = len(memorysize_df.index)
    memorysize_df_reshaped = reshape_df(memorysize_df, 'memorysize')

    plt.figure(figsize=(36, 9))
    # plt.figure(figsize=(25, 12))

    # barを描画
    bar = sns.barplot(data=memorysize_df_reshaped, x='matrix', y='memorysize', hue='sparse_matrix_format', palette=color)

    hatches = itertools.cycle(['/', '+', 'o', 'x', '\\', '*', 'o', 'O', '.'])

    # Loop over the bars
    for i, thisbar in enumerate(bar.patches):
        # Set a different hatch for each bar
        if i % n_matrices == 0:
            hatch = next(hatches)
        thisbar.set_hatch(hatch)

    # 文字サイズを大きくする
    plt.title(platform, fontsize=20)

    # xy軸の値の文字サイズを大きくする
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    # plt.xticks(fontsize=16, rotation=90)

    plt.ylabel('Relative Memory Size Over CSR', fontsize=20)
    # x軸のラベルを表示しない
    plt.xlabel('')
    # labelを下部に移動. 枠線を消す
    plt.legend(bbox_to_anchor=(0.5, -0.1), loc='upper center', ncol=4, fontsize=20, frameon=False)
    # plt.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=4, fontsize=20, frameon=False)


    # 余白を調整
    plt.subplots_adjust(left=0.05, right=0.95, bottom=0.2, top=0.9)

    plt.savefig(OUTPUT_FILEPATH)

if __name__ == '__main__':
    main()
