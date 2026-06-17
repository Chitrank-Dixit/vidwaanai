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

### Verse 1 (Bramha 0.4121)
- **Original**: अपने पिता-पितामहोंके राज्यका पालन करते थे। मनुष्य सब पापोंसे मुक्त हो जाता है। इक्ष्वाकुवंशमें
- **Translation**: 

---

### Verse 2 (Bramha 0.4122)
- **Original**: महाराज दशरथके तीन रानियाँ थीं-कौसल्या, दशरथ नामके क्षत्रिय राजा हुए, जो सम्पूर्ण सुमित्रा और कैकेयी। बे तीनों कुलीन, विश्वमें विख्यात थे। वे इन्द्रको हो भाँति बलबान्‌, सौभाग्यशालिनी, रूपबती और सुलक्षणा थीं।
- **Translation**: 

---

### Verse 3 (Bramha 0.4123)
- **Original**: * औरापतीर्थकी पहिमा « 3203 राजा दशरथ जब अयोध्याके राजसिंहासनपर
- **Translation**: 

---

### Verse 4 (Bramha 0.4124)
- **Original**: है; अतः दैत्य और दानव लौट जाय॑ँ।' राजा आसीन थे और ब्रह्मवेत्ताओमें श्रेष्ठ बसिष्ठजी
- **Translation**: 

---

### Verse 5 (Bramha 0.4125)
- **Original**: दशरथने बैसा ही किया। स्वर्गमे पहुँचकर उन्होंने उनके पुरोहितके पदपर प्रतिष्ठित थे, उस समय
- **Translation**: 

---

### Verse 6 (Bramha 0.4126)
- **Original**: दैत्यों, दानवों तथा राक्षसोंक साथ लोहा लिया। देशमें न रोग थे न मानसिक चिन्ताएँ। न तो
- **Translation**: 

---

### Verse 7 (Bramha 0.4127)
- **Original**: उस समय नमुचिके भाइयोंने देवताओंके देखते- अनावृष्टि होती थी और न अकाल ही पड़ता था।
- **Translation**: 

---

### Verse 8 (Bramha 0.4128)
- **Original**: देखते तोखे बाण मारकर राजाके रथकी धुरी तोड़ ब्राह्मण, क्षत्रिय, वैश्य तथा शुद्रोंको और चारों
- **Translation**: 

---

### Verse 9 (Bramha 0.4129)
- **Original**: डाली। राजा बड़े बेगसे युद्धमें लगे थे। उन्हें धुरी आश्रमोंको भी पृथक्‌ू-पृथक्‌ बड़ा सुख मिलता
- **Translation**: 

---

### Verse 10 (Bramha 0.4130)
- **Original**: टूटनेका पता न लगा। नारद! उस युद्धमें रानी था। एक समयकी बात है, देवताओं और दानवोंमें
- **Translation**: 

---

### Verse 11 (Bramha 0.4131)
- **Original**: कैकेयी भी राजाके पास ही बैठी थी। उसे रथकी राज्यके लिये युद्ध छिड़ गया। न तो उसमें अवस्थाका पता लग गया, परंतु उसने राजाकों देवताओंकी जीत होती थी और न दैत्यों एवं
- **Translation**: 

---

### Verse 12 (Bramha 0.4132)
- **Original**: इस बातकी सूचना नहीं दी। धुरी टूटी देख उसने दानवॉंकी ही। वह युद्ध कई दिनोंतक लगातार
- **Translation**: 

---

### Verse 13 (Bramha 0.4133)
- **Original**: उसकी जगह अपना हाथ हो लगा दिया। यह चलता रहा। इसी बीचमें आकाशवाणी हुई--'राजा
- **Translation**: 

---

### Verse 14 (Bramha 0.4134)
- **Original**: बड़ा अद्भुत कार्य था। रथियोंमें श्रेष्ठ महाराज दशरथ जिनका पक्ष ग्रहण करेंगे, वे ही विजयी
- **Translation**: 

---

### Verse 15 (Bramha 0.4135)
- **Original**: दशरथने कैकेयौके हाथसे धाँमें हुए रथके द्वारा होंगे, दूसरे नहीं।' यह सुनकर देवता और दानव
- **Translation**: 

---

### Verse 16 (Bramha 0.4136)
- **Original**: दैत्यों और दानवॉपर विजय पायी, फिर देवताओंसे दोनों अपनी विजयके लिये राजाके पास चले।
- **Translation**: 

---

### Verse 17 (Bramha 0.4137)
- **Original**: अनेक बर पाकर उनकी अनुमति ले बे पुनः देवताओंकी ओरसे वायु शीघ्र जा पहुँचे और
- **Translation**: 

---

### Verse 18 (Bramha 0.4138)
- **Original**: अयोध्या लौट आये। आते समय मार्गके बीचमें राजासे बोले--' महाराज ! देव-दानब-संग्राममें आपको
- **Translation**: 

---

### Verse 19 (Bramha 0.4139)
- **Original**: जब महाराज दशरथने अपनी प्रिया कैकेयीौकी चलना चाहिये। वहाँ यह आकाशवाणी सुनायी दी
- **Translation**: 

---

### Verse 20 (Bramha 0.4140)
- **Original**: ओर दृष्टिपात किया, तब उसका यह साहसपूर्ण है कि जिस ओर राजा दशरथ रहेंगे, उसी पक्षकी
- **Translation**: 

---

