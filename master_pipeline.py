import os
import argparse
import subprocess
from dotenv import load_dotenv

def main():
    parser = argparse.ArgumentParser(description="Master Pipeline: Orchestrating Sub-div, RAG-schema, and Embeddings")
    parser.add_argument("-p", "--problem-statement", required=True, help="Path to the Markdown problem statement file")
    parser.add_argument("-s", "--schema-input", required=True, help="Path to a single raw schema CSV file OR a directory of CSVs")
    
    args = parser.parse_args()
    
    # Convert input arguments to absolute paths to prevent relative path (cwd) issues
    problem_statement_abs = os.path.abspath(args.problem_statement)
    schema_input_abs = os.path.abspath(args.schema_input)
    
    # Ensure root .env is loaded
    load_dotenv()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define script paths
    sub_div_script = os.path.join(base_dir, "01_sub_problem_generation", "pipeline.py")
    rag_schema_script = os.path.join(base_dir, "02_schema_enrichment", "rag_schema.py")
    embeddings_script = os.path.join(base_dir, "03_vectorization", "gemini_pipeline.py")
    semantic_search_script = os.path.join(base_dir, "04_similarity_search", "semantic_search.py")
    
    # Output paths
    sub_div_output = os.path.join(base_dir, "01_sub_problem_generation", "output")
    enriched_schema_output_dir = os.path.join(base_dir, "02_schema_enrichment", "output")
    
    # Step 1: Sub-div
    print("="*50)
    print("STEP 1: Sub-dividing Problem Statement")
    print("="*50)
    subprocess.run(["python", sub_div_script, "-i", problem_statement_abs, "-o", sub_div_output], check=True)
    
    # Step 2: RAG Schema Enrichment
    print("\n" + "="*50)
    print("STEP 2: Enriching Schema with NLP (Groq API)")
    print("="*50)
    subprocess.run(["python", rag_schema_script, "-i", schema_input_abs, "-o", enriched_schema_output_dir], cwd=os.path.join(base_dir, "02_schema_enrichment"), check=True)
    
    # Step 3: Embeddings
    print("\n" + "="*50)
    print("STEP 3: Generating Embeddings for Enriched Schema & Sub-problems")
    print("="*50)
    vectorization_dir = os.path.join(base_dir, "03_vectorization")
    subprocess.run(["python", embeddings_script, "-i", enriched_schema_output_dir, "-j", sub_div_output], cwd=vectorization_dir, check=True)
    
    # Step 4: Similarity Search
    print("STEP 4: Semantic Similarity Search")
    print("="*50)
    chroma_db_dir = os.path.join(base_dir, "03_vectorization", "chroma_gemini_db")
    docs_dir = os.path.join(base_dir, "docs")
    
    subprocess.run(["python", semantic_search_script, "-d", chroma_db_dir, "-o", docs_dir], cwd=os.path.join(base_dir, "04_similarity_search"), check=True)
    
    print("\n" + "="*50)
    print("Master Pipeline Completed Successfully!")
    print(f"-> Sub-problems JSONs saved in: {sub_div_output}")
    print(f"-> Enriched Schemas saved to: {enriched_schema_output_dir}")
    print(f"-> Embeddings DB created/updated at: {os.path.join(base_dir, '03_vectorization', 'chroma_gemini_db')}")
    print(f"-> Similarity Reports saved to: {docs_dir}")
    print("="*50)

if __name__ == "__main__":
    main()
