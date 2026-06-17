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

### Verse 1 (Mahabharat 0.2031)
- **Original**: पूछा कि “ये किसके हैं?” उत्तरसे बोले, 'राजकुमार ! मेरी आज्ञा मानकर तुम ज्ञीघ्र ही
- **Translation**: 

---

### Verse 2 (Mahabharat 0.2031)
- **Original**: पूछा कि “ये किसके हैं?” उत्तरसे बोले, 'राजकुमार ! मेरी आज्ञा मानकर तुम ज्ञीघ्र ही
- **Translation**: 

---

### Verse 3 (Mahabharat 0.2032)
- **Original**: . अर्जुले कहा--राजकुमार ! इनमें यह तो अर्जुनका इस वृक्षपरसे धनुष उतारो, ये तुन्हारे धनुष मेरे बाहुबछूको
- **Translation**: 

---

### Verse 4 (Mahabharat 0.2032)
- **Original**: . अर्जुले कहा--राजकुमार ! इनमें यह तो अर्जुनका इस वृक्षपरसे धनुष उतारो, ये तुन्हारे धनुष मेरे बाहुबछूको
- **Translation**: 

---

### Verse 5 (Mahabharat 0.2033)
- **Original**: सुप्रसिद्ध गाण्डीज धनुष है। यह संग्रामधूमिसे शन्ुुओंकी सहन नहीं कर सकेंगे। इस वृक्षपर पाण्डबोंके झस््र रखे हुए
- **Translation**: 

---

### Verse 6 (Mahabharat 0.2033)
- **Original**: सुप्रसिद्ध गाण्डीज धनुष है। यह संग्रामधूमिसे शन्ुुओंकी सहन नहीं कर सकेंगे। इस वृक्षपर पाण्डबोंके झस््र रखे हुए
- **Translation**: 

---

### Verse 7 (Mahabharat 0.2034)
- **Original**: सेनाको क्षणभरमें न्ट-भ्रह्ठ कर डालता है, तीनों ल्लेकॉमें हैं।' यह सुनकर राजकुमार उत्तर रथसे उतर पड़ा और उसे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.2034)
- **Original**: सेनाको क्षणभरमें न्ट-भ्रह्ठ कर डालता है, तीनों ल्लेकॉमें हैं।' यह सुनकर राजकुमार उत्तर रथसे उतर पड़ा और उसे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.2035)
- **Original**: इसकी सुप्रसिद्धि है और यह सभी झख्रोंसे बढ़ा-चढ़ा है। यह विवश होकर उस वृक्षपर चढ़ना पड़ा। अर्जुनने रथपर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.2035)
- **Original**: इसकी सुप्रसिद्धि है और यह सभी झख्रोंसे बढ़ा-चढ़ा है। यह विवश होकर उस वृक्षपर चढ़ना पड़ा। अर्जुनने रथपर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.2036)
- **Original**: अकेला ही एक त्यख झखस्तरोंकी बराबरी करनेवाला है। बैठे-बैठे ही फिर आज्ञा दी, 'इन्हें झटपट उतार लाओ, देरी
- **Translation**: 

---

### Verse 12 (Mahabharat 0.2036)
- **Original**: अकेला ही एक त्यख झखस्तरोंकी बराबरी करनेवाला है। बैठे-बैठे ही फिर आज्ञा दी, 'इन्हें झटपट उतार लाओ, देरी
- **Translation**: 

---

### Verse 13 (Mahabharat 0.2037)
- **Original**: अजुनने इसीके द्वारा संप्राममें देशता और मनुष्योंकों परास्त मत करो और जल्दी ही इनके ऊपर जो ब्नादि लिपटे हुए हैं,
- **Translation**: 

---

### Verse 14 (Mahabharat 0.2037)
- **Original**: अजुनने इसीके द्वारा संप्राममें देशता और मनुष्योंकों परास्त मत करो और जल्दी ही इनके ऊपर जो ब्नादि लिपटे हुए हैं,
- **Translation**: 

---

### Verse 15 (Mahabharat 0.2038)
- **Original**: किया था। देखो, यह चित्र-विचित्र रंगोंसे सुझओभित, उन्हें खोल दो । उत्तर पाण्डवोंके उन अत्पुत्तम धनुषोंको लेकर
- **Translation**: 

---

### Verse 16 (Mahabharat 0.2038)
- **Original**: किया था। देखो, यह चित्र-विचित्र रंगोंसे सुझओभित, उन्हें खोल दो । उत्तर पाण्डवोंके उन अत्पुत्तम धनुषोंको लेकर
- **Translation**: 

---

### Verse 17 (Mahabharat 0.2039)
- **Original**: लखकीला और गाँठ आदिसे रहित है। आरम्भमें एक हजार नीले उतरा और उनपर लिपटे हुए पत्तोंको हटाकर उन्हें
- **Translation**: 

---

### Verse 18 (Mahabharat 0.2039)
- **Original**: लखकीला और गाँठ आदिसे रहित है। आरम्भमें एक हजार नीले उतरा और उनपर लिपटे हुए पत्तोंको हटाकर उन्हें
- **Translation**: 

---

### Verse 19 (Mahabharat 0.2040)
- **Original**: वर्षतक तो इसे ब्रह्माजीने धारण किया था। फिर पाँच सौ अर्जुनके आगे रखा। उत्तस्को गाण्डीबके सिया वहाँ चार
- **Translation**: 

---

### Verse 20 (Mahabharat 0.2040)
- **Original**: वर्षतक तो इसे ब्रह्माजीने धारण किया था। फिर पाँच सौ अर्जुनके आगे रखा। उत्तस्को गाण्डीबके सिया वहाँ चार
- **Translation**: 

---

