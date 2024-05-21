import json
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Carregar o conteúdo do arquivo med_tratamentos.ttl
g = Graph()
g.parse('med_tratamentos.ttl', format='turtle')

# Definir o namespace
ns = Namespace("http://www.example.org/disease-ontology#")

# Função para formatar a URI
def format_uri(name):
    formatted_name = ''.join(word.capitalize() for word in name.split())
    return URIRef(ns + formatted_name)

# Função para formatar a URI do paciente
def format_patient_uri(patient_id):
    return URIRef(ns + 'Patient' + str(patient_id))

# Criar a propriedade de dados para o nome dos pacientes
name_property = ns['name']

# Abrir e ler o arquivo JSON pg53924.json
with open('pg53924.json') as json_file:
    data = json.load(json_file)
    patient_id = 3

    for entry in data:
        patient_name = entry['nome']
        symptoms = entry['sintomas']

        patient_uri = format_patient_uri(patient_id)
        g.add((patient_uri, RDF.type, ns.Patient))

        # Adicionar o nome do paciente como um data property
        g.add((patient_uri, name_property, Literal(patient_name)))

        for symptom in symptoms:
            symptom_uri = format_uri(symptom)
            g.add((patient_uri, ns.exhibitsSymptom, symptom_uri))

        patient_id += 1

# Salvar o novo conteúdo no arquivo med_doentes.ttl
g.serialize(destination='med_doentes.ttl', format='turtle')
