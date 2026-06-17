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

### Verse 1 (Rig Ved 0.281)
- **Original**: 126 अग्ने सुखतमे रथे देवा ईकित आ वह । असि होता मनुर्हित:
- **Translation**: 

---

### Verse 2 (Rig Ved 0.282)
- **Original**: मानवमात्र के हितैषी हे अग्निदेव ! आप अपने श्रेष्ठ - सुखदायी रथ से देवताओं को लेकर (यज्ञस्थल पर) पधारें । हम आपकी वन्दना करते हैं
- **Translation**: 

---

### Verse 3 (Rig Ved 0.283)
- **Original**: 127 स्तृणीत बर्हिरानुषग्‌ घृतपृष्ठं मनीधिण:। यत्रामृतस्थ चक्षणम्‌
- **Translation**: 

---

### Verse 4 (Rig Ved 0.284)
- **Original**: हे मेधावी पुरुषों ! आप इस यज्ञ में कुशा के आसनों को परस्पर मिलाकर इस तरह बिछाएँ कि उस पर घृत-पात्र को भली प्रकार रखा जा सके, जिससे अपृततुल्य घृत का सम्यक्‌ दर्शन हो सके
- **Translation**: 

---

### Verse 5 (Rig Ved 0.285)
- **Original**: 128. वि श्रयन्तामृतावृधो द्वारो देवीरसश्चत: । अद्या नून॑ च यष्टवे
- **Translation**: 

---

### Verse 6 (Rig Ved 0.286)
- **Original**: आज बच्ञ करने के लिए निश्चित रूप से ऋऋ्त (यज्ञीय वातावरण) की वृद्धि करने वाले अविनाशी दिव्य- द्वार खुल जाएँ
- **Translation**: 

---

### Verse 7 (Rig Ved 0.287)
- **Original**: 129. नक्तोषासा सुपेशसास्मिन्‌ यज्ञ उप हये। इदं नो बर्हिरासदे
- **Translation**: 

---

### Verse 8 (Rig Ved 0.288)
- **Original**: सुन्दर रूपवती रात्रि और उषा का हम इस यज्ञ में आवाहन करते हैं । हमारी ओर से आसन रूप में यह बर्हि (कुश) प्रस्तुत है
- **Translation**: 

---

### Verse 9 (Rig Ved 0.289)
- **Original**: 130. ता सुजिद्डा उप ह्ये होतारा दैव्या कवी
- **Translation**: 

---

### Verse 10 (Rig Ved 0.290)
- **Original**: यज्ञ नो यक्षतामिमम्‌
- **Translation**: 

---

### Verse 11 (Rig Ved 0.291)
- **Original**: उन उत्तम वचन वाले और मेधावी दोनों ( अग्नियों ) दिव्य होताओं को यज्ञ में यजन के निभित्त हम बुलाते हैं
- **Translation**: 

---

### Verse 12 (Rig Ved 0.292)
- **Original**: 131. इब्ठा सरस्वती मही तिस्रो देवीमयोभुव:। बर्हि: सीदन्त्वस्निधः
- **Translation**: 

---

### Verse 13 (Rig Ved 0.293)
- **Original**: इत्ठा, सरस्वती और मही ये तोनों देवियाँ सुखकारी और क्षयरहित हैं । ये तीनों बिछे हुए दीप्तिमान्‌ कुश के आसनों पर विराजमान हों
- **Translation**: 

---

### Verse 14 (Rig Ved 0.294)
- **Original**: 132. इह त्वाष्टारम्ग्रियं विश्वरूपमुप ह्ये। अस्माकमस्तु केवल:
- **Translation**: 

---

### Verse 15 (Rig Ved 0.295)
- **Original**: प्रथम पूज्य, विविध रूप वाले त्वष्टदेव का इस यज्ञ में आवाहन करते हैं, बे देव केवल हमारे ही हों
- **Translation**: 

---

### Verse 16 (Rig Ved 0.296)
- **Original**: 133. अब सृजा वनस्पते देव देवेभ्यो हवि:। प्र दातुरस्तु चेतनम्‌
- **Translation**: 

---

### Verse 17 (Rig Ved 0.297)
- **Original**: है वनस्पतिदेव ! आप देवों के लिए नित्य हविष्यानन प्रदान करने वाले दाता को प्राणरूप उत्साह प्रदान करें
- **Translation**: 

---

### Verse 18 (Rig Ved 0.298)
- **Original**: 134. स्वाहा यज्ञ कृणोतनेन्द्राय यज्वनो गृहे। तत्र देवाँ उप हये
- **Translation**: 

---

### Verse 19 (Rig Ved 0.299)
- **Original**: (है अध्वर्यु )) आप याजकों के घर में इन्द्रदेव की वुष्टि के लिये आहुतियाँ समर्पित करें । हम होता वहाँ देवों को आमन्नित करते हैं
- **Translation**: 

---

### Verse 20 (Rig Ved 0.300)
- **Original**: 56 ऋण्वेद संहिता भाग-9 ... [
- **Translation**: 

---

