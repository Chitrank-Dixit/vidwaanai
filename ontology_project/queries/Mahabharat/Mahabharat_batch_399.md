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

### Verse 1 (Mahabharat 0.3981)
- **Original**: गये। मैं युद्धमें अर्जुनकी रक्षा करना जितना आवश्यक आज सारी पृथ्वी उसके बकमें हो जाती। उसने भी उनपर
- **Translation**: 

---

### Verse 2 (Mahabharat 0.3981)
- **Original**: गये। मैं युद्धमें अर्जुनकी रक्षा करना जितना आवश्यक आज सारी पृथ्वी उसके बकमें हो जाती। उसने भी उनपर
- **Translation**: 

---

### Verse 3 (Mahabharat 0.3982)
- **Original**: समझता हूँ उतनी पिता, माता, तुम-जैसे भाइयों और अपने झक्ति-प्रहारका विद्यार किया था; पर युद्धमें भगवान्‌
- **Translation**: 

---

### Verse 4 (Mahabharat 0.3982)
- **Original**: समझता हूँ उतनी पिता, माता, तुम-जैसे भाइयों और अपने झक्ति-प्रहारका विद्यार किया था; पर युद्धमें भगवान्‌
- **Translation**: 

---

### Verse 5 (Mahabharat 0.3983)
- **Original**: प्राणोंकी भी रक्षा आवश्यक नहीं मानता। तीनों स्लोकोंके आ्रीकृष्णके निकट जाते ही उसपर ऐसा पोह छा जाता कि यह
- **Translation**: 

---

### Verse 6 (Mahabharat 0.3983)
- **Original**: प्राणोंकी भी रक्षा आवश्यक नहीं मानता। तीनों स्लोकोंके आ्रीकृष्णके निकट जाते ही उसपर ऐसा पोह छा जाता कि यह
- **Translation**: 

---

### Verse 7 (Mahabharat 0.3984)
- **Original**: राज्यकी अपेक्षा भी यदि कोई दुर्लभ वस्तु हो तो उसे भी मैं थात भूल जाती थी। उधरसे भगवान्‌ सदा ही बड़े-बड़े
- **Translation**: 

---

### Verse 8 (Mahabharat 0.3984)
- **Original**: राज्यकी अपेक्षा भी यदि कोई दुर्लभ वस्तु हो तो उसे भी मैं थात भूल जाती थी। उधरसे भगवान्‌ सदा ही बड़े-बड़े
- **Translation**: 

---

### Verse 9 (Mahabharat 0.3985)
- **Original**: अर्जुनके बिना नहीं चाहता। इसीलिये आज अर्जुनमानो महारियोंको कर्णसे लड़नेके लिये भेजा कस्ते थे, वे निरन्तर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.3985)
- **Original**: अर्जुनके बिना नहीं चाहता। इसीलिये आज अर्जुनमानो महारियोंको कर्णसे लड़नेके लिये भेजा कस्ते थे, वे निरन्तर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.3986)
- **Original**: मरकर जी उठे हैं, ऐसा समझकर मुझे बड़ा आनन्द हो रहा है। इसी फिक्रमें रहते कि कैसे कर्णकी झक्तिकों व्यर्थ कर दूँ।
- **Translation**: 

---

### Verse 12 (Mahabharat 0.3986)
- **Original**: मरकर जी उठे हैं, ऐसा समझकर मुझे बड़ा आनन्द हो रहा है। इसी फिक्रमें रहते कि कैसे कर्णकी झक्तिकों व्यर्थ कर दूँ।
- **Translation**: 

---

### Verse 13 (Mahabharat 0.3987)
- **Original**: यही बजह है कि इस राश्रिमें मैंने राक्षमको ही कर्णसे लड़नेके महाराज ! जो कर्णसे अर्जुनकी इस प्रकार रक्षा करते थे, वे
- **Translation**: 

---

### Verse 14 (Mahabharat 0.3987)
- **Original**: यही बजह है कि इस राश्रिमें मैंने राक्षमको ही कर्णसे लड़नेके महाराज ! जो कर्णसे अर्जुनकी इस प्रकार रक्षा करते थे, वे
- **Translation**: 

---

### Verse 15 (Mahabharat 0.3988)
- **Original**: लिये भेजा था; उसके सिया दूसरा कोई कर्णको नहीं दबा अपनी रक्षा क्‍यों नहीं करते ? तीनों ल्तेकॉमें कोई भी ऐसा
- **Translation**: 

---

### Verse 16 (Mahabharat 0.3988)
- **Original**: लिये भेजा था; उसके सिया दूसरा कोई कर्णको नहीं दबा अपनी रक्षा क्‍यों नहीं करते ? तीनों ल्तेकॉमें कोई भी ऐसा
- **Translation**: 

---

### Verse 17 (Mahabharat 0.3989)
- **Original**: सकता था। पुरुष नहीं है, जो जनादनपर विजय पा सके। महाराज ! अर्जुनका प्रिय और हित करलेमें निरन्तर रूगे घटोत्कचके मारे जानेपर सात्यकिने भी भगवान्‌ कृष्णसे
- **Translation**: 

---

### Verse 18 (Mahabharat 0.3989)
- **Original**: सकता था। पुरुष नहीं है, जो जनादनपर विजय पा सके। महाराज ! अर्जुनका प्रिय और हित करलेमें निरन्तर रूगे घटोत्कचके मारे जानेपर सात्यकिने भी भगवान्‌ कृष्णसे
- **Translation**: 

---

### Verse 19 (Mahabharat 0.3990)
- **Original**: रहनेबाले भगवान्‌ श्रीकृष्णने सात्यकिके पूछनेपर यही उत्तर यही प्रश्न किया था कि 'भगवन्‌ ! जब कर्णने वह अमोध
- **Translation**: 

---

### Verse 20 (Mahabharat 0.3990)
- **Original**: रहनेबाले भगवान्‌ श्रीकृष्णने सात्यकिके पूछनेपर यही उत्तर यही प्रश्न किया था कि 'भगवन्‌ ! जब कर्णने वह अमोध
- **Translation**: 

---

