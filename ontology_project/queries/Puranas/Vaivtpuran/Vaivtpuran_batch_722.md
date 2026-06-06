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

### Verse 1 (Vaivtpuran 543.12754)
- **Original**: * भ्रीकृष्णजन्मखण्ड * 559 ##%#%%%#%##%###### ## #ऋ # कक 436440400400%00000000200400000404040400000000000000 0 40 000400 0400 00004 8
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12755)
- **Original**: 008 6 4
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12756)
- **Original**: 4 44 4 4 4.4 4. गड्भाकी जो धारा पाताललोकको जाती है,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12757)
- **Original**: रहती हैं। मेरी इस पुत्रीका विनाश प्रलयकालमें उसका नाम भोगवती है। वह सदा दुग्ध-फेनके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12758)
- **Original**: भी नहीं होता। उसका परम मनोहर दिव्य तट समान स्वच्छ तथा अत्यन्त वेगवती है। अमूल्य
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12759)
- **Original**: नाना रत्नोंकी खान है। इस प्रकार गज्गजाके जन्मका रत्नों तथा श्रेष्ठ मणियोंकी वह सदा खान बनी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12760)
- **Original**: सारा पुण्यदायक प्रसज् मैंने कह सुनाया। अब रहती है। सुस्थिर यौवनवाली नागकन्याएँ उसके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12761)
- **Original**: ब्रह्माजीको मोहिनीके शापसे किस प्रकार छुटकारा तटपर सदा ही क्रौड़ा करती हैं। स्वयं देवी गड्भा
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12762)
- **Original**: मिला, यह सुनो। वैकुण्ठको चारों ओरसे घेरकर सदा प्रवाहित होती (अध्याय 34) >>“ फसचरथर/ज> गड्जा-स््रानसे ब्रह्माजीको मिले हुए शापकी निवृत्ति, गोलोकमें ब्रह्माजीको भारतीकी प्राप्ति, भारतीसहित ब्रह्माका अपने लोकमें प्रवेश, भगवान्‌ शिवके दर्पभड्गकी कथा, वृकासुरसे उनकीं रक्षा, श्रीराधिकाके पूछनेपर श्रीकृष्णके द्वारा शिवके तत्त्व-रहस्यका निरूपण भगवान्‌ श्रीकृष्ण कहते हैं--प्रिये ! तदनन्तर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12763)
- **Original**: गड्भाके जलमें स्नान किया और मुझे प्रणाम करके सबने गड्भाको देखकर मेरी माया मानी। उस
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12764)
- **Original**: वे शीघ्र ही गोलोककों चले गये। फिर समस्त समय नारायणने कृपापूर्वक ब्रह्माजीसे कहा।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12765)
- **Original**: देवता और मुनि भी प्रसन्नतापूर्वक अपने-अपने श्रीनारायण बोले--चतुर्मुख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12766)
- **Original**: ! उठो, जाओ,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12767)
- **Original**: स्थानको लौट गये। वे बारंबार मेरे परम निर्मल तुम्हारा कल्याण होगा। तुम्हें शाप लगा है; अत:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12768)
- **Original**: यशका गान कर रहे थे। ब्रह्माजीने गोलोकमें मेरी आज्ञासे इस गड्जामें स्नान करके पवित्र हो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12769)
- **Original**: जाकर मेरे मुखारविन्दसे निर्गत, सम्पूर्ण विद्याओंकी जाओ। यद्यपि तुम स्वयं पवित्र हो और वे समस्त
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12770)
- **Original**: अधिदेवी सती भारतीको प्राप्त किया। वागीश्वरी तीर्थ तुम वैष्णवपतिका स्पर्श प्राप्त करना चाहते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12771)
- **Original**: भारतीकों पाकर उन्हें बड़ी प्रसन्नता हुई। उन हैं, तथापि प्रकृतिकी अवहेलना करने (हँसी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12772)
- **Original**: त्रिभुवनमोहिनी देवीकों प्राप्त करके मुझे प्रणाम उड़ाने)- से तुम्हें शाप मिला है। अहंकार सभीके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12773)
- **Original**: करनेके अनन्तर वे लौट आये। ब्रह्मलोकके लिये पापोंका बीज और अमड्गलकारी होता है।
- **Translation**: 

---

