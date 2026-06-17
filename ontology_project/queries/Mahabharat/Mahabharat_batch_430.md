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

### Verse 1 (Mahabharat 0.4291)
- **Original**: दबाकर कुचल डालते थे। कितने ही योद्धाओंको उन्होंने दौंतोंकी धृष्टयुप्रको मार डालनेकी इच्छासे उसकी ओर बढ़े। पूर्व नोकसे चीर डाल्ला और कितनोंको सैड़में लपेटकर ऊपर फेंक और दक्षिण देशके रहनेवाले गजयुद्धमें कुछल जो
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4291)
- **Original**: दबाकर कुचल डालते थे। कितने ही योद्धाओंको उन्होंने दौंतोंकी धृष्टयुप्रको मार डालनेकी इच्छासे उसकी ओर बढ़े। पूर्व नोकसे चीर डाल्ला और कितनोंको सैड़में लपेटकर ऊपर फेंक और दक्षिण देशके रहनेवाले गजयुद्धमें कुछल जो
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4292)
- **Original**: दिया। दाँतोंसे कुचले हुए जो लोग जमीरपर गिरते थे, उनकी अधान-ग्रधान वीर थे, वे सभी उपस्थित थे। इनके सिला
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4292)
- **Original**: दिया। दाँतोंसे कुचले हुए जो लोग जमीरपर गिरते थे, उनकी अधान-ग्रधान वीर थे, वे सभी उपस्थित थे। इनके सिला
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4293)
- **Original**: सूरत बड़ी भयानक हो जाती थी। इसी समय अद्भराजके अड्ड, बड़; पुण्ड, मगध, मेकल, कोसल, मद्र, दझ्षार्ण,
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4293)
- **Original**: सूरत बड़ी भयानक हो जाती थी। इसी समय अद्भराजके अड्ड, बड़; पुण्ड, मगध, मेकल, कोसल, मद्र, दझ्षार्ण,
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4294)
- **Original**: हाथीका सात्यकिसे सामना हुआ । सात्यकिने भयंकर बेगवाले निषध और कलिशुदेशीय योद्धा भी, जो हस्तियुद्धमें निपण
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4294)
- **Original**: हाथीका सात्यकिसे सामना हुआ । सात्यकिने भयंकर बेगवाले निषध और कलिशुदेशीय योद्धा भी, जो हस्तियुद्धमें निपण
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4295)
- **Original**: नाराचसे हाथीके मर्मस्थानोंको बींथ डाला। हाथी बेदनासे थे, वहाँ आये । ये सब ल्तेग पाज्चाल्लॉंकी सेनापर बाण, तोमर मृर्छित होकर गिर पड़ा । अड्जराज उसकी ओटमें अपने शरीरको और नाराचोंकी वर्षा करते हुए आगे बढ़े।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4295)
- **Original**: नाराचसे हाथीके मर्मस्थानोंको बींथ डाला। हाथी बेदनासे थे, वहाँ आये । ये सब ल्तेग पाज्चाल्लॉंकी सेनापर बाण, तोमर मृर्छित होकर गिर पड़ा । अड्जराज उसकी ओटमें अपने शरीरको और नाराचोंकी वर्षा करते हुए आगे बढ़े।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4296)
- **Original**: छिपाये बैठा था, अब वह हाथीसे कूदना ही चाहता था कि र्‌ उन्हें आते देख धृष्टयु्न उनके हाथियोंपर नाराचोंकी वर्षा
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4296)
- **Original**: छिपाये बैठा था, अब वह हाथीसे कूदना ही चाहता था कि र्‌ उन्हें आते देख धृष्टयु्न उनके हाथियोंपर नाराचोंकी वर्षा
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4297)
- **Original**: सात्यकिने उसकी छातीपर भी नाराचसे प्रहार किया । चोटको न करने लगा। अत्येक हाथीको उसने दस-दस, छः-छः और
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4297)
- **Original**: सात्यकिने उसकी छातीपर भी नाराचसे प्रहार किया । चोटको न करने लगा। अत्येक हाथीको उसने दस-दस, छः-छः और
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4298)
- **Original**: सैभाल सकतेके कारण वह भी पृथ्वीपर गिर पड़ा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4298)
- **Original**: सैभाल सकतेके कारण वह भी पृथ्वीपर गिर पड़ा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4299)
- **Original**: इसके बाद आठ-आठ बाणोंसे मारकर घायल कर दिया। उस समय
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4299)
- **Original**: इसके बाद आठ-आठ बाणोंसे मारकर घायल कर दिया। उस समय
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4300)
- **Original**: नकुलने यमदण्डके समान तौन नाराच हाथमें लिये और उनके धृष्टसुक्रको हाथियोंकी सेनासे घिर-गया देख पाण्डव
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4300)
- **Original**: नकुलने यमदण्डके समान तौन नाराच हाथमें लिये और उनके धृष्टसुक्रको हाथियोंकी सेनासे घिर-गया देख पाण्डव
- **Translation**: 

---

