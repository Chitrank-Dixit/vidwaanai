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

### Verse 1 (Vishnu Puran 0.3821)
- **Original**: बे युग- युगान्तरमें विच्छिन्न हुए वैदिक धर्मकों, सनन्‍्तान तपस्या वर्णाश्रम-मर्यादा और विविध चाखोंके ट्वारा पुनः स्थापना करते हैं।87
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3822)
- **Original**: पूर्बतन धर्मप्रबर्तक ही अपनों उत्तरकालीन सनन्‍्तानके यहाँ उत्पन्न होते हैं और फिर उत्तरकाल्जीन धर्म-प्रचारकशण अपने यहाँ सत्तानरूपसे उत्पन्न हुए अपने पितृगणके कुस्मेंमें जन्म लेते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3823)
- **Original**: इस प्रकार, वे व्रतदीछ महर्षिगण चन्द्रमा और तारागणकी स्थितिपर्यन्त सूर्यके दक्षिणमार्गमें पुनः-पुनः आते-जाते रहते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3824)
- **Original**: नागवीथिके उत्तर और सप्तर्षियोंके दक्षिणमें जो सूर्यका उत्तरीय मार्ग है उसे देवयानमार्ग कहते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3825)
- **Original**: उसमें जो प्रसिद्ध निर्मलस्थभाव और जितेन्द्रिय ब्रह्मचारिगण निवास करते है वे सनन्‍्तानकी इच्छा नहीं करते, अतः उन्होंने मृत्युको जीत लिया है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3826)
- **Original**: सूर्यके उत्तरमार्गमें अस्सी हजार ऊध्वरेता मुनिगण प्र्यकालपर्यन्त निवास करते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3827)
- **Original**: उन्होंने ल्ोभधके असंयोग, मैथुनके स्याग, इच्छा और द्वेषकी अप्रवृत्ति, कर्मानुष्ठानके त्याग, काम-वासनाके अस॑योग और शब्दादि विषयोंके दोष- दर्शन इत्यादि कारणोंसे शुद्धचित्त होफ़र अमरता प्राप्त कर ली है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3828)
- **Original**: धूतोंके प्रलूयपर्यन्त स्थिर रहनेको ही अमरता कहते हैं। त्रिकोकीकी स्थितितकके इस कालक्य ही अपुनर्मार (पुनर्मुत्युयहित) कहा जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3829)
- **Original**: हे द्विज
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3830)
- **Original**: ब्रह्महत्या और अश्वमेधयज्ञसे जो पाप और पुण्य होते हैं उनका फल प्रल्यपर्यन्त कहा गया है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3831)
- **Original**: 135 अ्रीविष्णुपुराण ([आ्8 याजम्तत्रे प्रदेशे तु मैश्नेयालस्थितो घुलः । क्षयमायाति तावक्तु भूमेराभूतसम्प्रवात्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3832)
- **Original**: 97 ऊर्ध्वोत्तरमृषिभ्यस्तु धुवों यत्र व्यवस्थित: । एतद्ठिष्णुपर्द दिव्य तृतीय व्योज़ि भासुरम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3833)
- **Original**: 98 निर्धूतदोषपद्कानां यतीनां संयतात्मनाम्‌। स्थान तत्परमं विप्र पुण्यपापपरिक्षये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3834)
- **Original**: 99 यत्र गत्वा न शोचन्ति तद्विष्णो: परम पदम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3835)
- **Original**: 100 धर्मधुवाद्यास्तिप्नन्ति यत्र ते लोकसाक्षिण: । तत्साष्ट्त्पन्नयोगेद्धास्तद्विष्णो: परम पदम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3836)
- **Original**: 101 अन्नोतमेतत्मोत॑ कल 20 0 । पारव्य चर विश्व मैत्रेय : परम पदम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3837)
- **Original**: 102 विवेक टन नहिएणो योगिनां तन्ययात्मनाम्‌ । चर : परम पदम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3838)
- **Original**: 103 यसिमिग्रतिप्ठितो भास्वान्मेडी भूत: स्वय॑ ध्रुव: । धरुवे च सर्वज्योतीषि ज्योति:घ्ृष्भोमुचो द्विज
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3839)
- **Original**: 1904 मेघेषु सड्गतता वृष्टिवृष्टि: सृष्टेश्न पोषणम्‌। आप्यायन च॒ सर्वेषां देबादीनां महामुने
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3840)
- **Original**: 105 त़तः पोषितास्ते हविर्भुज: । वृष्टे: कारणतां यान्ति भूतानां स्थितये पुनः
- **Translation**: 

---

