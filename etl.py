import pandas as pd
import requests

def requestApiBcb(data: str) -> pd.DataFrame:

    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%2720051%27&$format=json"
    req = requests.get(url)
    print("Status Code: ", req.status_code)
    dados = req.json()

    df = pd.json_normalize(dados["value"])
    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
    return df

dadosBcb = requestApiBcb('20191')
print(dadosBcb.info())