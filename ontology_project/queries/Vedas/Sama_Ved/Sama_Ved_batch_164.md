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

### Verse 1 (Sama Ved 0.3261)
- **Original**: अपनी सामर्थ्य से निठल्ले दुष्टों को पीड़ित करता हुआ यह सोम, उन्हें मर्यादित रखता है और हिंसक दुष्टों का विनाश कर देता है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3262)
- **Original**: 1273. एतमुत्यं दश क्षिपो हरि हिन्वन्ति यातवे
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3263)
- **Original**: स्वायुध॑ मदिन्तमम्‌
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3264)
- **Original**: श्रेष्ठ प्राण-शक्ति की धारण करने वाला हरिताभ सोम, दसों अँगुलियों द्वारा निचोड़ा जाकर समर्पित किया जाता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3265)
- **Original**: इति द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3266)
- **Original**: के के के
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3267)
- **Original**: तृतीय: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3268)
- **Original**: 1274. एघ उ स्य वृषा रथो5व्या वारेभिरव्यत। गच्छन्वाजं सहस्लनिणम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3269)
- **Original**: रथ के सदृशद्वेगवान, अभीष्ठ अनन-प्रदायक यह सोम, कलश में छलनी के द्वारा छाना जाता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3270)
- **Original**: 1275. एतं त्रितस्य योषणो हरिं हिन्वन्त्यद्रिभि: । इन्दुमिन्द्राय पीतये
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3271)
- **Original**: इन्द्रदेव द्वारा प्रयुक्त किये जाने के लिए यह हरिताभ सोम त्रित (तीन प्रकार से - अंतरिक्ष में, भौतिक यंत्रों में तथा शरीरस्थ तंत्र में) निचोड़ा जा रहा है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3272)
- **Original**: 1276. एघ स्य मानुषीष्वा श्येनो न विक्षु सीदति । गच्छ॑ जारो न योषितम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3273)
- **Original**: जिस प्रकार बाज़ पक्षी अपने शिकार के प्रति तथा प्रेमी अपनी प्रियतमा के प्रति वेगपूर्वक जाता है, उसी प्रकार यह सोम मानवों के बीच शौघतापूर्वक पहुँचकर प्रतिष्ठित होता है.
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3274)
- **Original**: 1277. एष स्य मद्यो रसो5व चष्टे दिव: शिशु: । य इन्दुर्वारमाविशत्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3275)
- **Original**: चुलोक में उत्पन्न हुआ यह आनन्दवर्द्धक सोम, सबको देखता हुआ (प्राकृतिक) छलनी से शुद्ध होता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3276)
- **Original**: 1278. एष स्य पीतये सुतो हरिर्षति धर्णसिः। क्रन्दन्योनिमभि प्रियम्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3277)
- **Original**: सबको धारण करने वाला यह अविनाशी सोम, देवों के पीने के लिए तैयार किया गया है, जो ध्वनि करता हुआ अपने प्रिय निवास स्थान, कलश में प्रवेश करता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3278)
- **Original**: 10.4 सापवेद-संहिता 1279. एत॑ त्यं हरितो दश मर्मुज्यन्ते अपस्युव:। याभिर्मदाय शुम्भते
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3279)
- **Original**: इद्रदेव को प्रसन करने के लिए वज्ञार्थ दसों अँगुलियाँ उस सोम को शोधित करती हैं
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3280)
- **Original**: [() इद् »जीव चेतना, () दसों अँगुलियाँ -+ दशेन्द्रियाँ, (
- **Translation**: 

---

