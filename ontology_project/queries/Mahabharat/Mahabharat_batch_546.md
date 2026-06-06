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

### Verse 1 (Mahabharat 0.5451)
- **Original**: पाँच-पाँच बाण मारकर बींध डाला। बींधना आरम्भ कर दिया। भीमसेनने शल्यकों पहले एक
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5451)
- **Original**: पाँच-पाँच बाण मारकर बींध डाला। बींधना आरम्भ कर दिया। भीमसेनने शल्यकों पहले एक
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5452)
- **Original**: तब सात्यकिने क्रोधमें भरकर झाल्यपर तोमरका प्रहार और फिर सात बाणोंसे घायल किया। सात्यकिने उन्हें सौ किया, भीमसेनने सर्पके समान नाराच चलाया, नकुरूने बाण मारकर सिंहके समान गर्जना की। नकुलने पाँच और
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5452)
- **Original**: तब सात्यकिने क्रोधमें भरकर झाल्यपर तोमरका प्रहार और फिर सात बाणोंसे घायल किया। सात्यकिने उन्हें सौ किया, भीमसेनने सर्पके समान नाराच चलाया, नकुरूने बाण मारकर सिंहके समान गर्जना की। नकुलने पाँच और
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5453)
- **Original**: झंक्ति छोड़ी और सहदेवने गदा तथा धर्मराजने झतप्लीका बार सहतदेवने सात बाणोंसे झल्यको बींधकर पुन: सात सायकोंसे
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5453)
- **Original**: झंक्ति छोड़ी और सहदेवने गदा तथा धर्मराजने झतप्लीका बार सहतदेवने सात बाणोंसे झल्यको बींधकर पुन: सात सायकोंसे
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5454)
- **Original**: किया। इस तरह पाँच वीरोंके चलाये हुए पाँच असर एक घायल किया।
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5454)
- **Original**: किया। इस तरह पाँच वीरोंके चलाये हुए पाँच असर एक घायल किया।
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5455)
- **Original**: ही साथ झल्यकी ओर छूटे, किंतु शल्यने अपने झख्ोंसे इन महारथियोंसे पीड़ित होकर भी झुस्वीर झल्य रणमें
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5455)
- **Original**: ही साथ झल्यकी ओर छूटे, किंतु शल्यने अपने झख्ोंसे इन महारथियोंसे पीड़ित होकर भी झुस्वीर झल्य रणमें
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5456)
- **Original**: मारकर उन सबको पीछे हटा दिया और सिंहके समान डटे रहे। उन्होंने सात्यकिको पश्चीस भीमसेनको तिहत्तर और
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5456)
- **Original**: मारकर उन सबको पीछे हटा दिया और सिंहके समान डटे रहे। उन्होंने सात्यकिको पश्चीस भीमसेनको तिहत्तर और
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5457)
- **Original**: गर्जना की। नकुछको सात बाणोंसे बींघ दिया। इसके बाद सहदेवके
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5457)
- **Original**: गर्जना की। नकुछको सात बाणोंसे बींघ दिया। इसके बाद सहदेवके
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5458)
- **Original**: . झन्नुकी यह गर्जना सात्यकिसे नहीं सही गयी। उन्होंने बाणसहित धनुषको काटकर उसे इक्कीस सायकोंसे घायल
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5458)
- **Original**: . झन्नुकी यह गर्जना सात्यकिसे नहीं सही गयी। उन्होंने बाणसहित धनुषको काटकर उसे इक्कीस सायकोंसे घायल
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5459)
- **Original**: दो बाणोंसे मद्राजको और तीससे उनके सारथ्षिको बींघध किया। सहदेवने भी दूसरा धनुष लेकर मामाजीको पाँच
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5459)
- **Original**: दो बाणोंसे मद्राजको और तीससे उनके सारथ्षिको बींघध किया। सहदेवने भी दूसरा धनुष लेकर मामाजीको पाँच
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5460)
- **Original**: डाला। तब झल्यने क्रोधमें भरकर पाण्डवपक्षके उन सभी बाण पारे। फिर एक बाणसे उनके सारधिको घायल किया,
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5460)
- **Original**: डाला। तब झल्यने क्रोधमें भरकर पाण्डवपक्षके उन सभी बाण पारे। फिर एक बाणसे उनके सारधिको घायल किया,
- **Translation**: 

---

