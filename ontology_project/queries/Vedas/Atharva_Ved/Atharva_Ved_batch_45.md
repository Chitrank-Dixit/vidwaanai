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

### Verse 1 (Atharva Ved 0.881)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.882)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.883)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.884)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.885)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.886)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.887)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.888)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.889)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.890)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.891)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.892)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.893)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.894)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.895)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.896)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.897)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.898)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.899)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.900)
- **Original**: www.awgp.org
- **Translation**: 

---

