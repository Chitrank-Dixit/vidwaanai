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

### Verse 1 (Vishnu Puran 0.13501)
- **Original**: य्वोतमेतओत॑ च 27704 780 942 यतिसु एन्प॑ मैष्छत्‌ 4. 10 2
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.13502)
- **Original**: च्वोतमेतलोत॑ च “0. 6 197 8<8दे ++. 3 318... 25
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.13503)
- **Original**: यर्थवपृत॒च्मितति गा यो धूकन्यपेदणि 3. 17 12
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.13504)
- **Original**: यय सभिध्रिसत्रेण न. ह रे 8 5-30 यहो बृज्णिसंक्रम्‌ “.. 4 211... 28 यकयुए यदैवेसु: 5, बे*.. 047 चतो हि स्का: ».. 48 15- . डेंड
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.13505)
- **Original**: यथा केशिप्कजे प्राद 6।#हक जताते अतः काण्यायना द्विजः 4 169. 32
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.13506)
- **Original**: यथाचपादयोपूछः 2 87:08 रेरे यतः काण्वाधताः 4 19: --7
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.13507)
- **Original**: यथा सपर्ज देवोझसौ 306 क्09 यत_ः कुरल्षित्सप्पाप्य 3... रै4 28
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.13508)
- **Original**: यधा च वर्णानसूजत्‌ 3 #9>7 कृफ़ारे यतः सा फवताकलम्‌ 2 < - 122
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.13509)
- **Original**: यवाककथितो देपैः 24 +4 हा 97रें5 यतः प्रधानफ़ुषो + 9 17... 30
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.13510)
- **Original**: ययाभिकम्छठान्‌ 504 रैंड रे अतः सह ठतो लक्ष्मी: है... - 29
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.13511)
- **Original**: यथा चायधने तस्य 2 018-- 556 यत्कि्टित्मृन्यते येन है...23 . 38
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.13512)
- **Original**: वयास्फिदर्तशिलः 6 7878 हट यत्किड्विनानसा ब्राह्मण है... 4. -- 69
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.13513)
- **Original**: यया गह्ेतामम्भोधे 5 35. 8 तरेंडे यह्ते दश्ञभिर्व 6-2. 8 65
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.13514)
- **Original**: यथा यथा प्रसप्रोध्सी 5738 0575 सत्तस्पाईप्णव तेज: 3.02 50
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.13515)
- **Original**: यधाईमस्प कोक्स्‍्य 658 5 6 73 ऐ8 यक्तदव्यक्तमजरम्‌ & 5. 466
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.13516)
- **Original**: यदाहि कदरीनात्या 1 713:8-5 907 अतु किष्माशते कार्षम्‌ है. 14 ... “22
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.13517)
- **Original**: यया सूर्यस्य मैपेय 2 15 «139 सतु सम्प्रणोक्रापि 2. 136. 2100
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.13518)
- **Original**: यश सवें। पूरे है है8:-- 7 डें0 सु मेफे: समुस्यृष्टभ्‌ 2.6... 368
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.13519)
- **Original**: यफा संगत विष्णुम्‌ है (8-70 क डे: दवु पृथप्स मूजल 3:47 <
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.13520)
- **Original**: झथाते तिस चेतः 180 दे08- 4628 यल्यया प्राध्की स्थनम्‌ 1 62... 82
- **Translation**: 

---

