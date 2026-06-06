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

### Verse 1 (Vishnu Puran 0.12841)
- **Original**: 97 ख़ाण्डिक्य उवाच कथिते योगसद्धाबे सर्वमेब कृत मम । तबोपदेशेनाशेषो नष्टअ्रत्तमलो यतः
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12842)
- **Original**: 98 ममेति यन्मया चोक्तमसदेतन्न चान्यथा । नरेन्द्र गदितुं शक्यमपि विज्ञेयवेदिभि:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12843)
- **Original**: 99 अहं ममेत्यविद्येये व्यवहारस्तथानयो: । परमार्थस्व्वर्सलापो गोचरे बचा न यः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12844)
- **Original**: 100 तब्च्छ श्रेयसे सर्व ममैतद्धवता कृतम्‌। यद्विपुक्तिप्रदो योग: प्रोक्त: केशिध्वजाव्यय:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12845)
- **Original**: 101 अ्रीपशशर उवाच यथाहईँ पूजया तेन खाण्डिक्येन स पूजित: । आजमगाम पुर॑ ब्रह्म॑स्ततः केशिध्वजो नृपः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12846)
- **Original**: 102 खाण्डिक्यो5पि सुतत कृत्वा राजाने योगसिद्धये । वन जगाम गोविन्दे विनिवेशितमानसः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12847)
- **Original**: 1503 तत्रैकात्तमतिर्भूखा यमादिगुणसंयुत: । विष्णवाख्ये निर्मले ब्रह्मण्यवाप नृपतिर्लयम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12848)
- **Original**: 104 पष्ठ अंझ 453 है राजन्‌ ! जिसमें परमेश्वरके रूपकी ही प्रतीति होती है, ऐसी जो विषयान्तरकी स्पृहासे रहित एक अनवरत धारा है उसे ही ध्यान कहते हैं; यह अपनेसे पूर्व यम-नियमादि छ« अड्भोंसे निष्पन्न होता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12849)
- **Original**: उस ध्येय पदार्थका ही जो मनके द्वारा ध्यानसे सिद्ध होनेयोग्य कल्पनाहीन (ध्याता, ध्येय और ध्यानके भेदसे रहित) स्वरूप अहण किया जाता है उसे ही समाधि कहते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12850)
- **Original**: हे राजन्‌ ! [ समाधिसे होनेबाला भगवक्‍त्साक्षात्काररूप ] विज्ञान ही प्रामव्य परअह्मतक पहुँचानेबात्प् है तथा सम्पूर्ण भावनाओंसे रहित एकमात्र आत्मा ही प्रापणीय (वहाँतक ) है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12851)
- **Original**: मुक्ति-लाभमें क्षेत्रज्ञ कर्ता है है आला ज्ञान करण है; ।ज्ञानरूपों करणके द्वारा क्षेत्रज्ञके] मुक्तिरूपी कार्यको सिद्ध करके वह विज्ञान कृतकृत्य होकर निवृत्त हो जाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12852)
- **Original**: उस समय यह भगवद्भावसे भरकर परमात्मासे अभिन्न हो जाता है। इसका भेद-ज्ञान तो अज्ञानजन्य ही है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12853)
- **Original**: भेद उत्पन्न करनेवाफ़े अज्ञानके सर्वधा नष्ट हो जानेपर ब्रह्म और आत्मामें असत्‌ (अविद्यमान) भेद कौन कर सकता है?
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12854)
- **Original**: है खाण्डिक्य ! इस प्रकार तुम्हारे पूछनेके अनुसार मैंने सैक्षेप और विस्तारसे योगका वर्णन किया; अब मैं तुम्हा।ा और क्या कार्य ककूँ 7
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12855)
- **Original**: खाण्डिक्य योले--आपने इस महायोगका वर्णन कस्के सेरा सभी कार्य कर दिया, क्योकि आपके उपदेदसे गेरे चित्तका सम्पूर्ण मल नष्ट हो गया है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12856)
- **Original**: हे राजन्‌ ! मैंने जो 'मेरा' कहा यह भी असत्य ही है, अन्यथा ज्ञेय बस्तुको जाननेवाले तो यह भी नहीं कह सकते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12857)
- **Original**: “मैं' और 'मेरा' ऐसो बुद्धि और इनका व्यवहार भी अविद्या ही है, परमार्थ तो कहने-सुननेकी बात नहीं है क्योंकि वह वाणीका अखिषय है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12858)
- **Original**: हे केशिध्वज ! आपने इस मुक्तिप्रद योगका वर्णन करके मेरे कल्याणके लिये सब कुछ कर दिया, अब आप सुख्पूर्वक पधारिये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12859)
- **Original**: श्रीपपाशरजी ओले--हे ब्रहान्‌ ! तदनन्तर खाष्डिक्यससे यथोचित पूजित हो राजा केशिध्वज अपने नगरमें चले आये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12860)
- **Original**: तथा खाप्डिक्य भी अपने पुत्रकों राज्य दे* श्रीगोविन्दर्में चित्त गाकर योग सिद्ध करनेके लिये [ निर्जन ] वनकों चले गये
- **Translation**: 

---

