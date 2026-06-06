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

### Verse 1 (Vishnu Puran 0.8181)
- **Original**: स्वीकार कर लिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.8182)
- **Original**: इस प्रकार यवांतिके शापसे पोरवमेब बंशं समाश्रितवान्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.8183)
- **Original**: तुर्वसुके बंशने पुरुवंशका ही आश्रय ला
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.8184)
- **Original**: ्त्त्त्त् कै कतक्‍ततः इति श्रीविष्णुपुराणे चतुर्थेशे षोडशो5ध्यायः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.8185)
- **Original**: जी म्् सत्रहवाँ अध्याय डुब्यु-वंझ श्रीपराझर उवाच श्रीपराह्रजी बोले--ट्रुह्मुका पुत्र बभु था, बभुका दुल्लोस्तु तनयो बच्चु:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.8186)
- **Original**: वश्ोस्सेतु: 305.472:/ सेतु, सेतुका आरब्ध, आरब्धका गान्धार, गाखारका धर्म, सेतुपुत्र आरब्धनामा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.8187)
- **Original**: आरब्धस्य गाश्थारों गाव्धारस्थ धर्मों धर्माद्‌ घृतः घृतादू
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.8188)
- **Original**: के 17. 'ृतका दुर्दम, दुर्दमका प्रचेता तथा प्रचेताका दुर्दमस्तत: प्रचेता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.8189)
- **Original**: प्रचेतस: पुत्रइशतधर्मो
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.8190)
- **Original**: पुत्र शतधर्म था। इसने उत्तरवर्ती बहुत-से म्लेच्छोंका बहुलानां म्लेच्छानामुदीच्यानामाधिपत्यमकरोत्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.8191)
- **Original**: आधिपत्य किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.8192)
- **Original**: नक्सल, है 3 _83-+0_0>0_ इति श्रीविष्णुपुराणे चतुर्थेशे सप्तदशोध्यायः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.8193)
- **Original**: स्तन औ तत+ अठारहबाँ अध्याय अनुवंदा जीप ययातेश्षतपु्रस्यानोस्सभानलकश्ष:परमेषु- श्रीपराशरजी खोछे--ययातिके चौथे पुत्र अनुके संज्ञाख्रय: पुत्रा: बभूवु:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.8194)
- **Original**: सभानलपुत्र:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.8195)
- **Original**: सभानल, चक्षु और परमेषु नामक तीन पुत्र थे। कालानल:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.8196)
- **Original**: कालानल्ात्सूझ्य:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.8197)
- **Original**: सभानकका पुत्र काल्मनल हुआ तथा काल्थनलके सृझ्यात्‌ पुरञ्ञयः
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.8198)
- **Original**: पुरज्ञयाजनमेजय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.8199)
- **Original**: सुक्षय, सुझ्यके पुरक्षय, पुरक्रयके जनमेजय, जनमेजयके
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.8200)
- **Original**: 288 छः >> ञशविष्पुपरण # ु$"ुहतचु्ाः [आ0 98 श्रीविष्णुपुराण [ आऔ* 18 तस्माअहाशालः
- **Translation**: 

---

