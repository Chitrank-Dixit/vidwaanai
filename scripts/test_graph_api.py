import sys
import os
import logging

# Add src to python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fastapi.testclient import TestClient
from src.api import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_api():
    client = TestClient(app)

    # 1. Search
    logger.info("Testing Search...")
    resp = client.get("/api/kg/search/entities?q=Krishna")
    if resp.status_code != 200:
        logger.error(f"Search failed: {resp.text}")
        return

    results = resp.json()
    logger.info(f"Search found {len(results)} results")
    if not results:
        logger.error("No results found for 'Krishna'. Aborting.")
        return

    first_result = results[0]
    entity_id = first_result.get("id")
    name = first_result.get("name")
    logger.info(f"Using Entity: {name} ({entity_id})")

    # 2. Get Entity Details
    logger.info(f"Testing Get Entity {entity_id}...")
    resp = client.get(f"/api/kg/entity/{entity_id}")
    if resp.status_code == 200:
        data = resp.json()
        logger.info(f"Entity: {data['entity'].get('name')}")
        logger.info(f"Outgoing Relations: {len(data['outgoing'])}")
        logger.info(f"Incoming Relations: {len(data['incoming'])}")
    else:
        logger.warning(f"Get Entity failed: {resp.status_code} - {resp.text}")

    # 3. Path Finding
    # Try to find path to another character if possible
    # Search for Arjuna
    resp_arj = client.get("/api/kg/search/entities?q=Arjuna")
    if resp_arj.status_code == 200 and resp_arj.json():
        end_id = resp_arj.json()[0]["id"]
        logger.info(f"Testing Path from {entity_id} to {end_id}...")
        resp = client.get(f"/api/kg/path/{entity_id}/{end_id}")
        if resp.status_code == 200:
            path_data = resp.json()
            logger.info(f"Path Found: {path_data['found']}")
            if path_data["found"]:
                logger.info(f"Path Length: {path_data['length']}")
        else:
            logger.warning(f"Path finding error: {resp.text}")
    else:
        logger.warning("Could not find Arjuna for path testing")

    # 4. Reasoning
    # Use Dharma if found, else use Krishna
    resp_dharma = client.get("/api/kg/search/entities?q=Dharma")
    reason_id = (
        resp_dharma.json()[0]["id"]
        if (resp_dharma.status_code == 200 and resp_dharma.json())
        else entity_id
    )

    logger.info(f"Testing Reasoning for {reason_id}...")
    resp = client.post("/api/kg/reason", json={"entity_id": reason_id, "hops": 2})
    if resp.status_code == 200:
        r_data = resp.json()
        logger.info(f"Implications found: {len(r_data.get('implications', []))}")
        for imp in r_data.get("implications", [])[:3]:
            logger.info(f" - {imp}")
    else:
        logger.warning(f"Reasoning error: {resp.text}")


if __name__ == "__main__":
    test_api()
