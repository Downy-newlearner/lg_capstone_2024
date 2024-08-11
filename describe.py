#위 txt 파일로 저장하는 구문을 함수로 만들어서 사용
def describe_df(df):
    with open(f'./datas/df_summary.txt', 'w') as f:
        for i in range(len(df.columns)):

            f.write(f'{i+1}: {df.columns[i]}:\nnunique: ' + \
                    str(df[df.columns[i]].nunique()) + "\n" \
                        + str(df[df.columns[i]].unique()) + "\n\n")
    print('저장완료')