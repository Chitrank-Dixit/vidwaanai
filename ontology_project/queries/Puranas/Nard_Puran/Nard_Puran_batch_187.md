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

### Verse 1 (Nard Puran 224.3721)
- **Original**: ब्राह्मणोंको मिठाई और खीरका भोजन कराना चाहिये श्रेष्ठ द्विजोंके समाजमें, भगवान्‌ विष्णुके मन्दिस्में,
- **Translation**: 

---

### Verse 2 (Nard Puran 224.3722)
- **Original**: तथा भक्तिभावसे उन्हें दक्षिणा देनी चाहिये; क्योंकि मथुरा और प्रयागमें, पुरुषोत्तम जगननाथजीके समीप,
- **Translation**: 

---

### Verse 3 (Nard Puran 224.3723)
- **Original**: भगवान्‌ माधव भक्तिसे ही संतुष्ट होते हैं। जैसे सेतुबन्ध रामेश्वरमें, काझ्ली, द्वारका, हरद्धार और
- **Translation**: 

---

### Verse 4 (Nard Puran 224.3724)
- **Original**: नदियोंमें गड्ढा, सरोवरोंमें पुष्कर, पुरियोंमें काशीपुरी, कुशस्थलमें, त्रिपुष्कर तीर्थमें, किसी नदीके तटपर
- **Translation**: 

---

### Verse 5 (Nard Puran 224.3725)
- **Original**: पर्वतोंमें मेरु, तीनों देवताओंमें सबका पाप हरनेवाले अथवा जहाँ-कहीं भी भक्तिभावसे कोर्तन करता है,
- **Translation**: 

---

### Verse 6 (Nard Puran 224.3726)
- **Original**: भगवान्‌ नारायण, युगोंमें सत्ययुग, वेदोंमें सामजेद, वह सम्पूर्ण यज्ञों और तीर्थोंका महान्‌ फल पाता है।
- **Translation**: 

---

### Verse 7 (Nard Puran 224.3727)
- **Original**: पशुओंमें धेनु, वर्णांमें ब्राह्मण, देने योग्य तथा पोषक सम्पूर्ण दानों और समस्त तपस्याओंका भो पूरा-पूरा
- **Translation**: 

---

### Verse 8 (Nard Puran 224.3728)
- **Original**: बस्तुओंमें अन्न और जल, मासोमें मार्गशीर्ष, मृगोमे फल प्राप्त कर लेता है। जो उपवास करके या हविष्य
- **Translation**: 

---

### Verse 9 (Nard Puran 224.3729)
- **Original**: सिंह, देहधारियोंमें पुरुष, वृक्षोंमें पीपल, दैत्योंमें भोजन करके इद्धियोंकों काबूमें रखते हुए भगवान्‌
- **Translation**: 

---

### Verse 10 (Nard Puran 224.3730)
- **Original**: प्रह्मद, अज्ेंमें मुख, अश्वॉमें उच्नै:श्रवा, ऋतुओंमें नारायण या शिवकी भक्तिमें तत्पर हो इस पुराणका
- **Translation**: 

---

### Verse 11 (Nard Puran 224.3731)
- **Original**: वसन्त, यज्ञोंमें जपयज्ञ, नागोंमें शेष, पितरोंमें अर्यमा, श्रवण अथवा प्रवचन करता है, वह सिद्धि पाता है।
- **Translation**: 

---

### Verse 12 (Nard Puran 224.3732)
- **Original**: अस्त्रोंमें धनुष, वसुओंमें पावक, आदित्योंमें विष्णु, इस पुराणमें सब प्रकारके पुण्यों और सिद्धिबोंके
- **Translation**: 

---

### Verse 13 (Nard Puran 224.3733)
- **Original**: देवताओंमें इन्द्र, सिद्धोंमें कपिल, पुरोहितोंमें बृहस्पति, उद्धवका वर्णन किया गया है, जो सदा पढ़ने और
- **Translation**: 

---

### Verse 14 (Nard Puran 224.3734)
- **Original**: कवियोंमें शुक्राचार्य, पाण्डबोंमें अर्जुन, दास्य-भक्तोंमें सुननेवाले पुरुषोंके समस्त पापोंका नाश करनेवाला
- **Translation**: 

---

### Verse 15 (Nard Puran 224.3735)
- **Original**: हनुमान, तृणोंमें कुश, इन्द्रियोंमें मन (चित्त), गन्धवॉमें है। यह मनुष्योंके कलिसम्बन्धी दोषको हर लेता है
- **Translation**: 

---

### Verse 16 (Nard Puran 224.3736)
- **Original**: चित्ररथ, पुष्पोंगे कमल, अप्सराओंमें उर्वशी तथा और सब सम्पत्तियोंकों वृद्धि करता है। यह सभीको
- **Translation**: 

---

### Verse 17 (Nard Puran 224.3737)
- **Original**: धातुओंमें सुवर्ण श्रेष्ठ है। जिस प्रकार ये सब वस्तुएँ अभीष्ट है। यह तपस्या, ब्रत और उनके फलोंका
- **Translation**: 

---

### Verse 18 (Nard Puran 224.3738)
- **Original**: अपने सजातीय पदार्थों श्रेष्ठ हैं, उसी प्रकार प्रकाशक है। मन्त्र, यन्त्र, पृथक्‌ -पृथक्‌ वेदाक़,
- **Translation**: 

---

### Verse 19 (Nard Puran 224.3739)
- **Original**: पुराणोंमें श्रीनारदमहापुराण श्रेष्ठ कहा गया है। आगम, सांख्य और वेद-सबक्ा इसमें संक्षेपसे
- **Translation**: 

---

### Verse 20 (Nard Puran 224.3740)
- **Original**: द्विजवरों! आप सब लोगॉंको शान्ति प्रास हो, आपका संग्रह किया गया है। इस बेदसम्मित नारदीय
- **Translation**: 

---

