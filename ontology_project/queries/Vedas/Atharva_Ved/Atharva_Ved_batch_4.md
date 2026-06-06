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

### Verse 1 (Atharva Ved 0.61)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.62)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.63)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.64)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.65)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.66)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.67)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.68)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.69)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.70)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.71)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.72)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.73)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.74)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.75)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.76)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.77)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.78)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.79)
- **Original**: Atherveda : Part-1www.awgp.org
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.80)
- **Original**: www. .orgakhandjyoti Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

