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

### Verse 1 (Vaivtpuran 44.8337)
- **Original**: हँसते हुए बालक और बालिकाओंका समूह था जाता है, तुम्हारे वे सभी सम्बन्धी शुद्ध मनवाले
- **Translation**: 

---

### Verse 2 (Vaivtpuran 44.8338)
- **Original**: और कैलासवासी आबालवृद्ध सभी उसकी ओर हैं। तुमने करुणासागर गुरु और अमोघ फरसा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 44.8339)
- **Original**: हर्षपूर्वक देख रहे थे। उस बालकको देखकर पाकर पहले क्षत्रिय-जातिपर परीक्षा करके पुन:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 44.8340)
- **Original**: पुत्रों तथा भृत्योंसहित शम्भुने घबराकर भक्तिपूर्वक गुरु-पुत्रपर परीक्षा की है। कहाँ तो श्रुतिमें 'गुरुको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 44.8341)
- **Original**: सिर झुकाकर प्रणाम किया। तत्पश्चात्‌ दुर्गने भी दक्षिणा देना उचित है'--यों सुना जाता है और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 44.8342)
- **Original**: दण्डकी भाँति भूमिपर लेटकर नमस्कार किया। कहाँ तुमने गुरुपुत्रके दाँतको ही तोड़ दिया, अब
- **Translation**: 

---

### Verse 7 (Vaivtpuran 44.8343)
- **Original**: तब बालकने सबको अभीष्टप्रद आशीर्वाद दिया। उसका मस्तक भी काट डालो। शंकरके वरदान
- **Translation**: 

---

### Verse 8 (Vaivtpuran 44.8344)
- **Original**: उसे देखकर सभी बालक भयके कारण महान्‌ तथा अमोघबीर्य फरसेसे तो चूहोंकों खानेवाला
- **Translation**: 

---

### Verse 9 (Vaivtpuran 44.8345)
- **Original**: आश्चर्यमें पड़ गये। तदनन्तर शिवजीने भक्तिपूर्वक सियार सिंह और शार्दूलकों भी मार सकता है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 44.8346)
- **Original**: उसे षोडशोपचार समर्पित करके उस परिपूर्णतमकी जितेन्द्रिय पुरुषोंमें श्रेष्ठ गणेश तुम्हारे-जैसे लाखों-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 44.8347)
- **Original**: वेदोक्त-विधिसे पूजा कौ और फिर सिर झुकाकर करोड़ों जन्तुओंको मार डालनेकी शक्ति रखता है,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 44.8348)
- **Original**: काण्वशाखामें कहे हुए स्तोत्रद्वारा उन सनातन परंतु वह मक्खीपर हाथ नहीं उठाता। श्रीकृष्णके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 44.8349)
- **Original**: भगवान्‌की स्तुति की। उस समय उनके सर्वाड़िमें अंशसे उत्पन्न हुआ यह गणेश तेजमें श्रीकृष्णके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 44.8350)
- **Original**: रोमाक्ष हो आया था। पुनः जो रत्रसिंहासनपर ही समान है। अन्य देवता श्रीकृष्णकी कलाएँ हैं।। आसीन थे और अपने उत्कृष्ट तेजसे जिन्होंने इसीसे इसकी अग्रपूजा होती है। सबको आच्छादित कर रखा था, उन वामन यों कहकर पार्वती क्रोधवश उन परशुरामकों
- **Translation**: 

---

### Verse 15 (Vaivtpuran 44.8351)
- **Original**: भगवानूसे स्वयं शंकरजी कहने लगे। मारनेके लिये उद्चत हो गयीं। तब परशुरामने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 44.8352)
- **Original**: . शंकरजीने कहा--ब्रह्मनू! जो आत्माराम मन-ही-मन गुरुकों प्रणाम करके अपने इष्टदेव
- **Translation**: 

---

### Verse 17 (Vaivtpuran 44.8353)
- **Original**: हैं, उनके विषयमें कुशलप्रश्न करना अत्यन्त श्रीकृष्णका स्मरण किया। इतनेमें ही दुगने अपने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 44.8354)
- **Original**: विडम्बनाकी बात है; क्योंकि वे स्वयं कुशलके सामने एक अत्यन्त बौने ब्राह्मग-बालकको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 44.8355)
- **Original**: आधार और कुशल-अकुशलके प्रदाता हैं। उपस्थित देखा। उसकी कान्ति करोड़ों सूर्योंके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 44.8356)
- **Original**: श्रीकृष्णजी सेवाके फलोदयसे आज आप जो मुझे समान थी। उसके दाँत स्वच्छ थे। वह शुक्ल
- **Translation**: 

---

