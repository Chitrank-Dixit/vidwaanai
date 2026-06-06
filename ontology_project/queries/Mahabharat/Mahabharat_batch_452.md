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

### Verse 1 (Mahabharat 0.4511)
- **Original**: प्रयत्रपूर्वक्ष अपना अपराध क्षमा कराने। छूगा तो उस विजयं ग्राप्त करनेके लिये मैं अर्जुनपर अपना अप्रमेय और
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4511)
- **Original**: प्रयत्रपूर्वक्ष अपना अपराध क्षमा कराने। छूगा तो उस विजयं ग्राप्त करनेके लिये मैं अर्जुनपर अपना अप्रमेय और
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4512)
- **Original**: आ्राह्मणने कहा, 'सूतपुत्र ! मैंने जो बात कही है बह तो बदल अजेय ज्रह्माख छोड़ैगा। इस दिव्य अखके प्रभावसे मैं
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4512)
- **Original**: आ्राह्मणने कहा, 'सूतपुत्र ! मैंने जो बात कही है बह तो बदल अजेय ज्रह्माख छोड़ैगा। इस दिव्य अखके प्रभावसे मैं
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4513)
- **Original**: नहीं सकती। मिथ्याभाषण प्रजाका नाश करनेवाल्पर होता दंण्डपोँणि यम, पाशहस्त वरुण, गंदाधर कुबेर और
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4513)
- **Original**: नहीं सकती। मिथ्याभाषण प्रजाका नाश करनेवाल्पर होता दंण्डपोँणि यम, पाशहस्त वरुण, गंदाधर कुबेर और
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4514)
- **Original**: है। यदि मैं अपने कथनको मिथ्या कर दूँगा तो मुझे पाप बज्जपाणि इद्रसे तथा किसी अन्य आततायी झब्रुसे भी नहीं लूगेगा। अतः धर्मकी रक्षाके लिये मैं झूठ तो बोल नहीं डरता हुँ; अतः मुझे श्रीकृष्ण और अर्जुनसे भी किसी
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4514)
- **Original**: है। यदि मैं अपने कथनको मिथ्या कर दूँगा तो मुझे पाप बज्जपाणि इद्रसे तथा किसी अन्य आततायी झब्रुसे भी नहीं लूगेगा। अतः धर्मकी रक्षाके लिये मैं झूठ तो बोल नहीं डरता हुँ; अतः मुझे श्रीकृष्ण और अर्जुनसे भी किसी
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4515)
- **Original**: सकता। मुझसे झूठ बुलवाकर तुम मेरी ब्राह्मी गतिका प्रकारंकां भय नहीं है।
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4515)
- **Original**: सकता। मुझसे झूठ बुलवाकर तुम मेरी ब्राह्मी गतिका प्रकारंकां भय नहीं है।
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4516)
- **Original**: ञच्छेद न करे । लोकमें कोई भी मेरी बातको मिथ्या नहीं परंतु मुझे एक भय अवश्य है--एक बारंकी बात है,
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4516)
- **Original**: ञच्छेद न करे । लोकमें कोई भी मेरी बातको मिथ्या नहीं परंतु मुझे एक भय अवश्य है--एक बारंकी बात है,
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4517)
- **Original**: कर सकता। अतः अब तुम शात्त हो जाओ।' मैं विजयके उद्देश्यसे अख्ा पानेके लिये घूम झा था। उस
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4517)
- **Original**: कर सकता। अतः अब तुम शात्त हो जाओ।' मैं विजयके उद्देश्यसे अख्ा पानेके लिये घूम झा था। उस
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4518)
- **Original**: . इस प्रकार यद्यपि तुमने मेरा तिरस्कार किया है तो भी समय अनेकों भीषण बाणोंको चलानेका अध्यास
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4518)
- **Original**: . इस प्रकार यद्यपि तुमने मेरा तिरस्कार किया है तो भी समय अनेकों भीषण बाणोंको चलानेका अध्यास
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4519)
- **Original**: मैंने सौहार्दबझ तुम्हें यह असंग सुना दिया है। अब तुम चुप करते करते मैंने भूलसे एक होमथेंनुके बछड़ेकों बाण मार
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4519)
- **Original**: मैंने सौहार्दबझ तुम्हें यह असंग सुना दिया है। अब तुम चुप करते करते मैंने भूलसे एक होमथेंनुके बछड़ेकों बाण मार
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4520)
- **Original**: रहो और आगेकी बातपर ध्यान दो। तुम मेरे साथी, स्रेही दिया। बेचात बछड़ा निर्जन वनमें चर रहा था। यह देखकर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4520)
- **Original**: रहो और आगेकी बातपर ध्यान दो। तुम मेरे साथी, स्रेही दिया। बेचात बछड़ा निर्जन वनमें चर रहा था। यह देखकर
- **Translation**: 

---

