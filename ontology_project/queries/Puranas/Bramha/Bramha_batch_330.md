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

### Verse 1 (Bramha 0.6581)
- **Original**: समय महात्मा बलरामजीके क्रोधकों बढ़ाती हुई और उस कन्याने भी श्रीहरिके पुत्र प्रद्युन्ननाकों' आकाशवाणी हुई--“जीत तो बलदेवजीकी ही हुई स्वयंवरमें ग्रहण किया। उसके गर्भसे प्रद्यु्नजीके
- **Translation**: 

---

### Verse 2 (Bramha 0.6582)
- **Original**: है। रुक्मी झूठ बोलता है। मुँहसे अनुमोदनसूचक अनिरुद्ध नामक पुत्र हुआ, जो महाबली, महापयाक्रमी,
- **Translation**: 

---

### Verse 3 (Bramha 0.6583)
- **Original**: वचन न करनेपर भी जो उसने दाँवको स्वीकार युद्धपें कभी रुद्ध (कुण्ठित) न होतेवाला, बलका करके पासा फेंका है, इस कर्मसे उसका अनुमोदन समुद्र तथा शत्रुओंका दमन करनेवाला था। अनिरुद्धको
- **Translation**: 

---

### Verse 4 (Bramha 0.6584)
- **Original**: सिद्ध हो जाता है।' भी रुक्मीकी पौत्रीने वरण किया। यद्यपि रुक्मी
- **Translation**: 

---

### Verse 5 (Bramha 0.6585)
- **Original**: इतना सुनते ही बलगमजी क्रोधसे लाल श्रीकृष्णेके साथ लाग-डॉट रखता था तो भी उसने , आँखें करके उठ खड़े हुए। उन्होंने जूआ खेलनेके अपने दौहित्र अनिरुद्धके साथ पौत्रोका विवाह कर
- **Translation**: 

---

### Verse 6 (Bramha 0.6586)
- **Original**: पासेसे ही रुक्मीको मौतके घाट उतार दिया। फिर दिया। उस बिबाहमें बलराम आदि यदुबंशी श्रोकृष्णके
- **Translation**: 

---

### Verse 7 (Bramha 0.6587)
- **Original**: काँपते हुए कलिब्जराजकों बलपूर्वक धर दबाया साथ रुक्मीके भोजकट नगरमें गये थे। विवाह हो
- **Translation**: 

---

### Verse 8 (Bramha 0.6588)
- **Original**: और जिन्हें दिखा-दिखाकर बह हँसता था, उन जानेपर कलिक़्राज आदिने रुक्मोसे कहा--' राजन!
- **Translation**: 

---

### Verse 9 (Bramha 0.6589)
- **Original**: दाँतोंको कुपित होकर तोड़ डाला। फिर सभाभवनके बलराम जुआ खेलना नहों जानते, तथापि उन्हें
- **Translation**: 

---

### Verse 10 (Bramha 0.6590)
- **Original**: सुबर्णमय बिशाल स्तम्भकों खाँच लिया और जुएका बड़ा भारी व्यसन है; अत: आज हमलोग , क्रोधमें आकर रुक्मीके पक्षमें आये हुए समस्त उनको जुएसे हो परास्त करें।' “बहुत अच्छा'
- **Translation**: 

---

### Verse 11 (Bramha 0.6591)
- **Original**: राजाओंका संहार कर डाला। बलरामजीके कुपित कहकर रुक्मीने सभामें बलरामजीके साथ जुएका
- **Translation**: 

---

### Verse 12 (Bramha 0.6592)
- **Original**: होनेपर सम्पूर्ण राजालोग हाहाकार करते हुए भाग खेल प्रारम्भ किया। पहले ही दाँवमें बलभद्रजी
- **Translation**: 

---

### Verse 13 (Bramha 0.6593)
- **Original**: खड़े हुए। बलरामजोके द्वारा रुक्मीकों मारा गया एक हजार स्वर्ण॑मुद्रा हार गये। उसके बाद भो कई
- **Translation**: 

---

### Verse 14 (Bramha 0.6594)
- **Original**: सुनकर श्रीकृष्ण चुप रहे। रुक्मिणी और बलराम यार उनकी हार हुई। यह देख मूर्ख कलिज्गराज दाँत
- **Translation**: 

---

### Verse 15 (Bramha 0.6595)
- **Original**: दोनोंके संकोचसे वे कुछ बोल न सके। तदनन्तर दिखाते हुए बलरशामजींका उपहास करने लगा।
- **Translation**: 

---

### Verse 16 (Bramha 0.6596)
- **Original**: विवाहके बाद भगवान्‌ श्रीकृष्ण अनिरुद्धसहित मदोन्‍्मत्त रुकमीने भी कहा--'बलभद्रकों तो चूत-
- **Translation**: 

---

### Verse 17 (Bramha 0.6597)
- **Original**: यादवोंकों साथ ले द्वारका चले आये।
- **Translation**: 

---

### Verse 18 (Bramha 0.6598)
- **Original**: + श्रीकृष्णकी संतति, अनिरुद्धके विवाहमें रुक्मीका वध तथा इचकी पराजय * एक दिन त्रिभुवनके स्वामी इन्द्र मतवाले
- **Translation**: 

---

### Verse 19 (Bramha 0.6599)
- **Original**: ओर सौ योजनोंतक भयंकर पाशों (लोहेके कैंटीले ऐरावतकी पीठपर बैठकर द्वारकामें श्रीकृष्णके पास
- **Translation**: 

---

### Verse 20 (Bramha 0.6600)
- **Original**: तारों)-का घेरा बना था। शत्रुऑकी सेनाको रोकनेके आये और इस प्रकार योले--' मधुसूदन! यद्यपि
- **Translation**: 

---

