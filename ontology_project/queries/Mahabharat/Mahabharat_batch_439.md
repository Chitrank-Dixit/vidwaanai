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

### Verse 1 (Mahabharat 0.4381)
- **Original**: देख लेना। जरा मेरी इन बतन्रके समान मोटी और गैंठीली 0 >> बाक:ज् री“ 7 44 2: कक 1
- **Translation**: 

---

### Verse 2 (Mahabharat 0.4381)
- **Original**: देख लेना। जरा मेरी इन बतन्रके समान मोटी और गैंठीली 0 >> बाक:ज् री“ 7 44 2: कक 1
- **Translation**: 

---

### Verse 3 (Mahabharat 0.4382)
- **Original**: ब्राण और सुवर्णपत्रसे तो । मैं और मेरे हितके लिये केबल प्रेमके ही नाते कर्णका सारथ्य
- **Translation**: 

---

### Verse 4 (Mahabharat 0.4382)
- **Original**: ब्राण और सुवर्णपत्रसे तो । मैं और मेरे हितके लिये केबल प्रेमके ही नाते कर्णका सारथ्य
- **Translation**: 

---

### Verse 5 (Mahabharat 0.4383)
- **Original**: अपने तेजसे सारी कमल के बकण है करना स्वीकार कर लीजिये। आपके सारथि बन जानेपर
- **Translation**: 

---

### Verse 6 (Mahabharat 0.4383)
- **Original**: अपने तेजसे सारी कमल के बकण है करना स्वीकार कर लीजिये। आपके सारथि बन जानेपर
- **Translation**: 

---

### Verse 7 (Mahabharat 0.4384)
- **Original**: क्लिन्न-भिन्न कर सकता हूँ और समुद्रोंकों सुखा सकता हैँ। राधापुत्र कर्ण मेरे झन्रुओंको परास्त कर देगा। आपके सिवा
- **Translation**: 

---

### Verse 8 (Mahabharat 0.4384)
- **Original**: क्लिन्न-भिन्न कर सकता हूँ और समुद्रोंकों सुखा सकता हैँ। राधापुत्र कर्ण मेरे झन्रुओंको परास्त कर देगा। आपके सिवा
- **Translation**: 

---

### Verse 9 (Mahabharat 0.4385)
- **Original**: इस प्रकार झत्नुऑंका दमन करनेमें पूर्णतया समर्थ होनेपर कर्णके घोड़ोंकी रास पकड़ने योग्य कोई दूसरा व्यक्ति नहीं
- **Translation**: 

---

### Verse 10 (Mahabharat 0.4385)
- **Original**: इस प्रकार झत्नुऑंका दमन करनेमें पूर्णतया समर्थ होनेपर कर्णके घोड़ोंकी रास पकड़ने योग्य कोई दूसरा व्यक्ति नहीं
- **Translation**: 

---

### Verse 11 (Mahabharat 0.4386)
- **Original**: श्री तुम मुझे इस नीच सूतपुत्रके सारध्यका काम करनेकी है। आप संग्राममें साक्षात्‌ श्रीकृष्णके समान हैं। अत» जिस
- **Translation**: 

---

### Verse 12 (Mahabharat 0.4386)
- **Original**: श्री तुम मुझे इस नीच सूतपुत्रके सारध्यका काम करनेकी है। आप संग्राममें साक्षात्‌ श्रीकृष्णके समान हैं। अत» जिस
- **Translation**: 

---

### Verse 13 (Mahabharat 0.4387)
- **Original**: आज्ञा कैसे दे रहे हो? मैं इस नोचकी अपेक्षा सभी
- **Translation**: 

---

### Verse 14 (Mahabharat 0.4387)
- **Original**: आज्ञा कैसे दे रहे हो? मैं इस नोचकी अपेक्षा सभी
- **Translation**: 

---

### Verse 15 (Mahabharat 0.4388)
- **Original**: 16 संक्षिप्त महाभारत [ कर्णफर्व प्रकार श्रेष्ठ हूँ, इसलिये उसका दासत्व करनेको कभी तैयार
- **Translation**: 

---

### Verse 16 (Mahabharat 0.4388)
- **Original**: 16 संक्षिप्त महाभारत [ कर्णफर्व प्रकार श्रेष्ठ हूँ, इसलिये उसका दासत्व करनेको कभी तैयार
- **Translation**: 

---

### Verse 17 (Mahabharat 0.4389)
- **Original**: है, मेरे मस्तकपर झास््नानुसार राज्याभिषेक किया गया है, नहीं हो सकता। जो पुरुष प्रेमकश्ष अपने आश्रित हुए किसी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.4389)
- **Original**: है, मेरे मस्तकपर झास््नानुसार राज्याभिषेक किया गया है, नहीं हो सकता। जो पुरुष प्रेमकश्ष अपने आश्रित हुए किसी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.4390)
- **Original**: लोग मुझे महारथी कहते हैं और वन्दीजन मेरी स्तुति किया श्रेष्ठ व्यक्तिको नीच पुरुषके अधीन कर देता है, उसे उच्चको
- **Translation**: 

---

### Verse 20 (Mahabharat 0.4390)
- **Original**: लोग मुझे महारथी कहते हैं और वन्दीजन मेरी स्तुति किया श्रेष्ठ व्यक्तिको नीच पुरुषके अधीन कर देता है, उसे उच्चको
- **Translation**: 

---

