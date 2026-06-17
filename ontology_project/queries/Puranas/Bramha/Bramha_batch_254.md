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

### Verse 1 (Bramha 0.5061)
- **Original**: सब पापोंका नाश करनेवाला है। मैंने बड़े-बड़े हुआ हूँ और इसीलिये यह पर्वत सूना दिखायी
- **Translation**: 

---

### Verse 2 (Bramha 0.5062)
- **Original**: मुनियोंसे सुना है कि वह सब अभीष्ट वस्तुओंको देता है। राजन्‌! और भी धर्मयुकू वचन सुनो,
- **Translation**: 

---

### Verse 3 (Bramha 0.5063)
- **Original**: देनेवाला है। गौतमी गज्भा तथा भगवान्‌ विष्णुके जिसके पालन किये बिना ब्रह्महत्याके समात्र।
- **Translation**: 

---

### Verse 4 (Bramha 0.5064)
- **Original**: सिवा दूसरा कोई क्लेशोंका नाश करनेवाला पाप लगता है। क्षत्रिय युद्धमें जाकर अथकः
- **Translation**: 

---

### Verse 5 (Bramha 0.5065)
- **Original**: नहीं है। मैं चाहता हूँ “सर्वतोभावेन! उस युद्धसे अन्यत्र भी यदि भागनेवाले, हथियार रख
- **Translation**: 

---

### Verse 6 (Bramha 0.5066)
- **Original**: तीर्थका दर्शन करूँ। किंतु मेरे प्रय्नले यह कभी देनेवाले, अपना विश्वास करनेवाले, युद्धमें पीठ
- **Translation**: 

---

### Verse 7 (Bramha 0.5067)
- **Original**: सम्भव नहीं है। भला, पापियोंको मनोवाड्छित दिखानेवाले, अपरिचित, बैठे हुए तथा *मैं डरता
- **Translation**: 

---

### Verse 8 (Bramha 0.5068)
- **Original**: बस्तुकी प्राप्ति कैसे हो सकती है। वीर! मैं यत्र हूँ' यों कहनेवाले मनुष्यको मार डालता है तो
- **Translation**: 

---

### Verse 9 (Bramha 0.5069)
- **Original**: करनेपर भी उस तीर्थका दर्शन नहीं कर पाता। उसे ब्रह्महत्यारा कहते हैं। जो सामने प्रिय
- **Translation**: 

---

### Verse 10 (Bramha 0.5070)
- **Original**: यह कार्य मेरे लिये अत्यन्त दुष्कर है। तुम्हारी योलता, पसोक्षमें कटुबचन कहता, मनमें दूसरी
- **Translation**: 

---

### Verse 11 (Bramha 0.5071)
- **Original**: कृपा हो तो मैं भगवान्‌ गदाधरका दर्शन कर बात सोचता, वाणीसे दूसरी बात कहता और
- **Translation**: 

---

### Verse 12 (Bramha 0.5072)
- **Original**: सकता हूँ। भगवान्‌ करुणाके सागर हैं। वे बिना क्रियारूपमें सदा दूसरा ही कार्य करता है, जो
- **Translation**: 

---

### Verse 13 (Bramha 0.5073)
- **Original**: बताये ही सबके दुःखोंकों जानते हैं। उनका गुरुजनोंकी शपथ खाता, द्वेष रखता, ब्राह्मणोंकी
- **Translation**: 

---

### Verse 14 (Bramha 0.5074)
- **Original**: दर्शन कर लेनेपर पुत्र: भनुष्योंको सांसारिक * प्रत्यक्षे च प्रिय॑ वक्ति पशेक्षे पत्याणि थ। अन्यद्धूदि वचस्यन्यत्करोत्यन्यत्सदैव यः
- **Translation**: 

---

### Verse 15 (Bramha 0.5075)
- **Original**: गुरूणां शपर्थ कर्ता द्वेश ब्राह्मणनिन्दक:। मिध्याविनीतः परापात्मा स तु स्पादब्रह्मघातक:
- **Translation**: 

---

### Verse 16 (Bramha 0.5076)
- **Original**: देव॑ वेदमथाध्यात्म॑ धर्मब्राह्मणसद्गतिम्‌
- **Translation**: 

---

### Verse 17 (Bramha 0.5077)
- **Original**: एताप्रिन्दति यो द्वेषात्स तु स्यादूब्रह्मघातक:
- **Translation**: 

---

### Verse 18 (Bramha 0.5078)
- **Original**: 33--35)
- **Translation**: 

---

### Verse 19 (Bramha 0.5079)
- **Original**: + भद्वतीर्थ, पतत्रितीर्ध और विप्रतीर्थकी महिमा * 247 क्लेशका अनुभव नहीं करना पड़ता। राजन्‌ ! मैं । निकली हो। संसारके प्राणियोंकी तुम्हारे सिवा तुम्हारे प्रसादसे भगवानका दर्शन करते ही
- **Translation**: 

---

### Verse 20 (Bramha 0.5080)
- **Original**: कहाँ कोई भी गति नहीं है।' स्वर्गलोकको चला जाऊँगा।' पक्षीका अन्तःकरण श्रद्धासे शुद्ध हो गया पक्षीके यों कहनेपर राजा पवमानने उसे
- **Translation**: 

---

