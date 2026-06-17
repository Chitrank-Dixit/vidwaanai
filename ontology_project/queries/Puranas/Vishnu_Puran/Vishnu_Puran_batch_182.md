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

### Verse 1 (Vishnu Puran 0.3621)
- **Original**: हे मुनिसत्तम ! जिस प्रकार धानके बीजमें मुल्ल, नाल, पत्ते. अर _र, तना, कोष, पृष्प, क्षौर, तण्डुल, तुष और कण सभी हैं; तथा अल्भुरोत्पत्तिकी हेतुभूत [ भूमि एवं जल आदि] सामग्रीके प्राप्त होनेपर थे प्रकट हो जाते हैं, डसी प्रकार अपने अनेक पूर्वकर्मांमें स्थित देलता आदि थिष्णु-चक्तिका आश्रय पानेपर आविर्धूत हो जाते है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3622)
- **Original**: 37--39
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3623)
- **Original**: जिससे यह सम्पूर्ण जगत्‌ उत्पन्न हुआ है, जो स्वयं जगत्रूपसे स्थित है, जिसमें यह स्थित है तथा जिसमें यह लीन हो जायगा यह परबह्मा ही विष्णुभगवान्‌ हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3624)
- **Original**: वह ब्रह्म ही उन (विष्णु) का परमधाम (परस्वरूप) है, वह पद सत्‌ और असत्‌ दोनोंसे खिल्क्षण है तथा उससे अभिन्र हुआ ही यह सम्पूर्ण चणचर जगत्‌ उससे उत्पन्न हुआ है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3625)
- **Original**: वही अव्यक्त मूलप्रकृति है, जड्ही व्यक्तस्वरूप संसार है, उसीमें यह सम्पूर्ण जगत्‌ लीग होता है तथा उसीके आश्रय स्थित है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3626)
- **Original**: यज्ञादि क्रियाओऑँका कर्ता वही है, यज्ञरूपसे उसीका यजन किया जाता है, और उन यज्ञादिका फलस्वरूप भी बही है तथा यज्ञके साधनरूप जो आदि हैं वे सब भी हरिसे _ हरेने किम्निदव्यतिरिक्तमस्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3627)
- **Original**: अतिरिक्त और कुछ नहीं है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3628)
- **Original**: --_-_- जौर ननना+ इति श्रीविष्णुपुराणे द्वितीयेंठदों सप्तमोडघ्यायः
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3629)
- **Original**: ह्वितीय अंश 129 आठवाँ अध्याय सूर्व, नक्षत्र एवं राक्षियोंकी व्यवस्था तथा कालचक्र, त्ओोेकपाल और गड्जाविर्भावका वर्णन श्रीपराझर उवाच व्याख्यातमेतदूह्माण्डसंस्थानं॑ तब सुब्रत । ततः प्रमाणसंस्थाने सूर्यादीनां श्ृणुष्न पे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3630)
- **Original**: 91 योजनानां सहस्नाणि भास्करस्य रथो नव
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3631)
- **Original**: ईषादण्डस्तथैवास्थ द्विगुणो मुनिसत्तम
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3632)
- **Original**: 2 सार्थकोटिस्तथा सप्त नियुतान्यधिकानि वे । योजनानां तु तस्याक्षस्तत्र चक्र प्रतिष्ठितम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3633)
- **Original**: 3 जिनाभिमति पश्चारे बण्नेमिन्यक्षयात्मके । संवत्सरमये कृत्स्ले कालचक़ं प्रतिष्ठितम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3634)
- **Original**: 4 हयाश्च सप्तच्छन्दांसि तेषां नामानि से श्रृणु । चत्वारिंशत्सहस्राणि द्वितीयो क्षो विवस्वत: । पश्चान्यानि तु साथानि स्वन्दनस्थ महामते
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3635)
- **Original**: 6 अक्षप्रमाणमुभयो: प्रमाणं तद्युगार्द्धवो: । ध्रुवाधारो रथस्य वे । द्वितीयेउक्षे तु तक संस्थितं मानसाखले
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3636)
- **Original**: 7 मानसोत्तरशैलस्थ पूर्वती वासवी पुरी। दक्षिणे तु यमस्यान्या प्रतीच्यां वरुणस्य च । उत्तरेण च सोमस्य तासां नामानि मे शरण
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3637)
- **Original**: 8 वस्वोकसारा झक्रस्य याम्या संयमनी तथा । पुरी सुख्वा जलेशस्य सोमस्य च विभावरी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3638)
- **Original**: 9 मैत्रेय भगवान्भानुज्योंतिषां चक्रसंयुतः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3639)
- **Original**: 10 अहोरात्रव्यवस्थानकारणं. भगवात्रवि: । देवयान: परः पन्था योगिनां ख्लेशस्बये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3640)
- **Original**: 29 दिवसस्य रविर्मध्ये सर्वकालं व्यवस्थित: । सर्वद्वीपेषु मैश्रेय निशार्ड्स्थ च सम्मुख:
- **Translation**: 

---

