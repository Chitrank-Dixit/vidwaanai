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

### Verse 1 (Atharva Ved 0.1221)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.1222)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.1223)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.1224)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.1225)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.1226)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.1227)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.1228)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.1229)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.1230)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.1231)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.1232)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.1233)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.1234)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.1235)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.1236)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.1237)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.1238)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.1239)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.1240)
- **Original**: Atherveda: Part-2www.awgp.org Disclaimer / Warning:All literary and artistic material on this website is copyright protected and constitutes an exclusive intellectual property of the owner of the website. Any attempt to infringe upon the owners copyrights or any other form of intellectual property rights over the work would be legally dealt with. Though any of the information (text, image, animation, audio andvideo) present on the website can be used for propagation with prior written consent.
- **Translation**: 

---

