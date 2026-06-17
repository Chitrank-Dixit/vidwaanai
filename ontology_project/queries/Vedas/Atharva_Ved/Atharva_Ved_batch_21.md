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

### Verse 1 (Atharva Ved 0.401)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 2 (Atharva Ved 0.402)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 3 (Atharva Ved 0.403)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 4 (Atharva Ved 0.404)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 5 (Atharva Ved 0.405)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 6 (Atharva Ved 0.406)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 7 (Atharva Ved 0.407)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 8 (Atharva Ved 0.408)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 9 (Atharva Ved 0.409)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 10 (Atharva Ved 0.410)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 11 (Atharva Ved 0.411)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 12 (Atharva Ved 0.412)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 13 (Atharva Ved 0.413)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 14 (Atharva Ved 0.414)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 15 (Atharva Ved 0.415)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 16 (Atharva Ved 0.416)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 17 (Atharva Ved 0.417)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 18 (Atharva Ved 0.418)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 19 (Atharva Ved 0.419)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

### Verse 20 (Atharva Ved 0.420)
- **Original**: Atherveda: Part-1www.awgp.org / www.akhandjyoti.org Disclaimer / Warning:All literary and artistic material on this websiteis copyright protected and constitutes an exclusive intellectual property of the ownerof the website.Any attempt to infringe upon the ownerscopyrights or any other form of intellectual property rights over the work wouldbe legallydealt with. Though any of the information(text, image, animation, audio and video)present on the websitecan be used for propagationwith prior writtenconsent.
- **Translation**: 

---

