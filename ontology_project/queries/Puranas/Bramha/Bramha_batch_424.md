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

### Verse 1 (Bramha 0.8461)
- **Original**: अनुसंधान करना चाहिये। जो इस विनाशशील इन्द्रियेकि संयोग--उनकी एकाग्रताको ही योग कहते
- **Translation**: 

---

### Verse 2 (Bramha 0.8462)
- **Original**: शरीरमें अव्यक्तभावसे स्थित परमपूजित परमेश्ररका हैं। मुनिवरो! इस प्रकार मैंने संसार-बन्धनसे मुक्तिके
- **Translation**: 

---

### Verse 3 (Bramha 0.8463)
- **Original**: ज्ञानमयों दृष्टिसे निरन्तर साक्षात्कार करता रहता है, साधनभूत मोक्षदायक योगका यर्णन किया। वह मृत्युके पश्चात्‌ ब्रह्मभावको प्राप्त होता है। ज्ञानीजन मुनि बोले--द्विजक्रेश! आपके मुखरूपी समुद्रसे
- **Translation**: 

---

### Verse 4 (Bramha 0.8464)
- **Original**: विद्या-विनयसम्पन्त ब्राह्मणमें तथा गौ, हाथी, कुत्ते निकले हुए वचनामृतका पान करनेसे हमें ठृत्ति होती
- **Translation**: 

---

### Verse 5 (Bramha 0.8465)
- **Original**: और चाण्डालमें भी समभावसे ही देखनेवाले होते नहीं दिखायी देती। अतः पुन: मोक्षदायक योग और
- **Translation**: 

---

### Verse 6 (Bramha 0.8466)
- **Original**: हैं।* जिससे यह सम्पूर्ण जगत्‌ व्याप्त है, वह परमात्मा सांख्यका विस्तारपूर्वक वर्णन कीजिये। तपस्या,
- **Translation**: 

---

### Verse 7 (Bramha 0.8467)
- **Original**: समस्त चराचर प्राणियोंके भीतर निवास करता है। ब्रह्मयचर्य, सर्वस्वत्याग और बुद्धि-जिस उपायसे मन
- **Translation**: 

---

### Verse 8 (Bramha 0.8468)
- **Original**: जब जीवात्मा सम्पूर्ण प्राणियोंमें अपनेको और अपनेमें और इद्धियोंकी एकाग्रता प्राप्त हो सके, वह बतलानेकी
- **Translation**: 

---

### Verse 9 (Bramha 0.8469)
- **Original**: सम्पूर्ण प्राणियोंकों स्थित देखता है, उस समय बह कृपा कोजिये। अह्यभावको प्राप्त हो जाता है। अपने शरीरके भीतर व्यासजीने कहा--विद्या, तप, इद्धियनिग्रह और
- **Translation**: 

---

### Verse 10 (Bramha 0.8470)
- **Original**: जैसा आत्मा है, वैसा ही दूसरेंके शरीरमें भी सर्वस्वत्यागके ब्रिगा कोई भी सिद्धि नहीं पा
- **Translation**: 

---

### Verse 11 (Bramha 0.8471)
- **Original**: है--जिस पुरुषको निरन्‍्तर ऐसा झ्ान बना रहता है, सकता। सम्पूर्ण महाभूत विधाताकी पहली सृष्टि है।
- **Translation**: 

---

### Verse 12 (Bramha 0.8472)
- **Original**: वह अमृतत्व (मोक्ष)- को प्राप्त होता है
- **Translation**: 

---

### Verse 13 (Bramha 0.8473)
- **Original**: जो बे प्राणियेंकि शरीरमें भरे हुए हैं। पृथ्वौसे देहका
- **Translation**: 

---

### Verse 14 (Bramha 0.8474)
- **Original**: सम्पूर्ण प्राणियोंका आत्मा होकर सबके हितमें लगा निर्माण हुआ है। चिकनाहट और पसोने आदि जलके
- **Translation**: 

---

### Verse 15 (Bramha 0.8475)
- **Original**: हुआ है, जिसका अपना कोई मार्ग नहीं है तथा जो अंश हैं। अग्निसे नेत्र तथा बायुसे प्राण और अपान
- **Translation**: 

---

### Verse 16 (Bramha 0.8476)
- **Original**: ब्रह्मपदको प्राप्त करना चाहता है, उसके मार्गकी उत्पन्न हुए हैं। नाक, कान आदिके छिद्र आकाशतत्त्वके
- **Translation**: 

---

### Verse 17 (Bramha 0.8477)
- **Original**: खोज करनेमें देवता भी मोहित हो जाते हैं। जैसे » विधयाविनवसम्पन्ने ब्राह्मणे गति हस्तिनि। शुनि चैव 'फाके थ पण्डिता: समदर्शिन:
- **Translation**: 

---

### Verse 18 (Bramha 0.8478)
- **Original**: 20) * स्वंधूतेषु चात्मानं सर्वभूतानि चात्मनि
- **Translation**: 

---

### Verse 19 (Bramha 0.8479)
- **Original**: यदा पश्यति भूृतात्या ब्रह्म सम्पद्तते तदा
- **Translation**: 

---

### Verse 20 (Bramha 0.8480)
- **Original**: यावागात्मनि येदात्मा ताबानात्मा परात्मनि।य एवं सतत येद सो5मृतत्वाय कस्पते
- **Translation**: 

---

