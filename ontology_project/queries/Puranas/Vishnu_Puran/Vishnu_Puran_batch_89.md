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

### Verse 1 (Vishnu Puran 0.1761)
- **Original**: हुए और उन्होंने रोषपूर्वक अपने मुखसे वायु और अप्रिको उच्यूछानथ तान्वृक्षान्कृत्वा वायुरशोषयत्‌। तानप्रिरक्हद्घो रस्तत्राभूदृदूमसद्ब॒य:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1762)
- **Original**: ड हुमक्षयमथों दृष्टा किश्निच्छिप्टेषु शाखिषु। उपगम्याब्रवीदेतात्नाजा सोमः प्रजापतीन्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1763)
- **Original**: 5 छोड़ा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1764)
- **Original**: कायुने वृक्षोंको उख्ाड़-उखाड़कर सुख्ता दिया और प्रचण्ड अभ्निने उन्हें जला डाल्ड । इस प्रकार उस समय वहाँ वृक्षोंका नाश होने छगा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1765)
- **Original**: तब वह भयंकर वृक्ष-प्रकूथ देखकर थोड़े-से वृक्षोके रह जानेपर उनके राजा सोमने प्रजापति
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1766)
- **Original**: आ2 15 ] कोप॑ यच्छत राजानः श्रृणुध्बं च क्लो मम । सन्धान॑ व: करिष्यामि सह क्षितिस्हैरहम्‌। 6 रलभूता चर कन्येयं वार्क्षेबी बरवर्णिनी। भ्रविष्यज्ञानता पूर्व मया गोभिर्विषर्द्धता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1767)
- **Original**: 7 मारिषा नाम नाम्रैषा वृक्षाणामिति निर्मिता । भार्या वोउस्तु महाभागा ध्रुव बंशविवर्स्धिनी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1768)
- **Original**: । 8 युष्मार्क तेजसोउर्द्धेन मम चार्द्ेन तेजस: । अस्थामुत्पत्य्यते विद्वान्दक्षो नाम प्रजापति:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1769)
- **Original**: 9 मम्त चांचोन संयुक्तो युष्मत्तेजोमयेन सै। तेजसाप्रिसमो भूय: प्रजा: संबर्द्धयिष्यति
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1770)
- **Original**: 10 कष्छुर्नाम मुनिः पूर्वमासीद्वेदविदां बरः । सुरम्ये गोमतीतीरे स तेपे परम तपः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1771)
- **Original**: 11 तत्क्षोभाय सुरेन्‍्द्रेण प्रम्कोचाख्या वराष्सरा: । भ्रयुक्ता क्षोभयामास तमृर्षि सा शुच्चिस्मिता
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1772)
- **Original**: 12 त॑ सा प्राह महाभाग गन्तुमिच्छाम्यह॑ दिवम्‌। प्रसादसुमुखो ब़्रहान्ननुज्ञा दातुमहसि
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1773)
- **Original**: 14 तयैबमुक्त: स ॒मुनिस्तस्यथामासक्तमानसः । दिनानि कतिचिउ्धद्रे स्थीयतामित्यभाषत
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1774)
- **Original**: 15 एवमुक्ता ततस्तेन साम्र॑ वर्षशत॑ पुनः । जुभुजे विषयांस्तन्वी तेन साकं महात्मना
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1775)
- **Original**: 16 अनुज्ञां देहि भगवन्‌ ब्रजामि त्रिदशालयम्‌ । उक्तस्तथेति स्॒ पुनः स्थीयतामित्यभाषत
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1776)
- **Original**: 17 पुनर्गते वर्षशते साधिके सा शुभानना। यामीत्याह दिव॑ ब्रह्मग्रणयस्मितशों भनम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1777)
- **Original**: 18 उक्तस्तयैव स॒ मुनिरुषगुह्यायतेक्षणाम्‌ । इहास्यतां क्षणं सुभ्रु चिरकालं गमिष्यसि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1778)
- **Original**: 19 सा क्रीडमाना सुओओणी सह तेनर्षिणा पुनः । अतह॒यं॑ किझ्निदून॑ वर्षाणामन्जतिप्ठत
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1779)
- **Original**: 20 गमनाय महाभाग देवराजनिवेशनम्‌ । ज्रोक्तः प्रोक्तस्तया तन्व्या स्थीयतामित्यभाषत
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1780)
- **Original**: 29 प्रथम अंञ 63 प्रचेताओंके पास जाकर कहां---
- **Translation**: 

---

