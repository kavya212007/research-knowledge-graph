from pdf_parser import extract_text
from entity_extraction import extract_entities
from graph_builder import build_graph, visualize_graph

print("Program started...")

paper_path = "sample_paper.pdf"

text = extract_text(paper_path)

print("Text extracted!")

entities = extract_entities(text)

print("Entities Found:", entities[:20])

graph = build_graph("Research Paper", entities)

visualize_graph(graph)

print("Graph visualization created!")