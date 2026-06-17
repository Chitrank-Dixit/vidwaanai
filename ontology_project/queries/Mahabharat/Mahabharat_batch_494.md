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

### Verse 1 (Mahabharat 0.4931)
- **Original**: हो जायैगे। बाणोंकी मारसे आपके पुतन्रोंकी सेनाको अत्यन्त संताप
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4931)
- **Original**: हो जायैगे। बाणोंकी मारसे आपके पुतन्रोंकी सेनाको अत्यन्त संताप
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4932)
- **Original**: . भौससेत ओोले--सूत ! आज अकेले मैं ही समस्त देने छगे।
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4932)
- **Original**: . भौससेत ओोले--सूत ! आज अकेले मैं ही समस्त देने छगे।
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4933)
- **Original**: कौरबोंको मार गिराऊँगा या वे ही मुझे पीड़ित करेंगे। इस उस घमासान युद्धमें बहुत-से झन्ुओंद्वारा घिरे हुए
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4933)
- **Original**: कौरबोंको मार गिराऊँगा या वे ही मुझे पीड़ित करेंगे। इस उस घमासान युद्धमें बहुत-से झन्ुओंद्वारा घिरे हुए
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4934)
- **Original**: भीमसेन अपने सारथिसे बोले--“सारथे ! तू घोड़ोंको तेज हॉँककर मुझे ज्ञीघ्र धृतराष्रके पुत्रोंके पास ले चल, आज उन सबको मैं यमल्प्रेक पहुँचाये देता हूँ।' आज्ञा पाते ही सारचिने
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4934)
- **Original**: भीमसेन अपने सारथिसे बोले--“सारथे ! तू घोड़ोंको तेज हॉँककर मुझे ज्ञीघ्र धृतराष्रके पुत्रोंके पास ले चल, आज उन सबको मैं यमल्प्रेक पहुँचाये देता हूँ।' आज्ञा पाते ही सारचिने
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4935)
- **Original**: घोड़ोंकी खाक तेज की और तुरंत ही रथ लिये आपके
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4935)
- **Original**: घोड़ोंकी खाक तेज की और तुरंत ही रथ लिये आपके
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4936)
- **Original**: पुत्रोंकी सेनामें,जा पहुँचा। कौरव-पक्षके योद्धा भी सब ' ओरसे हाथी, घोड़े, रथ और पैंदलॉको साथ ले आगे बढ़ आये
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4936)
- **Original**: पुत्रोंकी सेनामें,जा पहुँचा। कौरव-पक्षके योद्धा भी सब ' ओरसे हाथी, घोड़े, रथ और पैंदलॉको साथ ले आगे बढ़ आये
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4937)
- **Original**: भीमके रथपर चारों ओस्से बाणोंकी बौछार होने लगी _ और भीम उन सबको अपने बाणोंसे काटने छगे। उन्होंने शत्बुओंके छोड़े हुए प्रत्येक बाणके दो-दो, तीन-तीन टुकड़े कर डाल्े। तदनन्तर, उनके द्वारा मारे गये हाथी , घोड़े, रथ और पैदल जबानोंका चीत्कार सुनायी देने छगा। भीमसेनके ् 23 0 उन्होंने उनपर सब ओस्से थावा कर दिया । तब भीमने अपना
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4937)
- **Original**: भीमके रथपर चारों ओस्से बाणोंकी बौछार होने लगी _ और भीम उन सबको अपने बाणोंसे काटने छगे। उन्होंने शत्बुओंके छोड़े हुए प्रत्येक बाणके दो-दो, तीन-तीन टुकड़े कर डाल्े। तदनन्तर, उनके द्वारा मारे गये हाथी , घोड़े, रथ और पैदल जबानोंका चीत्कार सुनायी देने छगा। भीमसेनके ् 23 0 उन्होंने उनपर सब ओस्से थावा कर दिया । तब भीमने अपना
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4938)
- **Original**: है: जप प्रच॒ण्ड वेग प्रकट किया, जिसे झत्नु रेक न सके । महात्या . ख स्क्ष््ज/पव््स्स्ड भीषके द्वारा भस्म होती हुई आपको सेना भयभीत हो रणसे
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4938)
- **Original**: है: जप प्रच॒ण्ड वेग प्रकट किया, जिसे झत्नु रेक न सके । महात्या . ख स्क्ष््ज/पव््स्स्ड भीषके द्वारा भस्म होती हुई आपको सेना भयभीत हो रणसे
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4939)
- **Original**: है (- डि /2*/ $ भारा चली। यह देख भीम प्रसन्न होकर पुनः अपने सारथिसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4939)
- **Original**: है (- डि /2*/ $ भारा चली। यह देख भीम प्रसन्न होकर पुनः अपने सारथिसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4940)
- **Original**: 2 द जोले--'सूत ! थे जो ध्वजाओंसहित बहुत-से रथ इस ओर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4940)
- **Original**: 2 द जोले--'सूत ! थे जो ध्वजाओंसहित बहुत-से रथ इस ओर
- **Translation**: 

---

