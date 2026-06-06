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

### Verse 1 (Vaivtpuran 13.11762)
- **Original**: ग्वाल-बालोंने भी उनके गुण गाये। वे खुशीके गया और श्रीकृष्णने उस सुदर्शनचक्रकों अपने
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11763)
- **Original**: मारे नाचने लगे। श्रीकृष्ण और बलरामको कुछ हाथमें ले लिया। उसमें सोलह अरे थे। उस
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11764)
- **Original**: पके हुए फल देकर शेष सभी फलोंकों उन उत्तम अस्त्रकों घुमाकर श्रीकृष्णे उसकी ओर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11765)
- **Original**: बालकोंने प्रसन्न-चित्त होकर खाया। खा-पीकर फेंका तथा जिसे त्रह्मा, विष्णु और शिव भी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11766)
- **Original**: बलराम और बालकोंके साथ श्रीहरि शीघ्र अपने नहीं मार सकते थे, उसे लीलासे ही काट डाला। घरकों गये। (अध्याय 22) 8+>अशथे(3क्‍0>>0
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11767)
- **Original**: + श्रीकृष्णजन्मखण्ड « 529 धेनुकके पूर्वजन्मका परिचय, बलि-पुत्र साहसिक तथा तिलोत्तमाका स्वच्छन्द बिहार, दुर्वासाका शाप और वर, साहसिकका गदहेकी योनिमें जन्म लेना तथा तिलोत्तमाका बाणपुत्री 'उषा' होना नारदजीने पूछा--भगवन्‌! किस पापसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11768)
- **Original**: कल्पका वृत्तान्त मुझसे सुनो। दैत्यके इस सुधा- बलि-पुत्र साहसिकको गदहेकी योनि प्राप्त हुई ?
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11769)
- **Original**: तुल्य मधुर वृत्तान्तको मैं तुम्हें सुना रहा हूँ। दुर्वासाजीनी किस अपराधसे दानवराजको शाप एक दिनकी बात है। बलिका बलवान पुत्र दिया? नाथ! फिर किस पुण्यसे दानवे श्वरने साहसिक अपने तेजसे देवताओंको परास्त करके महाबली श्रीहरिका धाम एवं उनके साथ एकत्व
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11770)
- **Original**: गन्धमादनकी ओर प्रस्थित हुआ। उसके सम्पूर्ण (सायुज्य) मोक्ष प्राप्त कर लिया? संदेह-भंजन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11771)
- **Original**: अड्भ चन्दनसे चर्चित थे। वह रत्नमय आशभूषणोंसे करनेवाले महर्षे ! इन सब बातोंको आप विस्तारपूर्वक
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11772)
- **Original**: विभूषित हो रत्रके ही सिंहासनपर विराजमान था। बताइये। अहो! कविके मुखमें काव्य पद-पदपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11773)
- **Original**: उसके साथ बहुत बड़ी सेना थी। इसी समय नया-नया प्रतीत होता है। स्वर्गकी परम सुन्दरी अप्सरा तिलोत्तमा उस भगवान्‌ श्रीनारायणने कहा--वत्स ! नारद!
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11774)
- **Original**: मार्गसे आ निकली। उसने साहसिककों देखा और सुनो। मैं इस विषयमें प्राचीन इतिहास कहूँगा।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11775)
- **Original**: साहसिकने उसको। पुंश्वली स्त्रियोंका आचरण मैंने इसे पिता धर्मके मुखसे गन्धमादन पर्वतपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11776)
- **Original**: दोषपूर्ण होता ही है। वहाँ दोनों एक-दूसरेके सुना था। यह विचित्र एवं अत्यन्त मनोहर वृत्तान्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11777)
- **Original**: प्रति आकर्षित हो गये। चन्द्रमाके समीप जाती पाद्म-कल्पका है और श्रीनारायणदेवकी कथासे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11778)
- **Original**: हुई तिलोत्तमा वहाँ बौचमें ही ठहर गयी। कुलटा युक्त होनेके कारण कानोंके लिये उत्तम अमृत
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11779)
- **Original**: स्त्रियाँ कैसी दुष्टददया होती हैं और वे किसी है। जिस कल्पकी यह कथा है, उसमें तुम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11780)
- **Original**: भी पापका विचार न करके सदा पापरत हो रहा उपबर्हण नामक गन्धर्वके रूपमें थे। तुम्हारी आयु
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11781)
- **Original**: करती हैं-यह सब बतलाकर भी तिलोत्तमाने एक कल्पकी थी। तुम शोभायमान, सुन्दर और
- **Translation**: 

---

