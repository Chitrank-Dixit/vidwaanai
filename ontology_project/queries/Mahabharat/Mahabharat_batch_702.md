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

### Verse 1 (Mahabharat 0.7011)
- **Original**: सुखदायक दिव्य पुष्पोंकी बारम्बार वर्षा की। इतनेहीमें एक इतनेमें बाज भी वहाँ आकर बोला--“राजन्‌ ! यह
- **Translation**: 

---

### Verse 2 (Mahabharat 0.7011)
- **Original**: सुखदायक दिव्य पुष्पोंकी बारम्बार वर्षा की। इतनेहीमें एक इतनेमें बाज भी वहाँ आकर बोला--“राजन्‌ ! यह
- **Translation**: 

---

### Verse 3 (Mahabharat 0.7012)
- **Original**: विधान उपस्थित हुआ। जिसमें सुवर्णके महल बने हुए थे, कबूतर मेरा भोजन है। इसके मास, मज्जा, रक्त और मेदेसे
- **Translation**: 

---

### Verse 4 (Mahabharat 0.7012)
- **Original**: विधान उपस्थित हुआ। जिसमें सुवर्णके महल बने हुए थे, कबूतर मेरा भोजन है। इसके मास, मज्जा, रक्त और मेदेसे
- **Translation**: 

---

### Verse 5 (Mahabharat 0.7013)
- **Original**: सोने और मणियोंकी बच्चनवारें लगी थीं और बैदूर्यमणिके मेरा हित होनेवाला है। यह मेरी घूख मिथाकर मेरी पूर्ण दृप्ति
- **Translation**: 

---

### Verse 6 (Mahabharat 0.7013)
- **Original**: सोने और मणियोंकी बच्चनवारें लगी थीं और बैदूर्यमणिके मेरा हित होनेवाला है। यह मेरी घूख मिथाकर मेरी पूर्ण दृप्ति
- **Translation**: 

---

### Verse 7 (Mahabharat 0.7014)
- **Original**: खम्मे झोभा पा रहे थे। राज्िं उज्ीनर उस विभानमें बैठकर कर सकता है। आप मेरे और इसके बीचमें न पड़िये। मुझे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.7014)
- **Original**: खम्मे झोभा पा रहे थे। राज्िं उज्ीनर उस विभानमें बैठकर कर सकता है। आप मेरे और इसके बीचमें न पड़िये। मुझे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.7015)
- **Original**: सनातन स्त्रेककों प्राप्त हुए। युधिष्ठिर ! तुष्हें भी झरणागत धूंखकी ज्वाला जल्मा रही है, आप इस कबृतरको छोड़
- **Translation**: 

---

### Verse 10 (Mahabharat 0.7015)
- **Original**: सनातन स्त्रेककों प्राप्त हुए। युधिष्ठिर ! तुष्हें भी झरणागत धूंखकी ज्वाला जल्मा रही है, आप इस कबृतरको छोड़
- **Translation**: 

---

### Verse 11 (Mahabharat 0.7016)
- **Original**: प्राणियोंकी इसी प्रकार रक्षा करनी चाहिये। जो मनुष्य अपने दीजिये,*मैं जड़ों दूरसे इसके पीछे उड़ता आ रहा हूँ। मेरे
- **Translation**: 

---

### Verse 12 (Mahabharat 0.7016)
- **Original**: प्राणियोंकी इसी प्रकार रक्षा करनी चाहिये। जो मनुष्य अपने दीजिये,*मैं जड़ों दूरसे इसके पीछे उड़ता आ रहा हूँ। मेरे
- **Translation**: 

---

### Verse 13 (Mahabharat 0.7017)
- **Original**: भक्त, प्रेमी और झरणागत पुरुषोंकी रक्षा करता है तथा सब नाखून और परोंसे यह काफी घायल हो चुका है, अब इसमें
- **Translation**: 

---

### Verse 14 (Mahabharat 0.7017)
- **Original**: भक्त, प्रेमी और झरणागत पुरुषोंकी रक्षा करता है तथा सब नाखून और परोंसे यह काफी घायल हो चुका है, अब इसमें
- **Translation**: 

---

### Verse 15 (Mahabharat 0.7018)
- **Original**: प्राणियोपर दया रखता है, वह परल्मेकर्ये सुख पाता है। जो
- **Translation**: 

---

### Verse 16 (Mahabharat 0.7018)
- **Original**: प्राणियोपर दया रखता है, वह परल्मेकर्ये सुख पाता है। जो
- **Translation**: 

---

### Verse 17 (Mahabharat 0.7019)
- **Original**: 516 संक्षिप्त महाभारत [ अनुजासनपर्व राजा होकर सबके साथ सदबर्ताब है, वह
- **Translation**: 

---

### Verse 18 (Mahabharat 0.7019)
- **Original**: 516 संक्षिप्त महाभारत [ अनुजासनपर्व राजा होकर सबके साथ सदबर्ताब है, वह
- **Translation**: 

---

### Verse 19 (Mahabharat 0.7020)
- **Original**: गये । यदि दूसरा कोई पुरुष भी इसी प्रकार झरणागतकी रक्षा अपने किस वस्तुको नहीं छेता ?
- **Translation**: 

---

### Verse 20 (Mahabharat 0.7020)
- **Original**: गये । यदि दूसरा कोई पुरुष भी इसी प्रकार झरणागतकी रक्षा अपने किस वस्तुको नहीं छेता ?
- **Translation**: 

---

