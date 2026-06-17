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

### Verse 1 (Mahabharat 941.8381)
- **Original**: निवेदन किया। कज+ओऔ पे इन्द्र और धर्मका युथिष्ठिरको सान्त्वना देना तथा युधिष्ठिरका शरीर त्यागकर दिव्य लोकको जाना वैज्ञग्पायनजी कहते हैं--जनमेजय ! धर्मराज युधिष्ठिस्को
- **Translation**: 

---

### Verse 2 (Mahabharat 941.8381)
- **Original**: निवेदन किया। कज+ओऔ पे इन्द्र और धर्मका युथिष्ठिरको सान्त्वना देना तथा युधिष्ठिरका शरीर त्यागकर दिव्य लोकको जाना वैज्ञग्पायनजी कहते हैं--जनमेजय ! धर्मराज युधिष्ठिस्को
- **Translation**: 

---

### Verse 3 (Mahabharat 941.8382)
- **Original**: अनुभव करता है। जिसके पाप-कर्म अधिक और पुण्य थोड़े उस स्थानपर खड़े हुए एक मुहूर्त भी नहीं बीतने पाया था कि
- **Translation**: 

---

### Verse 4 (Mahabharat 941.8382)
- **Original**: अनुभव करता है। जिसके पाप-कर्म अधिक और पुण्य थोड़े उस स्थानपर खड़े हुए एक मुहूर्त भी नहीं बीतने पाया था कि
- **Translation**: 

---

### Verse 5 (Mahabharat 941.8383)
- **Original**: होते हैं, बह पहले स्वर्गका सुख भोगता है (तथा जो पुण्य इन्द्र आदि सम्पूर्ण देवता वहाँ आ पहुँचे। साक्षात्‌ धर्म भी
- **Translation**: 

---

### Verse 6 (Mahabharat 941.8383)
- **Original**: होते हैं, बह पहले स्वर्गका सुख भोगता है (तथा जो पुण्य इन्द्र आदि सम्पूर्ण देवता वहाँ आ पहुँचे। साक्षात्‌ धर्म भी
- **Translation**: 

---

### Verse 7 (Mahabharat 941.8384)
- **Original**: अधिक और पाप कम किये रहता है, बह पहले नरक झरीर धारण करके राजासे मिलनेके लिये आये। उन तेजस्वी
- **Translation**: 

---

### Verse 8 (Mahabharat 941.8384)
- **Original**: अधिक और पाप कम किये रहता है, बह पहले नरक झरीर धारण करके राजासे मिलनेके लिये आये। उन तेजस्वी
- **Translation**: 

---

### Verse 9 (Mahabharat 941.8385)
- **Original**: भोगकर पीछे स्वर्गमें आनन्द भोगता है) । इसी नियमके देबेताओंके आते ही बहाँका सारा अख्कार दूर हो गया।
- **Translation**: 

---

### Verse 10 (Mahabharat 941.8385)
- **Original**: भोगकर पीछे स्वर्गमें आनन्द भोगता है) । इसी नियमके देबेताओंके आते ही बहाँका सारा अख्कार दूर हो गया।
- **Translation**: 

---

### Verse 11 (Mahabharat 941.8386)
- **Original**: अनुसार तुम्हारी भलाई सोचकर पहले मैंने तुम्हें नरकका पापियोंकी यातनाका वह दृश्य कहीं नहीं दिखायी देता था।
- **Translation**: 

---

### Verse 12 (Mahabharat 941.8386)
- **Original**: अनुसार तुम्हारी भलाई सोचकर पहले मैंने तुम्हें नरकका पापियोंकी यातनाका वह दृश्य कहीं नहीं दिखायी देता था।
- **Translation**: 

---

### Verse 13 (Mahabharat 941.8387)
- **Original**: दर्शन कराया है। तुमने अश्वत्थामाके मरनेकी बात कहकर फिर शीतल, मन्द, सुग-थ वायु चलने लूणी। इन्द्रसहित
- **Translation**: 

---

### Verse 14 (Mahabharat 941.8387)
- **Original**: दर्शन कराया है। तुमने अश्वत्थामाके मरनेकी बात कहकर फिर शीतल, मन्द, सुग-थ वायु चलने लूणी। इन्द्रसहित
- **Translation**: 

---

### Verse 15 (Mahabharat 941.8388)
- **Original**: छलसे ड्रोणाचार्यको उनके पुत्रकी मृत्युका विश्वास दिलाया मरूदगण, बसु, अश्विनीकुमार, साध्य, रद्द, आदित्य तथा
- **Translation**: 

---

### Verse 16 (Mahabharat 941.8388)
- **Original**: छलसे ड्रोणाचार्यको उनके पुत्रकी मृत्युका विश्वास दिलाया मरूदगण, बसु, अश्विनीकुमार, साध्य, रद्द, आदित्य तथा
- **Translation**: 

---

### Verse 17 (Mahabharat 941.8389)
- **Original**: था, इसीलिये तुम्हें भी छलसे ही नरक दिखलाया गया है। अन्यान्य स्वर्गवासी देवता सिद्धों और महर्षियोंक साथ
- **Translation**: 

---

### Verse 18 (Mahabharat 941.8389)
- **Original**: था, इसीलिये तुम्हें भी छलसे ही नरक दिखलाया गया है। अन्यान्य स्वर्गवासी देवता सिद्धों और महर्षियोंक साथ
- **Translation**: 

---

### Verse 19 (Mahabharat 941.8390)
- **Original**: तुम्हारे पक्षके जितने राजा युद्धमें मारे गये हैं, वे सभी महातेजस्वी युथिष्ठिर्के पास- एकत्रित हुए। उस समय इत्ले
- **Translation**: 

---

### Verse 20 (Mahabharat 941.8390)
- **Original**: तुम्हारे पक्षके जितने राजा युद्धमें मारे गये हैं, वे सभी महातेजस्वी युथिष्ठिर्के पास- एकत्रित हुए। उस समय इत्ले
- **Translation**: 

---

