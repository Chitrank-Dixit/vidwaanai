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

### Verse 1 (Vishnu Puran 0.4881)
- **Original**: 29 तस्य शिष्यास्तु ये पद्च तेवां नामानि मे शृणु । मुद्ल्लो गोमुखश्षैव वात्यइशालीय एव च । शरीर: पद्चमश्चासीन्पैत्रेय सुमहामति:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4882)
- **Original**: 22 संहितात्रितय॑ चक्रे झ्ाकपूर्णस्तथेतर: । निरुक्तमकरोत्तदचतुर्थ मुनिसत्तम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4883)
- **Original**: 23 क्रौज्धो वैताल्किस्तदद्वडलाकक्ष महामुनि: । निरुक्तकृचतुर्थो 5भूद्वेदवेदाड़॒पारग:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4884)
- **Original**: रेड इत्येता: प्रतिशाखाभ्यो हानुझाखा द्विजोत्तम
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4885)
- **Original**: बाष्कलश्ापरास्तिस्नस्संहिता:.. कृतवान्द्रिज । दिष्यः कालायनिर्गाग्यस्तृुतीयश्ष॒ कथाजब:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4886)
- **Original**: 25 श्रीविष्णुपुराण [आ5 शिष्य-परम्परासे ही जाकल्य वेदमित्रने उस सं॑हिताको पढ़ा और उसको पाँच अनुज्ञास््ाओमें विभक्त कर अपने पाँच विष्योंकों पढ़ाया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4887)
- **Original**: उसके जो पाँच शिष्य थे उनके नाम सुनो । हे मैत्रेय ! थे मुद्रल, गोमुख, बात्स्य और चझालीय तथा पाँचवें मतामति शरीर थे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4888)
- **Original**: है मुनिसत्तम ! उनके एक दूसरे शिष्य शाकपूर्णने तीन वेदसंहिताओंक्ी तथा चौथे एक निरुक्त-म्रन्थकी रचना की
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4889)
- **Original**: [उन संहिताओंका अध्ययन करनेयाले उनके ज्षिष्य] महामुनि क्रौक्ष, नैतालिक और बलाक थे तथा [निरुक्तका अध्ययन करनेवाले] एक चौथे शिष्य खेद- बेदाड़के पारगामी निरुक्तकार हुए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4890)
- **Original**: इस अकार वेदरूप खुक्षकी प्रतिशाखाओँसे अनुझाख्नाओंको उर्त्पत्ति हुई । हे द्विजोत्तम ! बाष्कलने और भी लीन संहिताओंकी रचना की
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4891)
- **Original**: उनके [उन संहिताओंको पढ़नेवाले] दिष्य काल्शायनि, गार्ग्य तथा कथाजब थे। इस प्रकार जिन्होंने इत्येते बहवृच्ा: प्रोक्ता: संहिता यै: प्रवर्तिता:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4892)
- **Original**: सेहिताओंको रचना को वे बहुबूच कहलाये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4893)
- **Original**: स्््िय् जौ हनन इति श्रीविष्णुपुराणे तृतीयेंडशों चतुर्थोंउध्याय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4894)
- **Original**: पाँचवाँ अध्याय शुछयजुर्लेद तथा तैत्तिरीय यजु:झाखाओंका वर्णन श्रीपराइर उताव यजुर्वेदतरोइशासास्सप्तविंशन्पहायुनि:. । वैज्ञम्पायननामासौ व्यासशिष्यश्रकार बै
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4895)
- **Original**: 1 किष्येभ्य: प्रददो ताश्व जगृहुस्तेउप्यनुक्रमात्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4896)
- **Original**: 2 याज्ञवल्क्यस्तु तत्राभूदह्ारातसुतो द्विज । ज्िष्य:. परमधर्मज्ञो गुरुवृत्तिपरस्सदा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4897)
- **Original**: 3 ऋषियों5हा महामेरों: समाजे नागमिष्यति । तस्य ले सप्तरात्रात्तु ब्रह्महत्या भविष्यति
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4898)
- **Original**: 4 पूर्वमेव॑ मुनिगणैस्समयो यः कृतों द्विज । वैज्ञप्पायन एकस्तु ते व्यतिक्रान्तवांस्तदा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4899)
- **Original**: 5 स्वस्रीयं बालक॑ सो5थ पदा स्पृष्टमघातयत्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4900)
- **Original**: 6 शिष्यानाह स भो श्षिष्या ब्रह्महत्यापहं त्रतम्‌ । चरध्व॑ मत्कृते सर्वे न विच्रार्यमिदं तथा
- **Translation**: 

---

