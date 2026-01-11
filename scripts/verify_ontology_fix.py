import logging
import sys
import os
from neo4j import GraphDatabase

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.core.config import settings


def verify_fix():

    print("Connecting to Neo4j for Ontology Verification...")
    try:
        driver = GraphDatabase.driver(
            settings.NEO4J_URI, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )
    except Exception as e:
        print(f"Failed to connect: {e}")
        return

    with driver.session() as session:
        # 1. Check Totals
        print("\n--- 1. Graph Totals ---")
        res = session.run("MATCH (n) RETURN count(n) as nodes").single()
        nodes = res["nodes"]
        res = session.run("MATCH ()-[r]->() RETURN count(r) as rels").single()
        rels = res["rels"]
        
        print(f"Nodes: {nodes}")
        print(f"Relationships: {rels}")
        
        if rels == 0 and nodes > 0:
            print("❌ FAILED: Nodes exist but NO relationships found!")
        elif rels > 0:
             print("✅ SUCCESS: Relationships exist.")

        # 2. Check Text -> Concept Relations (MENTIONS)
        print("\n--- 2. Checking Text -> MENTIONS -> Concept ---")
        q = """
        MATCH (t:Text)-[r:MENTIONS]->(c:Concept) 
        RETURN t.verse_id as verse, c.name as concept, r.confidence as conf 
        LIMIT 5
        """
        res = session.run(q).data()
        if not res:
            # Try matching generalized labels just in case
            q2 = "MATCH (a)-[r:MENTIONS]->(b) RETURN labels(a) as al, labels(b) as bl LIMIT 1"
            res2 = session.run(q2).data()
            if res2:
                print(f"Found MENTIONS but types might differ: {res2}")
            else:
                 print("❌ FAILED: No 'MENTIONS' relationships found between Text and Concepts.")
        else:
            print("✅ SUCCESS: Found MENTIONS relationships:")
            for row in res:
                print(f"   Verse {row['verse']} --[MENTIONS]-> {row['concept']}")

        # 3. Check Isolated Nodes
        print("\n--- 3. Checking for Isolated Nodes ---")
        q_iso = "MATCH (n) WHERE NOT (n)-[]-() RETURN labels(n) as lbl, count(*) as c"
        res_iso = session.run(q_iso).data()
        
        total_isolated = sum(r['c'] for r in res_iso)
        if total_isolated == 0:
            print("✅ SUCCESS: No isolated nodes found.")
        else:
            print(f"⚠️ WARNING: Found {total_isolated} isolated nodes:")
            for r in res_iso:
                print(f"   {r['lbl']}: {r['c']}")

        # 4. Check Ontology Internal Relations
        print("\n--- 4. Checking Ontology Internal Relations (e.g. RELATED_TO, PARENT_OF) ---")
        q_ont = """
        MATCH (c1:Concept)-[r]->(c2:Concept) 
        WHERE type(r) <> 'MENTIONS'
        RETURN c1.name, type(r), c2.name LIMIT 5
        """
        res_ont = session.run(q_ont).data()
        if res_ont:
            print("✅ SUCCESS: Found Ontology connections:")
            for row in res_ont:
                print(f"   {row['c1.name']} --[{row['type(r)']}]--> {row['c2.name']}")
        else:
            print("⚠️ WARNING: No internal Concept-Concept relationships found (might be okay if seeded ontology has none or concepts disjoint).")

    driver.close()

if __name__ == "__main__":
    verify_fix()
