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

### Verse 1 (Vishnu Puran 0.12601)
- **Original**: 27 खाण्डिक्यश्वाह तान्सबनिवमेतन्न संशय: । हते$स्मिन्यूथिवी सर्वा मप्र वश॒या भविष्यति
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12602)
- **Original**: 28 परव्म्रेकजयस्तस्थ पृथिवी सकला मम। न हन्पि चेल्‍्लोकजबो मम तस्य वसुन्धरा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12603)
- **Original**: 29 नाहँ मन्‍्ये लोकजयादधिका स्याह्सुन्धरा । परलोकजयोउनन्तस्स्वल्पकालो महीजय:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12604)
- **Original**: 30 तस्पान्नैनं हनिष्यामि यत्पृच्छति वदामि तत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12605)
- **Original**: 31 अऔपराशर उवाच ततस्तमभ्युपेत्याह खाण्डिक्यजनको रिपुम्‌। प्रष्टव्यं यत्तया सर्व तत्पृच्छस्ब बदाम्यहम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12606)
- **Original**: 32 ततस्सर्व॑ यथावृत्त॑ धर्मधेनुबर्ध॑ द्विज । कथयित्वा स पप्रच्छ प्रायश्चित्त हि तद़तम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12607)
- **Original**: 33 सचाचष्ट यथान्याय॑ द्विज केशिध्वजाय तत्‌ । भ्रायक्षित्तमशेषेण यहै तत्र विधीयते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12608)
- **Original**: 34 बिदितार्थस्स तेनैख ह्ानुज्ञातों महात्मना। यागभूमिमुपागम्य चक्रे सर्वा: क्रिया: क्रमात्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12609)
- **Original**: 35 क्रमेण विधिवद्यागं नीत्वा सोप्वभृथाहुत ः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12610)
- **Original**: कृतकृत्यस्ततो भूत्वा चिन्तयामास पार्थिव:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12611)
- **Original**: 36 पूजिताश्ष द्विजास्सवें सदस्या मानिता मया । तथैवार्थिजनो5प्यर्थैयोंजितोइभिमतैर्मया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12612)
- **Original**: 37 यथाईमस्य लोकस्य मया सर्व विचेष्टितम्‌ । अनिष्पन्नक्रियं चेतस्तथापि मम कि यथा
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12613)
- **Original**: 38 इत्थे सख्िन्तयन्नेव सस्मार स महीपतिः । खाण्डिक्याय न दिवत्तेति मया ये गुरुदक्षिणा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12614)
- **Original**: 39 स॒ जगाप्त तदा भूयो रथमारुह्म पार्थिव: । मैत्रेय दुर्गगहन॑ खाण्डिक्यों यत्न संस्थित:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12615)
- **Original**: 40 खाण्डिक्यो5पि पुनर्दष्ठा तमायान्ते धृतायुधम्‌। तस्थौ हन्तुं कृतमतिस्तमाह स पुनर्नुपः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12616)
- **Original**: 49 भो नाहे तेःपराधाय प्राप्त: खाण्डिक्य मा क्ुध: । गुरोर्निष्क्रधदानाय मामवेहि त्वमागतम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12617)
- **Original**: 42 घष्ठ अंश 445 स्ताण्डिक्नने अपने सम्पूर्ण पुरोहित और मच्वियोंसे एकान्तमें सत्मरृह की
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12618)
- **Original**: मन्जियोने कहा कि 'इस समय शात्रु आपके वहामें है, इसे मार डालना चाहिये। इसको मार देनेपर यह सम्पूर्ण पृथिबी आपके अधीन हो जायगी'
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12619)
- **Original**: खाण्डिक्यने कहा--““यह निस्सनन्‍देह ठीक है, इसके मारे जानेपर अवश्य सम्पूर्ण पृथिवी मेरे अधीन हो जायगी; किन्तु इसे पारलौकिक जय प्राप्त होगी और मुझे सम्पूर्ण पृथिवी । परन्तु यदि इसे नहीं मारूँगा तो मुझे पारछौकिक जय प्राप्त होगी और इसे सारी पृथिवी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12620)
- **Original**: मैं पारल्लैकिक जयसे पृथिवोकों अधिक नहीं मानता; क्योंकि परलोक-जय अनन्तकालक्रे लिये होती है और पृथिवों तो थोड़े ही दिन रहती है। इसलिये मैं इसे मारूँगा नहीं, यह जो कुछ पूछेगा, बतत्ख दूँगा!"
- **Translation**: 

---

