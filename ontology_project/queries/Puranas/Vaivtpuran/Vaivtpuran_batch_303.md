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

### Verse 1 (Vaivtpuran 13.12202)
- **Original**: जाओगी? तुम्हारे इस ब्रतका क्‍या होगा? ब्रतके प्रकारके द्रव्य, लाल, पीले, सफेद और मिश्रित
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12203)
- **Original**: द्वावा जिस देवीकी आराधना की जा रही थी, रंगवाले मनोहर वस्त्र यमुनाजीके तटपर छा रहे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12204)
- **Original**: वह कैसी है? तुम्हारी बस्तुओंकी रक्षा क्यों नहीं थे। उनकी गणना नहीं की जा सकती थी। उन
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12205)
- **Original**: कर रही है? सबके द्वारा यमुनाजीके उस तटकी बड़ी शोभा श्रीकृष्णकी यह बात सुनकर ब्रजाड्ननाओंको हो रही थी। चन्दन, अगुरु और कस्तूरीकी वायुसे
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12206)
- **Original**: बड़ी चिन्ता हुई। उन्होंने देखा, यमुनाजीके तटपर सारा तट-प्रान्त सुरभित था। भाँति-भाँतिके नैवेच्य,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12207)
- **Original**: न तो हमारे वस्त्र हैं और न वस्तुएँ ही। वे जलमें देश-कालके अनुसार प्राप्त होनेवाले फल, धूप,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12208)
- **Original**: नंगी खड़ी हो विषाद करने लगीं। जोर-जोरसे दीप, सिन्दूर और कुंकुम यमुनाके उस तटको
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12209)
- **Original**: रोने लगीं और बोलीं--'यहाँ रखे हुए हमारे वस्त्र सुशोभित कर रहे थे। जलमें उतरनेपर गोपियाँ
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12210)
- **Original**: कहाँ गये और पूजाकी वस्तुएँ भी कहाँ हैं? इस कौतूहलवश क्रीडाके लिये उन्मुख हुईं। उनका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12211)
- **Original**: प्रकार विषाद करके वे सब गोपकन्याएँ दोनों हाथ मन श्रीकृष्णको समर्पित था। वे अपने नग्र शरीरसे
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12212)
- **Original**: जोड़ भक्ति और विनयके साथ हाथ जोड़कर वहीं जल-क्रौड़ामें आसक्त हो गयीं। श्रीकृष्णने तटपर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12213)
- **Original**: श्यामसुन्दरसे बोलीं।' रखे हुए भाँति-भाँतिके द्रव्यों और वस्त्रोंको देखा।। . गोपिकाओंने कहा--गोविन्द! तुम्हीं हम देखकर वे ग्वाल-बालॉके साथ वहाँ गये और
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12214)
- **Original**: दासियोंके श्रेष्ठ स्वामी हो; अत: हमारे पहनने सारे वस्त्र लेकर वहाँ रखी हुई खाद्य वस्तुओंको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12215)
- **Original**: योग्य वस्त्रोंको तुम अपनी ही वस्तु समझो। उन्हें सखाओंके साथ खाने लगे। फिर कुछ वस्त्र लेकर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12216)
- **Original**: लेने या स्पर्श करनेका तुम्हें पूरा अधिकार है; बड़े हर्षके साथ उनका गट्टर बाँधा और कदम्बकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12217)
- **Original**: परंतु ब्रतके उपयोगमें आनेवाली जो दूसरी वस्तुएँ ऊँची डालपर चढ़कर गोविन्दने गोपिकाओंसे इस
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12218)
- **Original**: हैं, बे इस समय आराध्य देवताकी सम्पत्ति हैं; प्रकार कहा। उन्हें दिये बिना उन वस्तुओंको ले लेना तुम्हारे श्रीकृष्ण बोले--गोपियो! तुम सब-कौ-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12219)
- **Original**: लिये कदापि उचित नहीं है। हमारी साड़ियाँ दे सब इस ब्रतकर्ममें असफल हो गयीं। पहले मेरी
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12220)
- **Original**: दो; उन्हें पहनकर हम ब्रतकी पूर्ति करेंगी। बात सुनकर विधि-बिधानका पालन करो। उसके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12221)
- **Original**: श्यामसुन्दर! इस समय उनके अतिरिक्त अन्य बाद इच्छानुसार जलक्रीड़ा करना। जो मास व्रत
- **Translation**: 

---

