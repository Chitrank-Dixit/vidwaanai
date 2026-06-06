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

### Verse 1 (Bramha 0.141)
- **Original**: पर्वत और वृक्ष--सबने पृथ्वीको दुहा
- **Translation**: 

---

### Verse 2 (Bramha 0.142)
- **Original**: उनके दूध, लगता। अत: बसुन्धरे। मैं प्रजाका कल्याण
- **Translation**: 

---

### Verse 3 (Bramha 0.143)
- **Original**: बछड़ा, पात्र और दुहनेबाला-ये सभी पृथक्‌-
- **Translation**: 

---

### Verse 4 (Bramha 0.144)
- **Original**: 8 * संक्षिम ब्रह्मपुराण « पृथक्‌ थे। ऋषियोंके चन्द्रमा बछड़ा बने, यृहस्पतिने
- **Translation**: 

---

### Verse 5 (Bramha 0.145)
- **Original**: नामसे बिख्यात है। यह समुद्रतक पृथुके ही दुहनेका काम किया, तपोमव ब्रह्म उनका दूध, अधिकारमें थो। मधु और कैटभके मेदसे व्याप्त था और वेद ही उनके पात्र थे। देवताओंने , होनेके कारण यह मेदिनी कहलाती है। फिर राजा सुवर्णमय पात्र लेकर युष्टिकारक दूध दुह्य। उनके
- **Translation**: 

---

### Verse 6 (Bramha 0.146)
- **Original**: लिये इन्द्र बछड़ा बने और भगवान्‌ सूर्यने दुहनेका
- **Translation**: 

---

### Verse 7 (Bramha 0.147)
- **Original**: काम किया। पितरोंका चाँदीका पात्र था। प्रतापी
- **Translation**: 

---

### Verse 8 (Bramha 0.148)
- **Original**: फिमशसबब लिवर यम बछड़ा बने, अन्तकने दूध दुह्या । उनके दुधको । “ 'स्वधा' नाम दिया गया है। नागोंने तक्षककों >> ब्रछड़ा बनाया। तुम्बीका पात्र रखा। ऐरावत नागसे
- **Translation**: 

---

### Verse 9 (Bramha 0.149)
- **Original**: दुहनेका काम लिया और बिपरूपी दुग्धका दोहन
- **Translation**: 

---

### Verse 10 (Bramha 0.150)
- **Original**: किया। असुरोंमें मधु दुहनेवाला बना। उसने
- **Translation**: 

---

### Verse 11 (Bramha 0.151)
- **Original**: मायापय दूध दुहा। उस समय विरोचन बछड़ा बना था और लोहेके पात्रमें दूध दुह्हा गया था।
- **Translation**: 

---

### Verse 12 (Bramha 0.152)
- **Original**: 0 यक्षोंका कच्चा पात्र था। कुबेर बछड़ा बने थे।
- **Translation**: 

---

### Verse 13 (Bramha 0.153)
- **Original**: कओ' रजतनाभ यक्ष दुहनेवाला था और अन्तर्धान
- **Translation**: 

---

### Verse 14 (Bramha 0.154)
- **Original**: 90 होनेकी विद्या ही उनका दूध था। राक्षसेद्रोरपे ; (5: 5304; हु नि रच के रे भ " सुमाली नामका राक्षस बछड़ा बना। रजतनाभ
- **Translation**: 

---

### Verse 15 (Bramha 0.155)
- **Original**: जी 745, 2 0 दुहनेबाला था। उसने कपालरूपी पात्रमें शोणितरूपी
- **Translation**: 

---

### Verse 16 (Bramha 0.156)
- **Original**: पृथुकी आज्ञाके अनुसार भूदेयी उनकी पुत्री बन दूधका दोहन किया। गन्धर्वो्में चित्ररथने बछड़ेका
- **Translation**: 

---

### Verse 17 (Bramha 0.157)
- **Original**: गयी, इसलिये इसे पृथ्वी भी कहते हैं। पृथुने इस काम पूरा किया। कमल हो उनका पात्र था।। पृथ्वीका विभाग और शोधन किया, जिससे यह सुरुचि दुहनेवाला था और पवित्र सुगन्ध ही, अन्नकी खान और समृद्धिशालिनी बन गयी। गाँवों उनका दुध था। पर्वतोंमें महागिरि मेरुने हिमवान्‌को
- **Translation**: 

---

### Verse 18 (Bramha 0.158)
- **Original**: और नगरोंके कारण इसकी बड़ी शोभा होते वछड़ा बनाया और स्वय॑ दुहनेवाला बनकर
- **Translation**: 

---

### Verse 19 (Bramha 0.159)
- **Original**: लगी। वेन-कुमार महाराज पृथुका ऐसा ही प्रभाव शिलामय पात्रमें रत्नों एवं ओषधियोंको दूधके
- **Translation**: 

---

### Verse 20 (Bramha 0.160)
- **Original**: भथा। इसमें संदेह नहीं कि थे समस्त प्राणियोंके रुपमें दुह्म। वृक्षोमें प्कक्ष (पाकड़) बछड़ा था।, पूजनीय और वन्दनीय हैं। बेद-वेदाड्लोंके पारज्गत खिले हुए शालके वृक्षने दुहनेका काम किया। । विद्वान्‌ ब्राह्मणोंको भी महाराज पृथुकी ही वन्दना पलाशका पात्र था और जलने तथा कटनेपर पुनः
- **Translation**: 

---

