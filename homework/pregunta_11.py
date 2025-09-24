"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    import pandas as pd

    df = pd.read_csv("files/input/tbl1.tsv", delimiter='\t')

    # agrupar por c0, obtener valores únicos de c4, ordenarlos y unir por coma
    df_grouped = (
        df.groupby('c0')['c4']
          .apply(lambda x: ','.join(sorted(x.astype(str).unique())))
          .reset_index()
          )
    df_grouped = df_grouped[['c0', 'c4']]

    return df_grouped
print(pregunta_11())