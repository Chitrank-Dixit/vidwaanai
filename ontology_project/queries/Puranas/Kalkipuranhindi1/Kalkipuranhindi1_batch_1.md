# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Kalkipuranhindi1 0.1)
- **Original**: कल्कक पुराण के बारे में ध्यान देने योग्य बातें ये भूतकाल वाचक वाक्य में ललखा गया है (Past Sentence) जैसे हम कहेंगे :- “भगवान कललक का अवतार सम्बल ग्राम में होगा “ परन्तु कल लक पुराण में ललखा गया है:- “भगवान कललक का अवतार सम्बल ग्राम में हुआ“
- **Translation**: 

---

