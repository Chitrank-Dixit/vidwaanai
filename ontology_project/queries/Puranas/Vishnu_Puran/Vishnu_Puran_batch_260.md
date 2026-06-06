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

### Verse 1 (Vishnu Puran 0.5181)
- **Original**: है गजन्‌ ! इस प्रकार कर्णधर्मौंका वर्णन तो मैंने तुमसे कर दियो; अब आश्रम धर्मानाश्रमिणां सम्यग्ब्युवतो मे निशामय
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5182)
- **Original**: धर्मोका निरूपण और करता हूँ, सावधान होकर सुनो
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5183)
- **Original**: व्यक्त पु इति श्रीविष्णुपुराणे तृतीयेंडशे अष्टमोधध्यायः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5184)
- **Original**: अतनससस जौ लच्च्चि नवाँ अध्याय ब्रह्माखर्य आदि आश्रमोंका वर्णन ऑर्यउयाच कृतोपनयनो .वेदाहरणतत्पर: । गुरुगेहे वसेद्धप ब्रह्मचारी समाहितः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5185)
- **Original**: 91 शौचाचारत्रत॑ तत्र कार्य शुश्रूषणं गुरो: । ब्रतानि चरता ग्राह्मों वेदक्ष कृतबुद्धिना
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5186)
- **Original**: 2 उभे सन्ध्ये रविं भूष तथेवाश समाहित: । उपतिष्ठेत्तता. कुर्याद्रुरोरप्यभिबादनम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5187)
- **Original**: 3 स्थिते तिष्ठेद्रजेग्याते नीचैरासीत चासति। शिष्यों गुरोन॑पश्रेष्ठ प्रतिकूल न सख्धरेत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5188)
- **Original**: 4 तेनैवोक्त॑ पठेक्वेदे नान्यचित्त: पुरस्स्थितः । अनुज्ञातश्च भिक्षात्रमश्नीयादुरुणा ततः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5189)
- **Original**: 5 अबगाहेदप: .. पूर्बमाचार्येणाबगाहिता: । समिज्ज्लादिकं चास्य कल्य॑ कल्यमुपानयेत्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5190)
- **Original**: 6 गृहीतगआहावेदश्य ततोनुज्ञामवाप्प च। गाहस्थ्यमाविशेद्याज़ो निष्पन्नगुरुनिष्कृति:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5191)
- **Original**: 7 विधिनावाप्रदारस्तु धन प्राप्य स्वकर्षणा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5192)
- **Original**: गृहस्थकार्यमखिलं कुर्याद्धपाल दाक्तित:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5193)
- **Original**: 8 निबापेन. पितृनर्चन्यज्ैदेंबास्तथातिथीन्‌ । अन्नैर्मुनीक्ष स्वाध्यायैरपत्येन प्रजापतिम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5194)
- **Original**: 9 भूतानि बलिभिश्नेव वात्सल्येनाखिलं जगत्‌। ग्राप्रोति लोकान्पुरुषो निज्रकर्मसमार्जितान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5195)
- **Original**: 90 ओऔर्व बोले--हे भूपतें! बाल्केकों चाहिये कि उफ्यन-संस्कारके अनत्तर क्रेदाध्ययनमें तत्पर होकर बद्मचर्यका अवबलम्बन कर सावधानतापूर्वक गुरुगृहमें निवास करे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5196)
- **Original**: वहाँ रहकर उसे ज्ौच और आचार- ब्रतका पालन करते हुए गुरूकी सेचा-जुश्रूषा करमी चाहिये तथा ब्रतादिका आचरण करते हुए स्थिर-बुद्धिसे वेदाध्ययन करना चाहिये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5197)
- **Original**: हे राजन्‌! [प्रातःकाल और सायकाल] दोनों सख्याओंमें एकाप होकर सूर्य और अप्रिकी उपासना करे तथा गुरुका अभिवादन करे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5198)
- **Original**: गुरुके खड़े होनेपर खड़ा हो जाय, चलनेपर पीछे पीछे चलने लगे तथा बैठ जानेपर नीचे बैठ जाथ। हे नृपश्रेश्च
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5199)
- **Original**: इस प्रकार कभी गुरुके विरुद्ध कोई आचरण न करे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5200)
- **Original**: गुरुजीके कहनेपर ही उनके सामने बैठकर एक्प्रथ्चित्तसे वेदाध्ययन करे और उनकी आज्ञा होनेएः ही भिक्षात्र भोजन करे
- **Translation**: 

---

