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

### Verse 1 (Vaivtpuran 49.4834)
- **Original**: निवास करता है। तदनन्तर शराबी और शूद्र होता दूत उन्हें पीटते हैं। उस नरकयातनाके अन्तमें है। इसके बाद उसकी शुद्धि होती है। वह महापापी जीव भारतवर्षमें विष्ठाका कीड़ा जैगीषव्य बोले--जो पिता, माता तथा होता है। उस योनिमें उसे देवताके वर्षसे साठ गुरुके प्रति भक्तिसे हीन होकर उनका पालन नहीं हजार वर्षोतक रहना पड़ता है। तत्पश्चात्‌ वह
- **Translation**: 

---

### Verse 2 (Vaivtpuran 49.4835)
- **Original**: करता, उलटे वाणीद्वारा उनकी ताड़ना करता है, मानव भूमिहीन, संतानहीन, दरिद्र, कृपण, रोगी उसे “कृतपघ्र' कहा गया है। जो कुलटा नारी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 49.4836)
- **Original**: प्रतिदिन वाणीद्वारा अपने स्वामीको ताने मारती या
- **Translation**: 

---

### Verse 4 (Vaivtpuran 49.4837)
- **Original**: राजेन्द्र! अब ब्रह्माजीके बताये अनुसार दोषका फटकारती है, वह “कृतप्नरी' कही गयी है।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 49.4838)
- **Original**: निरूपण करूँगा। जो महापापी मानव इन सबके भारतवर्षमें वह बहुत बड़ी पापिनी है। कृतप्न पुरुष
- **Translation**: 

---

### Verse 6 (Vaivtpuran 49.4839)
- **Original**: साथ मैथुन करता है वह जीते-जी ही मृतक- हो या स्त्री, दोनों “वह्िकुण्ड' नामक महाघोर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 49.4840)
- **Original**: तुल्य होता है, चाण्डाल एवं अस्पृश्य समझा जाता नरकमें पड़ते हैं। वहाँ बहुत लंबे समयतक वे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 49.4841)
- **Original**: है। उसे सूर्यमण्डलके दर्शनका भी अधिकार नहीं अग्निमें ही वास करते हैं। तत्पश्चात्‌ सात जन्मोंतक
- **Translation**: 

---

### Verse 9 (Vaivtpuran 49.4842)
- **Original**: होता। वह शालग्रामका, उनके चरणामृतका, जलौका (जोंक) होकर वह शुद्ध होता है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 49.4843)
- **Original**: तुलसीदलमिश्रित जलका, सम्पूर्ण तीर्थजलका तथा वाल्मीकिने कहा--राजन्‌ ! जैसे सभी तरुओंमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 49.4844)
- **Original**: ब्राह्मणोंके चरणोदकका स्पर्श भी नहीं कर सकता। सर्वत्र वृक्षत्व है, कहीं भी वृक्षत्वका त्याग नहीं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 49.4845)
- **Original**: वह पातकी मनुष्य विष्ठाके तुल्य घृणित होता है। है, उसी तरह सम्पूर्ण पापोंमें कृतप्रता है। जो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 49.4846)
- **Original**: उसे देवता, गुरु और ब्राह्मणको नमस्कार करनेका काम, क्रोध तथा भयके कारण झूठी गबाही देता
- **Translation**: 

---

### Verse 14 (Vaivtpuran 49.4847)
- **Original**: भी अधिकार नहीं रह जाता है। उसका जल है तथा सभामें पक्षपातपूर्वक बात करता है, वह
- **Translation**: 

---

### Verse 15 (Vaivtpuran 49.4848)
- **Original**: मूत्रसे भी अधिक अपवित्र होता है। भारतमें पृथ्वी कृतघ्न माना गया है। राजन्‌! जो पुण्यमात्रका हनन
- **Translation**: 

---

### Verse 16 (Vaivtpuran 49.4849)
- **Original**: उसके भारसे दब जाती है। वह उसके बोझकों करता है, वह भी कृतप्न ही है। सर्वत्र सबके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 49.4850)
- **Original**: ढोनेमें असमर्थ हो जाती है। बेटी बेचनेवाले पुण्यकी हानिमें कृतप्नता निहित है। नरेध्वर! जो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 49.4851)
- **Original**: पापीकी भाँति गुरुपत्नीगामीके पापसे भी सारा देश भारतवर्षमें झूठी गवाही देता या पक्षपातपूर्ण बात
- **Translation**: 

---

### Verse 19 (Vaivtpuran 49.4852)
- **Original**: पतित हो जाता है। उसके स्पर्शसे, उसके साथ करता है, वह निश्चय ही बहुत लंबे समयतक
- **Translation**: 

---

### Verse 20 (Vaivtpuran 49.4853)
- **Original**: बार्तालाप करनेसे, सोनेसे, एक स्थानमें रहने और सर्पकुण्डमें निवास करता है। सदा उसके शरीरमें [साथ-साथ भोजन करनेसे मनुष्योंको पाप लगता साँप लिपटे रहते हैं; वह डरा रहता है और साँप है। वह कुम्भीपाकमें निवास करता है। वहाँ उसे उसे खाये जाते हैं। यमदूतोंकी मार पड़नेपर वह
- **Translation**: 

---

