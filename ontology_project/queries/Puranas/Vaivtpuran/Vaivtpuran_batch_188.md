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

### Verse 1 (Vaivtpuran 13.3129)
- **Original**: चाहिये-ये सभी बातें बतला दीं। तब तुलसीने विष्णु तुम्हें प्राणोंसे भी अधिक प्रिय मानेंगे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.3130)
- **Original**: भगवती राधाकी उपासना कौ और उनके तुम्हारे बिना पूजा निष्फल समझी जायगी। कृपाप्रसादसे वह देवी राधाके समान ही सिद्ध वृन्दावनमें वृक्षरूपसे रहते समय लोग तुम्हें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.3131)
- **Original**: हों गयी। मन्त्रके प्रभावसे ब्रह्माजीने जैसा कहा *वृन्दावनी ' कहेंगे। तुमसे उत्पन्न पत्तोंसे गोपी और
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.3132)
- **Original**: था, ठीक बैसा ही फल तुलसीको प्राप्त हो गया। गोपोंद्वारा भगवान्‌ माधवकी पूजा सम्पन्न होगी।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.3133)
- **Original**: तपस्या-सम्बन्धी जो भी क्लेश थे, वे मनमें तुम मेरे बरके प्रभावसे बृक्षोंकी अधिष्ठात्री देवी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.3134)
- **Original**: प्रसन्नता उत्पन्न होनेके कारण दूर हो गये; क्योंकि बनकर गोपरूपसे विराजनेवाले भगवान्‌ श्रीकृष्ण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.3135)
- **Original**: फल सिद्ध हो जानेपर मनुष्योंका दुःख हो साथ स्वेच्छापूर्वक निरन्तर आनन्द भोगोगी।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.3136)
- **Original**: उत्तम सुखके रूपमें परिणत हो जाता है। नारद! ब्रह्माकी यह अमरवाणी सुनकर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.3137)
- **Original**: (अध्याय 15) #2/8 रिपीरि/-2त
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.3138)
- **Original**: तुलसीको स्वप्रमें शद्भचचूड़के दर्शन, शद्भुचूड़ तथा तुलसीके विवाहके लिये ब्रह्माजीका दोनोंको आदेश, तुलसीके साथ शद्जुचूड़का गान्धर्व-विवाह तथा देवताओंके प्रति उसके पूर्वजन्मका स्पष्टीकरण भगवान्‌ नारायण कहते हैं--नारद! एक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.3139)
- **Original**: सुगन्ध्रपूर्ण चन्दनद्वारा उसके अज्गभ अनुलिप्त थे। समयकी बात है। वृषध्वजकी कन्या तुलसी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.3140)
- **Original**: मनकों मुग्ध कर देनेवाला वह शद्भुचूड़ अमूल्य अत्यन्त प्रसन्न होकर शयन कर रही थी। उसने
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.3141)
- **Original**: रत्नोंसे बने हुए बिमानपर विराजमान था। स्वप्रमें एक सुन्दर वेषवाले पुरुषको देखा। वह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.3142)
- **Original**: इस शक्लुचूड़को देखकर तुलसीने बस्त्रसे पुरुष अभी पूर्ण नवयुवक था। उसके मुखपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.3143)
- **Original**: अपना मुख ढँक लिया। कारण, लज्जावश मुस्कान छायी थी। उसके सम्पूर्ण अड्जोंमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.3144)
- **Original**: उसका मुख नीचेकी ओर झुक गया था। चन्दनका अनुलेपन था। रत्रमय आभूषण उसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.3145)
- **Original**: शरत्पूर्णिमाके चन्द्रमा उसके निर्मल दिव्य चन्द- सुशोभित कर रहे थे। उसके गलेमें सुन्दर माला
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.3146)
- **Original**: जैसे मुखके सामने तुच्छ थे। अमूल्य रत्रोंसे थी। उसके नेत्र-भ्रमर तुलसीके मुख-कमलका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.3147)
- **Original**: बने हुए नूपुर उसके चरणोंकी शोभा बढ़ा रहे रस-पान कर रहे थे। थे। बह मनोहर त्रिवलीसे सम्पन्न थी। सर्वोत्तम मुने! यों स्वप्न देखनेके पश्चात्‌ तुलसी जगकर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.3148)
- **Original**: मणिसे निर्मित करधनी सुन्दर शब्द करती हुई विषाद करने लगी। इस प्रकार तरुण अबस्थासे
- **Translation**: 

---

