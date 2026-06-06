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

### Verse 1 (Vaivtpuran 543.15094)
- **Original**: मांसका सेबन करनेसे मनुष्य चाण्डाल-योनिमें बताती है; बह निश्चय ही कुम्भीपाकमें जाती है।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15095)
- **Original**: जन्म लेता है। रविवारको कॉँस्‍्यपात्रमें भोजन न वाणीद्वारा डाँट बतानेके कारण वह कौएकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15096)
- **Original**: करे। उस दिन मसूरकी दाल, अदरख और लाल योनिमें जन्म लेती है। हिंसा करनेसे सूअर होती
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15097)
- **Original**: रंगका शाक भी न खाय। ब्रजेश्वर! जो ब्राह्मण है। क्रोध करनेसे सर्पिणी और दर्प दिखानेसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15098)
- **Original**: रजस्वला और बेश्याके हाथका तथा मदिरामिश्रित गर्दभी होती है। कुवाक्य बोलनेसे कुछुरी और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15099)
- **Original**: अन्न खा लेता है; वह निश्चय ही मलभोजी जन्तु विष देनेसे अन्धी होती है। पतिब्रता स्त्री निश्चय
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15100)
- **Original**: होता है। बह उस दिन जो सत्कर्म करता है, ही पतिके साथ बैकुण्ठधाममें जाती है। जो मूढ़
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15101)
- **Original**: उसका फल उसे नहीं मिलता। वह सदा अपवित्र शिव, पार्वती, गणेश, सूर्य, ब्राह्मण, वैष्णव तथा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15102)
- **Original**: रहता है। उसका अशौच उसके मरनेके बाद ही विष्णुकी निन्‍्दा करता है; वह महारौरव नामक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15103)
- **Original**: समाप्त होता है। जिस स्त्रीने अपने जीवनमें चार नरकमें गिरता है। पिता, माता, पुत्र, सतो पत्नी,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15104)
- **Original**: पुरुषोंके साथ समागम कर लिया; उसे बेश्या गुरु, अनाथा स्त्री, बहिन और पुत्रीकी निन्‍दा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15105)
- **Original**: समझना चाहिये। वह देवताओं और पितरोंके करके मनुष्य नरकगामी होता है। जो क्षत्रिय,
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15106)
- **Original**: लिये भोजन बनानेकी अधिकारिणी नहीं है। वैश्य और शुद्र ब्राह्मणोंके प्रति भक्तिभावसे रहित जो प्रातःकाल और सायंकालकी संध्योपासना हैं और भगवद्धक्तिसे भी दूर हैं; वे निश्चय ही
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15107)
- **Original**: नहीं करता, उसका समस्त द्विजोचित कर्मोंसे नरकमें पकाये जाते हैं। यही दशा पतिभक्तिसे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15108)
- **Original**: शूद्रकी भाँति बहिष्कार कर देना चाहिये। संध्याहीन शून्य नराधमा स््रियोंकी होती है। द्विज नित्य अपवित्र तथा समस्त कर्मोंके लिये जो ब्राह्मण शालग्रामका चरणामृत पीते और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15109)
- **Original**: अयोग्य होता है। बह दिनमें जो सत्कर्म करता भगवान्‌ विष्णुका प्रसाद खाते हैं वे तीर्थोंकों भी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15110)
- **Original**: है; उसका फल उसे नहीं मिलता। राममन्त्रसे हीन पवित्र कर देते हैं। अपनी सौ पीढ़ियोंको तारते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15111)
- **Original**: ब्राह्मण नरकमें पड़ता है। नदीके बीचमें, गड्ठेमें, और पृथ्वोको भी उबारते हैं। जो भगवान्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15112)
- **Original**: वृक्षकी जड़में, पानीके निकट, देवताके समीप विष्णुका प्रसाद ग्रहण करता और मछली-मांस
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15113)
- **Original**: और खेतीसे भरी हुई भूमिपर समझदार मनुष्य नहीं खाता है; वह निश्चय ही पग-पगपर
- **Translation**: 

---

