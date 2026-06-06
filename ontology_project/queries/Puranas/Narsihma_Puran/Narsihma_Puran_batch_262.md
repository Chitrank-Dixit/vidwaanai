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

### Verse 1 (Narsihma Puran 0.5221)
- **Original**: 68 / इस प्रकार सृत- भाद्राजादि- संकादकूप ऑनरसिंहपुराणमें इसके 'सर्वाद:खड़ारी माहत्प्दज्ञा यजक कक अड्सठवाँ अध्याय पूरा हुआ
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.5222)
- **Original**: 68 # अ्गथब+ बे रमरमरर
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.5223)
- **Original**: त् “कल्याण ' के पुनर्मुद्रित विशेषाडू कृष्णाहु इश्वराकू
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.5224)
- **Original**: सं0 वाल्मीकीय रामायणाडु
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.5225)
- **Original**: संक्षिप्त पश्षपुराण संक्षिप्त मार्कण्डेयपुराण
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.5226)
- **Original**: सं0 स्कन्दपुराणाडु
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.5227)
- **Original**: भक्त-चरिताडू बालक-अड्ड 435
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.5228)
- **Original**: भ्रगवन्नाम-महिमा और प्रार्थना-अड्डू $72
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.5229)
- **Original**: परलोक-पुनर्जन्माद्ल गर्ग-संहिता-[ भगयान्‌ श्रीराधाकृष्णकी पक्ष
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.5230)
- **Original**: / 4 सानुताद
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.5231)
- **Original**: सं0 अग्रिपुराण
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.5232)
- **Original**: श्रीगणेश-अड्ू 42
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.5233)
- **Original**: हनुमान-अड्डू-- 136।
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.5234)
- **Original**: सं0 श्रीवराहपुराण 797
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.5235)
- **Original**: सूर्याद्भ 584
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.5236)
- **Original**: 2] के । 628
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.5237)
- **Original**: रामभक्ति-अद्भू 7732
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.5238)
- **Original**: धर्मशास्त्राडू
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.5239)
- **Original**: कूर्मपुराणाडू द्याता [34 सरणकषला-अह ह््प 24 किद-कणक सत्कथा-अ्ू
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.5240)
- **Original**: तीर्थाकु
- **Translation**: 

---

