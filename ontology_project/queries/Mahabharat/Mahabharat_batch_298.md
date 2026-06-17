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

### Verse 1 (Mahabharat 0.2971)
- **Original**: ही ग्रहण करता है; अज्ञानके द्वारा ज्ञान ढका हुआ है, उसीसे निःसंदेह ऐसा माने कि मैं कुछ भी नहीं करता । जो पुरुष सब
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2971)
- **Original**: ही ग्रहण करता है; अज्ञानके द्वारा ज्ञान ढका हुआ है, उसीसे निःसंदेह ऐसा माने कि मैं कुछ भी नहीं करता । जो पुरुष सब
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2972)
- **Original**: सब जीव मोहित हो रहे हैं। परंतु जिनका जह अज्ञान कमोंको परमात्मामें अर्पण करके और आसक्तिको त्यागकर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2972)
- **Original**: सब जीव मोहित हो रहे हैं। परंतु जिनका जह अज्ञान कमोंको परमात्मामें अर्पण करके और आसक्तिको त्यागकर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2973)
- **Original**: परमात्माके ज्ञानड्वारा नष्ट कर दिया गया है, उनका वह ज्ञान
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2973)
- **Original**: परमात्माके ज्ञानड्वारा नष्ट कर दिया गया है, उनका वह ज्ञान
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2974)
- **Original**: 600 संक्षिप्त महाभारत [ भीष्परर्ष सूर्यके सदृश उस सश्षिदानन्दघन परमात्पाकों प्रकाशित कर
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2974)
- **Original**: 600 संक्षिप्त महाभारत [ भीष्परर्ष सूर्यके सदृश उस सश्षिदानन्दघन परमात्पाकों प्रकाशित कर
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2975)
- **Original**: नाश होनेसे पहले-पहले ही काम-क्रोबसे उत्पन्न होनेवाले देता है। जिनका मन तथूप है; जिनकी बुद्धि तदप है और
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2975)
- **Original**: नाश होनेसे पहले-पहले ही काम-क्रोबसे उत्पन्न होनेवाले देता है। जिनका मन तथूप है; जिनकी बुद्धि तदप है और
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2976)
- **Original**: वेगको सहन करलेमें समर्थ हो जाता है, जही पुरुष योगी है सखिदानन्दघन परमात्पामें ही जिनकी निरन्‍्तर एकीभावसे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2976)
- **Original**: वेगको सहन करलेमें समर्थ हो जाता है, जही पुरुष योगी है सखिदानन्दघन परमात्पामें ही जिनकी निरन्‍्तर एकीभावसे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2977)
- **Original**: और यही सुखी है। जो पुरुष निश्चयपूर्वक अन्तरात्पामें ही स्थिति है, ऐसे तत्परायण पुरुष ज्ञानके द्वारा पापरहित होकर
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2977)
- **Original**: और यही सुखी है। जो पुरुष निश्चयपूर्वक अन्तरात्पामें ही स्थिति है, ऐसे तत्परायण पुरुष ज्ञानके द्वारा पापरहित होकर
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2978)
- **Original**: सुखवाल्मा है, आत्पामें ही रमण करनेवाल्ा है तथा जो अपुनरणाृत्तिको प्राप्त होते हैं। थे ज्ञानीजन विद्या और
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2978)
- **Original**: सुखवाल्मा है, आत्पामें ही रमण करनेवाल्ा है तथा जो अपुनरणाृत्तिको प्राप्त होते हैं। थे ज्ञानीजन विद्या और
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2979)
- **Original**: आत्पायें ही ज्ञानवाला है, बह सखछिदानन्दघन पखह्ा बिनययुक्त ब्राह्मणमें तथा गौ, हाथी, कुत्ते और चाण्डालमें भी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2979)
- **Original**: आत्पायें ही ज्ञानवाला है, बह सखछिदानन्दघन पखह्ा बिनययुक्त ब्राह्मणमें तथा गौ, हाथी, कुत्ते और चाण्डालमें भी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2980)
- **Original**: परमात्याके साथ एकीभावको प्राप्त सांख्ययोगी झात्त ब्रह्मको समदर्शी ही होते हैं। जिनका मन समत्वभावमें स्थित है, उनके
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2980)
- **Original**: परमात्याके साथ एकीभावको प्राप्त सांख्ययोगी झात्त ब्रह्मको समदर्शी ही होते हैं। जिनका मन समत्वभावमें स्थित है, उनके
- **Translation**: 

---

