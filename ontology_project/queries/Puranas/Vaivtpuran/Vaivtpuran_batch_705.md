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

### Verse 1 (Vaivtpuran 543.12414)
- **Original**: वन्दनीय, परात्पर एवं गुणातीत भगवान्‌ श्रीकृष्ण सकता है? परशुरामजीने भगवान्‌ शंकरसे तुम्हारे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12415)
- **Original**: स्वयं तुम्हारे अधीन होंगे। पतिक्रते ! ब्रह्मा, शेषनाग मन्त्रको प्राप्त कर पुष्करतीर्थमें उसे सिद्ध किया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12416)
- **Original**: तथा शिव भी जिनकी आराधना करते हैं, जो और उसीके प्रभावसे वे कार्तवीर्य अर्जुनका संहार
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12417)
- **Original**: ध्यानसे भी वशमें होनेवाले नहीं हैं तथा जिन्हें कर सके; फिर तुम मानुषी कैसे हो? उन्होंने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12418)
- **Original**: आराधनाद्वारा रिझ्ा लेना समस्त योगियोंके लिये अभिमानपूर्वक महात्मा गणेशका एक दाँत तोड़
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12419)
- **Original**: भी अत्यन्त कठिन है; वे ही भगवान्‌ तुम्हारे दिया। वे केवल तुमसे ही भय मानते थे; फिर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12420)
- **Original**: अधीन रहेंगे। राधे! स्त्रीजातिमें तुम विशेष तुम मानवी स्त्री कैसे हो? जब मैं क्रोधसे उन्हें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12421)
- **Original**: सौभाग्यशालिनी हो। तुमसे बढ़कर दूसरी कोई
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12422)
- **Original**: के श्रीकृष्णजन्मखण्ड न 7 [[][[[[[[000]0//4040]
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12423)
- **Original**: 0 03344 030
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12424)
- **Original**: 40484044 4 49345495535_>>अअ्जच्ंडअ: स्त्री नहीं है। तुम दीर्घकालतक यहाँ रहनेके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12425)
- **Original**: अझलसे अपना मुख ढँक लिया। उनकी बारंबार पश्चात्‌ श्रीकृष्णे साथ ही गोलोकमें चली जाओगी।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12426)
- **Original**: ऐसी अवस्था हुई। श्रीराधाकों देखकर श्यामसुन्दरके मुने! ऐसा कहकर पार्वतीदेवी तत्काल वहीं
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12427)
- **Original**: मुख और नेत्र प्रसन्नतासे खिल उठे। समस्त अन्तर्हित हो गयीं। फिर गोपकुमारियोंके साथ
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12428)
- **Original**: गोपिकाओंके सामने खड़े हुए वे भगवान्‌ श्रीराधिका भी घर जानेको उद्यत हुईं। इतनेमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12429)
- **Original**: श्रीराधासे बोले। हो श्रीकृष्ण राधिकाके सामने उपस्थित हो गये। श्रीकृष्णने कहा--प्राणाधिके राधिके ! तुम राधाने किशोर-अवस्थाबाले श्यामसुन्दर श्रीकृष्णको
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12430)
- **Original**: मनोवाज्छित वर माँगो। हे गोपकिशोरियों! तुम देखा। उनके श्रीअद्जॉपर पीताम्बर शोभा पा रहा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12431)
- **Original**: सब लोग भी अपनी इच्छाके अनुसार बर माँगो। था। वे नाना प्रकारके आभूषणोंसे विभूषित थे। श्रीकृष्णकी यह बात सुनकर श्रीराधिका तथा घुटनोंतक लटकती हुई मालती-माला एवं वनमाला
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12432)
- **Original**: अन्य सब गोपकन्याओंने बड़े हर्षक साथ उन उनकी शोभा बढ़ा रही थी। उनका प्रसन्न मुख
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12433)
- **Original**: भक्तवाज्छाकल्पतरु प्रभुसे वर माँगा। मन्द हास्यसे शोभायमान था। बे भक्तजनोंपर राधिका बोलीं--प्रभो! मेरा चित्तरूपी अनुग्रह करनेके लिये कातर जान पड़ते थे। उनके
- **Translation**: 

---

