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

### Verse 1 (Vishnu Puran 0.6961)
- **Original**: 250 अ्रीविष्णुपुराण [ अ0 4 रामोषपि बाल एव विश्वामित्रयागरक्षणाय गछछंस्ताटकां जघान
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6962)
- **Original**: यज्ञे च मारीच- प्रिषुवाताहते समुद्रे चिक्षेप
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6963)
- **Original**: सुबाहु- प्रमुस्यांश्व क्षयमनयत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6964)
- **Original**: दर्शनमात्रे- णाहल्यामपापाँ च्रकार
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6965)
- **Original**: जनकगूहे लऋ माहेश्व चापमनायासेन_ बभक्ञ
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6966)
- **Original**: सीतामयोनिजा जनकराजतनयां वीर्यशुल्कां लेभे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6967)
- **Original**: सकलक्षत्रियक्षयकारिणमशेष- हैहयकुलधूमकेतुभूते॑ च परशुराममपास्तवीर्य- बलावलेप॑ं चकार
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6968)
- **Original**: पितृबचनाध्ागणितराज्याभिलाषो . ्रातृ- भार्यासमेतो बने प्रविवेश
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6969)
- **Original**: विराधखर- दूषणादीन्‌ कबन्धवाल्लिनों च निजघान
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6970)
- **Original**: बद्धवा चाम्मोनिधिमशेषराक्षसकुलक्ष्य कृत्वा दक्षाननापहतां भारया तद्धधादपहतकलड्ढा- मप्यनलप्रवेदशुद्धामशेषदेबसब्लैः स्तृयमानझोल्लां जनकराजकन्यामयोध्यामानिन्ये
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6971)
- **Original**: _ तत- श्राभिषेकमड्डलं मैत्रेय वर्षशतेनापि वक्तु न दक्यते सद्ठेपेण श्रूयताम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6972)
- **Original**: लक्ष्यमणभरतशत्रुप्नविभीषणसुग्रीवाड्द- जाम्बवद्धनुमठ्मभृतिभिस्समुत्फुल्लवदनैरेछत्र- चामरादियुते:ः सेव्यमानो दाशरथिर्रहोद्धाप्रि- विश्वापरित्रभरद्वाजागस्त्यप्रभृतिभिर्मुनिवरे: ऋग्यजुस्सामाथर्वभिस्संस्तूयणमानो. नृत्यगीत- पटहशद्भुकाहलगो पुखप्रभृतिभिस्सुनादैस्समस्त- भूभृतां मध्ये सकललोकरक्षार्थ यथोचित- मभिषिक्तो दाशरथि: कोसलेद्रो रघुकुलतिलकों जानकीप्ियो भ्रातृत्रयप्रियस्सिंहासनगत एकादशाज्दसहस््न॑ राज्यपकरोत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6973)
- **Original**: इन चार रूपोंसे पुत्र-भावको प्राप्त हुए
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6974)
- **Original**: रामजीने गल्यावस्थामें ही विश्वामित्रजीकी यजञ्रक्षाके लिये जाते हुए मार्गमें ही ताटका राक्षसीक््रे माय, फिर यज्ञशाल्ममें पहुँचकर मारीयको बाणरूपी यायुसे आहत कर समुद्रमें फेंक दिया और सुबाहु आदि राक्षस्रोंक्रो नष्ट कर डाला
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6975)
- **Original**: 88--90
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6976)
- **Original**: उन्होंने अपने दर्शनमात्रसे अहल्याको निष्पाप क्रिया, जनकजीके राजभवनगें बिना श्रम ही सहादेवजीका घनुष तोड़ा और पुरुषार्थसे ही प्राप्त होनेवार्ली अयोनिजा जनकराजनन्दिनी श्रीसीताजीको पत्नीरूपसे प्राप्त किया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6977)
- **Original**: 29--93
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6978)
- **Original**: और तदनन्तर सम्पूर्ण क्षत्रियोंवत् परशुरामजीके बलू-वीर्यका गर्व नष्ट किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6979)
- **Original**: फिर पिताके वचनसे राज्यलक्ष्मीको कुछ भी न गिनकर भाई लक्ष्मण और धर्मपत्री सीताके सहित वनमें चले गये
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6980)
- **Original**: वहाँ विराध, खर, दूषण आदि राक्षस तथा कबन्ध और वालीका वध किया और समुद्रका पुल बाँघकर सम्पूर्ण राक्षसकुलका विध्व॑ंस किया तथा राबणद्वारा हरी हुई और उसके बधसे कलकूहोना होनेपर भो अग्नि-प्रवेशसे जुदू हुई समस्त देखगणोंसे प्रशस्तित स्वभाववाली अपनी भार्या जनकराजकन्या सीताकों अयोध्यामें ले आये
- **Translation**: 

---

