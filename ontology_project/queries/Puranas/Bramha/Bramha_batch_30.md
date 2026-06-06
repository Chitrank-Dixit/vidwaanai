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

### Verse 1 (Bramha 0.581)
- **Original**: ऋक्ष, दो ही परीक्षित्‌ु, तीन भीमसेन तथा दो बाह्माश्वका जन्म हुआ। चाह्माश्चके पाँच पुत्र हुए, , जनमेजय नामके राजा हुए। द्वितीय ऋक्षके पुत्र जो समृद्धिशाली पाँच जनपदोंसे युक्त थे। उनके
- **Translation**: 

---

### Verse 2 (Bramha 0.582)
- **Original**: भीमसेन थे। भीमसेनसे प्रतीप और प्रतीपसे
- **Translation**: 

---

### Verse 3 (Bramha 0.583)
- **Original**: * यपाति-पुत्रोंके बंशका वर्णन + 29 शान्तनु, देवापि तथा बाहिक--ये तीन महारथी
- **Translation**: 

---

### Verse 4 (Bramha 0.584)
- **Original**: 42 कक 'कन उसको क्ड चुडमा न ं
- **Translation**: 

---

### Verse 5 (Bramha 0.585)
- **Original**: " चल दी। नवजात शिशु अहिकके 42 अं पल
- **Translation**: 

---

### Verse 6 (Bramha 0.586)
- **Original**: कक भूआअ न 3 था। तब उसपर कृपा ला कोन चुत इ।
- **Translation**: 

---

### Verse 7 (Bramha 0.587)
- **Original**: करनेके लिये आकाशमें मेघ प्रकट हो गये। -+ के; 200 का भा 3 श्रविष्ठाके दो पुत्र थे-पैप्पलादि और कौशिक। वे जात बी आज ना जाम थजखली (40 उस शिशुको देख दयासे द्रवीभूत हो गये। या न
- **Translation**: 

---

### Verse 8 (Bramha 0.588)
- **Original**: उन्होने उसे उजाकर जलते धोया और रक्तमें डूबे हुए। अब मैं शान्तनुके त्रिभुबनविख्यात वंशका ै के प्णाणकों शिललापर रपदकर सफ वर्णन करूँगा। शान्तनुने गद्गजाके गर्भसे देवक्नत ै 3 हम पेन हसन कीफे “मेज बिक । पष्डबोके 3574 +त्ीट ' शालतुकी
- **Translation**: 

---

### Verse 9 (Bramha 0.589)
- **Original**: भाँति श्यामवर्णकी हो गयों। इसलिये उन दोनोंने 40 8-9+4407 - बालकका नाम अजपार्शव रख दिया। उसे काली नामवाली पत्नीने विचित्रवीर्य नामक पुत्र
- **Translation**: 

---

### Verse 10 (Bramha 0.590)
- **Original**: उस ब गये सो जताणोने पास पासक जड़ा उत्पन्न किया, जो पिताका प्यारा तथा धर्मात्मा था। विकन रआ पा का शक 24847क+744944 गान्धारे,
- **Translation**: 

---

### Verse 11 (Bramha 0.591)
- **Original**: उसे गोद ले लिया। तबसे वह रेमकीका पुत्र माना +2037-0अ।32 4-4.
- **Translation**: 

---

### Verse 12 (Bramha 0.592)
- **Original**: आते । दोनों ब्राह्मण उसके सचिव हुए। उन गर्भसे सौ पुत्र उत्पन्न किये। उन सबमें दुर्योधन । नी न और असम सु038 3 सभवाकुम, कप. 2 व है। अभिमन्यु कर
- **Translation**: 

---

### Verse 13 (Bramha 0.593)
- **Original**: आयुवाले हुए । यह महात्मा पाण्डवोंका पौरव- परीक्षित्‌ और परीक्षि चने छा हुआ।
- **Translation**: 

---

### Verse 14 (Bramha 0.594)
- **Original**: वंश बतलाया गया। नहुषनन्दन ययातिने अपनी समय अत्यन्त प्रसन्न जनमेजयके काश्या नामकी पत्नीसे चन्द्रापीड॒ तथा
- **Translation**: 

---

### Verse 15 (Bramha 0.595)
- **Original**: मृदाबस्थाका परिएन करे समन आह रे 5 मियहअ पी. अध आ
- **Translation**: 

---

### Verse 16 (Bramha 0.596)
- **Original**: पृथ्वी चन्द्रमा, सूर्य और ग्रहोंके प्रकाशसे रहित हो मोक्ष-धर्मके ज्ञाता थे। सा पवीपर महान्‌ न चुर
- **Translation**: 

---

### Verse 17 (Bramha 0.597)
- **Original**: तु का थे। ये सब इस पृथ्वीपर जानमेजय
- **Translation**: 

---

### Verse 18 (Bramha 0.598)
- **Original**: पौरवबंशसे अति आपसे प्रसिद्र हुए। उन सी परम सबसे
- **Translation**: 

---

### Verse 19 (Bramha 0.599)
- **Original**: बट िक। अब पबेछू आह अत और बड़ा सत्यकर्ण था, जो हस्तिनापुरमें रहा करता । का का आप कं था। महाबाहु सत्यकर्ण प्रचुर दक्षिणा देनेवाले "ता दी कक सत्यकर्णके पुत्र प्रतापी श्वेतकर्ण हुए। वे पुत्र न
- **Translation**: 

---

### Verse 20 (Bramha 0.600)
- **Original**: कक रत, अत, कथन तथा करंधमके कक जलिकों जो बाकुतने कथा हुई बनमें महत । अवीक्षित्‌-नन्दन राजा मरुत्त इस मरुत्तसे 8 कस है -+8+कैक पीतल किया । । घिन्न हैं। करंपमकुमार मरुत्तके कोई पुत्र नहीं दी आयी थी। अकुब5 उस गर्भके स्थापित हो जानेपर राजा श्वेतकर्ण
- **Translation**: 

---

