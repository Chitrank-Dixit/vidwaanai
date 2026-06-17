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

### Verse 1 (Vishnu Puran 0.701)
- **Original**: हे द्विज ! समस्त भूतोंका चार प्रकारका प्रलू4 टै--मैमित्तिक, प्राकृतिक, आह्मन्तिक
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.702)
- **Original**: 533] श्रीकिष्णुपुरण [ अब 8 ब्राह्मो नेमित्तिकस्तत्र शेतेड्यं जगतीपति: । प्रयाति प्राकृते चैव ब्रह्माण्ड प्रकृते लयम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.703)
- **Original**: 42 ज्ञानादौत्यन्तिक: प्रोक्तो योगिनः परमात्मनि। नित्यः सदेव भूतानों यो विनाझ्ञो दिबानिशम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.704)
- **Original**: 43 प्रसूति: प्रकृतेर्या तु सा सृष्टि: प्राकृता स्मृता । दैनन्दिनी तथा प्रोक्ता यात्तरप्रलयादनु
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.705)
- **Original**: '4ड भूतान्यनुदिन॑ यत्र जायन्ते मुनिसत्तम। नित्यसर्गो हि स प्रोक्त: पुराणार्थविच्क्षण:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.706)
- **Original**: 45 एवं सर्वशरीरेषु. भगवान्भूतभावन: । संस्थित: कुरुते विष्णुरुत्पत्तिस्थितिसंयमान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.707)
- **Original**: । 46 सृष्टिस्थितिबिनाशारनां शक्तय: सर्वदेहिषु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.708)
- **Original**: वष्णव्य: परिकर्त्तन्ते मैत्रेयाहर्निशं समा:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.709)
- **Original**: 47 गुणनत्रयपर्य॑ ह्लोतदृह्मम्‌ शक्तित्र्य महत्‌ । और नित्य
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.710)
- **Original**: उनमेंसे नैमित्तिक अल्थ्यः रही ब्राह्म-अलय है, जिसमें जगत्पति ब्रह्माजी कल्पात्तमें शयन करते हैं; तथा प्राकृतिक प्रलयमें ब्रह्माण्ड प्रकृतिमें लोन हो जाता है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.711)
- **Original**: ज्ञानके द्वारा योगीका पंरमात्मामें ल्वैन हो जाना आस्यन्तिक प्रछूय है और रात-दिन जो भूतोंका क्षय होता है वही नित्य-प्रलय है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.712)
- **Original**: प्रकृतिसे महत्तत्त्वादि- क्रम्से जो सृध्दि होतो है वह प्राकृतिक सृष्टि कहल्त्रतीं है और अवाक्तर-प्रकूषके अनच्तर जो [जद्याकेः द्वारा] चराचर जगत्‌क़ो उत्पत्ति होती है कह दैनन्दिनी सृष्टि क्रहो जाती है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.713)
- **Original**: ओर हे मुनिश्रेष् ! जिसमें प्रतिदिन प्राणियॉकी उत्पत्ति होती रहती है उसे पुराणार्थमं कुशल सहानुभावोंनि नित्य-सष्टि कहा हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.714)
- **Original**: इस प्रकार समस्त दारोरमें स्थित भूतभावन भगवान्‌ विष्णु जगत्‌की उत्पत्ति, स्थिति और प्रकूय करते रहते हैं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.715)
- **Original**: है मैत्रेय ! सृष्टि, स्थिति और लिनाशकी इन वैष्णवी शक्तियोंका समस्त दारेरोंमे समान भावसे अहर्निश सझ्ार डोता रहता है
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.716)
- **Original**: हे ब्रह्मन्‌ ! ये तोनों महतो दाक्तियाँ परिगुणमयी हैं; अतः जो उन तीनों गुणोंका अतिक्रमण कर जाता है घट परमपदको ही प्राप्त-कर लेता यो5उतियाति स सात्येब परं नावर्त्तते पुन:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.717)
- **Original**: है, फिर जन्म-मरणादिके चक्रमें नहीं पड़ता
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.718)
- **Original**: _--__0%0-. जौ अन्‍लक--न इति श्रीविष्णुपुराणे प्रथमेंडशे सप्तपो5थ्यायः
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.719)
- **Original**: 0-+_>-+ जद अन्न आठवाँ अध्याय रौद्-सृष्टि और भगवान तथा लक्ष्मीजीकी सर्वव्यापकताका वर्णन श्रीप्रराश्र उवाच कथितस्तामसः सर्गो ब्रह्मणस्ते महामुने । रुद्टसर्ग प्रवक्ष्यामि तन्पे निगदत: श्रूणु
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.720)
- **Original**: 19 कल्पादावात्मनस्तुल्य॑ सुतं प्रध्यायतस्तत; । प्रादुरासीद्भभोरञ्ले कुमारो नीललोहित:
- **Translation**: 

---

