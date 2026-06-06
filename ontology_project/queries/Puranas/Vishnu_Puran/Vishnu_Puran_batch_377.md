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

### Verse 1 (Vishnu Puran 0.7521)
- **Original**: पम्राहिष्मत्यां दिग्विजयाभ्यागतो नर्मदाजलावगाहन- क्रीडातिपानमदाकुलेनायत्रेनेब तेनाहेषदेवरैत्य गश्धवेशजयोद्धूतमदावलेपो5पि रावण: पशुरिव बद्ध्वा. स्वनगरैकान्ते. स्थापित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7522)
- **Original**: यश्च॒ पश्चाशीतिवर्षसहल्नोपलक्षणकालावसाने भगवन्नारायणांशेन परशुरामेणोपसंहतः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7523)
- **Original**: तस्य च पुत्रशतप्रधाना: पञ्ञ पुत्रा बभूवुः शूरशूरसेनवृषसेनमधुजयध्वजसंज्ञा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7524)
- **Original**: जयध्वजात्तालजडू: . पुत्रो$भवत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7525)
- **Original**: तालजड्डस्य
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7526)
- **Original**: एपां ज्येप्लो बीतिहोत्रस्तथान्यों भरतः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7527)
- **Original**: भरतादबृष:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7528)
- **Original**: वृषस्य पुत्रों मधुरभवत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7529)
- **Original**: _ तस्थापि वृष्णिप्रमुखं पुत्रशतमासीत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7530)
- **Original**: यतो बृष्णिसंज्ञामेत- ड्रोत्रमवाप
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7531)
- **Original**: मधुसंज्ञाह्देतुअ मधुरभवत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7532)
- **Original**: बादवाश्ष बदुनामोपलक्षणादिति
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7533)
- **Original**: तालजड्डाख्य॑ पुत्रशतमासीत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7534)
- **Original**: और कुतवीर्य, कृताभि, कृताथर्म और कतौजा नामक चार पुत्र हुए
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7535)
- **Original**: कृतवीर्यके सहस्त॒भुजाओँवाले सप्रद्वीपाधिपति अर्जुनका जन्म हुआ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7536)
- **Original**: सहल्ार्जुनने अत्रिकुल्में उत्पन्न भगवर्देशरूप श्रोदतात्रेयजोकी उपासना कर 'सहरन भुजाएँ, अधर्मायरणक् निवारण, स्वधर्मका सेवन, युद्धके द्वारा सम्पूर्ण पृथिवोमण्डलकका विजय, अर्मानुसार अ्रजा-पालन, झत्रुओंसे अपराजय तथा त्रिस्मेकप्रसिद्ध पुरुषसे मृत्य
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7537)
- **Original**: --ऐसे कई वर माँगे और प्राप्त किये थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7538)
- **Original**: अर्जुनने इस सम्पूर्ण सप्तद्वीपलती पृथियीक्ा पालन तथा दस हजार यज्ञॉका अनुष्तान किया था
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7539)
- **Original**: उसके विषय्में यह इलोक आजतक कहा जाता है---
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7540)
- **Original**: यज्ञ, दान, तप, त्रिनय और विद्यामें कार्तजीर्य-- सहलार्जुनकी समता खोई भी राजा गहीं कर सकता
- **Translation**: 

---

