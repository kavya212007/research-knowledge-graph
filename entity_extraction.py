import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "WORK_OF_ART"]:
            entities.append((ent.text, ent.label_))

    return entities