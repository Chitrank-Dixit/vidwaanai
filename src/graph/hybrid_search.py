from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)


class HybridSearcher:
    """Combine graph traversal with vector search."""

    def __init__(
        self, graph_retriever, vector_db, embeddings, entity_extractor, alpha=0.5
    ):
        self.graph = graph_retriever
        self.vector = vector_db
        self.embeddings = embeddings
        self.extractor = entity_extractor
        self.alpha = alpha  # balance between graph and vector

    def search(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """
        Hybrid search combining graph and vector results.

        Returns:
        {
            "graph_results": [...],  # from graph traversal
            "vector_results": [...], # from vector similarity
            "fused_context": "...",  # combined context for LLM
            "sources": [...]         # all sources cited
        }
        """
        try:
            # 1. Extract entities from query
            # We use a simplified extraction or the full LLM extractor
            # For query, we might want a faster extraction or just keyword matching if LLM is slow
            # But per plan, we use the extractor.
            # Note: EntityExtractor requires verse_text, translation, scripture_name.
            # We might need a specific method for query entity extraction in EntityExtractor
            # or reuse extract_entities with dummy values if it's flexible.
            # Let's assume we use the LLM to extract entities from the query string.
            # We might need to extend EntityExtractor to handle queries specifically.
            # For now, let's try to use it as is or assume it has a method.
            # Checking EntityExtractor again... it takes verse_text.
            # I should probably add a method to EntityExtractor for queries or just use the LLM directly here.
            # Better: Add extract_query_entities to EntityExtractor.

            # For now, let's implement a simple extraction here using the same LLM client if accessible,
            # or rely on the extractor having a method.
            # Let's assume we update EntityExtractor to have extract_from_query.
            # Or we can just use the LLM client from the extractor if it's public.

            entities = self._extract_query_entities(query)

            # 2. Graph traversal
            graph_results = []
            for entity in entities:
                if entity["type"] == "Person":
                    # Find teachings
                    teachings = self.graph.find_teachings(entity["name"], query)
                    graph_results.extend(teachings)
                elif entity["type"] == "Concept":
                    # Find related concepts
                    related = self.graph.find_related_concepts(entity["name"])
                    graph_results.extend(related)

            # 3. Vector search
            query_embedding = self.embeddings.embed_text(query)
            vector_results = self.vector.retrieve_verses(query_embedding, top_k=top_k)

            # 4. Fusion
            fused_context = self._fuse_context(graph_results, vector_results)

            return {
                "graph_results": graph_results,
                "vector_results": vector_results,
                "fused_context": fused_context,
                "sources": vector_results,  # Graph results might not have direct verse IDs easily mapping to sources yet
            }

        except Exception as e:
            logger.error(f"Hybrid search failed: {str(e)}")
            # Fallback to vector search
            try:
                query_embedding = self.embeddings.embed_text(query)
                vector_results = self.vector.retrieve_verses(
                    query_embedding, top_k=top_k
                )
                return {
                    "graph_results": [],
                    "vector_results": vector_results,
                    "fused_context": self._format_vector_context(vector_results),
                    "sources": vector_results,
                }
            except Exception as e2:
                logger.error(f"Fallback vector search failed: {str(e2)}")
                return {
                    "graph_results": [],
                    "vector_results": [],
                    "fused_context": "",
                    "sources": [],
                }

    def _extract_query_entities(self, query: str) -> List[Dict]:
        """Extract entities from query using the extractor's LLM."""
        # This is a placeholder. Ideally we extend EntityExtractor.
        # For now, let's try to use the extractor's LLM to parse the query.
        prompt = f"""
        Extract entities from this query.
        Query: {query}
        
        Return JSON with list of entities:
        [{{"name": "Krishna", "type": "Person"}}, {{"name": "dharma", "type": "Concept"}}]
        """
        try:
            import json

            response = self.extractor.llm.generate(prompt, max_tokens=200)
            # Basic cleanup if needed
            response = response.replace("```json", "").replace("```", "").strip()
            return json.loads(response)
        except (json.JSONDecodeError, ValueError):
            return []

    def _fuse_context(
        self, graph_results: List[Dict], vector_results: List[Dict]
    ) -> str:
        """Combine graph and vector results into a context string."""
        context_parts = []

        if graph_results:
            context_parts.append("--- Knowledge Graph Context ---")
            for res in graph_results:
                # Format graph result based on what GraphRetriever returns
                # It returns path, entities, relations
                # We need to make it readable
                # This is a simplified representation
                context_parts.append(str(res))

        if vector_results:
            context_parts.append("\n--- Scripture Verses ---")
            for verse in vector_results:
                context_parts.append(
                    f"{verse['scripture']} {verse['chapter']}.{verse['verse']}: {verse['translation']}"
                )

        return "\n".join(context_parts)

    def _format_vector_context(self, vector_results: List[Dict]) -> str:
        parts = ["--- Scripture Verses ---"]
        for verse in vector_results:
            parts.append(
                f"{verse['scripture']} {verse['chapter']}.{verse['verse']}: {verse['translation']}"
            )
        return "\n".join(parts)
