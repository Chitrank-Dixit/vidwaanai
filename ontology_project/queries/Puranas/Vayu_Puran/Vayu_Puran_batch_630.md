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

### Verse 1 (Vayu Puran 0.12581)
- **Original**: इस गयास्यान के सम्बन्ध में मैं जितना जानता था, जितना सुना था, वह सब आप को बतला चुका !56-67। खूत बोले--इस प्रकार सनत्कुमार मुनिपुज्भव नारद जी को भक्तिपूर्वक इस पुण्थकथा को सुना चुकते के उपरान्त उस सज्भीत गुर (नारद जी) से बिदा लेकर पुण्य वन्य प्रान्त में अवस्थित अपने आश्रम को चले गये ।65
- **Translation**: 

---

### Verse 2 (Vayu Puran 0.12582)
- **Original**: वायुकथित महापुराण के उपसंहार नामक चतुर्थंचरण में गयामाहात्म्म नामक एक सो बारहवाँ अध्याय समाप्त
- **Translation**: 

---

### Verse 3 (Vayu Puran 0.12583)
- **Original**: । श्रीगुरुचरणाभ्यां नमः शिवमस्तु > एतदधंस्थाने5्यं पाठः ख. प्स्तके--पठेद्वा पाठयेद्वाउपि पूजयेद्वाउपि पुस्तकम् । इति
- **Translation**: 

---

