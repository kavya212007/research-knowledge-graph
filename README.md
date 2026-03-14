# AI Research Knowledge Graph Builder

This project automatically reads research papers and builds a knowledge graph showing relationships between research entities such as authors, methods, and topics.

## Features

- Extracts text from research paper PDFs
- Uses NLP to detect entities like authors and research topics
- Builds a knowledge graph from extracted entities
- Visualizes the graph interactively

## Technologies Used

- Python
- spaCy
- PyMuPDF
- NetworkX
- PyVis

## How to Run

1. Install required libraries
pip install pymupdf spacy networkx pyvis

2. Download spaCy model
python -m spacy download en_core_web_sm

3. Run the program
python main.py

## Output

The program generates an interactive knowledge graph saved as:

research_graph.html