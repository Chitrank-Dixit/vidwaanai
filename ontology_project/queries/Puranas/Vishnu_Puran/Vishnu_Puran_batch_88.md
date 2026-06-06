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

### Verse 1 (Vishnu Puran 0.1741)
- **Original**: धर लअखीविष्युपुराण >> >> >> आः 18 श्रीविष्णुपुराण [ आ* 15 अऔप्राशर उवाच एवं प्रचेतसो विष्णु स्तुवन्तस्तत्समाधय: । दडवर्षसहस्नाणि. तपश्चेरुमहार्णवे..
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1742)
- **Original**: डड ततः प्रसन्नों भगवांस्तेषामन्तर्जले हरिः। ददौ.. दर्शनमुन्रिद्रनीकोत्यलदलच्छवि:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1743)
- **Original**: 45 पतल्रिराजमारूढमवल्लोक्य प्रचेतस: । प्रणिपेतु: शिरोभिस्तं भक्तिभारावनामितै:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1744)
- **Original**: 46 ततस्तानाह भगवान्त्रियतामीप्सितो बरः। प्रसादसुमुखो5ह॑ वो बरदः समुपस्थितः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1745)
- **Original**: 47 ततस्तमूचुर्वरद॑ प्रणिपत्य प्रचेतस: । यथा पित्रा समादिष्टं प्रजानां वृद्धकारणम्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1746)
- **Original**: 48 स चापि देबस्ते दत्वा यथाभिलबित॑ वरम्‌ । परमगण है, जो सर्वरूप और अनाधार है तथा जिढ़ा और दृष्टिका अविषय है, भगवान्‌ विष्णुके उस परमपदको हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1747)
- **Original**: श्रीपरादारजी खोले--इस प्रकार श्रीविष्णु- भगवानूमें समाधिस्थ होकर प्रचेताओने महासागरमें रहकर उनकी स्तुति करते हुए दस हजार वर्षतक तपस्या की
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1748)
- **Original**: तब भगवान्‌ श्रीहरिने प्रसन्न होकर उन्हें खिले हुए नील कमलकी-सी आभायुक्त दिव्य छविसे जलके भीतर ही दर्द्धन दिया
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1749)
- **Original**: प्रचेताओने पक्षिराज गरुड़पर चढ़े हुए श्रीहरिकों देखकर उन्हें भक्तिभावके भारसे झुके हुए मस्तकोंद्वारा प्रणाम किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1750)
- **Original**: तब भगवानने उनसे कहा--“मैं तुमसे प्रसन्न होकर तुष्हें वर देनेके छिये आया हूँ, तुप अपना अभीष्ट बर माँगा”
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1751)
- **Original**: तब प्रचेताओंने वरदायक श्रीहरिको प्रणाम कर, जिस प्रकार उनके पिताने उन्हें प्रजा-वृद्धिके लिये आज़ा दी थो यह सब उनसे नियेदन की
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1752)
- **Original**: तदनच्तर, भगवान्‌ उन्हें अभीष्ट बर देकर अन्तर्धान हो गये अन्तर्धाने जगामाशु ते च निश्चक्रमुर्जलात्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1753)
- **Original**: और वे जलसे बाहर निकल आये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1754)
- **Original**: न फ पता इति श्रीविष्णुपुराणे प्रथमेंडशों चतुर्दशोउघ्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1755)
- **Original**: ऋणष0000-: नूर पतन पन्द्रहवाँ अध्याय अ्च्ेताओंका मारिषा नामक कन्याके साथ विवाह, दक्ष प्रजापतिकी उत्पत्ति एवं दक्षकी आठ कन्याओंके वंशका वर्णन औपरादर उवाच श्रीपराह्ररजी बोले--अचेताओंके तपस्पामें छगे तपश्चरत्सु पृथियीं प्रचेतःसु महीरुहा:।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1756)
- **Original**: रहनेसे [ कृषि आदिद्वारा ] किसी प्रकारकी रक्षा न होनेके अरक्ष्यमाणामावल्रुर्बभूवाथ प्रजाक्षय:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1757)
- **Original**: कारण पृथिवीको वृक्षेनर ठैंक लिया और प्रजा बहुत कुछ भांसकनारतो , नष्ट हो गयी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1758)
- **Original**: आकाश वृक्षोंसे भर गया था। दहावर्षसहस्नाणि बा चूत समघवदह । कर इसलिये दस हजार वर्षतक न तो वायु ही चलता और न शेकुश्चेष्टितु * प्रजा ही किसी प्रकास्की चेश कर सकी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1759)
- **Original**: जल्से तान्‍्दूद्वा जलनिष्क्रान्ता: सर्वे क्ुद्धा: फ्रत्ेतस: ।
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1760)
- **Original**: निकलनेपर उन वृक्षोंको देखकर प्रचेतागण अति क्रोघित मुखेभ्यो वायुमर च तेउसृजन्‌ जातमन्यवः
- **Translation**: 

---

