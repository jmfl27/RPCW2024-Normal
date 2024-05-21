import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, OWL, XSD, RDFS

# Carregar a ontologia
onto = '''
@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

:Ontology a owl:Ontology .

# Classes
:Disease a owl:Class .
:Symptom a owl:Class .
:Treatment a owl:Class .
:Patient a owl:Class .

# Properties
:hasSymptom a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Symptom .

:hasTreatment a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Treatment .

:exhibitsSymptom a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Symptom .

:hasDisease a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Disease .

:receivesTreatment a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Treatment .

# Disease instances
:Flu a :Disease ;
    :hasSymptom :Fever, :Cough, :SoreThroat ;
    :hasTreatment :Rest, :Hydration, :AntiviralDrugs .

:Diabetes a :Disease ;
    :hasSymptom :IncreasedThirst, :FrequentUrination, :Fatigue ;
    :hasTreatment :InsulinTherapy, :DietModification, :Exercise .

# Symptom instances
:Fever a :Symptom .
:Cough a :Symptom .
:SoreThroat a :Symptom .
:IncreasedThirst a :Symptom .
:FrequentUrination a :Symptom .
:Fatigue a :Symptom .

# Treatment instances
:Rest a :Treatment .
:Hydration a :Treatment .
:AntiviralDrugs a :Treatment .
:InsulinTherapy a :Treatment .
:DietModification a :Treatment .
:Exercise a :Treatment .


# Patient instances
:Patient1 a :Patient ;
    :name "Paul Harrods" ;
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana" ;
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .
'''

def format_uri(name):
    # Remover espaços em branco e juntar as palavras com a primeira letra em maiúscula
    formatted_name = ''.join(word.capitalize() for word in name.split())
    
    return ns[formatted_name]

g = Graph()
g.parse(data=onto, format="turtle")
ns = Namespace("http://www.example.org/disease-ontology#")
RDF.type

g.add((ns['hasDescription'], RDF.type, RDF.Property))
g.add((ns['hasDescription'], RDFS.domain, ns['Disease']))
g.add((ns['hasDescription'], RDFS.range, RDFS.Literal))

# Abrir o arquivo CSV e adicionar as doenças à ontologia
with open('Disease_Syntoms.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pular o cabeçalho se houver

    for row in reader:
        disease_name = row[0]
        symptoms = row[1:]
        
        # Verificar se a doença já existe no grafo, senão adicionar como indivíduo
        disease_uri = format_uri(disease_name)
        if (disease_uri, RDF.type, ns['Disease']) not in g:
            g.add((disease_uri, RDF.type, ns['Disease']))

        for symptom in symptoms:
            if symptom != '':
                symptom_uri = format_uri(symptom)
                # Verificar se o sintoma já existe no grafo, senão adicionar como indivíduo
                if (symptom_uri, RDF.type, ns['Symptom']) not in g:
                    g.add((symptom_uri, RDF.type, ns['Symptom']))

                # Adicionar a relação entre a doença e o sintoma
                g.add((disease_uri, ns['hasSymptom'], symptom_uri))

# Abrir o arquivo CSV Disease_Description.csv e associar descrições às doenças
with open('Disease_Description.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Pular o cabeçalho se houver

    for row in reader:
        disease_name, description = row

        disease_uri = format_uri(disease_name)

        # Adicionar a descrição à doença
        g.add((disease_uri, ns['hasDescription'], Literal(description)))

# Salvar o grafo RDF atualizado em um arquivo .ttl
g.serialize(destination='med_doencas.ttl', format='turtle')