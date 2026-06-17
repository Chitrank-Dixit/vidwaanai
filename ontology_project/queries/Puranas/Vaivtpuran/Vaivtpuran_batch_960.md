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

### Verse 1 (Vaivtpuran 543.17514)
- **Original**: विष्णुमाया, सर्वरूपा, सनातनी, परन्रह्मस्वरूपा, प्रख्भात करते हैं और शेषनाग जिस नौ प्रकारके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17515)
- **Original**: परमात्मस्वरूपिणी सगुणा, निर्गुणा, परा और रूप धारण करनेवाले ईश्वरकों अनन्त कहते हैं; स्वेच्छामयी हैं; वे सती-साध्वी देवी पार्वती छ: प्रकारके धर्म ही उनके छ: रूप हैं, फिर एक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17516)
- **Original**: सनातन भगवान्‌ श्रीकृष्णसे बोलीं। रूप वैष्णबोंका, एक रूप वेदोंका और एक रूप
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17517)
- **Original**: . पार्वतीने कहा--प्रभो! गोलोकस्थित पुराणोंका है; इसीलिये वे नौ प्रकारके कहे जाते
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17518)
- **Original**: रासमण्डलमें मैं ही अपने एक राधिकारूपसे हैं। जो मत शंकरका है, उसी मतका आश्रय ले रहती हूँ। इस समय गोलोक रासशून्य हो गया है; न्यायशास्त्र जिसे अनिर्वचनीय रूपसे निरूपण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17519)
- **Original**: अतः आप मुक्ता और माणिक्यसे विभूषित रथपर करता है, दीर्थदर्शी वैशेषिक जिसे नित्य बतलाते
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17520)
- **Original**: आरूढ़ हो वहाँ जाइये और उसे परिपूर्ण कीजिये। हैं; सांख्य उन देवको सनातन ज्योतिरूप, मेरा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17521)
- **Original**: आपके बक्ष:स्थलपर बास करनेवाली परिपूर्णतमा अंशभूत वेदान्त सर्वरूप और सर्वकारण,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17522)
- **Original**: देवी मैं ही हूँ। आपकी आज्ञासे वैकुण्ठमें वास
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17523)
- **Original**: * भ्रीकृष्णजन्मखण्ड * 75 5666 64888 44 5444 88944 8 94 444 4 4 # ऋ 4 # #4 4 44 4 5 4 ऋ अ 4 8 5 5 ऋ कह 5 हक हक कफ ऊ 4 $ 8 5 4 54 4 8 8 करनेवाली महालक्ष्मी मैं ही हूँ। वहीं श्रीहरिके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17524)
- **Original**: हरिनामोच्चारण करके विस्मयात्रिष्ट हो अपने- बामभागमें स्थित रहनेबाली सरस्वती भी मैं ही
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17525)
- **Original**: अपने स्थानकों चले गये। श्रीदुर्गा भी हर्षमग्र हूँ। मैं आपकी आज्ञासे आपके मनसे उत्पन्न हुई
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17526)
- **Original**: हों शिवके साथ अपने नगरको चली गयीं। सिन्धुकन्या हूँ। ब्रह्मके संनिकट रहनेवाली अपनी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17527)
- **Original**: तदनन्तर सर्वज्ञा राधा हर्षविभोर हो आते हुए कलासे प्रकट हुई वेदमाता सावित्री मेरा ही नाम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17528)
- **Original**: प्राणवल्लभ श्रीकृष्णके स्वागतार्थ गोपियोंके साथ है। पहले सत्ययुगमें आपकी आज्ञासे मैंने समस्त
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17529)
- **Original**: आगे आरयीं। श्रीकृष्फो समीप आते देखकर देवताओंके तेजोमें अपना वासस्थान बनाया और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17530)
- **Original**: सती राधिका रथसे उतर पड़ीं और सखियोंके उससे प्रकट होकर देवीका शरीर धारण किया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17531)
- **Original**: साथ आगे बढ़कर उन्होंने उन जगदी श्वरके चरणोंमें उसी शरीरसे मेरेद्वारा लीलापूर्वक शुम्भ आदि दैत्य
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17532)
- **Original**: सिर झुकाकर प्रणाम किया। ग्वालों और गोपियोंके मारे गये। मैं ही दुर्गासुरका वध करके “दुर्गा',
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17533)
- **Original**: मनमें सदा श्रीकृष्णेके आगमनकी लालसा बनी त्रिपुरका संहार करनेपर 'त्रिपुरा' और रक्तबीजको
- **Translation**: 

---

