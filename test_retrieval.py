from src.db.db_manager import DatabaseManager
from src.rag.embeddings import EmbeddingManager
from src.core.config import settings

# Test retrieval
db = DatabaseManager(settings.DATABASE_URL)
embeddings = EmbeddingManager()

query = "Who is Krishna?"
query_embedding = embeddings.embed_text(query)

print(f"Query: {query}")
print(f"Embedding dimension: {query_embedding[0]}")

results = db.search_similar_verses(query_embedding[0], top_k=3)
print(f"\nFound {len(results)} results:")
for r in results:
    print(f"  - {r}")