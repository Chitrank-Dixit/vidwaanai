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

### Verse 1 (Bramha 0.2221)
- **Original**: कार्य करेंगे? किसलिये इस बनस्पतिकों काट देती है, वहाँ एक बहुत बड़ा वृक्ष खड़ा है,
- **Translation**: 

---

### Verse 2 (Bramha 0.2222)
- **Original**: गिराया है?' जिसका कुछ भाग तो जलमें है और कुछ
- **Translation**: 

---

### Verse 3 (Bramha 0.2223)
- **Original**: उन दोनॉंकी बात सुनकर राजा बहुत प्रसन्न स्थलमें है। वह समुद्रकौ लहरोंसे आहत होनेपर
- **Translation**: 

---

### Verse 4 (Bramha 0.2224)
- **Original**: हुए। उन्होंने मौठौ वाणीमें उत्तर दिया--' मैं यहाँ भी कम्पित नहीं होता। तुम हाथमें कुल्हाड़ो
- **Translation**: 

---

### Verse 5 (Bramha 0.2225)
- **Original**: आदि-अन्तसे रहित देवाधिदेव जगदीश्वर भगवान्‌ लेकर लहरोंके बीचसे अकेले ही वहाँ चले
- **Translation**: 

---

### Verse 6 (Bramha 0.2226)
- **Original**: विष्णुकी आराधनाके लिये प्रतिमा बनवाना चाहता जाना। तुम्हें बह वृक्ष दिखायी देगा। मेरे बताये
- **Translation**: 

---

### Verse 7 (Bramha 0.2227)
- **Original**: हूँ। इसके लिये स्वयं भगवानने ही मुझे स्वप्रमें अनुसार उसको पहचानकर निःशह्भूभावसे उस
- **Translation**: 

---

### Verse 8 (Bramha 0.2228)
- **Original**: प्रेरित किया है।! राजाकी यह बात सुनकर वृक्षकों काट डालना। उसे काटते समय तुम्हें
- **Translation**: 

---

### Verse 9 (Bramha 0.2229)
- **Original**: भगवान्‌ जगननाथने हँसकर कहा--' महाराज! आपका कोई अद्भुत वस्तु दिखायो देगी। उसीसे सोच- विचार बड़ा उत्तम है। इसके लिये आपको
- **Translation**: 

---

### Verse 10 (Bramha 0.2230)
- **Original**: 108 + संक्षिप्त ब्रह्मपुराण « सहुंकार है। यह पपेकर उलत-साक केलीक, .. पफानका जे. फकन छुलार उच्य कर उत्तम कर्म पत्तेकी भाँति सारहीन है। दुःखकी के अधिकता है। काम-क्रोध इसमें पूर्णरूपसे व्याप्त
- **Translation**: 

---

### Verse 11 (Bramha 0.2231)
- **Original**: £ 53 0++7%-57%8.:0:- हैं। इन्द्रियकूपी भँवर और कीचड़के कारण >ब
- **Translation**: 

---

### Verse 12 (Bramha 0.2232)
- **Original**: बल 325 कर" हलक दुस्तर है। नाना प्रकारके सैकड़ों रोग यहाँ (आज आन दगाओर ह। इसमे भर हर जे आप कि" फणाकार होनेसे बिकट जान पड़ता था। वे नील क्षणभञ्जुर है। इसमें रहते हुए जो आपके मन
- **Translation**: 

---

### Verse 13 (Bramha 0.2233)
- **Original**: शंकर होपसे विस "मल अं बा ेव दक को ह। आााकना ये 5
- **Translation**: 

---

### Verse 14 (Bramha 0.2234)
- **Original**: होते थे। उन्होंने एक कुण्डल धारण कर रखा षा बंकका खेलल काका इ साथ बे उनके हाथोंमें गदा और मूसल शोभा पाते थे। वृक्षकी शीतल छायामें हम दोनोंके साथ बैठिये।
- **Translation**: 

---

### Verse 15 (Bramha 0.2235)
- **Original**: या और नर मेल तो के ये मेरे साथी एक ओह शित्पों हैं। ये सभ प्रकारके
- **Translation**: 

---

### Verse 16 (Bramha 0.2236)
- **Original**: याका स्वरूप कि तय जाया शिल्प-कर्ममें साक्षात्‌ विश्वकर्मेके समान निपुण । 3054 -003 । ली के नेत्र कक हैं। आप किनारा छोड़कर चले आहये। ये मेरे
- **Translation**: 

---

### Verse 17 (Bramha 0.2237)
- **Original**: समान खदालरीक है पक कहर और डेप बताये अनुसार प्रतिमा तैयार कर देंगे।
- **Translation**: 

---

### Verse 18 (Bramha 0.2238)
- **Original**: समान कम का न बेल जे जे के पा ओर दक
- **Translation**: 

---

### Verse 19 (Bramha 0.2239)
- **Original**: लकी उपमा धारण करते थे। शरीरपर सब ब9। इस ऋषनिव विजल चल शोभा पा रहा था। वक्षःस्थलमें श्रीवत्सका छायामें बैठे। तदनन्तर ब्राह्मणरूपधारी विश्वात्मा कह पक पल जोक से द य हम जा पकादा “नल बह सम
- **Translation**: 

---

### Verse 20 (Bramha 0.2240)
- **Original**: सर्वपापहारी श्रीहरि बड़े दिव्य दिखायी देते थे। ला .2 02904 5847 %0:05:
- **Translation**: 

---

