from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class EntityType(str, Enum):
    """Types of entities in the Vedic Knowledge Graph."""

    DEITY = "Deity"  # e.g., Agni, Indra, Shiva
    CONCEPT = "Concept"  # e.g., Dharma, Karma, Atman
    CHARACTER = "Character"  # e.g., Arjuna, Rama
    LOCATION = "Location"  # e.g., Ayodhya, Kurukshetra
    EVENT = "Event"  # e.g., Mahabharata War
    TEXT = "Text"  # e.g., Rig Veda, Bhagavad Gita
    TEACHING = "Teaching"  # e.g., Four Noble Truths (if applicable), Upadesha
    PRACTICE = "Practice"  # e.g., Yoga, Yajna
    EMOTION = "Emotion"  # e.g., Bhakti, Kopa
    QUALITY = "Quality"  # e.g., Guna (Sattva, Rajas, Tamas)
    TIME_PERIOD = "TimePeriod"  # e.g., Yuga


class RelationType(str, Enum):
    """Types of relationships between entities."""

    # Hierarchical
    IS_A = "IS_A"  # Inheritance (Shiva is a Deity)
    PART_OF = "PART_OF"  # Composition (Ayodhya is part of Kosala)

    # Causal / Functional
    CAUSES = "CAUSES"  # Action -> Result
    LEADS_TO = "LEADS_TO"  # Practice -> Goal
    MANIFESTS_AS = "MANIFESTS_AS"  # Avatar definition (Vishnu manifests as Rama)

    # Relational
    RELATED_TO = "RELATED_TO"  # Generic association
    PARENT_OF = "PARENT_OF"  # Genealogy
    CHILD_OF = "CHILD_OF"
    SPOUSE_OF = "SPOUSE_OF"
    SIBLING_OF = "SIBLING_OF"
    TEACHER_OF = "TEACHER_OF"  # Guru-Shishya
    STUDENT_OF = "STUDENT_OF"
    DEVOTEE_OF = "DEVOTEE_OF"  # Bhakti relation
    ENEMY_OF = "ENEMY_OF"
    ALLY_OF = "ALLY_OF"

    # Contextual
    MENTIONS = "MENTIONS"  # Entity appears in Text
    MENTIONED_IN = "MENTIONED_IN"  # Entity appears in Text
    LOCATED_AT = "LOCATED_AT"  # Spatial
    HAPPENED_AT = "HAPPENED_AT"  # Event location
    OCCURRED_DURING = "OCCURRED_DURING"  # Temporal

    # Conceptual
    EXEMPLIFIES = "EXEMPLIFIES"  # Character exemplifies Concept (Rama -> Dharma)
    OPPOSES = "OPPOSES"  # Concept duality (Dharma opposes Adharma)


class EntityNode(BaseModel):
    """Represents a node in the graph."""

    id: str  # Unique identifier (e.g., "entity:Agni")
    name: str  # Display name
    type: EntityType
    description: Optional[str] = None
    properties: Dict[str, Any] = Field(default_factory=dict)


class RelationEdge(BaseModel):
    """Represents a relationship edge."""

    source_id: str
    target_id: str
    type: RelationType
    description: Optional[str] = None
    properties: Dict[str, Any] = Field(default_factory=dict)
    weight: float = 1.0
