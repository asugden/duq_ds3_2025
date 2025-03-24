from dataclasses import dataclass
import xml.etree.ElementTree as ET
import sqlalchemy
import pandas as pd

@dataclass
class Assignee():
    name: str
    address: str

    def is_valid(self):
        if self.name is None or len(self.name) == 0:
            return False
        if self.address is None:
            return False
        return True

@dataclass
class Assignor():
    forename: str
    surname: str

    def is_valid(self):
        if (self.forename is None or 
            len(self.forename) == 0 or 
            self.surname is None 
            or len(self.surname) == 0
        ):
            return False
        return True

# @ is "decorator" 
@dataclass
class Patent():
    assignors: list[Assignor]
    assignees: list[Assignee]
    name: str
    document_ids: list[str]

    def is_valid(self):
        if self.assignors is None or len(self.assignors) == 0:
            return False
        if self.name is None or len(self.name) == 0:
            return False
        
        for assignor in self.assignors:
            if not assignor.is_valid():
                return False
        for assignee in self.assignees:
            if not assignee.is_valid():
                return False
            
        return True

def parse_address(company:ET.Element) -> str|None:
    """takes an assignee xml element and returns 
    the adress (formated to the best of my ability)

    Args:
        company (ET.Element): an xml element of <patent-assignee>

    Returns:
        str|None: an adress needs all city, state, and postal code and
        atleast 1 adress line
    """
    address = ''
    line = 0
    while True:
        line += 1
        xml_line = company.find(f'address-{line}')
        if xml_line is None:
            break
        address += xml_line.text + '\n'
    xml_city = company.find('city')
    xml_state = company.find('state')
    xml_postcode = company.find('postcode')
    if xml_city is None:
        return None
    if xml_state is None:
        return None
    if xml_postcode is None:
        return None
    city = xml_city.text
    state = xml_state.text
    postcode = xml_postcode.text
    address += f'{city} {state} {postcode}' 
    return address



def parse_assignment(element:ET.Element) -> Patent|None:
    """parse a specific patent assigment from an element

    Args:
        element (ET.Element): an xtml element
    """
    assignors = element.find('patent-assignors')
    assinees = element.find('patent-assignees')
    records = element.find('patent-properties')
    if assignors is None:
        return None
    if records is None:
        return None
    if assinees is None:
        return None

    people = []
    companies = []
    for company in assinees.findall('patent-assignee'):
        xml_name = company.find('name')
        if xml_name is None:
            continue
        name = xml_name.text
        address = parse_address(company)
        companies.append(Assignee(name=name,address=address))


    for person in assignors.findall('patent-assignor'):
        try:
            name = person.find('name')
            if name is None:
                # no name
                continue
            name_parts = name.text.split(', ')
            surname = name_parts[0]
            forename = name_parts[1]
            people.append(Assignor(forename=forename,surname=surname))
        except IndexError:
            pass
        
    
    doc_ids = []
    patent_name = None
    for record in records.findall('patent-property'):
        for title in record.findall('invention-title'):
            if patent_name is None:
                patent_name = title.text
        for doc in record.findall('document-id'):
            for num in doc.findall('doc-number'):
                doc_ids.append(num.text)
    return Patent(document_ids=doc_ids,name=patent_name,assignors=people,assignees=companies)


def get_engine():
    """Get SQLAlchemy connectino to the db"""
    engine = sqlalchemy.create_engine('sqlite:///data/patent_npi_db.sqlite')
    return engine.connect()


def parse_patents(path:str) -> list[Patent]:
    """parses patents from a xtml file returning a list of patents

    Args:
        path (str): path to xtml

    Returns:
        list[Patent]: list of patents
    """
    tree = ET.parse(path)
    root = tree.getroot()
    
    out = []
    assignments = root.find('patent-assignments')
    if assignments is None:
        return []
    for el in assignments.findall('patent-assignment'):
        out.append(parse_assignment(el))
    
    
    for patent in out:
        if patent is not None and len(patent.document_ids) > 0:
            ext_id = patent.document_ids[0]
            rows = pd.read_sql(f'SELECT patent_id FROM external_ids WHERE external_id={ext_id}', get_engine())
            if len(rows) == 0:
                conn = get_engine()
                pd.DataFrame([[patent.name]], columns=['title']).to_sql('patents', 
                                                                        conn, 
                                                                        if_exists='append',
                                                                        index=False)
                patent_id = pd.read_sql('SELECT last_insert_rowid() FROM patents;', conn)
                patent_id = int(patent_id.iloc[0]['last_insert_rowid()'])
                
                pd.DataFrame([[patent_id, docid] for docid in patent.document_ids], 
                             columns=['patent_id', 'external_id']).to_sql('external_ids', get_engine(), if_exists='append',
                                                                        index=False)
                pd.DataFrame([[patent_id, assignee.name, assignee.address] for assignee in patent.assignees], 
                             columns=['patent_id', 'name', 'address']).to_sql('assignees', get_engine(), if_exists='append',
                                                                        index=False)
                # pd.DataFrame([[patent_id, docid] for docid in patent.document_ids], 
                #              columns=['patent_id', 'name', 'address']).to_sql('external_ids', conn, if_exists='append')

    return [patent for patent in out if patent is not None and patent.is_valid()]


def patents_to_dataframes(patents: list[Patent]):
    """Convert patents to tables for adding to SQL."""

    # database connection
    engine = sqlalchemy.create_engine('sqlite:///data/patent_npi_db.sqlite')
    conn = engine.connect()

    temp_patents_table = [[patent.document_ids[0], patent.name] for patent in patents]
    temp_assignees_table = [[patent.document_ids[0], assignee.name, assignee.address] for patent in patents for assignee in patent.assignees]
    temp_assignors_table = [[patent.document_ids[0], assignor.forename, assignor.surname] for patent in patents for assignor in patent.assignors]
    temp_external_ids_table = [[patent.document_ids[0], docid] for patent in patents for docid in patent.document_ids[1:]]

    pd.DataFrame(temp_patents_table, 
                 columns=['ext_id', 'title']).to_sql('temp_patents', 
                                                     conn, 
                                                     if_exists='append')
    pd.DataFrame(temp_assignees_table, 
                 columns=['ext_id', 'name', 'address']).to_sql('temp_assignees', 
                                                     conn, 
                                                     if_exists='append')
    pd.DataFrame(temp_assignors_table, 
                 columns=['ext_id', 'forename', 'surname']).to_sql('temp_assignors', 
                                                     conn, 
                                                     if_exists='append')
    pd.DataFrame(temp_external_ids_table, 
                 columns=['ext_id', 'ext_id_alt']).to_sql('temp_external_ids', 
                                                     conn, 
                                                     if_exists='append')


if __name__ == '__main__':
    import zipfile
    zf = zipfile.ZipFile('data/ad20250218.zip')
    patents = parse_patents(zf.open('ad20250218.xml'))
    patents_to_dataframes(patents)