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

### Verse 1 (Atharva Ved 0.681)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.682)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.683)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.684)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.685)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.686)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.687)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.688)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.689)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.690)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.691)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.692)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.693)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.694)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.695)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.696)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.697)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.698)
- **Original**: Atherved: Part-1-
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.699)
- **Original**: www.awgp.org
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.700)
- **Original**: www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

