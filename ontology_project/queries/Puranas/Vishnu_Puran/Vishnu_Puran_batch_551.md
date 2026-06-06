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

### Verse 1 (Vishnu Puran 0.11001)
- **Original**: 34 आरुह्म च स्वयं कृष्णस्सत्यभामासहायवान्‌ । अदित्या: कुण्डले दातुं जगाम त्रिदशालयम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11002)
- **Original**: 35 पृथिवी बोली--हे नाथ ! जिस समय वराहरूप घारणकर आपने मेरा उद्धार किया था उसी समय आपके स्पर्डासे मेरे यह पुत्र उत्पन्न हुआ था
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11003)
- **Original**: इस प्रकार आपहौने मुझे यह पुत्र दिया था और अब आपहीने इसको नष्ट किया है; आप ये कुण्डल लीजिये और अब इसकी सन्तानकी रक्षा कीजिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11004)
- **Original**: हे प्रभो ! मेरे ऊपर प्रसन्न होकर ही आप मेरा भार उतारनेके छिये अपने अदासे इस ल्मरेकमें अवतीर्ण हुए हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11005)
- **Original**: हे अच्युत ! इस जगत्‌के आप ही कर्ता, आप हो विकर्ता (पोषक) और आप ही हर्ता (संहारक) हैं; आप ही इसकी उत्पत्ति और लयके स्थान हैं तथा आप ही जगत्रूप हैं। फिर हम आपकी स्तुति किस प्रकार करें ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11006)
- **Original**: है भगवबन्‌ ! जब कि च्याप्ति, व्याप्य, क्रिया, कर्ता और कार्यरूप आप ही हैं तब सबके आत्मस्वरूप आपकी किस प्रकार स्तुति को जा सकती है 7
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11007)
- **Original**: हे नाथ ! जब आप ही परमात्मा, आप ही भूतात्मा और आप ही अन्यय जीवात्मा हैं तब किस वस्तुको लेकर आपको स्तुति हो सकती है ?
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11008)
- **Original**: है सर्वभूतात्मन्‌ ! आप असन्न होइये और इस नरकासुरके सम्पूर्ण अपराध क्षमा कोजिये । निश्चय ही आपने अपने पुत्रको निर्दोष करनेके लिये ही स्वये मारा है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11009)
- **Original**: श्रीपराहरजी बोले--हे मुनिश्रेष्ठ )! तदनन्तर भगवान्‌ भूतभावनने पृथिवीसे कहा--' तुम्हारी इच्छा पूर्ण हो” और फिर नरकासुरके महरूसे नाना प्रकारके रल लिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11010)
- **Original**: हे महामुने ! अतुलबिक्रम श्रीभगवानने नस्कासुरके कन्यान्तःपुरमें जाकर सोलह हजार एक सौ कन्याएँ देखीं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11011)
- **Original**: तथा चार दाँतवाले छः: हजार गजश्रे'ष्ठ और इक्कीस राख काम्बोजदेशीय अश्व देखे
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11012)
- **Original**: उन कन्याओं, हाथियों और छोड़ोंको श्रीकृष्णचन्द्रने नरकासुरके सेवकोंद्वारा तुरन्त ही द्वास्कापुरी पहुँचया दिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11013)
- **Original**: तदनन्तर भगवानने वरुणका छत्र और मणिपवैत देखा, उन्हें उठाकर उन्होंने पक्षिराज गरुडपर रख लिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11014)
- **Original**: और सत्यभामाके सहित स्वयं भी उसीपर चढ़कर अदितिके कुष्डल देनेके लिये स्वर्गलोककों गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11015)
- **Original**: न जद च+-- इति श्रीविष्णुपुराणे पद्चमेंडशे एकोनत्रिशोउध्यायः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11016)
- **Original**: 388 [ अ« 30 तीसवाँ अध्याय पारिजात-हरण अपराशर उवाच गरुड़ो वारु्ण छत्र॑ तथैव मणिपर्वतम्‌। सभाय॑च हृषीकेश लीलयैव वहन्ययों
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11017)
- **Original**: 9 ततद्दाब्डमुपाध्मासीत्सवर्गद्वरागतो हरि: । उपतस्थुस्तथा देवास्सार्घ्यहस्ता जनार्दनम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11018)
- **Original**: 2 स देवैरचिंत: कृष्णो देवमातुर्निबेशनम्‌। सिताभ्रशिखराकार॑ प्रविश्य ददृशेददितिम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11019)
- **Original**: 3 सतां प्रणम्य शक्रेण सह ते कुण्डल्लत्तमे । ददौं नरकनाश च शशंसास्थै जनार्दन:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11020)
- **Original**: 4 ततः प्रीता जगन्म्राता धातारं जगतां हरिम्‌। तुष्टाबादितिरव्यग्रा कृत्वा तत्मबर्ण मनः
- **Translation**: 

---

