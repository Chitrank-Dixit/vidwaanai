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

### Verse 1 (Vishnu Puran 0.6761)
- **Original**: उसके प्रभावसे उसका गर्भ सात वर्षतक गर्भाशय ही में रहा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6762)
- **Original**: अन्तमें, बहु चुद्धावस्थाके कारण ओऔर्य मुनिके आंश्रमके समीप मर गया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6763)
- **Original**: तब उसकी पटरानीने चिता बनाकर
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6764)
- **Original**: श्डड॑ जज छः इखआख्रीधिध्युपराण अर [आर तमारोप्यानुमरणकृतनिश्चयाउभूत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6765)
- **Original**: अध्ैैतामतीतानागतवर्त्तमानकालत्रयवेदी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6766)
- **Original**: । अल्मलपनेनासद्वाहेणाखिलभूमण्डलपति- रतिवीर्यपराक्रमो नैकयज्ञकृदरातिपक्षक्षयकर्त्ा तवोदरे चक्रवर्ती तिष्ठति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6767)
- **Original**: नैवमति- साहसाध्यवसायिनी भवती भवत्वित्युक्ता सा तस्मादनुमरणनिर्बन्धाद्विराम
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6768)
- **Original**: तेनैत् च् भ्रगवता स्वाश्रममानीता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6769)
- **Original**: तत्र कतिपयदिनाभ्यन्तरे च सहैव तेन गरेणाति- तेजस्वी बालको जज्ञे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6770)
- **Original**: तस्वौवों जातकर्मादि- क्रिया निष्पाद्य सगर ड़ति नाम चकार
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6771)
- **Original**: कृतोपनयन॑ चैनमोर्बों बेदशास्त्राण्यस्त्र॑ चाभेय॑ भार्गवाख्यमध्यापयामास
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6772)
- **Original**: उत्पन्नबुद्धि,भ्ष मातरमत्रवीत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6773)
- **Original**: अम्ब कथमत्र ययं क्र वा तातोउस्माकमित्येवः मादिपृच्छन्तं माता सर्वमेवावोचत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6774)
- **Original**: ततशञ्ष पित्राज्यापहरणादमर्धितो.. हैहयतालजब्लादि- वधायप्रतिज्ञामकरोत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6775)
- **Original**: प्रायशञ्र हैहयतालजज्ञाझ्घान
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6776)
- **Original**: ._ शकयवन काम्बोजपारदपह्वत्रा: हन्यमानास्तत्कुलगुरुं वसिष्ठं शरण जम्पुः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6777)
- **Original**: अथैनान्वसिष्ठो जीवन्यूतकान्‌ू_ कृत्वा सगरमाह
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6778)
- **Original**: वत्साल्मेभिजीवन्पृतकैरनुस॒तै:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6779)
- **Original**: एते च मयैव त्वत्मतिज्ञापरिपालनाय निजधर्मद्विजसड़ परित्यागं कारिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6780)
- **Original**: तथेति तदगुरुवचन- मभिनन्धतेषां वेषान्यत्वमकारयत्‌
- **Translation**: 

---

