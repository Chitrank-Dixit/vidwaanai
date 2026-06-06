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

### Verse 1 (Vishnu Puran 0.741)
- **Original**: 17 अर्थो विष्णुरियं बाणी नीतिरेषा नयो हरि: । बोधो विष्णुरियं बुद्धिर्धमोञसो सत्क्रिया त्वियम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.742)
- **Original**: 18 सरष्टा विष्णुरियं सृष्टि: श्रीभूमिर्भूथरो हरिः । सनन्‍्तोषो भगवाललक्ष्मीस्तुष्टिमैत्रेय शाश्वती
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.743)
- **Original**: 19 इच्छा श्री्भगवान्कामो यज्ञोउसौ दक्षिणा त्वियम्‌ । आज्याहृतिरसो देवी पुरोडाझो जनार्दन:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.744)
- **Original**: 20 वि* पु0 2-- प्रथम अंझ 27 रोया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.745)
- **Original**: तब भगनान्‌ ब्रह्माजीने उसके सात नाम और रखे; तथा उन आठोंके स्थान, स्त्री और पुत्र भी निश्चित किये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.746)
- **Original**: द्वे द्विज ! प्रजापतिने उसे भव, शर्व, ईशान, पशुपति, भोम, उप्र और महादेव कहकर सम्बोधन किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.747)
- **Original**: यही उसके नाम रखे और इनके स्थान भी निश्चित किये। सूर्य, जलू, पृथिवी, वायु, अग्नि, आकादा, (यज्ञमें] दीक्षित ब्राह्मण और चन्द्रमा--ये क्रमदा: उनकी मूर्तियाँ हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.748)
- **Original**: हे द्विजश्रेष्ठ ! रुद्र आदि नामोकि साथ उन सूर्य आदि मूर्तियोंकी क्रमशः सुवर्चस्त, ऊषा, विकेशी, अपरा, शिखा, स्वाहा, दिदा, दीक्षा और रोहिणी नामकी पत्नियाँ हैं। हे महाभाग ! अब उनके पुत्रोंके नाम सुनो; उन्हींके पुन्र-पौत्रादिकोंसे यह सम्पूर्ण जगत्‌ परिपूर्ण है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.749)
- **Original**: झशनैश्वर, झुक्र, ल्लोहिताडु, सनोजथ, स्कन्द, सर्ग, सन्तान और बुध--ये क्रमद्ा: उनके पुत्र हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.750)
- **Original**: ऐसे भगवान्‌ रद्रने प्रजापति दक्षकी अनिन्दिता पुत्री सतीको अपनी भार्यारूपसे ग्रहण किया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.751)
- **Original**: हे द्विजसत्तम ! उस सतीने दक्षपर कुपित होनेके कारण अपना दारीर त्याग दिया था। फिर यह मेनाके गर्भसे हिमाचलकी पुत्री (उम्रा) हूई। भगवान्‌ शंकरने उस अनन्यपरायणा उमासे फिर भी विवाह किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.752)
- **Original**: भूगुके द्वारा ख्यातिने थाता और चलिखातानामक दो देखताओंको तथा लक्ष्मीजीकों जन्म दिया जो भगवान्‌ विष्णुकी पत्नी हुईं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.753)
- **Original**: आीपैत्रेबजी जोले--भगवन्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.754)
- **Original**: सुना जाता है कि लक्ष्मीजी तो अमृत-मन्थनके समय क्षीर-सागरसे उत्पन्न हुई थीं, फिर आप ऐसा कैसे कहते हैं कि वे भृगुके द्वारा ख्यातिसे उत्पन्न हुई
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.755)
- **Original**: भ्रीपराइरजी बोले--हे द्विजोत्तम ! भगवानका कभी संग न छोड़नेबाली जगज्जननी लश््मीजी तो नित्य ही हैं और जिस प्रकार श्रीविष्णुभगवान्‌ सर्वव्यापक हैं वैसे ही ये भी हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.756)
- **Original**: विष्णु अर्थ हैं और ये वाणी हैं, हरि नियम हैं और ये नीति हैं, भगवान्‌ विष्णु बोध हैं और ये बुद्धि हैं तथा के धर्म हैं और ये सत्क्रिया हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.757)
- **Original**: हे सैत्रेय ! भगवान्‌ जगतके स्रष्टा हैं और रूक्ष्मीजी सृष्टि हैं, श्रीहरि भूधर (पर्वत अथवा राजा) हैं और लक्ष्मोजी भूमि हैं तथा भगवान्‌ सन्तोष हैं और लक्ष्मीजी नित्प-तुष्टि हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.758)
- **Original**: भगतान्‌ काम हैं और लक्ष्मीजी इच्छा हैं, वे यज्ञ हैं और ये दक्षिणा हैं, श्रीजनार्दन पुरोडाश हैं और देवी
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.759)
- **Original**: 28 अ्रीकिष्णुपुराण [ आू & पत्नीशाल्ा मुने लक्ष्मी: प्राग्वंशो मधुसूदन: । चितिर्लक्ष्मीहीरियुप डृध्मा श्रीर्भगवान्कुशः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.760)
- **Original**: 219 सामस्वरूपी भगवानुद्वीति: कमलालया । स्वाहा लक्ष्मी्जगन्नाथो वासुदेवों हुताशन:
- **Translation**: 

---

