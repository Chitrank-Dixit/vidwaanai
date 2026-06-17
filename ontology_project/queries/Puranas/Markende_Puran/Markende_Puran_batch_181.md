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

### Verse 1 (Markende Puran 0.3601)
- **Original**: यग्रार्श्यते त्वया भूप त्वग्रा ध क़ुलनन्दन। प्रचस्तत्माप्यतां लव परितुष्ठा दच्वामि तत््‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3602)
- **Original**: देवी बोलीं--
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3603)
- **Original**: त़था अपने कुलकों आनन्दित करनेवाले बैश्य! तुमलोग जिम्त चस्तुको अभ्रलाषा रखते हो, बह सुन्नसे भांगों। मैं स-पुष्ट हूँ, अत: तुप्हें बह रूब कुछ दूंगी
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3604)
- **Original**: म़र्रुण्डेय उकाज 429 5 ततो बढ़े नृफों राज्यमत्िभ्रेएवन्थजन्मनि। अन्नैब अ निज राज्यं हतशत्रुअलं बलात्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3605)
- **Original**: सो5पि चैश्बस्तत्तों ज्ञान बच्ने निर्चिएणपानसः
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3606)
- **Original**: मम्रेत्यहमिति प्राज़ः सक्लव्रिच्युतिकारकम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3607)
- **Original**: मार्कण्डेयजी ऋढते हैं --
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3608)
- **Original**: तत्र राजाने दूसरे जम्ममें तट गे होगेबाला राज्य माँग तथा इस
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3609)
- **Original**: जन्मपें भो अत्रुओंकों सेनाकों बलपूर्वक नष्ट करके पुतः आपदा राज्य प्राप रूर लेनेचर जरद्धर पाँक
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3610)
- **Original**: वैश्यका लित्त संसारको ओरसे स्विक्त
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3611)
- **Original**: चान्मनुतीय।......
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3612)
- **Original**: एवं विसक्त हो चुका था और वे बड़े बुद्धिमान थे; अज्: उस समय उन्होंद्रे तो ममता और अहंत्तारूप आसक्तिका वाश करनेबाला ज्ञान माँगा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3613)
- **Original**: वैब्युबाप
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3614)
- **Original**: 19 / स्लल्पैरहोभिन॑पत्ै स्व॑ शब्ध॑ प्राप्ल्यते भवान्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3615)
- **Original**: इत्वा रिपूनस्खलित॑ 'तथ ततन्न भविष्यति
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3616)
- **Original**: मृतञ्ष भूष: साप्राप्य जन्म देबाद्वित्रस्तत:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3617)
- **Original**: स्रावर्णिको नाम मनुर्भवान्‌ भुवि भविष्यति
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3618)
- **Original**: चैश्यवर्य त्वयां यश्व बरोउस्मत्तोडभिवाजिछत: ह ए4
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3619)
- **Original**: त॑ प्रयच्छामि संखिद्धय तब ज़ान॑ भविष्यति।
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3620)
- **Original**: देवी बोलीं --
- **Translation**: 

---

