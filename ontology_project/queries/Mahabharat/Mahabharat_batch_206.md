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

### Verse 1 (Mahabharat 0.2051)
- **Original**: फिर रथके भीतर घुसकर बैठ गया। उस झद्घध्वनि, धतुषकी टक्कर, ध्यजामें रहनेवाले अमानुषी भूतोंकी हु्डार
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2051)
- **Original**: फिर रथके भीतर घुसकर बैठ गया। उस झद्घध्वनि, धतुषकी टक्कर, ध्यजामें रहनेवाले अमानुषी भूतोंकी हु्डार
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2052)
- **Original**: गाण्डीबकी टक्लार और रथकी घरघराहटसे धरती दहल उठी । ज्ज्बैना अर्जुनसे युद्ध करनेके विषयमें कौरव महारथियॉमें विवाद इस भीषण झब्दकों सुनकर कौरवसेनायें द्रोणाचार्यी कह्ा--
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2052)
- **Original**: गाण्डीबकी टक्लार और रथकी घरघराहटसे धरती दहल उठी । ज्ज्बैना अर्जुनसे युद्ध करनेके विषयमें कौरव महारथियॉमें विवाद इस भीषण झब्दकों सुनकर कौरवसेनायें द्रोणाचार्यी कह्ा--
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2053)
- **Original**: करके खड़े हो जाये। यह मेघगर्जनके समान जो रथकी भीषण घरघराहट सुनायी दे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2053)
- **Original**: करके खड़े हो जाये। यह मेघगर्जनके समान जो रथकी भीषण घरघराहट सुनायी दे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2054)
- **Original**: . अब राज़ा दु्योधनने भीष्य, ड्रोण और महारथी कृपाचार्यसे रही है, जिससे पृथ्वीमें भी कम्प होने ूगा है--इससे जान
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2054)
- **Original**: . अब राज़ा दु्योधनने भीष्य, ड्रोण और महारथी कृपाचार्यसे रही है, जिससे पृथ्वीमें भी कम्प होने ूगा है--इससे जान
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2055)
- **Original**: कह--मैंने और कर्णने आचार्यच्रणसे यह बात कई बार पड़ता है कि यह अर्जुनके सिया कोई और नहीं है। देखो, हमारे
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2055)
- **Original**: कह--मैंने और कर्णने आचार्यच्रणसे यह बात कई बार पड़ता है कि यह अर्जुनके सिया कोई और नहीं है। देखो, हमारे
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2056)
- **Original**: कही है और फिर भी कहता हूँ, पाण्डवोंसे हमारी यह बात झख्नोंकी कान्ति फीकी पड़ गयी है, घोड़े भी प्रसन्न नहीं जान
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2056)
- **Original**: कही है और फिर भी कहता हूँ, पाण्डवोंसे हमारी यह बात झख्नोंकी कान्ति फीकी पड़ गयी है, घोड़े भी प्रसन्न नहीं जान
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2057)
- **Original**: ठहरी थी कि जूएमें हारनेपर उन्हें बारह वर्षतक वनमें रहता पड़ते और अभिक्षेत्रोंकी अप्रियाँ भी प्रकाशहीन-सी हो रही हैं;
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2057)
- **Original**: ठहरी थी कि जूएमें हारनेपर उन्हें बारह वर्षतक वनमें रहता पड़ते और अभिक्षेत्रोंकी अप्रियाँ भी प्रकाशहीन-सी हो रही हैं;
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2058)
- **Original**: पड़ेगा तथा एक वर्षतक किसी नगर या बनमें अज्ञातवास इससे जान पड़ता है कि कोई अच्छा परिणाम नहीं होगा। सभी
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2058)
- **Original**: पड़ेगा तथा एक वर्षतक किसी नगर या बनमें अज्ञातवास इससे जान पड़ता है कि कोई अच्छा परिणाम नहीं होगा। सभी
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2059)
- **Original**: करना पड़ेगा। अभी इनका तेरहवाँ वर्ष पूरा नहीं हुआ है; योद्धाओंके मुख निस्तेज और मन उदास दिखायी देते हैं।
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2059)
- **Original**: करना पड़ेगा। अभी इनका तेरहवाँ वर्ष पूरा नहीं हुआ है; योद्धाओंके मुख निस्तेज और मन उदास दिखायी देते हैं।
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2060)
- **Original**: और यदि उसके पूरे होनेसे पहले ही अर्जुन हमारे सामने आ अतः हम गौओंको हस्तिनापुरकी ओर भेजकर व्यूहरचना
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2060)
- **Original**: और यदि उसके पूरे होनेसे पहले ही अर्जुन हमारे सामने आ अतः हम गौओंको हस्तिनापुरकी ओर भेजकर व्यूहरचना
- **Translation**: 

---

