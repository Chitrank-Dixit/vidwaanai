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

### Verse 1 (Mahabharat 0.6481)
- **Original**: उत्तम तप हैं; इनका पालन करनेवाला मनुष्य नित्य उपबासी दया करना, किसीकी चुगली न करना तथा स्केगोंकी
- **Translation**: 

---

### Verse 2 (Mahabharat 0.6481)
- **Original**: उत्तम तप हैं; इनका पालन करनेवाला मनुष्य नित्य उपबासी दया करना, किसीकी चुगली न करना तथा स्केगोंकी
- **Translation**: 

---

### Verse 3 (Mahabharat 0.6482)
- **Original**: और सतत ब्रह्मचारी कहा गया है। त्यागी और विनयी ब्राह्मण झ्षिकायत, मिथ्याभाषण, निन्‍्दा और स्तुतिसे दूर रहना,
- **Translation**: 

---

### Verse 4 (Mahabharat 0.6482)
- **Original**: और सतत ब्रह्मचारी कहा गया है। त्यागी और विनयी ब्राह्मण झ्षिकायत, मिथ्याभाषण, निन्‍्दा और स्तुतिसे दूर रहना,
- **Translation**: 

---

### Verse 5 (Mahabharat 0.6483)
- **Original**: ही मुनि तथा देवता माना जाता है। अतः वह कुदुष्बके साथ सबकी भल्ाईकी इच्छा रखना तथा भविष्यमें आनेवाले
- **Translation**: 

---

### Verse 6 (Mahabharat 0.6483)
- **Original**: ही मुनि तथा देवता माना जाता है। अतः वह कुदुष्बके साथ सबकी भल्ाईकी इच्छा रखना तथा भविष्यमें आनेवाले
- **Translation**: 

---

### Verse 7 (Mahabharat 0.6484)
- **Original**: रहकर भी सदा धर्मपालनकी इच्छा रखे और नित्य जाग्रतू सुख-दुःखकी चित्ता न कस्ना--यें सब गुण दमके पालनसे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.6484)
- **Original**: रहकर भी सदा धर्मपालनकी इच्छा रखे और नित्य जाग्रतू सुख-दुःखकी चित्ता न कस्ना--यें सब गुण दमके पालनसे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.6485)
- **Original**: (सावधान) रहे। मांस कभी न ख़ाय। सदा पत्ित्र रहे। प्रकट होते हैं। जितेन्द्रिय पुरुष किसीके साथ बैर नहीं करता,
- **Translation**: 

---

### Verse 10 (Mahabharat 0.6485)
- **Original**: (सावधान) रहे। मांस कभी न ख़ाय। सदा पत्ित्र रहे। प्रकट होते हैं। जितेन्द्रिय पुरुष किसीके साथ बैर नहीं करता,
- **Translation**: 

---

### Verse 11 (Mahabharat 0.6486)
- **Original**: यज्ञसे बचे हुए अमृतमय अन्नका भोजन तथा देवता और उसका ससबके साथ अच्छा बर्ताव होता है। वह निन्दा और
- **Translation**: 

---

### Verse 12 (Mahabharat 0.6486)
- **Original**: यज्ञसे बचे हुए अमृतमय अन्नका भोजन तथा देवता और उसका ससबके साथ अच्छा बर्ताव होता है। वह निन्दा और
- **Translation**: 

---

### Verse 13 (Mahabharat 0.6487)
- **Original**: अतिथियोंकी पूजा करें। उसे सदा यज्ञश्रिष्ट अन्नका भोक्ता; स्तुतिमें समान भाव रखनेवाला, सदाचारी, झीलबान,
- **Translation**: 

---

### Verse 14 (Mahabharat 0.6487)
- **Original**: अतिथियोंकी पूजा करें। उसे सदा यज्ञश्रिष्ट अन्नका भोक्ता; स्तुतिमें समान भाव रखनेवाला, सदाचारी, झीलबान,
- **Translation**: 

---

### Verse 15 (Mahabharat 0.6488)
- **Original**: अतिथिसेवाका ब्रती, श्रद्धालु और देवता तथा ब्राह्मणोंकी प्रसन्नचित्त, वैर्यथान्‌ तथा दोषोंका दमन करनलेमें समर्थ होता
- **Translation**: 

---

### Verse 16 (Mahabharat 0.6488)
- **Original**: अतिथिसेवाका ब्रती, श्रद्धालु और देवता तथा ब्राह्मणोंकी प्रसन्नचित्त, वैर्यथान्‌ तथा दोषोंका दमन करनलेमें समर्थ होता
- **Translation**: 

---

### Verse 17 (Mahabharat 0.6489)
- **Original**: पूजा करनेवाला होना चाहिये। है। दमनझील पुरुष समस्त प्राणियोंको दुर्लभ बस्तुएँ युधिढिरते पूछ--पितामह ! मनुष्य नित्य उपवासी, सतत देकर--दूसरोंको सुख पहुँचाकर स्वयं प्रसन्न और सुखी होता
- **Translation**: 

---

### Verse 18 (Mahabharat 0.6489)
- **Original**: पूजा करनेवाला होना चाहिये। है। दमनझील पुरुष समस्त प्राणियोंको दुर्लभ बस्तुएँ युधिढिरते पूछ--पितामह ! मनुष्य नित्य उपवासी, सतत देकर--दूसरोंको सुख पहुँचाकर स्वयं प्रसन्न और सुखी होता
- **Translation**: 

---

### Verse 19 (Mahabharat 0.6490)
- **Original**: ब्रह्मचारी, यज्ञशिष्ट अन्नका भोक्ता तथा अतिथिसेवाका ब्रती है। वह सबके हितमें लूगा रहता है और किसीसे द्वेष नहीं
- **Translation**: 

---

### Verse 20 (Mahabharat 0.6490)
- **Original**: ब्रह्मचारी, यज्ञशिष्ट अन्नका भोक्ता तथा अतिथिसेवाका ब्रती है। वह सबके हितमें लूगा रहता है और किसीसे द्वेष नहीं
- **Translation**: 

---

