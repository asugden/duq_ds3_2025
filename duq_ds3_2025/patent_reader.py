from dataclasses import dataclass
import xml.etree.ElementTree as ET

@dataclass
class Assignor():
    forename: str
    surname: str
    # address: str

    def is_valid(self):
        if (self.forename is None or 
                len(self.forename) == 0 or 
                self.surname is None or 
                len(self.surname) == 0):
            return False
        return True

# The at symbol is called a "decorator"
@dataclass
class Patent():
    assignees: list[Assignor]
    name: str
    # date: str
    document_ids: list[str]

    def is_valid(self):
        if len(self.assignees) == 0:
            return False
        
        for assignee in self.assignees:
            if not assignee.is_valid():
                return False
            
        if self.name is None or len(self.name) == 0:
            return False
            
        # if self.date is None or len(self.date) == 0:
        #     return False
            
        return True


def parse_assignment(el: ET.Element):
    """Parse a specific patent assignment, returning a patent"""
    assignors = el.findall('patent-assignors')
    records = el.findall('patent-properties')

    if len(assignors) == 0 or len(records) == 0:
        return None
    
    people = []
    for person in assignors[0].findall('patent-assignor'):
        try:
            name = person.findall('name')[0]
            name_parts = name.text.split(',')
            surname = name_parts[0]
            forename = name_parts[1]
            people.append(Assignor(forename=forename, surname=surname))
        except IndexError:
            pass
    
    doc_ids = []
    name = None
    for record in records[0].findall('patent-property'):
        for title in record.findall('invention-title'):
            if name is None:
                name = title.text
        for doc in record.findall('document-id'):
            for num in doc.findall('document-number'):
                doc_ids.append(num.text)

    return Patent(assignees=people, name=name, document_ids=doc_ids)


def parse_patents(path: str) -> list[Patent]:
    """Parse an XML patent file into Patent dataclass objects
    """
    tree = ET.parse(path)
    root = tree.getroot()
    
    out = []
    assignments = root.findall('patent-assignments')[0]
    for el in assignments.findall('patent-assignment'):
        out.append(parse_assignment(el))

    return [patent for patent in out if patent is not None and patent.is_valid()]


if __name__ == '__main__':
    import zipfile
    zf = zipfile.ZipFile('data/ad20250218.zip')
    parse_patents(zf.open('ad20250218.xml'))