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

### Verse 1 (Vishnu Puran 0.5201)
- **Original**: जरूमें प्रथम आचार्यके स्रा3 कर चुकनेपर फिर स्वय॑ स्रान को तथा प्रतिदिन प्रातःकाल गुरुजीके समिधा, जल, कुश और पुष्पादि लाकर जुटा दे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5202)
- **Original**: इस प्रकार अपना अभिमत वेदपाठ समाप्त कर चुकनेपर बुद्धिमान शिष्य गुरूजीकी आज्ञासे उन्हें गुरु- टक्षिणा देकर गृहस्थाश्रममें प्रवेश़ा करे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5203)
- **Original**: हे राजन्‌ ! फिर विधिपूर्वक पाणिग्रहण कर अपनी वर्णानुकूछ खुत्तिसे द्रव्योपार्जत करता हुआ सामर्थ्यातुसार समस्त गृहकार्य करता रहे
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5204)
- **Original**: पिण्ड-दानादिसे पितृगणकी, स्वाध्यायसे ऋषियोंकी, पुत्रोत्पत्तिसे प्रजापतिकी, बलियों (अन्नभाग) से भूतगणको तथा वात्सल्यभावसे सम्पूर्ण जगत्‌की पूजा करते हुए पुरुष अपने कर्मोद्गारा मिले हुए लोकॉंको प्राप्त कर छेता- है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5205)
- **Original**: 0] तृतीय अंश 987 9) अंझ 187 जो केबल भिक्षावृत्तिसे ही रहनेवाले परिब्राजक और भिक्षाभुजश्न केचित्परित्राइब्रह्मचारिण तेजप्यत्रैत् प्रतिष्ठन्ते गाहस्थ्य लेन ले परम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5206)
- **Original**: तरह्मचारो आदि हैं उनका आश्रय भी गृहस्थाश्रम ही है, अत वेदाहरणकार्याय तीर्थसत्रनानाय चर प्रभो। यह सर्वश्रेष्ठ है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5207)
- **Original**: हे एजन्‌ ! बिप्रगण वेदाध्ययन तोर्थख्ान और देश दर्शनके लिये पृथिवी-पर्यटन किया अटठन्ति बसुथां विप्रा: पृथिवीदर्शनाय च्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5208)
- **Original**: करते है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5209)
- **Original**: उनमेंसे जिनका कोई निश्चित गृह अथवा अनिकेता ह्वानाहारा यत्र सायंगृहाश्न ये। तेषां गृहस्थः सर्वेषां प्रतिष्ठा योनिरेव च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5210)
- **Original**: 13 तेषां स्वागतदानादि वक्तव्य मधुरं नृप। गृहागतानां द्याध्ष शयनासनभोजनम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5211)
- **Original**: 14 अतिथ्िर्यस्थ भग्नाओे गृहात्मतिनियर्तते । स दच्त्वा दुष्कृतं तस्मै पुण्यमादाय गच्छति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5212)
- **Original**: 15 अवज्ञानमहक्लूरो दम्भक्षेव गृहे सतः। परितापोपघातो ञ्व पारुष्यं च न हस्यते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5213)
- **Original**: 16 यस्‍्तु सम्यक्वरोत्येव॑ गृहस्थः: परम॑ विधिम्‌। सर्वक्नधविनिर्मुक्तो ल्लोकानाप्रोत्यनुत्तमान्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5214)
- **Original**: 17 बबःपरिणतो राजन्कृतकृत्यो गृहाश्रमी । पुत्रेषु भार्या निक्षिप्य बने गच्छेत्सहैव वा
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5215)
- **Original**: 18 पर्णपूलफलाहार: केशइमश्ुजटाधर: । भूमिशायी भवेत्तत्र मुनिस्सर्वातिथिनंप
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5216)
- **Original**: 19 चर्मकाशकुद्दी: कुर्यात्यरिधानोत्तरीयके । तद्नत्न्रिपषर्ण सत्रान॑ झस्तमस्थ नरेश्वर
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5217)
- **Original**: 20 देक्ताभ्यर्चन॑ ह्वोमस्सर्वाभ्यागतपूजनम्‌ । भिक्षा बलिप्रदानं चर शास्तमस्य नरेश्वर
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5218)
- **Original**: 21 वन्यस्त्रेहन गात्राणामभ्यड्ुश्षास्थ झस्यते । तपश्च तस्य राजेन्द्र शीतोष्णादिसहिष्णुता
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5219)
- **Original**: 22 यस्त्वेतां नियतश्चर्यां वानप्रस्थश्षरेन्मुनि: । स॒ दहत्यप्रिवद्येषाअयेल्सत्रेकांश् शाश्रतान्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5220)
- **Original**: 23 चतुर्थश्लाश्रमो भिक्षो: प्रोच्यते यो मनीषिभिः । तस्थ स्वरूप गदतो मम ओ्रोतुं नृपाहसि
- **Translation**: 

---

