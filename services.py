def filtro_anual(df, ea_sub: str, mine_sub: str):
    filtro = (df['Subscription Type'] == 'Annual') & \
        (df['EA Play Season Pass'] == ea_sub) & \
        (df['Minecraft Season Pass'] == mine_sub)

    anual_filtro = df[filtro].copy()
    return anual_filtro['Total Value'].sum()

def filtro_planos(df, condicao_reno):
    filtro = (df['Auto Renewal'] == condicao_reno) & \
              (df['Subscription Type'] == 'Annual') & \
              (df['EA Play Season Pass'] == 'Yes') & \
              (df['Minecraft Season Pass'] == 'Yes')

    total_auto = df[filtro].copy()
    return int(total_auto['Total Value'].count())

