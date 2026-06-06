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

### Verse 1 (Vishnu Puran 0.12781)
- **Original**: 66 शक्रस्समस्तदेवेभ्यस्ततश्नाति प्रजापति: । हिरण्यगर्भोषपि ततः पुंस: शक्‍्त्युपलक्षित:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12782)
- **Original**: 67 एतान्यशेषरूपाणि तस्य रूपाणि पार्थिव
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12783)
- **Original**: यतस्तच्छक्तियोगेन युक्तानि नभसा यथा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12784)
- **Original**: 68 द्वितीयं विष्णुसंज्ञस्थ योगिध्येय॑ महामते । अमूर््त ब्रह्मणो रूपं यत्सदित्युच्यते बुध:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12785)
- **Original**: 69 समस्ता: दक्तयश्लैता नृप यत्र प्रतिष्ठिता: । तद्विश्ररूपवैरूप्य रूपमन्यद्धरेमहत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12786)
- **Original**: 70 समस्तझक्तिरूपाणि तत्करोति जनेश्वर । देवतिर्यइमनुष्यादिचेष्टावन्ति स्वल्लीलया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12787)
- **Original**: 79 जगतामृुपकाराय न सा कर्मनिमित्तजा । चेष्टा तस्थाप्रमेयस्य व्यापिन्यव्याहत्तात्मिका
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12788)
- **Original**: 72 तद्ग॒प॑ विश्वरूपस्थ तस्थ योगयुजा नृप। चिन्त्यमात्मविशुद्धर्थ सर्वकिल्ब्रिषनाशनम्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12789)
- **Original**: 73 यथाभिरुद्धतशिस्र: करे दहति सानिल: । तथा चित्तस्थितो विष्णुर्योगिनां सर्वकिल्बिषम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12790)
- **Original**: 74 तस्मात्समस्तशक्तीनामाधारे तत्र चेतस: । कुर्वीत संस्थितिं सा तु विज्ञेया शुद्धधारणा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12791)
- **Original**: 75 शुभाश्रयः स चित्तस्प सर्वगस्याचलात्मन: । त्रिभावभावनातीतो मुक्तये योगिनो नृप
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12792)
- **Original**: 76 घष्ठ अंधा 4751 किश्णुशक्ति परा है, क्षेत्रज्ञ नामक दाक्ति अपरा है और कर्म नामी तीसरी शक्ति अविद्या कहलाती है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12793)
- **Original**: हे राजन्‌ ! इस अखिट्या-पक्तिसि आवृत होकर यह सर्वगामिनी क्षेत्रज्ञ-दाक्ति सब प्रकारके अति बिस्तृत सांसारिक कष्ट भोगा करती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12794)
- **Original**: हे भूपाल ! अविद्या-झक्तिसे तिरेहित रहनेके कारण ही क्षेत्रज्ञशक्ति सम्पूर्ण प्राणियॉँमें तारतम्यसे दिखल्तयों देती है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12795)
- **Original**: यह सबसे कम जड़ पदार्थों है, उगसे अधिक वृक्ष- पर्वतादि स्थावरोमें, स्थावरोंसे अधिक सरीसूपादिमें और उनसे अधिक प्षियोंमें है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12796)
- **Original**: पक्षियोंसे मृगोंमें और मृगोंसे पशुओमें वह शक्ति अधिक है तथा पशुऑकी अपेक्षा मनुष्य भगवान्‌की उस (क्षेत्रज्) शक्तिसे अधिक प्रभावित हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12797)
- **Original**: मनुष्योंसे नाग, गन्धर्व और यक्ष आदि समस्त देवगणॉमें, देवताओंसे इन्द्रमें, इन्द्रसे अ्जापतिमें और प्रजापतिसे हिरण्यगर्भमें उस शक्तिका विशेष प्रकाज्ञ है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12798)
- **Original**: हे राजन ! ये सम्पूर्ण रूप उस परमेश्वरके हो शरोर हैं, क्योकि ये सब आकाशके समान उनकी उात्तिसे व्याप्त हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12799)
- **Original**: है महामते ! थिष्णु नामक बह्मका दूसरा अमूर्त (आकारहीन) रूप है, जिसका योगिजन ध्यान करते हैं और जिसे बुघजन 'सत्‌' कहकर पुकारते हैं
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12800)
- **Original**: है नूप ! जिसमें कि ये सम्पूर्ण झक्तियाँ प्रतिष्ठित हैं वही भगवान्‌का विश्वरूपसे विलक्षण द्वितीय रूप है
- **Translation**: 

---

