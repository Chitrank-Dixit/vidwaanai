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

### Verse 1 (Vaivtpuran 8.6280)
- **Original**: बालरूप धारण करके महलके. भीतर स्थित लिये भ्रमण करते रहते हैं। वे वैष्णव जिस तीर्थमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6281)
- **Original**: पार्वतीकी शय्यापर जा पहुँचे और जन्मे हुए गोदोहन-कालमात्र भी ठहर जाते हैं तो उनके बालककी भाँति घरकी छतके भीतरी भागकी चरणस्पर्शसे वसुन्धरा तत्काल ही पवित्र हो जाती
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6282)
- **Original**: ओर देखने लगे। उस बालकके शरीरकी आभा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6283)
- **Original**: इ्श्ड + संक्षिप्त ब्रह्मवैव्वर्तपुतण + %%$%%$%%$%%### 8 ########$###%#$% कक >> 42:42 22 04004040 0400 00044 45040 40000 044/ । 0 / /8./.
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6284)
- **Original**: शुद्ध चम्पकके समान थी। उसका प्रकाश करोड़ों
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6285)
- **Original**: अधरपुट ऐसे लाल थे कि उसे देखकर पका चन्द्रमाओंकी भाँति उद्दीत था। सब लोग
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6286)
- **Original**: हुआ बिम्बाफल भी लज्जित हो जाता था। कपाल सुखपूर्वक उसकी ओर देख सकते थे। वह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6287)
- **Original**: और कपोल परम मनोहर थे। गरुड़के चोंचकी नेत्रोंकी ज्योति बढ़ानेवाला था। कामदेवको
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6288)
- **Original**: भी निनन्‍दा करनेवाली रुचिर नासिका थी। उसके विमोहित करनेवाला उसका अत्यन्त सुन्दर शरीर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6289)
- **Original**: सभी अड्ग उत्तम थे। त्रिलोकीमें कहीं उसकी था। उसका अनुपम मुख शारदीय पूर्णिमाका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6290)
- **Original**: उपमा नहीं थी। इस प्रकार वह रमणीय शब्यापर उपहास कर रहा था। सुन्दर कमलको तिरस्कृत
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6291)
- **Original**: सोया हुआ शिशु हाथ-पैर उछाल रहा था। करनेवाले उसके सुन्दर नेत्र थे। ओछष्ठ और (अध्याय 8) #<0<>>वष्यिशक(9-200000+ श्रीहरिके अन्तर्धान हो जानेपर शिव-पार्वतीद्वारा ब्राह्मणकी खोज, आकाशवाणीके सूचित करनेपर पार्वतीका महलमें जाकर पुत्रको देखना और शिवजीको बुलाकर दिखाना, शिव-पार्वतीका पुत्रको गोदमें लेकर आनन्द मनाना श्रीनारायण कहते हैं--मुने! इस प्रकार
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6292)
- **Original**: शोकसे आतुर तथा बिकलतासे युक्त दुर्गाने सुना। जब श्रीहरि अन्तर्धान हो गये, तब दुर्गा और
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6293)
- **Original**: (आकाशबाणीने कहा-)जगन्माता! शान्त हो शंकर ब्राह्मणकी खोज करते हुए चारों ओर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6294)
- **Original**: जाओ और मन्दिरमें अपने पुत्रकी ओर दृष्टिपात घूमने लगे। करो। वह साक्षात्‌ गोलोकाधिपति परिपूर्णतम उस समय पार्वतीजी कहने लगीं--हे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6295)
- **Original**: परात्पर श्रीकृष्ण है तथा सुपुण्यक-ब्रतरूपी विप्रवर! आप तो अत्यन्त वृद्ध और भूखसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6296)
- **Original**: वृक्षका सनातन फल है। योगी लोग जिस व्याकुल थे। हे तात! आप कहाँ चले गये ? विभो!
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6297)
- **Original**: अविनाशी तेजका प्रसन्नमनसे निरन्तर ध्यान करते मुझे दर्शन दीजिये और मेरे प्राणोंकी रक्षा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6298)
- **Original**: हैं; वैष्णबगण तथा ब्रह्मा, विष्णु और शिव आदि कौजिये। शिवजी! शीघ्र उठिये और उन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6299)
- **Original**: देवता जिसके ध्यानमें लीन रहते हैं; प्रत्येक ब्राह्मणदेवकी खोज कीजिये। वे क्षणमात्रके लिये
- **Translation**: 

---

