import jarowinkler as jw
import fasttext
import pandas as pd
import numpy as np


class DistanceEmbedder():
    def __init__(self):
        self.ft_model = fasttext.load_model('data/cc.en.50.bin')

    def embed_series(self, names: pd.Series) -> pd.Series:
         return names.apply(lambda x: self.ft_model.get_sentence_vector(x))

    def embed_name(self, name: str) -> np.array:
        return self.ft_model.get_sentence_vector(name)
    
    def clean_series(self, names: pd.Series) -> pd.Series:
        return names.str.lower()


def calculate_distances(df: pd.DataFrame, 
                forename_col_1: str = 'npi_surname', 
                forename_col_2: str = 'patent_forename',
                surname_col_1: str = 'npi_surname',
                surname_col_2: str = 'patent_surname',
                vec_col_1: str = 'npi_vec',
                vec_col_2: str = 'patent_vec') -> pd.DataFrame:
    df['jw_dist_surname'] = df.apply(
        lambda row: jw.jaro_similarity(row[surname_col_1],
                                        row[surname_col_2]), axis=1)
    df['jw_dist_forename'] = df.apply(
        lambda row: jw.jaro_similarity(row[forename_col_1],
                                        row[forename_col_2]), axis=1)

    df['ft_dist_last_name'] = df.apply(
        lambda row: np.linalg.norm(row[vec_col_1] - 
                                    row[vec_col_2]), axis=1)
    
    return df