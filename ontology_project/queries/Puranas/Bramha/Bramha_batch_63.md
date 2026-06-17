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

### Verse 1 (Bramha 0.1241)
- **Original**: सम्पूर्ण विश्वका आत्मा, शर्व (संहारकारी) और महात्मा नारदकों जो बात बतलायी थी, वही मैं
- **Translation**: 

---

### Verse 2 (Bramha 0.1242)
- **Original**: अक्षर (अबिनाशी) माना गया है। उसने इस तुम लोगोंसे कहता हूँ। एक समयकी बात है,
- **Translation**: 

---

### Verse 3 (Bramha 0.1243)
- **Original**: एकात्मक त्रिलोकीको अपने आत्माके द्वारा धारण अपनी इन्द्रियॉंको वशमें रखनेबाले महायोगी
- **Translation**: 

---

### Verse 4 (Bramha 0.1244)
- **Original**: कर रखा है। वह स्वयं शरीरसे रहित है, किंतु नारदजी मेरुगिरिके शिखरसे गन्धमादन नामक
- **Translation**: 

---

### Verse 5 (Bramha 0.1245)
- **Original**: समस्त शरोरोंमें निवास करता है। शरीरमें पर्वतपर उतरे और सम्पूर्ण लोकॉंमें विचरते हुए
- **Translation**: 

---

### Verse 6 (Bramha 0.1246)
- **Original**: रहते हुए भी बह उसके कमोंसे लिप्त नहीं उस स्थानपर आये, जहाँ मित्र देवता तपस्या करते
- **Translation**: 

---

### Verse 7 (Bramha 0.1247)
- **Original**: होता। बह मेरा, तुम्हारा तथा अन्य जितने भी थे। उन्हें तपस्यामें संलग्र देख नारदजीके मनमें
- **Translation**: 

---

### Verse 8 (Bramha 0.1248)
- **Original**: देहधारी हैं, उनका भी आत्मा है। सबका कौतूृहल हुआ। वे सोचने लगे, “जो अक्षय,
- **Translation**: 

---

### Verse 9 (Bramha 0.1249)
- **Original**: साक्षी है, कोई भी उसका ग्रहण नहीं कर अविकारी, व्यक्ताव्यक्तस्वरूप और सनातन पुरुष
- **Translation**: 

---

### Verse 10 (Bramha 0.1250)
- **Original**: सकता। वह सगुण, निर्गुण, विश्वरूप तथा हैं, जिन महात्माने तीनों लोकोंको धारण कर रखा , ज्ञानगम्य माना गया है । उसके सब ओर हाथ- पैर है, जो सब देवताओंके पिता एवं परोंसे भी पर
- **Translation**: 

---

### Verse 11 (Bramha 0.1251)
- **Original**: हैं, सब ओर नेत्र, सिर और मुख हैं तथा सब हैं, वे किन देवताओं अथवा पितरोंका यजन करते
- **Translation**: 

---

### Verse 12 (Bramha 0.1252)
- **Original**: ओर कान हैं, वह संसारमें सबको व्याप्त करके
- **Translation**: 

---

### Verse 13 (Bramha 0.1253)
- **Original**: » भगवान्‌ सूर्सकी महिपा « 63 स्थित है।* सम्पूर्ण मस्तक उसके मस्तक, सम्पूर्ण
- **Translation**: 

---

### Verse 14 (Bramha 0.1254)
- **Original**: पितृकार्यके अबसरपर उसीको पूजा होती है। उससे भुजाएँ उसकी भुजा, सम्पूर्ण पैर उसके पैर, सम्पूर्ण
- **Translation**: 

---

### Verse 15 (Bramha 0.1255)
- **Original**: बढ़कर दूसरा कोई देवता या पितर नहीं है। उसका नेत्र उसके नेत्र एवं सम्पूर्ण नासिकाएँ उसकी नासिका
- **Translation**: 

---

### Verse 16 (Bramha 0.1256)
- **Original**: ज्ञान अपने आत्माके द्वारा होता है। अत: मैं उसी हैं। वह स्वेच्छाचारी है और अकेला ही सम्पूर्ण कषेत्रमें
- **Translation**: 

---

### Verse 17 (Bramha 0.1257)
- **Original**: सर्वात्माका पूजन करता हूँ। देवर! स्वर्गमें भी जो सुखपूर्वक विचरता है। यहाँ जितने शरीर हैं, ये सभी
- **Translation**: 

---

### Verse 18 (Bramha 0.1258)
- **Original**: जीव उस परमेश्वरको नमस्कार करते हैं, वे उसीके क्षेत्र कहलाते हैं। उन सबको वह योगात्मा जानता है,
- **Translation**: 

---

### Verse 19 (Bramha 0.1259)
- **Original**: द्वारा दिये हुए अभीष्ट गतिकों प्राप्त होते हैं। देवता इसलिये क्षेत्रज्ष कहलाता है। अव्यक्त पुरमें शयन
- **Translation**: 

---

### Verse 20 (Bramha 0.1260)
- **Original**: और अपने-अपने आश्रमोंमें स्थित मनुष्य भक्तिपूर्वक करता है, अत: उसे पुरुष कहते हैं। विश्वका अर्थ है
- **Translation**: 

---

