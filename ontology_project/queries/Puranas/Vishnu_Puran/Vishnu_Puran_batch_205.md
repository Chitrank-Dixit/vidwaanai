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

### Verse 1 (Vishnu Puran 0.4081)
- **Original**: 33 पुच्छेउग्रिश्न महेन्द्रक्ष कश्यपो5ध ततो धुत: । तारका शिशुमारस्यथ नास्तमेति चतुष्टयम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4082)
- **Original**: 34 इत्येष सन्निवेशो5यं पृथिव्या ज्योतिषां तथा । द्वीपानामुदधीनां चर पर्वतानां च कीर्तित:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4083)
- **Original**: 35 वर्षाणां च नदीनां च ये च तेषु बसन्ति वै । तेषां स्वरूपमाख्यात॑ सद्लेपः श्रूयतां पुनः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4084)
- **Original**: 36 यदम्बु वैष्णव: कायस्ततो विप्र वसुन्धरा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4085)
- **Original**: पद्माकारा समुद्धूता पर्वताव्ध्यादिसंयुता
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4086)
- **Original**: ज्योतीषि विष्णुर्भुवनानि विष्णु- 4. सबक पे इसका दिशक्ष । नहा: समुद्राश स एव यदस्ति यन्नास्ति च विप्रवर्य
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4087)
- **Original**: 38 ज्ञानस्वरूपो श भगवान्यतो5सा- तु वस्तुभूतः । द्वितीय अंश श्डण हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4088)
- **Original**: हे मैत्रेय ! समस्त ग्रह, नक्षत्र और तारामण्डल खायुमयी रखुसे धुवके साथ बैंधे हुए यथोचित प्रकारसे घूमते रहते हैं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4089)
- **Original**: जितने तारागण हैं उतनी ही वायुमयी डोरियाँ हैं। उससे बैंधकर वे सब स्वयं घूमते तथा ध्रुबको धभुपाते रहते हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4090)
- **Original**: जिस प्रकार तेली ल्पेग ख्ये घूमते हुए कोल्हूको भी घुमाते रहते हैं उसी प्रकार समस्त य्रहगण वायुसे बैध कर घूमते रहते है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4091)
- **Original**: क्योंकि इस वायुचक्रसे प्रेरित होकर समस्त ग्रहगण अल्मतचक्र (बनैती) के समान घूषा करते हैं, इसलिये यह 'प्रवह' कहलाता है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4092)
- **Original**: जिस शिशुमारचक्रका पहले वर्णन कर चुके हैं, तथा जहाँ चरुव स्थित है, हे मुनिश्रेहठ ! अब तुम उसकी स्थितिका सर्णन सुनो
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4093)
- **Original**: रात्रिके समय उनका दर्शन करनेसे मनुष्य दिनमें जो कुछ पापकर्म करता है उनसे मुक्त हो जाता है तथा आक्राञ्ममण्डलमें जितने तारे इसके आश्रित हैं उतने ही अधिक यर्ष वह जीवित रहता है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4094)
- **Original**: उत्तानपाद उसकी ऊपरकी हनु (ठोड़ी) है और यज्ञ नीचेकी तथा घर्मने उसके मस्तक्पर अधिकार कर रख्या है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4095)
- **Original**: उसके दृदय-देक्षमें नारायण हैं, दोनों चरणोंमें अश्विनीकुमार हैं तथा जंघाओंमें वरूण और अर्यमा हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4096)
- **Original**: संवत्सर उसका खिश्र है, मित्रने उसके अपान-देशको आश्रित कर रखा है, तथा अग्रि, महेन्द्र, कद्यप और धुव पुच्छभागमें स्थित हैं। शिश्षुमास्के पुच्छभागमें स्थित ये अग्रि आदि चार तारे कभी अस्त नहीं होते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4097)
- **Original**: इस प्रकार मैंने तुमसे पृथियो, ग्रहगण, ड्रीप, सम्तुद, पर्वत, वर्ष और नदियोंका तथा जो-जो उनमें बसते हैं उन सभीके स्वरूपका वर्णन कर दिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4098)
- **Original**: अब इसे संक्षेपसे फिर सुनो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4099)
- **Original**: 35- 26
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4100)
- **Original**: है त्रिप्र ! भगवान्‌ विष्णुका जो मूर्तरूप जल है उससे पर्बत और समुद्रादिकि सहित कमलके समान आकारवाली पृथिवी उतान्न हुई
- **Translation**: 

---

