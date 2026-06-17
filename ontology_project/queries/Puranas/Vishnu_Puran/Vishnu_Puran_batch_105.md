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

### Verse 1 (Vishnu Puran 0.2081)
- **Original**: जो इस संसारमें समस्त प्राणियोंके प्रति समानचित्त और अपने समान ही दूसरोंके लिये भी परमप्रेमयुक्त थे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2082)
- **Original**: और जो परम घ॒र्मात्मा महापुरुष, सत्य एवं ज्ञर्य आदि गुणोंक्ती खानि तथा समस्त साधु-पुरुषोंके लिये उपमास्वरूप हुए थे
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2083)
- **Original**: इति श्रीविष्णुपुराणे प्रथमेंउशे पह्षदशो5ध्याय:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2084)
- **Original**: स-+>+ और
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2085)
- **Original**: थड श्रीविष्णुपुराण ( अ0 96 सोलहवाँ अध्याय नृसिंहावतारलिषयक प्रश्न श्रीमैत्रेय उवाच श्रीमैत्रेयजी बोले--आपने महात्मा मनुपुव्रोफे कथ्चितो भवता वंशों मानवानां महात्मनामू।
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2086)
- **Original**: वंशॉंका वर्णन किया और यह भी बताया कि इस जगतके कारणं चास्य जगतो लिष्णुरेब सनातनः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2087)
- **Original**: 91 यक्त्वेतद्‌ भगवानाह प्रह्मादं दैत्यसत्तमम्‌। दाह नाभिरनास्त्रेश्न क्षुण्णस्तत्वाज जीवितम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2088)
- **Original**: 2 जगाम वसुधा क्षोभ॑ यत्राव्धिसलिले स्थिते । पाहैर्बद्धे विच्ललति विक्षिप्राड़ै: समाहता
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2089)
- **Original**: हे शैलैराक्रान्तदेहोईपि न मसार च य: पुरा । त्वया चातीव माहात्ग्य॑ कथित यस्य धीमतः
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2090)
- **Original**: 4 तस्व प्रभावमतुलं विष्णोर्भक्तिमतो मुने । श्रोतुमिच्छामि यस्यैतशरित दीप़तेजस:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2091)
- **Original**: 5 किन्निमित्तमसौ शजस्त्रैविक्षिप्तो दितिजैर्मुने। किमर्थ चाब्यिसलिले विक्षिप्तो धर्मतत्पर:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2092)
- **Original**: 6 आक्रात्त: पर्वत: कस्माइष्टअैव महोरगेः । क्षिप्तःकिमद्रिशिखरात्किं वा पावकसझ्ये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2093)
- **Original**: 7 दिग्दन्तिनां दन्‍्तभूमिं स च कस्मान्निरूपित: । संशोषको5निलश्चास्य प्रयुक्त: किंमहासुरैः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2094)
- **Original**: 8 कृत्याँ च॒ दैत्यगुरवो युयुजुस्तत्र कि मुने । झम्बरज्षापि मायानां सहस््न॑ कि प्रयुक्तान्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2095)
- **Original**: .9 हालाहलं विषमहो दैत्यसूदैर्महात्मन: । कस्माछ्तं ब्रिनाशाब यज्जीर्ण तेन धीमता
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2096)
- **Original**: 90 एतत्सर्व॑_महाभाग प्रह्लादस्य महात्मन: । चरित॑ ओ्रोतुमिच्छामि पहामाहात््यसूचकम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2097)
- **Original**: 119 न हि कौतृहलं तत्र यहैत्यैन हतो हि सः । अनन्यमनसो विष्णो कः समर्थो निपातने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2098)
- **Original**: 12 तस्मिन्धर्मपपरे नित्य॑ केशवाराधनोद्मते । स्ववंदप्रभवै्दैत्यै: कृतो द्वेघो5तिदुष्कर:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2099)
- **Original**: 13 धर्मात्मनि महाभागे किष्णुभक्ते बिमत्सरे। दैतेयैः प्रहंत कस्मात्तन्ममाख्यातुमहसि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2100)
- **Original**: 14 सनातन कारण भगवान्‌ विष्णु ही हैं
- **Translation**: 

---

