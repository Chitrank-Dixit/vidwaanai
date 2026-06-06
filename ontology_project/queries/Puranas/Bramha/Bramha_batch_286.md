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

### Verse 1 (Bramha 0.5701)
- **Original**: और पृथ्बीको उत्पन्न करनेवाले तथा अविनाशी * मद्धक्ता: क्षत्रिया वैश्या: स्त्रिय: शुद्रान्यजातिजा:। प्राप्रुवन्ति पर सिर्ि कि पुनस्‍्त्व॑ द्विजोश्तम
- **Translation**: 

---

### Verse 2 (Bramha 0.5702)
- **Original**: श्रपाको5पि च मद्धक्त: सम्यक्‌ ब्रद्धासमन्वित:
- **Translation**: 

---

### Verse 3 (Bramha 0.5703)
- **Original**: प्राप्रोत्यभिपतां सिद्धिमन्येषां तज का कथा
- **Translation**: 

---

### Verse 4 (Bramha 0.5704)
- **Original**: (178। 185-186)
- **Translation**: 

---

### Verse 5 (Bramha 0.5705)
- **Original**: रछ्ड * संक्षिप्त ्रह्मपुराण « परमात्मा हैं। उन्होंने अपने दिव्य स्वरूपको
- **Translation**: 

---

### Verse 6 (Bramha 0.5706)
- **Original**: हैं, सृष्टि और संहारकों भी जिनका स्वरूप मनुष्योंके बौचमें कैसे प्रकट किया? जो भगवान्‌
- **Translation**: 

---

### Verse 7 (Bramha 0.5707)
- **Original**: बतलाया जाता है, उन आदिदेव परब्रह्म परमात्माको सम्पूर्ण जड्भम प्राणियोंकों गति हैं, वे मानव- मैं समाधिके द्वारा प्रणाम करता हूँ। जो सम्पूर्ण शरीरमें कैसे आये? इसे देवता और दैत्य भी बड़े
- **Translation**: 

---

### Verse 8 (Bramha 0.5708)
- **Original**: विकारोंसे रहित, शुद्ध, नित्य, सदा एकरूप आश्चर्यकी बात मानते हैं। महामुने! आप भगवान्‌
- **Translation**: 

---

### Verse 9 (Bramha 0.5709)
- **Original**: रहनेबवाले और विजयी हैं, उन परमात्मा श्रीविष्णुको विष्णुके आश्चर्यजनक अबतारकी कथा सुनाइये।
- **Translation**: 

---

### Verse 10 (Bramha 0.5710)
- **Original**: नमस्कार है। जो हिरण्यगर्भ, हरि, शंकर तथा भगवान्‌के बल और पराक्रम विख्यात हैं। उनके
- **Translation**: 

---

### Verse 11 (Bramha 0.5711)
- **Original**: बासुदेव कहलाते हैं, जिनसे समस्त प्राणियोंका तेजकी कोई माप नहीं है। वे अपने अलौकिक तरण-तारण होता है, जो सृष्टि, पालन और संहार चरित्रोंके द्वारा आश्चर्यरूप जान पड़ते हैं। आप
- **Translation**: 

---

### Verse 12 (Bramha 0.5712)
- **Original**: करनेवाले हैं, उन भगवानूको नमस्कार है। जो उनके तत्त्वका वर्णन कीजिये। भगवान्‌ पुरुषोत्तम
- **Translation**: 

---

### Verse 13 (Bramha 0.5713)
- **Original**: एक होते हुए भी अनेक रूपोंमें प्रकट होते हैं, देवताओंकी पीड़ा दूर करनेवाले और सर्वव्यापी
- **Translation**: 

---

### Verse 14 (Bramha 0.5714)
- **Original**: स्थूल और सूक्ष्म, व्यक और अव्यक्त जिनके हैं। जगत्के रक्षक और सर्वलोकमहेश्वर हैं। स्वरूप हैं और जो मोक्षके कारण हैं, उन संसारकी सृष्टि, पालन और संहार-सब वे ही
- **Translation**: 

---

### Verse 15 (Bramha 0.5715)
- **Original**: भगवान्‌ विष्णुकों नमस्कार है। जो जगन्मय हैं, करते हैं। वे ही सब लोकोंको सुख देनेवाले हैं।
- **Translation**: 

---

### Verse 16 (Bramha 0.5716)
- **Original**: जगत्‌की सृष्टि, पालन और संहारके मूल कारण ये अक्षय, सनातन, अनन्त, क्षय और बृद्धिसे
- **Translation**: 

---

### Verse 17 (Bramha 0.5717)
- **Original**: हैं, उन परमात्मा, भगवान्‌ विष्णुको नमस्कार है। रहित, निर्लेप, निर्गुण, सूक्ष्म, निर्विकार, निरझ्ञन,
- **Translation**: 

---

### Verse 18 (Bramha 0.5718)
- **Original**: जो सूक्ष्मसे भी सूक्ष्मतर, सम्पूर्ण विश्वेके आधारभूत, समस्त उपाधियोंसे रहित, सत्तामात्ररूपसे स्थित,
- **Translation**: 

---

### Verse 19 (Bramha 0.5719)
- **Original**: समस्त प्राणियोंक भीतर विराजमान और अपनी अविकारी, विभु, नित्य, अचल, निर्मल, व्यापक,
- **Translation**: 

---

### Verse 20 (Bramha 0.5720)
- **Original**: महिमासे कभी च्युत न होनेवाले हैं, उन भगवान्‌ नित्यतृप्त, निरामय तथा शाश्वत परमात्मा हैं।
- **Translation**: 

---

