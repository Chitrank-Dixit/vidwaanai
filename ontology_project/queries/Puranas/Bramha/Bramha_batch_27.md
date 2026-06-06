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

### Verse 1 (Bramha 0.521)
- **Original**: कक्षेयुके सभानर, चाक्षुष तथा परमन्यु-ये तीन नलदा, सुरसा, गोचपला तथा स्त्रीस्‍लकूटा-ये
- **Translation**: 

---

### Verse 2 (Bramha 0.522)
- **Original**: महारथी पुत्र हुए। सभानरके पुत्र कालानल तथा दस कन्याएँ हुईं। अत्रिकुलमें उत्पन्न महर्षि प्रभाकर
- **Translation**: 

---

### Verse 3 (Bramha 0.523)
- **Original**: कालानलके धर्मज्ञ सृज्ञय हुए। सृजञ्ञयके पुत्र वीर ठन सबके पति हुए। उन्होंने भद्राके गर्भसे परम
- **Translation**: 

---

### Verse 4 (Bramha 0.524)
- **Original**: राजा पुरक्षय थे। पुरक्षयके पुत्र॒का नाम जनमेजय यशस्वी सोमको पुत्ररूपमें उत्पन्न किया। राहुसे
- **Translation**: 

---

### Verse 5 (Bramha 0.525)
- **Original**: जनमेजयके पुत्र महाशाल थे, जो देवताओंमें आहत होकर जब सूर्य आकाशसे पृथ्वोपर गिरने
- **Translation**: 

---

### Verse 6 (Bramha 0.526)
- **Original**: भी बिख्यात हुए और इस पृथ्बीपर भी उनका
- **Translation**: 

---

### Verse 7 (Bramha 0.527)
- **Original**: *ययाति-पुत्रॉंके बंशका वर्णन + 27 यश फैला था। महाशालके पुत्र महामनाके नामसे ! लोकोंकी देखभाल करोगे। सर्वश्र श्रेष्ठ मानें जाओगे विख्यात थे। देवताओंने भी उनका सत्कार किया
- **Translation**: 

---

### Verse 8 (Bramha 0.528)
- **Original**: और चारों बर्णोंको मर्यादाके भीतर स्थापित था। उन्होंने धर्मज्ञ उशोनर तथा महाबली तितिक्षु--
- **Translation**: 

---

### Verse 9 (Bramha 0.529)
- **Original**: करोगे।' ये दो पुत्र उत्पन किये। उशीनरकी पाँच पत्नियाँ
- **Translation**: 

---

### Verse 10 (Bramha 0.530)
- **Original**: . भगवान्‌ ब्रह्माजीके यों कहनेपर बलिको बड़ी थीं, जो राजर्पियोंके कुलमें उत्पन्न हुई थीं। उनके (शान्ति मिली। वे दीर्घ कालके बाद मरकर नाम इस प्रकार हैं--नृगा, कृमि, नवा, दर्वा तथा
- **Translation**: 

---

### Verse 11 (Bramha 0.531)
- **Original**: स्वर्गको गये। उनके पाँच पुत्रोंक अधिकारमें जो दृषटती। उनसे उशीनरके पाँच पुत्र हुए--नृगाके
- **Translation**: 

---

### Verse 12 (Bramha 0.532)
- **Original**: जनपद थे, उनके नाम इस प्रकार हैं-अज्ज, यक्, पुत्र नृग थे, कृमिके गर्भसे कृमिका ही जन्म हुआ
- **Translation**: 

---

### Verse 13 (Bramha 0.533)
- **Original**: सुह्य, कलिम्भ और पुण्ड़क। अब अज्गकी संतानका था। नवाके नब तथा दर्वाके सुब्रत हुए। दृषद्वतीके
- **Translation**: 

---

### Verse 14 (Bramha 0.534)
- **Original**: वर्णन करता हूँ। अज्जञके पुत्र महाराज दधिवाहन गर्भसे ठशीनरक्ुमार शिबिकी उत्पत्ति हुई। शिक्षिको
- **Translation**: 

---

### Verse 15 (Bramha 0.535)
- **Original**: हुए। दधिवाहनके पुत्र राजा दिविरथ। दिविरथके शिबिदेशका राज्य मिला। नृगके अधिकारमें यौधेय
- **Translation**: 

---

### Verse 16 (Bramha 0.536)
- **Original**: इद्धतुल्य पराक्रमी और विद्वान्‌ धर्मरथ तथा धर्मरथके प्रदेश आया। नवको नवराष्ट्र तथा कृमिको
- **Translation**: 

---

### Verse 17 (Bramha 0.537)
- **Original**: पुत्र चित्ररथ हुए। राजा धर्मरथ जब कालझर कृमिलापुरीका राज्य प्राप्त हुआ। सुव्रतके अधिकारमें
- **Translation**: 

---

### Verse 18 (Bramha 0.538)
- **Original**: पर्वतपर यज्ञ करते थे, उस समय महात्मा इन्द्रने अम्बष्ट देश आया। शिबिके विश्वविख्यात चार पुत्र
- **Translation**: 

---

### Verse 19 (Bramha 0.539)
- **Original**: उनके साथ बैठकर सोमपान किया था। चित्ररथके हुए बृषदर्भ, सुबवीर, केकय तथा मद्रक। उनके पुत्र दशरथ हुए, जो लोमपादके नामसे विख्यात समृद्धिशाली जनपद उन्हींके नामसे प्रसिद्ध हुए।
- **Translation**: 

---

### Verse 20 (Bramha 0.540)
- **Original**: थे। उन्हींकी पुत्री शान्ता थी। दशरथके पुत्र अब महामनाके दूसरे पुत्र तितिक्षुकी संतानोंका
- **Translation**: 

---

