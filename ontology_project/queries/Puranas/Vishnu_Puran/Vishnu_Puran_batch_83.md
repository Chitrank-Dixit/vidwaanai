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

### Verse 1 (Vishnu Puran 0.1641)
- **Original**: 91 सैषा धात्री विधात्री च धारिणी पोषणी तथा । सर्वस्य तु ततः पृथ्वी विष्णुपादतलोझ्धवा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1642)
- **Original**: 92 एवं प्रभावस्स पृथुः पुत्रों वेनस्प वीर्यवान्‌ । जज्जे महीपति: पूर्वो राजाभूज़नरक्धनात्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1643)
- **Original**: 93 न तस्य दुष्कृतं किल्लित्फलदायि प्रजायते
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1644)
- **Original**: 94 दुस्स्वप्रोपशर्म नृणां भ्रृण्वतामेतदुत्तमम्‌ । पृथोर्जत्प प्रभावश्व करोति सतत नृणाम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1645)
- **Original**: 95 हे द्विजोत्तम ! जहाँ-जहाँ भूमि समतलः थी वहीं-वहींपर प्रजाने निवास करना पसन्द किया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1646)
- **Original**: उस समयतक प्रजाका आहार केवल फल मूल्मदि ही था; यह भी ओषधियेंकि नष्ट हो जानेसे बड़ा दुर्लभ हो गया था
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1647)
- **Original**: तब पृथिवीपति पृथुने स्वायम्मुबमनुको बछड़ा बनाकर अपने हाथमें ही पृथिवीसे फ्रजाके हितके लिये समस्त धान्योंकों दुहा । हे तात ! उसी अन्नके आधारसे अब भी सदा प्रजा जीवित रहती है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1648)
- **Original**: महाराज पृथु प्राणदान करनेके कारण भूमिके पिता हुए,” इसर्व्यि उस सर्वभूतधारिणीको 'पृथिवी' नाम मिला
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1649)
- **Original**: है मुने ! फिर देवता, मुनि, दैत्य, राक्षस, पर्वत, गन्धर्व, सर्प, यक्ष और पितृगण आदिने अपने-अपने पात्रोंमे अपना अभिमत दूध दुह्मा तथा दुहनेवालोंके अनुसार उनके सजातीय ही दोग्धा और वत्स आदि हुए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1650)
- **Original**: इसीलिये लिष्णुभगवान्‌के चरणोंसे प्रकट हुई यह पृथिवी ही सक्‍को जन्म देनेवाली, यनानेवाली तथा धारण और पोषण करनेवाली है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1651)
- **Original**: इस प्रकार पूर्वकालमें बेनके पुत्र महाराज पृथु ऐसे प्रभावशाली और बीर्यवान्‌ हुए। प्रजाका रक्कन करनेके कारण वे 'राजा' कहलाये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1652)
- **Original**: जो मनुष्य महाराज पृथुके इस चरित्रका कीर्तन करता है उसका कोई भी दुष्कर्म फरूदायी नहीं होता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1653)
- **Original**: पृथुका यह अत्वृत्तम जन्म-कृत्तानन और उनका प्रभाव अपने सुननेवाले पुरुषोकि दुःस्वप्नॉक्ये सर्वदा शान्‍्त कर देता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1654)
- **Original**: का 3 का इति श्रीविष्णुपुराणे प्रथमेंडशे त्रयोदशोउध्यायः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1655)
- **Original**: नलजज- जौ जीनत * जन्म देनेबाला, यज्ञोपवीत करानेवास्म्र, अन्नदाता, भयसे रक्षा करनेबात्म तथा जो बिद्यादान करे--ये पाँचों पिता जनकश्योपनेता च गश्ष विद्या: प्रयच्छति। अन्नदाता भयत्राता पश्नैते फ्तिरः स्पृताः
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1656)
- **Original**: अआ्श्ड)] अआन्ड ) आज अधम अंक छः 59 चोदहवाँ अध्याय प्राचीनवर्हिका जन्प और प्रचेताओंका भ्रगवदाराधन अऔरपरासर उवाच पृथोः पुत्रौ तु धर्मज्ञो जज़ातेउत्तर्द्धेवादिनौ । शिखण्डिनी हविर्धानमन्तर्धानाइयजायत।
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1657)
- **Original**: 9 हविर्धानात्‌ षडाग्रेयी घधिषणाउजनयत्सुतान्‌ त्राचीनबर्हिष शुक्र गये कृष्णं खुजाजिनो
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1658)
- **Original**: 2 प्राचीनबर्हिर्भगवान्यहानासी त्मजापति हविर्धानान्थहाभाग येन संवर्धिता: प्रजा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1659)
- **Original**: 3 प्राचीनाग्रा: कुशास्तस्य पृथिव्यां विश्लुता मुने । प्राचीनवर्हिरिभवत्ख्यातो भुवि महाबल:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1660)
- **Original**: 4 समुद्रतनयायां_ तु॒ कृतदारो महीपतिः
- **Translation**: 

---

