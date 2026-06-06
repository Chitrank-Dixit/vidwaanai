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

### Verse 1 (Bramha 0.5501)
- **Original**: प्राप्त करता है। नाना प्रकारके यज्ञोंसे मनुष्य जो सोकर उठनेके बाद श्रीकृष्णका स्मरण करते हैं,
- **Translation**: 

---

### Verse 2 (Bramha 0.5502)
- **Original**: फल प्राप्त करता है, वह जितेन्द्रिय पुरुषको वहाँ वे शरीर त्यागनेके बाद श्रोकृष्णमें ही प्रवेश करते
- **Translation**: 

---

### Verse 3 (Bramha 0.5503)
- **Original**: प्रतिदिग मिला करता है। जो पुरुषोत्तमक्षेत्रमें हैं-ठीक बैसे हो जैसे मन्त्रोच्चारणपूर्वक होम
- **Translation**: 

---

### Verse 4 (Bramha 0.5504)
- **Original**: कल्पवृक्ष (अक्षयबट)-के पास जाकर शरीरत्याग किया हुआ हविष्य अग्निमें लीन हो जाता है।*
- **Translation**: 

---

### Verse 5 (Bramha 0.5505)
- **Original**: करते हैं, वे निःसंदेह मुक्त हो जाते हैं। जो मानव अत: मुनिवरो
- **Translation**: 

---

### Verse 6 (Bramha 0.5506)
- **Original**: मोक्षकी इच्छा रखनेवाले पुरुषोंको
- **Translation**: 

---

### Verse 7 (Bramha 0.5507)
- **Original**: बिना इच्छाके भी वहाँ प्राणत्याग करता है, वह पुरुषोत्तमक्षेत्रमें सदा यत्रपूर्वक कमलनयन श्रीकृष्णका
- **Translation**: 

---

### Verse 8 (Bramha 0.5508)
- **Original**: भी दुःखसे मुक्त हो दुर्लभ मोक्ष प्राप्त कर लेता है। दर्शन करना चाहिये। जो मनीषी पुरुष शबन और
- **Translation**: 

---

### Verse 9 (Bramha 0.5509)
- **Original**: कृमि, कोट, पतड्र आदि तथा पशु-पक्षियोंकी जागरणकालमें श्रीकृष्ण, बलभद्र तथा सुभद्राका
- **Translation**: 

---

### Verse 10 (Bramha 0.5510)
- **Original**: योनिमें पड़े हुए जीव भी बहाँ देहत्याग करनेपर दर्शन करते हैं, वे श्रीहरिके धाममें जाते हैं। जो
- **Translation**: 

---

### Verse 11 (Bramha 0.5511)
- **Original**: परमगतिको प्राप्त करते हैं। जो मनुष्य एक बार भी हर समय भक्तिपूर्वक पुरुषोत्तम श्रीकृष्ण, रेहिणीनन्दन , श्रद्धापूर्वक भगवान्‌ पुरुषोत्तमका दर्शन कर लेता बलभद्र और सुभद्रादेवोका दर्शन करते हैं, वे है, वह सहस्रों पुरुषोंमें उत्तम है। भगवान्‌ भगवान्‌ विष्णुके लोकमें जाते हैं। जो बर्षकि चार
- **Translation**: 

---

### Verse 12 (Bramha 0.5512)
- **Original**: प्रकृतिसे परे और पुरुषसे भी उत्तम हैं। इसलिये महीनोंमें पुरुषोत्तमक्षेत्रक भीतर निवास करते हैं,
- **Translation**: 

---

### Verse 13 (Bramha 0.5513)
- **Original**: वे वेद, पुराण तथा इस लोकमें पुरुषोत्तम कहलाते उन्हें सारी पृथ्वीको तीर्थयात्रोसे भी अधिक फल
- **Translation**: 

---

### Verse 14 (Bramha 0.5514)
- **Original**: हैं। जो पुराण और वेदान्तमें परमात्मा कहे गये हैं, प्राप्त होता है। जो इन्द्रियॉंको जीतकर और क्रोधको
- **Translation**: 

---

### Verse 15 (Bramha 0.5515)
- **Original**: वे ही सम्पूर्ण जगत्‌का उपकार करनेके लिये उस वशीभूत करके सदा पुरुषोत्तमक्षेत्रमें ही निवास
- **Translation**: 

---

### Verse 16 (Bramha 0.5516)
- **Original**: क्षेत्रमें पुरुषोतमरूपसे विराजमान हैं।
- **Translation**: 

---

### Verse 17 (Bramha 0.5517)
- **Original**: पुरुषोत्तमक्षेत्रके करते हैं, वे तपस्याका फल पाते हैं। मनुष्य अन्य
- **Translation**: 

---

### Verse 18 (Bramha 0.5518)
- **Original**: भीतर मार्गमें, श्मशानभूमिमें, घरके मण्डपमें, तीर्थामें दस हजारं वर्षोत्क तपस्या करके जो फल
- **Translation**: 

---

### Verse 19 (Bramha 0.5519)
- **Original**: सड़कों और गलियोंमें--जहाँ कहीं इच्छा या * कृष्णे रताः कृष्णमनुस्मरन्ति रात्री च कृष्णं पुनरुत्यिता ये। ते भिन्नदेहा: प्रविशन्ति कृष्णं हविर्यथा मन्त्रहुत॑ हुताशमु
- **Translation**: 

---

### Verse 20 (Bramha 0.5520)
- **Original**: (177। 5) तै प्रकृत: स परो यस्मात्‌ पुरुषादपि चोत्तम:। तस्माद्‌ केदे पुराणे च लोके5स्मिन्‌ पुरुषोत्तम:
- **Translation**: 

---

