import pytest
from unittest.mock import MagicMock
from src.graph.graph_ingestor import GraphIngestor


@pytest.fixture
def mock_db():
    db = MagicMock()
    # Mock context manager for connection
    conn = MagicMock()
    cursor = MagicMock()
    db._get_connection.return_value.__enter__.return_value = conn
    conn.cursor.return_value.__enter__.return_value = cursor
    return db


@pytest.fixture
def mock_builder():
    return MagicMock()


@pytest.fixture
def mock_extractor():
    return MagicMock()


def test_ingest_single_batch(mock_db, mock_builder, mock_extractor):
    ingestor = GraphIngestor(mock_db, mock_builder, mock_extractor)

    # Mock DB Return
    # _fetch_mantras is internal but we mocked the DB call inside it.
    # Actually, simpler to verify _fetch_mantras logic if we don't mock it out completely.
    # But let's mock _fetch_mantras for unit testing the loop logic if possible,
    # or better, mock the cursor return.

    cursor = (
        mock_db._get_connection.return_value.__enter__.return_value.cursor.return_value.__enter__.return_value
    )
    # Use aliases 'text' and 'translation' as per the SQL query in _fetch_mantras
    cursor.description = [("id",), ("text",), ("translation",), ("source",)]
    cursor.fetchall.side_effect = [
        [(1, "Om Agni", "Fire", "RV")],  # Batch 1
        [],  # Batch 2 (Empty -> Stop)
    ]

    # Mock Extractor Return
    mock_extractor.extract_entities.return_value = {
        "entities": [{"name": "Agni", "type": "Deity"}],
        "relationships": [],
    }

    stats = ingestor.ingest_all_mantras(batch_size=1)

    assert stats["processed"] == 1
    assert stats["entities"] == 1

    # Verify Builder calls
    mock_builder.create_entity.assert_called()  # Mantra node
    mock_builder.create_entities_batch.assert_called()  # Entities
    mock_builder.create_relationships_batch.assert_called()  # Relationships


def test_process_mantra_logic(mock_db, mock_builder, mock_extractor):
    ingestor = GraphIngestor(mock_db, mock_builder, mock_extractor)

    mock_extractor.extract_entities.return_value = {
        "entities": [{"name": "Agni", "type": "Deity"}],
        "relationships": [{"from": "Agni", "to": "Heat", "type": "CAUSES"}],
    }

    res = ingestor.process_mantra(101, "Text", "Trans", "Source")

    assert res["entities"] == 1
    assert res["relationships"] == 2  # 1 extracted + 1 mantra link

    # Check if mantra link was created
    # create_relationships_batch called twice: once for extracted, once for mantra links
    assert mock_builder.create_relationships_batch.call_count == 2

    # Verify mantra link content
    calls = mock_builder.create_relationships_batch.call_args_list
    mantra_links = calls[1][0][0]  # 2nd call, 1st arg
    assert mantra_links[0]["from"] == "Mantra 101"
    assert mantra_links[0]["to"] == "Agni"
