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

### Verse 1 (Mahabharat 0.7051)
- **Original**: जाती है। मन्दबुद्धि पुरुषके भीतर जो अधिमान होता है, यह ब्राह्मण भी अत्यन्त विश्वस्त होकर मेरे साथ बातचीत करते
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7051)
- **Original**: जाती है। मन्दबुद्धि पुरुषके भीतर जो अधिमान होता है, यह ब्राह्मण भी अत्यन्त विश्वस्त होकर मेरे साथ बातचीत करते
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7052)
- **Original**: उसकी लक्ष्मीका नाश करता है। गर्भ धारण करनेसे कन्या और मेरी कुझल पूछते हैं । ब्राह्मणोंके असावधान रहनेपर भी
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7052)
- **Original**: उसकी लक्ष्मीका नाश करता है। गर्भ धारण करनेसे कन्या और मेरी कुझल पूछते हैं । ब्राह्मणोंके असावधान रहनेपर भी
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7053)
- **Original**: और सदा घरमें रहनेसे ब्राह्मण दूषित समझे जाते हैं। मैं सदा सावधान रहता हूँ। उनके सोते रहनेपर भी मैं जागता
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7053)
- **Original**: और सदा घरमें रहनेसे ब्राह्मण दूषित समझे जाते हैं। मैं सदा सावधान रहता हूँ। उनके सोते रहनेपर भी मैं जागता
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7054)
- **Original**: . मेरे पिताने ऋन्द्रमासे यह बात सुनकर ब्राह्मणोंका पूजन रहता हूँ। वे मुझे झास्रीय मार्गपर चलनेबाला, ब्राह्मणभक्त
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7054)
- **Original**: . मेरे पिताने ऋन्द्रमासे यह बात सुनकर ब्राह्मणोंका पूजन रहता हूँ। वे मुझे झास्रीय मार्गपर चलनेबाला, ब्राह्मणभक्त
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7055)
- **Original**: किया था, उन्हींकी भाँति मैं भी उत्तम व्रत धारण करनेवाले तथा दोषदृष्टिसे रहित जानकर अपने सदुपदेशके अमृतसे
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7055)
- **Original**: किया था, उन्हींकी भाँति मैं भी उत्तम व्रत धारण करनेवाले तथा दोषदृष्टिसे रहित जानकर अपने सदुपदेशके अमृतसे
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7056)
- **Original**: ब्राह्मणोंकी पूजा करता हूँ। सौंचते रहते हैं। संतुष्ट होकर थे मुझसे जो कुछ कहते हैं, उसे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7056)
- **Original**: ब्राह्मणोंकी पूजा करता हूँ। सौंचते रहते हैं। संतुष्ट होकर थे मुझसे जो कुछ कहते हैं, उसे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7057)
- **Original**: . भीष्जी कहते हैं--दानवराज झग्बरके मुँहसे यह वचन मैं अपनी बुद्धिके द्वारा ग्रहण करता हूँ। मेरा मन सदा
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7057)
- **Original**: . भीष्जी कहते हैं--दानवराज झग्बरके मुँहसे यह वचन मैं अपनी बुद्धिके द्वारा ग्रहण करता हूँ। मेरा मन सदा
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7058)
- **Original**: सुनकर इतने ब्राह्मणोंका पूजन किया, इससे उन्हें महेतद्रपदकी ब्राह्मणोंमें लगा रहता है और मैं सदा उनके अनुकूल विचार
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7058)
- **Original**: सुनकर इतने ब्राह्मणोंका पूजन किया, इससे उन्हें महेतद्रपदकी ब्राह्मणोंमें लगा रहता है और मैं सदा उनके अनुकूल विचार
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7059)
- **Original**: प्राप्ति हुईं। दा दानपात्र पुरुषोंकी परीक्षा "और ख्री-रक्षाके विषयमें देवशर्मा तथा-विपुलकी कथा सुधिहिसते पूछा-+पितामह ! द्ानका पात्र कौन होता है ?
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7059)
- **Original**: प्राप्ति हुईं। दा दानपात्र पुरुषोंकी परीक्षा "और ख्री-रक्षाके विषयमें देवशर्मा तथा-विपुलकी कथा सुधिहिसते पूछा-+पितामह ! द्ानका पात्र कौन होता है ?
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7060)
- **Original**: मौनत्रतके कारण। जो मनुष्य (यज्ञ करने या गुरुदक्षिणा अपरिचित पुरुष या बहुत दिनोंतक अपने साथ रहा हुआ
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7060)
- **Original**: मौनत्रतके कारण। जो मनुष्य (यज्ञ करने या गुरुदक्षिणा अपरिचित पुरुष या बहुत दिनोंतक अपने साथ रहा हुआ
- **Translation**: 

---

