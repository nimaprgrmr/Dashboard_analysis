import pandas as pd


def read_data(path='all_sales.csv'):
    df = pd.read_csv(path, header=None)
    columns = ['id_factor', 'date', 'id_br', 'amount', 'id_gds', 'dsc_gds', 'gds_class', 'unit_price', 'id_clinet']
    df.columns = columns
    df['gds_class'] = df['gds_class'].astype(str)
    return df


def make_update_df(df):
    # branch 50938
    data_50938 = df[df['id_br'] == 50938].groupby('dsc_gds')['id_factor'].count()
    column = ['ایزدشهر']
    df_50938 = pd.DataFrame(data_50938.values, columns=column, index=data_50938.index)

    # branch 51038
    data_51038 = df[df['id_br']==51038].groupby('dsc_gds')['id_factor'].count()
    column = ['نوآ']
    df_51038 = pd.DataFrame(data_51038.values, columns=column, index=data_51038.index)

    # branch 51338
    data_51338 = df[df['id_br']==51338].groupby('dsc_gds')['id_factor'].count()
    column = ['بام لند']
    df_51338 = pd.DataFrame(data_51338.values, columns=column, index=data_51338.index)

    # branch 51238
    data_51238 = df[df['id_br']==51238].groupby('dsc_gds')['id_factor'].count()
    column = ['مگامال']
    df_51238 = pd.DataFrame(data_51238.values, columns=column, index=data_51238.index)

    # branch 51138
    data_51138 = df[df['id_br']==51138].groupby('dsc_gds')['id_factor'].count()
    column = ['معین مال']
    df_51138 = pd.DataFrame(data_51138.values, columns=column, index=data_51138.index)

    # branch 51638
    data_51638 = df[df['id_br']==51638].groupby('dsc_gds')['id_factor'].count()
    column = ['اکسین']
    df_51638 = pd.DataFrame(data_51638.values, columns=column, index=data_51638.index)

    # branch 51538
    data_51538 = df[df['id_br']==51538].groupby('dsc_gds')['id_factor'].count()
    column = ['پانوراما']
    df_51538 = pd.DataFrame(data_51538.values, columns=column, index=data_51538.index)

    # branch 51838
    data_51838 = df[df['id_br']==51838].groupby('dsc_gds')['id_factor'].count()
    column = ['شعبه اینترنتی']
    df_51838 = pd.DataFrame(data_51838.values, columns=column, index=data_51838.index)

    # branch 51738
    data_51738 = df[df['id_br']==51738].groupby('dsc_gds')['id_factor'].count()
    column = ['شریعتی']
    df_51738 = pd.DataFrame(data_51738.values, columns=column, index=data_51738.index)

    # branch 52038
    data_52038 = df[df['id_br']==52038].groupby('dsc_gds')['id_factor'].count()
    column = ['آرمیتاژ مشهد']
    df_52038 = pd.DataFrame(data_52038.values, columns=column, index=data_52038.index)

    # branch 51938
    data_51938 = df[df['id_br']==51938].groupby('dsc_gds')['id_factor'].count()
    column = ['سیرجان']
    df_51938 = pd.DataFrame(data_51938.values, columns=column, index=data_51938.index)

    # branch 53238
    data_53238 = df[df['id_br']==53238].groupby('dsc_gds')['id_factor'].count()
    column = ['نگین']
    df_53238 = pd.DataFrame(data_53238.values, columns=column, index=data_53238.index)

    # branch 53338
    data_53338 = df[df['id_br']==53338].groupby('dsc_gds')['id_factor'].count()
    column = ['نیایش مال']
    df_53338 = pd.DataFrame(data_53338.values, columns=column, index=data_53338.index)

    # branch 51438
    data_51438 = df[df['id_br']==51438].groupby('dsc_gds')['id_factor'].count()
    column = ['سیتی استار مشهد']
    df_51438 = pd.DataFrame(data_51438.values, columns=column, index=data_51438.index)

    # branch 54438
    data_54438 = df[df['id_br']==54438].groupby('dsc_gds')['id_factor'].count()
    column = ['سیوان']
    df_54438 = pd.DataFrame(data_54438.values, columns=column, index=data_54438.index)

    # branch 54538
    data_54538 = df[df['id_br']==54538].groupby('dsc_gds')['id_factor'].count()
    column = ['ایران مال']
    df_54538 = pd.DataFrame(data_54538.values, columns=column, index=data_54538.index)

    # branch 55238
    data_55238 = df[df['id_br']==55238].groupby('dsc_gds')['id_factor'].count()
    column = ['دیپلمات سنتر بروجرد']
    df_55238 = pd.DataFrame(data_55238.values, columns=column, index=data_55238.index)

    # branch 55438
    data_55438 = df[df['id_br']==55438].groupby('dsc_gds')['id_factor'].count()
    column = ['آرتمیس']
    df_55438 = pd.DataFrame(data_55438.values, columns=column, index=data_55438.index)

    # branch 55338
    data_55338 = df[df['id_br']==55338].groupby('dsc_gds')['id_factor'].count()
    column = ['قم']
    df_55338 = pd.DataFrame(data_55338.values, columns=column, index=data_55338.index)

    # branch 55538
    data_55538 = df[df['id_br']==55538].groupby('dsc_gds')['id_factor'].count()
    column = ['لاله پارک']
    df_55538 = pd.DataFrame(data_55538.values, columns=column, index=data_55538.index)

    # branch 55638
    data_55638 = df[df['id_br']==55638].groupby('dsc_gds')['id_factor'].count()
    column = ['هایپر']
    df_55638 = pd.DataFrame(data_55638.values, columns=column, index=data_55638.index)

    # branch 55738
    data_55738 = df[df['id_br']==55738].groupby('dsc_gds')['id_factor'].count()
    column = ['فدک مال']
    df_55738 = pd.DataFrame(data_55738.values, columns=column, index=data_55738.index)

    result = pd.concat([df_50938, df_51038, df_51338, df_51238, df_51138, df_51638, df_51538,
                       df_51838, df_51738, df_52038, df_51938, df_53238, df_53338, df_51438,
                       df_54438, df_54538, df_55238, df_55438, df_55338, df_55538, df_55638,df_55738], axis=1)
    result = result.fillna(0)
    result = result.T
    result.reset_index()
    return result


def make_score(df):

    df = make_update_df(df)

    df['بارانی'] = df['بارانی'].apply(
        lambda column: ((column - df['بارانی'].min()) / (df['بارانی'].max() - df['بارانی'].min())) * 100)

    df['بلوز'] = df['بلوز'].apply(
        lambda column: ((column - df['بلوز'].min()) / (df['بلوز'].max() - df['بلوز'].min())) * 100)

    df['تونیک'] = df['تونیک'].apply(
        lambda column: ((column - df['تونیک'].min()) / (df['تونیک'].max() - df['تونیک'].min())) * 100)

    df['تاپ'] = df['تاپ'].apply(
        lambda column: ((column - df['تاپ'].min()) / (df['تاپ'].max() - df['تاپ'].min())) * 100)

    df['سارافون'] = df['سارافون'].apply(
        lambda column: ((column - df['سارافون'].min()) / (df['سارافون'].max() - df['سارافون'].min())) * 100)

    df['سایر'] = df['سایر'].apply(
        lambda column: ((column - df['سایر'].min()) / (df['سایر'].max() - df['سایر'].min())) * 100)

    df['سویی شرت'] = df['سویی شرت'].apply(
        lambda column: ((column - df['سویی شرت'].min()) / (df['سویی شرت'].max() - df['سویی شرت'].min())) * 100)

    df['شال و روسری'] = df['شال و روسری'].apply(
        lambda column: ((column - df['شال و روسری'].min()) / (df['شال و روسری'].max() - df['شال و روسری'].min())) * 100)

    df['شلوار'] = df['شلوار'].apply(
        lambda column: ((column - df['شلوار'].min()) / (df['شلوار'].max() - df['شلوار'].min())) * 100)

    df['شومیز'] = df['شومیز'].apply(
        lambda column: ((column - df['شومیز'].min()) / (df['شومیز'].max() - df['شومیز'].min())) * 100)

    df['مانتو'] = df['مانتو'].apply(
        lambda column: ((column - df['مانتو'].min()) / (df['مانتو'].max() - df['مانتو'].min())) * 100)

    df['پارچه'] = df['پارچه'].apply(
        lambda column: ((column - df['پارچه'].min()) / (df['پارچه'].max() - df['پارچه'].min())) * 100)

    df['پالتو'] = df['پالتو'].apply(
        lambda column: ((column - df['پالتو'].min()) / (df['پالتو'].max() - df['پالتو'].min())) * 100)

    df['پیراهن'] = df['پیراهن'].apply(
        lambda column: ((column - df['پیراهن'].min()) / (df['پیراهن'].max() - df['پیراهن'].min())) * 100)

    df['ژاکت'] = df['ژاکت'].apply(
        lambda column: ((column - df['ژاکت'].min()) / (df['ژاکت'].max() - df['ژاکت'].min())) * 100)

    df['کاپشن'] = df['کاپشن'].apply(
        lambda column: ((column - df['کاپشن'].min()) / (df['کاپشن'].max() - df['کاپشن'].min())) * 100)

    df['کت'] = df['کت'].apply(
        lambda column: ((column - df['کت'].min()) / (df['کت'].max() - df['کت'].min())) * 100)

    df['کت شلوار'] = df['کت شلوار'].apply(
        lambda column: ((column - df['کت شلوار'].min()) / (df['کت شلوار'].max() - df['کت شلوار'].min())) * 100)

    df['کیف'] = df['کیف'].apply(
        lambda column: ((column - df['کیف'].min()) / (df['کیف'].max() - df['کیف'].min())) * 100)

    df['اورآل'] = df['اورآل'].apply(
        lambda column: ((column - df['اورآل'].min()) / (df['اورآل'].max() - df['اورآل'].min())) * 100)

    df['تی شرت'] = df['تی شرت'].apply(
        lambda column: ((column - df['تی شرت'].min()) / (df['تی شرت'].max() - df['تی شرت'].min())) * 100)

    df['دامن'] = df['دامن'].apply(
        lambda column: ((column - df['دامن'].min()) / (df['دامن'].max() - df['دامن'].min())) * 100)

    df['ماسک'] = df['ماسک'].apply(
        lambda column: ((column - df['ماسک'].min()) / (df['ماسک'].max() - df['ماسک'].min())) * 100)

    df['بادی'] = df['بادی'].apply(
        lambda column: ((column - df['بادی'].min()) / (df['بادی'].max() - df['بادی'].min())) * 100)

    df['بافت'] = df['بافت'].apply(
        lambda column: ((column - df['بافت'].min()) / (df['بافت'].max() - df['بافت'].min())) * 100)

    df['ست بلوز و شلوار'] = df['ست بلوز و شلوار'].apply(
        lambda column: ((column - df['ست بلوز و شلوار'].min()) / (df['ست بلوز و شلوار'].max() - df['ست بلوز و شلوار'].min())) * 100)

    df['کفش و صندل'] = df['کفش و صندل'].apply(
        lambda column: ((column - df['کفش و صندل'].min()) / (df['کفش و صندل'].max() - df['کفش و صندل'].min())) * 100)

    df['کلاه،هدبند،پاپوش'] = df['کلاه،هدبند،پاپوش'].apply(
        lambda column: ((column - df['کلاه،هدبند،پاپوش'].min()) / (df['کلاه،هدبند،پاپوش'].max() - df['کلاه،هدبند،پاپوش'].min())) * 100)

    df['بلوز و شلوار کودک'] = df['بلوز و شلوار کودک'].apply(
        lambda column: ((column - df['بلوز و شلوار کودک'].min()) / (df['بلوز و شلوار کودک'].max() - df['بلوز و شلوار کودک'].min())) * 100)

    df['بلوز کودک'] = df['بلوز کودک'].apply(
        lambda column: ((column - df['بلوز کودک'].min()) / (df['بلوز کودک'].max() - df['بلوز کودک'].min())) * 100)

    df['شلوار کودک'] = df['شلوار کودک'].apply(
        lambda column: ((column - df['شلوار کودک'].min()) / (df['شلوار کودک'].max() - df['شلوار کودک'].min())) * 100)

    df['هودی کودک'] = df['هودی کودک'].apply(
        lambda column: ((column - df['هودی کودک'].min()) / (df['هودی کودک'].max() - df['هودی کودک'].min())) * 100)

    columns = ['barani', 'bolooz', 'tonic', 'top', 'sarafone', 'sayer', 'suyishert',
               'shaloroosari', 'shalvar', 'shoomiz', 'manto', 'parche', 'palto', 'pirahan', 'zhackat', 'kapshan',
               'coat', 'coatshalvar', 'kif', 'overal', 'tshert', 'daman', 'mask', 'body', 'baft', 'set_bolooz_shalvar',
               'kafsh_sandal', 'kolah_headband_papoosh',
               'blooz_shalvar_koodak', 'blooz_koodak', 'shalvar_koodak', 'hoody_koodak']

    df.columns = columns
    return df

# df = read_data()
# # print(df.head())
# new_df = make_score(df)
# print(new_df.head())