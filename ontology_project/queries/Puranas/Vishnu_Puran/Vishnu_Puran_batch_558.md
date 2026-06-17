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

### Verse 1 (Vishnu Puran 0.11141)
- **Original**: वज्रचक्रकरी दृष्ठा. देवराजजनार्दनौ
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.11142)
- **Original**: 68 क्षिप्तं वश्रमथेन्रेण जग्राह भगवान्हरिः । न मुमोच तदा चक्र शक्रं तिष्ठेति चाब्रबीत्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.11143)
- **Original**: 69 प्रणष्रवरज्॑ देबेद्ूं. गरुडक्षतवाहनम्‌ । सत्यभामाब्रवीद्वीर॑. पल्लायनपरायणम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.11144)
- **Original**: 70 त्रक्लेक्येश न ते युक्ते शाचीभर्तु: पल्ायनम्‌। पारिजातस््रगाभोगा त्वामुपस्थास्यते झ़ची
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.11145)
- **Original**: 71 श्रीविष्णुपुराण
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.11146)
- **Original**: ( अ0 30 हुए शब्भध्वनि की और हजारों-लास्खों तीखे बाण छोड़े
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.11147)
- **Original**: इस प्रकार सम्पूर्ण दिशाओं और आक्य्द्को सैकड़ों बाणोंसे पूर्ण देख देखताओंने अनेकों अख-शख् छेड़े
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.11148)
- **Original**: त्रिलोकीके स्वामी श्रीमघुसूदनने देबताओंके छोड़े हुए प्रत्येक अख्न-शास््रके ल्वील्ससे ही हजारों टुकड़े कर दिये
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.11149)
- **Original**: सर्पाहारी गरुडने जलाधिपति वरुणके पाशको ख्लींचकर अपनी चॉँचसे सर्पके बच्चेके समान उसके कितने ही टुकड़े कर डाले
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.11150)
- **Original**: श्रीदेकको- नन्‍्दनने यमके फेंके हुए दण्डको अपनी गदासे खण्ड- खण्ड कर पृथित्रीप गिरा दिया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.11151)
- **Original**: कुबेरके विमानकों भगवानने सुदर्शनचक्रद्वाथ तिकू-तिक कर डाला और सूर्यको अपनी तेजोमय दृष्टिसे देस्खकर ही निस्तेज कर दिया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.11152)
- **Original**: भगवानने तदनन्तर व्राण बरसाकर अग्रिको शीतल कर दिया और बसुओंको दिदा-विदिज्ञाओमें भगा दिया तथा अपने चक्रसे त्रिशूलोंकी नॉंक काटकर रुद्गरगणको पृथिवीपर गिरा दिया
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.11153)
- **Original**: भगवानके चल्ये हुए बाणोंसे साध्यगण, विश्वेदेवगण, मरुद्रण और गन्धर्वगण सेमलकी रूईके समान आकाशतमें ही लीन हो गये
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.11154)
- **Original**: श्रीभगवानके साथ गरुडजी भी अपनी चॉंच, पद्ल और पजनॉसे देवताओंक्मे खाते, मारते और फाड़ते फिर रहे थे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.11155)
- **Original**: फिर जिस प्रकार दो मेघ जलूकी धाराएँ बरसाते हों उसी प्रकार देवराज इन्द्र और श्रीमधुसूदन एक दुसरेपर याण वरसाने लगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.11156)
- **Original**: उस युद्धमें गरुडजी ऐरावतके साथ और श्रीकृष्णचन्द्र इन्द्र तथा सम्पूर्ण देबताओंकि साथ लड़ रहे थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.11157)
- **Original**: सम्पूर्ण वाणोंके चूक, जाने और अख्न-शस्त्रोंक कट जानेपर इन्द्रने शीघतासे वद्ध और कृष्णने सुदर्शनचक्र हाथमें लिया
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.11158)
- **Original**: हे द्विजश्रेप्ठ ! उस समय सम्पूर्ण त्रिलोकीमें इन्द्र और कृष्णचन्द्रको क्रमश: वच्ञ और चक्र लिये हुए देखकर हाहाकार मच गया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.11159)
- **Original**: श्रीहरिने इन्द्रके छोड़े हुए वम्रको अपने हाथोंसे फ्कड़ लिया और स्वयं चक्र न छोड़कर इन्द्रसे कहा--' अरे, ठहर !'
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.11160)
- **Original**: इस प्रकार बज छिन जाने और अपने बाहन ऐग़बतके गरुडड्ारा क्षत-विक्षत हो जानेके कारण भागते हुए जोर इन्द्रसे सत्यभामाने कहा--
- **Translation**: 

---

