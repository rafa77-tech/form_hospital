import pandas as pd
from typing import Dict, Any
import json

def load_hospitals_data() -> Dict[str, Any]:
    try:
        df = pd.read_csv('data/hospitais.csv', sep=';')
        hospitals_dict = df.set_index('hospital_id').to_dict('index')
        # Converter todas as chaves para string
        hospitals_dict = {str(k): v for k, v in hospitals_dict.items()}
        return hospitals_dict
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return {}


def get_pending_hospitals(hospitals_data: Dict[str, Any]) -> Dict[str, str]:
    """
    Retorna um dicionário com id e nome dos hospitais pendentes
    """
    return {
        str(hospital_id): data['NO_FANTASIA'] 
        for hospital_id, data in hospitals_data.items()
    }

def save_hospital_data(hospitals_data: Dict[str, Any]) -> None:
    """
    Salva os dados dos hospitais atualizados no CSV
    """
    try:
        df = pd.DataFrame.from_dict(hospitals_data, orient='index')
        df.index.name = 'hospital_id'
        df.to_csv('data/hospitais.csv')
        df.to_csv('data/hospitais_processados.csv')
    except Exception as e:
        raise Exception(f"Erro ao salvar dados: {e}")