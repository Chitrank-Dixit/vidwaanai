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

### Verse 1 (Vishnu Puran 0.1701)
- **Original**: है मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1702)
- **Original**: सर्वलोकाश्रय जगत्पति श्रीनारायणमें चित्त लगाये हुए उन्होंने दस हजार बर्षतक वहीं (जलमें ही) स्थित रहकर देवाधिदेव श्रीहरिको एकाग्र-चित्तसे स्तुति की, जो अपनी स्तुति की जानेपर स्तुति करनेवाल्त्रेंकी सभी कामनाएँ सफल कर देते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1703)
- **Original**: अमैत्रेयजी बोले--हे मुनिश्रेष्ठ ! समुद्रके जरूमें स्थित रहकर प्रचेताओने भगवान्‌ विष्णुकी जो अति पवित्र स्तुति की थी कह कृपया मुझसे कहिये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1704)
- **Original**: ओपराशरजी खोल्हे--हे मैत्रेय ! पूर्वकालमें समुद्रमे,ं स्थित रहकर भ्रचेताओंने तत्मय-भावसे श्रीगोविन्दको जो स्तुति की, वह सुनो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1705)
- **Original**: अ्रल्लेताओंने कहा--जिनमें सम्पूर्ण वाक्योंकी नित्य-प्रतिष्ठा है [ अर्थात्‌ जो सम्पूर्ण वाक्योंके एकमात्र अतिपाद्य हैं] तथा जो जगत्क़ी उत्पत्ति और प्रल्यके कारण हैं उन निश्चिल-जगन्नायक परमप्रभुकों हम नमस्कार करते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1706)
- **Original**: जो आद्य ज्योतिस्स्वरूप, अनुपम, अणु, अनन्त, अपार और समस्त चराचरके कारण हैं, तथा जिन रूपहीन परमेश्वरके दिन, रात्रि और सख्या ही प्रथम रूप हैं, उन कालस्वरूप भगवान्‌कों नमस्कार है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1707)
- **Original**: 24-207
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1708)
- **Original**: समस्त प्राणियोंके जीवनरूप जिनके अपृतमय स्वरूपको देव और पितृगण नित्यप्रति भोगते है--उन सोमस्वरूप प्रभुको नमस्कार है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1709)
- **Original**: जो तोश्णस्वरूप अपने तेजसे आकाद्ममण्डलको प्रकाशित करते हुए अन्धकारक्म भक्षण कर जाते हैं तथा जो घाम, झीत और जलके ठद्गमस्थान हैं उन सूर्यस्वरूप
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1710)
- **Original**: अ« शड ] काठिन्यवान्‌ यो बिभर््ति जगदेतदशेषतः । शब्दादिसंश्रयो व्यापी तस्मै भूम्यात्यने नमः ।! 28 यद्योनिभूत॑ जगतो बीजं यत्सर्वदेहिनाम्‌। तत्तोयरूपमीझस्थ नमामो हरिमेश्वसः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1711)
- **Original**: 29 यो मुख सर्वदेवानां हव्यभुक्कव्यभुक्‌ तथा । पितृणां च नमस्तस्मै विष्णवे पावकात्मने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1712)
- **Original**: 30 पश्चधावस्थितो देहे यश्चेष्टां कुरुतेडनिशम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1713)
- **Original**: आकाशञयोनिर्भगवांस्तस्मै वाय्वात्मने नमः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1714)
- **Original**: 39 अवकाहशमशोषाणां भूतानां यः प्रयच्छति । अनन्तमूर्तिमाउछुद्धस्तस्मै व्योमात्मने नमः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1715)
- **Original**: 32 समस्तेन्द्रिबसर्गस्य यः सदा स्थानमुत्तमम्‌ तस्मै शब्दादिरूपाय नमः कृष्णाय बेधसे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1716)
- **Original**: 33 गृह्लाति विषयाज्नित्यमिच्ियात्मा क्षराक्षरः । अस्तस्मै ज्ञानपूलाय नता: सम हरिमेधसे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1717)
- **Original**: 34 गृहीतानिन्द्रियैरर्थानात्मने यः प्रयच्छति । अन्त:करणरूपाय तस्मै विश्वात्मने नमः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1718)
- **Original**: 35 अस्मिन्ननन्ते सकल विश्व यस्मात्तथोद्गतम्‌ । लबस्थान॑ च यस्तस्पै नमः प्रकृतिधर्मिणे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1719)
- **Original**: 36 मसकपण देव पता; अ पुणगनमरा सैल्लक्ष्यते भ्रान्या गुणवानिव यो5गुण: । जा रन बुकलेक्त
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1720)
- **Original**: 37 दम न पक्के के ँ नताः स्म तत्पर ब्र कदम
- **Translation**: 

---

