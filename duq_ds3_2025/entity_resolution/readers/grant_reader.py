import pandas as pd


class GrantReader():
    def __init__(self, path: str):
        """Read in an NIH grant exporter file

        Args:
            path (str): location of the file
        """
        self.df = pd.read_csv(path)
        self._clean_df_columns()
        self._clean_data()

    def _clean_df_columns(self):
        """Fix column names to be lowercase"""
        mapper = {
            'APPLICATION_ID': 'application_id',
            'BUDGET_START': 'budget_start',
            'ACTIVITY': 'grant_type',
            'TOTAL_COST': 'total_cost',
            'PI_NAMEs': 'pi_names',
            'PI_IDS': 'pi_ids',
            'ORG_NAME': 'organization',
            'ORG_CITY': 'city',
            'ORG_STATE': 'state',
            'ORG_COUNTRY': 'country',
        }
        self.df = self.df.rename(columns=mapper)[mapper.values()]

    def _clean_data(self):
        """Split PI names"""
        self.df['pi_names'] = self.df['pi_names'].str.split(';')
        self.df = self.df.explode('pi_names')
        self.df['is_contact'] = self.df['pi_names'].str.lower().str.contains('(contact)')
        self.df['pi_names'] = self.df['pi_names'].str.replace('(contact)', '')


if __name__ == '__main__':
    gr = GrantReader('data/RePORTER_PRJ_C_FY2024.csv')
    print(gr.df)