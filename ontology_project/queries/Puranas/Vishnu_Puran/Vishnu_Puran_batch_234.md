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

### Verse 1 (Vishnu Puran 0.4661)
- **Original**: श्रीपराशरजी बोले--हे मुने ! विश्वकर्माको पुत्री ,
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4662)
- **Original**: सैज्ञा सूर्यकी भार्या थी। उससे उनके मनु, यम और यमी--तीन सत्तानें हुईं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4663)
- **Original**: कालात्तरमें पतिका तेज सहन नय कर सकनेके कारण संज्ञा छायाको पतिकी सेवामें नियुक्त कर स्त्ये तपस्याके ल्यि जनको चली गयी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4664)
- **Original**: सुर्यदेवने यह समझकर कि यह संज्ञा ही है, स्मयासे हानैक्षर, एक और मनु तथा तपती---ये तीन सत्तानें उत्पन्न की। 4
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4665)
- **Original**: एक दिन जब छायारूपिणों संज्ञाने क्रोश्ित होकर (अपने पुक्रके पक्षपातसे] यमकों जाप दिया तब सूर्य और यमको छिदित हुआ कि यह तो कोई और है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4666)
- **Original**: तब छायाके द्वारा ही सारा रहस्य खुल जानेपर सूर्यदेयने समाधिपें स्थित होकर देखा कि संज्ञा घोड़ीका रूप धारण कर सममें तपस्या कर रहो है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4667)
- **Original**: अतः उन्होंने भी अश्वरूप होकर उससे दो अधिनीकुमार और रेतःखावके अनच्तर हो रेबनन्‍्तक्त्रे उत्पन्न किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4668)
- **Original**: फ़िर भगवान्‌ सूर्य संज्ञाकों अपने स्थानपर ले आये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4669)
- **Original**: आ2 )] भ्रममारोष्य सूर्य तु तस्थ तेजोनिशातनम्‌ । कृतबानष्टममं॑ भाग स्र॒ व्यज्ञातयदब्ययम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4670)
- **Original**: 9 यत्तस्मादैष्णव॑ तेजइशातित विश्वकर्मणा । जाज्वल्यमानमपतत्तद्धमा. मुनिसत्तम
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4671)
- **Original**: 10 त्वष्टेव तेजसा तेन विष्णोश्चक्रमकल्पयत्‌ । त्रिशूले चैब झर्वस्थ शिबिकां धनदस्थ च
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4672)
- **Original**: 11 शक्ति गुहस्य देवानामन्येषां च यदायुधम्‌ । तत्सर्य तेजसा तेन विश्वकर्मा व्यवर्धवत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4673)
- **Original**: 12 छायासंज्ञासुतो योउसौ द्वितीय: कधितो मनु: । पूर्वजस्य सवर्णोउसो सावर्णिस्तेन कथ्यते
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4674)
- **Original**: 13 तस्य मन्वन्तरं होतत्सावर्णिकमथाप्टमम्‌। तक्छृणुष्च महाभाग भविष्यत्कथयामि ते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4675)
- **Original**: 194 सावर्णिस्तु मनुर्योञसो मैत्रेय भविता ततः । सुतपाश्चामिताभाश्न मुख्याआपि तथा सुरा:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4676)
- **Original**: 15 तेषां गणश्न देवानामेकैको विंशक:ः स्मृतः । सप्तर्षीनपि वक्ष्यामि भविष्यान्पुनिसत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4677)
- **Original**: 16 दीप्रिमान्‌ गालवो रामः कृपों द्रौणिस्तथा पर: । मत्पुत्रश्न तथा व्यास ऋष्यश्ूड़श्न सप्तम:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4678)
- **Original**: 17 विष्णुप्रसादादनघ: पातालान्तरगोचर: । विरोचनसुतस्तेषां बल्रिन्द्रों भविष्यति
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4679)
- **Original**: 18 विरजाश्षोर्वरीवांक्ष निर्मोकाद्यास्तथापरे सावर्णेस्तु मनो: पुत्रा भविष्यन्ति नरेश्वरा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4680)
- **Original**: 19 नवमो दक्षसावर्णिभविष्यति मुने मनुः
- **Translation**: 

---

