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

### Verse 1 (Atharva Ved 0.361)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.362)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.363)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.364)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.365)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.366)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.367)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.368)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.369)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.370)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.371)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.372)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.373)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.374)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.375)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.376)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.377)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.378)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.379)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.380)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

