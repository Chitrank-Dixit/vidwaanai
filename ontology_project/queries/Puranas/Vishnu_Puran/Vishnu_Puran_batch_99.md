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

### Verse 1 (Vishnu Puran 0.1961)
- **Original**: 102 ददौ स दश धर्माय कद्यपाय त्रयोदश । सप्तविंशति सोमाय चतस्नो5रिप्टनेमिने
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1962)
- **Original**: 103 डे चैब बहुपुत्राय दे चैवाड्रिसे तथा। डे कृशाश्वाय विदुषे तासां नामानि मे श्रूणु
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1963)
- **Original**: 104 अरुन्धती वसुर्यामिर्लम्बा भानुर्मरुत्यती । सड्डल्पा च मुहूर्ता च साध्या विश्वा च॒ तादूझी । धर्मपल्यो दा त्वेतास्तास्वपत्वानि मे थृणु
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1964)
- **Original**: 105 विश्वेदेवास्तु विश्वाया: साध्वा साध्यानजायत । मसरुत्वत्यां मरुत्वनत्तो बसोश्न वसव: स्मृता: । भानोस्तु भानव:ः पुत्ना मुहूर्ताबां मुहूर्तजा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1965)
- **Original**: 106 लम्बायाश्षैव घोषो5थ नागबीधी तु याप्िजा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1966)
- **Original**: 107 पृथ्चिबीविष्य. सर्वमरूधत्यामजायत । सहूल्पायास्तु सर्वात्मा जज्ञे सक्ुल्प एवहि
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1967)
- **Original**: 108 ये त्वनेकवसुप्राणदेवा ज्योति:पुरोगमाः । बसवोःष्टी समास्यातास्तेषां वक्ष्यामि विस्तरम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1968)
- **Original**: 109 आपो धघ्रुवश्न सोमअ्र धर्मश्ैबानिलोइनल: । प्रत्यूषश् प्रभासक्ष वसवो नामभ्रि: स्मृता:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1969)
- **Original**: 110 आपस्य पुत्रो वैतण्ड: श्रम: झान्तों ध्वनिस्तथा । ध्रुवस्थ पुत्रों भगवान्कालो लछोकप्रकालन:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1970)
- **Original**: 111 सोमस्य भगवान्वर्न्ा वर्चस्वी येन जायते ।। 112 धर्मस्य पुत्रों द्रविणो हुतहव्यवहस्तथा । मनोहरायां झिश्शिरः प्राणो5थ वरुणस्तथा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1971)
- **Original**: 113 श्रीक्षिष्णुपुराण [ अ0 157 तब वे सब आपसमें एक-दूसरेसे कहने लगें---“महामृनि नारदजी ठीक कहते हैं; हमको भो, इसमें सन्देह नहीं, अपने भाइयोंके मार्गका ही अवल्म्बन करना चाहिये
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1972)
- **Original**: हम भी पृथिवीका परिमाण जानकर ही सुष्टि करेंगे ।' इस प्रकार सके भी उसी मार्गसे समस्त दिज्ञाओंको चले गये और समुद्रगत नदियोँंके समान आजतक नहीं ह्मौंटे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1973)
- **Original**: 97--99
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1974)
- **Original**: हे द्विज! तबसे हो यदि भाईकों स्वोजनेके र्त्ये भाई हो जाय ते बह नष्ट हो जाता है, अतः विज्ञ पुरुषको ऐसा न करना चाहिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1975)
- **Original**: महाभाग दक्ष प्रजापतिने उन पूत्रॉकों भी गये जान नारदजीपर बड़ा क्रोध किया और उन्‍हें द्ञाप दे दिया
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1976)
- **Original**: है चैत्रेय ! हमने सुना है कि फिर उस डिट्टान्‌ प्रजापतिने सर्गवृद्धिकी इच्झासे जैरुणीमें साठ कन्याएँ उत्पन्न की
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1977)
- **Original**: उनमेंसे उन्होंने दस घर्मको, तेरह कश्यपको, सत्ताईस सोम (चन्द्रमा) को और चार अरिश्नेमिको दीं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1978)
- **Original**: तथा दो बहुपुत्र, दो अज्लिरा और दो कृद्माश्चको विवाहीं। अब उनके नाम सुनो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1979)
- **Original**: 104 । अरुखती, बसु, यामी, एत्म्या, भानु, मरुत्वती, सड्लल्पा, मुहूर्ता, साध्या और विधा--ये दस धर्मकी पल्नियाँ थीं; अब तुम इनके पुत्रोंका विवरण सुनो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1980)
- **Original**: विश्वाके पुत्र क्शिदेवा थे, साध्यासे साध्यगण हुए, मरुत्वतीरें मस््यान्‌ और बसुस्े लखुगण हुए तथा भानुसे भानु और मुहूर्तासे मुहूर्ताभिमानी देवगण हुए
- **Translation**: 

---

