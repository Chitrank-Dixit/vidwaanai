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

### Verse 1 (Markende Puran 0.2001)
- **Original**: निशाप्रय॒तदुत्प्तिं विस्तरादू गदतों मम
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2002)
- **Original**: प्रश्नमचरित्रजपे विनियोगः। महाप्राआनुभावेन खथा. मन्वन्तराधिष:। प्रथम चरित्रके ब्रह्म त्र्रष, महाकालों देवता,
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2003)
- **Original**: स बभूब महाभागः सावर्णिस्तनयों रखे:
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2004)
- **Original**: गावत्री छन्द, नन्‍्दा शक्ति, रक्तदनतिका बीज,
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2005)
- **Original**: स्वारोच्ियेउन्तरः पूर्व चैत्रवेशसमुद्धव:
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2006)
- **Original**: आग तत्त्व और ऋग्वेद स्त्ररूप हैं। ओमहाकाली
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2007)
- **Original**: सुरक्षों नाम राजाभूत्समस्ते क्षितिमण्डले
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2008)
- **Original**: देखताको प्रप्नप्नताके लिये प्रथम चरित्रके जपमें
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2009)
- **Original**: तस्य पालयत: पसम्यक्‌ प्रजा: पुत्रानिवौरसानू। सिनियोग किया जाता हैं। बभूबु: शत्रवों भूपा: कोलाविध्य॑सिनस्तदा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2010)
- **Original**: ततस्य त्तेरभवद्युद्धमतिप्रबलदणिडिन: खड़गं चक्रगदेषुत्नापपरिघाउ्यूल॑ भुशुण्डी शिर:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2011)
- **Original**: न्यूनेरिपि स तैर्युद्धे कोलाबिथ्य॑स्िभिर्जित:
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2012)
- **Original**: शह्वं संदधत्तों करेस्त्रिनयनां सर्वाड्रभूष्वृताम्‌(!
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2013)
- **Original**: ततः स्वपुरमायातो निजरदेशाधिफ्रोडभवत्‌। तीलाश्मष्युतिमास्यपाददशकां सेवे महाकालिकां
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2014)
- **Original**: आक्रान्त: स महाभागस्तैस्तदा प्रजलारिभि:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2015)
- **Original**: 7 # याभस्तौल्सपिते हरी कमलजों हन्तु प्रधुं कैटभम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2016)
- **Original**: मार्कण्डेयजी खोलें--
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2017)
- **Original**: सूर्यके पुत्र साबर्गि भगवान्‌ श्षिष्णुके सो जानेपर मधु और
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2018)
- **Original**: जो आठसें मु कहे जाते हैं, ठनकों उत्पत्तिकी कैटभको पारनेके लिये ऋमल्लजन्सा ब्रह्माजीने
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2019)
- **Original**: कथा तिस्ताएपूर्वक कहता हूँ, सुनो
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2020)
- **Original**: सुर्यकुमार जितका स्तवन किया था, उन महाकाली देवीका
- **Translation**: 

---

