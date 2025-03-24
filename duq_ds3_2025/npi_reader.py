import pandas as pd
import sqlalchemy


def read(path: str) -> pd.DataFrame:
    """Read in NPI data and rename columns"""
    df = pd.read_csv(path)
    mapper = {
            'NPI': 'npi',
            'Healthcare Provider Taxonomy Code_1': 'taxonomy_code',
            'Provider Last Name (Legal Name)': 'surname',
            'Provider First Name': 'forename',
            'Provider First Line Business Practice Location Address': 'address',
            'Certification Date': 'cert_date',
            'Provider Business Practice Location Address State Name': 'city',
            'Provider Business Practice Location Address State Name': 'state',
            'Provider Business Practice Location Address Country Code (If outside U.S.)': 'country'
        }
    
    df = df.rename(columns=mapper)[mapper.values()]
    return df

    #There are 850 missing values for taxonomy_code, address, state, and country
    #There are 6,259 missing last names and 6,262 missing first names
    #There are 1,505 missing values for cert_date

def to_db():
    """Push data to the database"""
    """
    CREATE TABLE IF NOT EXISTS npi_providers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        forename VARCHAR(250),
        surname VARCHAR(250) NOT NULL
    )
    """
    engine = sqlalchemy.create_engine('sqlite:///data/patent_npi_db.sqlite')
    conn = engine.connect()
    df = read('data/npidata_pfile_20240205-20240211.csv')
    df = (df[['surname', 'forename']]
            .dropna(subset=['surname'])
            .to_sql('npi_providers', conn, if_exists='append', index=False))
    conn.close()


def test_read_db():
    """Read back the NPI data we pushed to the db"""
    engine = sqlalchemy.create_engine('sqlite:///data/patent_npi_db.sqlite')
    conn = engine.connect()

    df = pd.read_sql_query("""SELECT surname, forename
                              FROM npi_providers""", conn)
    print(df)

    conn.close()  # good habit-- not always necessary



if __name__ == '__main__':
    # df = read('data/npidata_pfile_20240205-20240211.csv')
    # print(df.head())
    # to_db()
    test_read_db()