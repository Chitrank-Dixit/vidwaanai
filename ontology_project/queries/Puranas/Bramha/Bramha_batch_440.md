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

### Verse 1 (Bramha 0.8781)
- **Original**: ज्ञाता मनीषी पुरुष ऐसा ही कहते हैं। जो तत्त्व उठता तथा वह काठकी भाँति स्थिर होकर
- **Translation**: 

---

### Verse 2 (Bramha 0.8782)
- **Original**: जिससे उत्पन्न होता है, उसका उसीमें लय भी किसी भी वस्तुका अभिमान या सुध-बुध नहीं
- **Translation**: 

---

### Verse 3 (Bramha 0.8783)
- **Original**: होता है
- **Translation**: 

---

### Verse 4 (Bramha 0.8784)
- **Original**: प्रकृति परमात्माके संनिधानसे अनुलोम- रखता, उस समय मनीषी पुरुष उसे अपने
- **Translation**: 

---

### Verse 5 (Bramha 0.8785)
- **Original**: क्रमके अनुसार तत्त्वोंकी रचना करतो है अर्थात्‌ स्वरूपको प्राप्त 'योगयुक्त' कहते हैं। ध्याननिष्ठ
- **Translation**: 

---

### Verse 6 (Bramha 0.8786)
- **Original**: प्रकृतिसे महत्तत््व, महत्तत््वसे: अहंकार तथा योगीकों अपने हृदयमें धूमरहित अग्नि, अहंकारसे सूक्ष्म भूत आदिके क्रमसे सृष्टि होती किरणमालाओंसे मण्डित सूर्य तथा विद्युतके
- **Translation**: 

---

### Verse 7 (Bramha 0.8787)
- **Original**: है; किंतु उसका संहार विलोमक्रमसे होता है। प्रकाशकी भाँति तेजस्वी आत्माका साक्षात्कार
- **Translation**: 

---

### Verse 8 (Bramha 0.8788)
- **Original**: अर्थात्‌ पृथ्वीका जलमें, जलका तेजमें और होता है। धैर्यवान्‌, मनीषी, वेदवेत्ता और महात्मा
- **Translation**: 

---

### Verse 9 (Bramha 0.8789)
- **Original**: तेजका वायुमें लय होता है; इसी प्रकार सभी ब्राह्मण ही उस अजन्मा एवं अमृतस्वरूप ब्रह्मका
- **Translation**: 

---

### Verse 10 (Bramha 0.8790)
- **Original**: तत्व अपने-अपने कारणमें लीन होते हैं। जैसे दर्शन कर पाते हैं। बह ब्रह्म अणुसे भी अणु
- **Translation**: 

---

### Verse 11 (Bramha 0.8791)
- **Original**: समुद्रसे उठी हुई लहरें फिर उसीमें शान्त हो और महानूसे भी महान्‌ कहा गया है। सर्वत्र
- **Translation**: 

---

### Verse 12 (Bramha 0.8792)
- **Original**: जाती हैं, उसी प्रकार सम्पूर्ण तत्त्व अनुलोमक्रमसे सम्पर्ण भूतोंमें स्थित होते हुए भी वह किसीको
- **Translation**: 

---

### Verse 13 (Bramha 0.8793)
- **Original**: उत्पन्न होकर विलोमक्रमसे लीन होते हैं।
- **Translation**: 

---

### Verse 14 (Bramha 0.8794)
- **Original**: ड20 * संक्षिप्त श्रह्मपुराण « नृपश्रेष्ठ ! इस प्रकार प्रकृतिसे ही जगत्‌की उत्पत्ति
- **Translation**: 

---

### Verse 15 (Bramha 0.8795)
- **Original**: उपदेश नहीं देना चाहिये। शिष्यकों बोध करानेके और उसीमें उसका लय होता है। प्रलयकालमें तो
- **Translation**: 

---

### Verse 16 (Bramha 0.8796)
- **Original**: लिये ही इस वत्वका उपदेश करना उचित है। वह एक रूपमें रहती है और सृष्टिके समय नाना
- **Translation**: 

---

### Verse 17 (Bramha 0.8797)
- **Original**: जो श्रद्धालु, गुणवान्‌, परायी निन्दासे दूर रहनेबाले, रूप धारण करती है। ज्ञान-निपुण पुरुषोंको इसी
- **Translation**: 

---

### Verse 18 (Bramha 0.8798)
- **Original**: विशुद्ध योगी, विद्वान, वेदोक्त कर्म करनेवाले, प्रकार प्रकृतिक एकत्व और नानात्वका ज्ञान प्राप्त
- **Translation**: 

---

### Verse 19 (Bramha 0.8799)
- **Original**: क्षाशील तथा सबके हितैषी हों, वे ही इस करना चाहिये। ज्ञानके अधिकारी हैं। जितेन्द्रिय तथा संयमी प्रकृतिका अधिष्ठाता जो अव्यक्त आत्मा है,
- **Translation**: 

---

### Verse 20 (Bramha 0.8800)
- **Original**: पुरुषको इसका उपदेश अवश्य देना चाहिये। उसके विषयमें भी यही बात है। जह भी
- **Translation**: 

---

