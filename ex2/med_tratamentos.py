import csv
from rdflib import Graph, Namespace, Literal,URIRef
from rdflib.namespace import RDF, RDFS

def format_uri(name):
    # Remover espaços em branco e juntar as palavras com a primeira letra em maiúscula
    formatted_name = ''.join(word.capitalize() for word in name.split())
    
    return URIRef(ns + formatted_name)

# Carregar o conteúdo do arquivo med_doencas.ttl
g = Graph()
g.parse('med_doencas.ttl', format='turtle')

# Definir o namespace
ns = Namespace("http://www.example.org/disease-ontology#")

# Definir o predicado hasTreatment
hasTreatment = ns.hasTreatment

# Abrir o arquivo CSV Disease_Treatment.csv e associar precauções aos tratamentos
with open('Disease_Treatment.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pular o cabeçalho se houver

    for row in reader:
        disease_name, *treatments = row

        # Criar URI para a doença
        disease_uri = format_uri(disease_name)

        # Iterar sobre os tratamentos
        for treatment_name in treatments:
            if treatment_name != '':
                treatment_uri = format_uri(treatment_name)

                # Verificar se a entidade de tratamento já existe no grafo
                if (treatment_uri, None, None) not in g:
                    # Se não existir, criar a entidade de tratamento
                    g.add((treatment_uri, RDF.type, ns.Treatment))

                # Adicionar a relação entre a doença e o tratamento
                g.add((disease_uri, hasTreatment, treatment_uri))

# Salvar o novo conteúdo no arquivo med_tratamentos.ttl
g.serialize(destination='med_tratamentos.ttl', format='turtle')