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

### Verse 1 (Bramha 0.5881)
- **Original**: माता यशोदा थर्रा उठीं और श्रीकृष्णको शीघ्र ही और उन्हें सब प्रकारसे संतुष्ट किया। तत्पश्चात्‌
- **Translation**: 

---

### Verse 2 (Bramha 0.5882)
- **Original**: गोदमें उठाकर गायकी पूँछ घुमाने आदिके द्वारा यह अपने महलके भीतर चला गया। अपने बालकके ग्रह-दोषकों शान्त किया। नन्दने बन्धनसे मुक्त होनेपर वसुदेवजी नन्दके छकड़ेके
- **Translation**: 

---

### Verse 3 (Bramha 0.5883)
- **Original**: भी गायका गोबर ले श्रीकृष्णके मस्तकमें लगाया पास आये। नन्द बड़े प्रसन्न दिखायी दिये। मुझे
- **Translation**: 

---

### Verse 4 (Bramha 0.5884)
- **Original**: और उनको रक्षा करते हुए इस प्रकार बोले--' समस्त पुत्र हुआ है, यह सोचकर वे फूले नहीं समाते थे।
- **Translation**: 

---

### Verse 5 (Bramha 0.5885)
- **Original**: प्राणियोंकी उत्पत्ति करनेवाले भगवान्‌ श्रीहरि, बसुदेवजीने भी कहा--“बड़े सौभाग्यकी बात है
- **Translation**: 

---

### Verse 6 (Bramha 0.5886)
- **Original**: जिनके नाभिकमलसे सम्पूर्ण जगत्‌ उत्पन्न हुआ कि इस समय वृद्धावस्थामें आपको पुत्र हुआ है।
- **Translation**: 

---

### Verse 7 (Bramha 0.5887)
- **Original**: है, तुम्हारी रक्षा करें। जिनकी दाढ़के अग्रभागपर अब तो आपलोगोंने राजाका वार्षिक कर चुका
- **Translation**: 

---

### Verse 8 (Bramha 0.5888)
- **Original**: रखी हुई यह पृथ्वी सम्पूर्ण जगत्‌को धारण करती दिया होगा। जिसके लिये यहाँ आये थे, वह काम
- **Translation**: 

---

### Verse 9 (Bramha 0.5889)
- **Original**: है, वे वराहरूपधारी केशव तुम्हारी रक्षा करें। पूरा हो गया। यहाँ किसी श्रेष्ठ पुरुषको अधिक
- **Translation**: 

---

### Verse 10 (Bramha 0.5890)
- **Original**: तुम्हारे गुदाभाग और उदरकी रक्षा भगवान्‌ विष्णु नहीं ठहरना चाहिये। नन्दजी! जब कार्य हो गया,
- **Translation**: 

---

### Verse 11 (Bramha 0.5891)
- **Original**: तथा जल्डा और चरणोंकी रक्षा श्रीजनार्दन करें। तब आपलोग क्‍यों यहाँ बैठे हैं। शीघ्र ही अपने
- **Translation**: 

---

### Verse 12 (Bramha 0.5892)
- **Original**: जो एक ही क्षणमें वामनसे विराटू बन गये और गोकुलमें जाइये। वहाँ रोहिणीके गर्भसे उत्पन्न मेरा
- **Translation**: 

---

### Verse 13 (Bramha 0.5893)
- **Original**: तीन पगोंसे सारी त्रिलोकीकों नापकर नाना प्रकारके भी एक बालक है। उसका भी अपने ही पुत्रकी
- **Translation**: 

---

### Verse 14 (Bramha 0.5894)
- **Original**: अस्त्र-शस्त्रोंसे सम्पन्न दिखायी देने लगे, वे भाँति लालन-पालन कीजियेगा।' भगवान्‌ वामन तुम्हारी सदा रक्षा करें। तुम्हारे बसुदेवजीके यों कहनेपर नन्द आदि गोप
- **Translation**: 

---

### Verse 15 (Bramha 0.5895)
- **Original**: सिरकी गोविन्द तथा कण्ठकी केशव रक्षा करें। छकड़ोंपर सामान लादकर वहाँसे चल दिये।
- **Translation**: 

---

### Verse 16 (Bramha 0.5896)
- **Original**: मुख, बाहु, प्रबाहु (कोहनीके नीचेका भाग), मन उनके गोकुलमें रहते समय रातमें बालकोंकी
- **Translation**: 

---

### Verse 17 (Bramha 0.5897)
- **Original**: और सम्पूर्ण इच्धियोंकी अखण्ड ऐश्वर्यशाली अविनाशी हत्या करनेवाली पूतना आयी और सोये हुए।
- **Translation**: 

---

### Verse 18 (Bramha 0.5898)
- **Original**: भगवान्‌ नारायण रक्षा करें। भगवान्‌ वैकुण्ठ कृष्णको लेकर अपना स्तन पिलाने लगी। पूतना
- **Translation**: 

---

### Verse 19 (Bramha 0.5899)
- **Original**: दिशाओंमें, मधुसूदन विदिशाओं (कोणों)-में, रातमें जिस-जिसके मुखमें अपना स्तन डालती
- **Translation**: 

---

### Verse 20 (Bramha 0.5900)
- **Original**: इषोकेश आकाशमें और पृथ्वीको धारण करनेवाले थी, उस-उस बालकका शरीर क्षणभरमें निर्जीव
- **Translation**: 

---

