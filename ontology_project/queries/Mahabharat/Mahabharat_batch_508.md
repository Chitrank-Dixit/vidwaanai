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

### Verse 1 (Mahabharat 0.5071)
- **Original**: योद्धाओंको सुनाकर बोले--'मैं दुःशासनकी बाँह उखाड़ सिंह जैसे बहुत बड़े हाथीकों दबोच लेता है, उसी प्रकार
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5071)
- **Original**: योद्धाओंको सुनाकर बोले--'मैं दुःशासनकी बाँह उखाड़ सिंह जैसे बहुत बड़े हाथीकों दबोच लेता है, उसी प्रकार
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5072)
- **Original**: छेता हुँ, अब यह प्राण त्यागना ही चाहता है। जिसमें ताकत उन्होंने कर्ण और दुर्वोधनके सामने ही दुःशासनकों धर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5072)
- **Original**: छेता हुँ, अब यह प्राण त्यागना ही चाहता है। जिसमें ताकत उन्होंने कर्ण और दुर्वोधनके सामने ही दुःशासनकों धर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5073)
- **Original**: हो बह आकर इसको मेरे हांथसे बचा ले।' इस्त प्रकार दबाया। इसके बाद उसकी ओर आँखें गड़कर देखते हुए
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5073)
- **Original**: हो बह आकर इसको मेरे हांथसे बचा ले।' इस्त प्रकार दबाया। इसके बाद उसकी ओर आँखें गड़कर देखते हुए
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5074)
- **Original**: समस्त बीरोंपर आक्षेप करके महाबली भीमने क्रोधमें भरकर भीमने तलवार उठायी और एक पैस्से उसका गला दबा
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5074)
- **Original**: समस्त बीरोंपर आक्षेप करके महाबली भीमने क्रोधमें भरकर भीमने तलवार उठायी और एक पैस्से उसका गला दबा
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5075)
- **Original**: उसकी बाँह उखाड़ ली। दुःशासनकी वह धुजा बज्रके समाते दिया। उस समय दुःझासन थर-थर काँप रहा था। अब
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5075)
- **Original**: उसकी बाँह उखाड़ ली। दुःशासनकी वह धुजा बज्रके समाते दिया। उस समय दुःझासन थर-थर काँप रहा था। अब
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5076)
- **Original**: कठोर थी, भीमसेन उसीसे सब बीरोंके सामने उसको पीटने उसकी ओर देख भीमसेन बोले--'दुःशासन ! याद है न यह
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5076)
- **Original**: कठोर थी, भीमसेन उसीसे सब बीरोंके सामने उसको पीटने उसकी ओर देख भीमसेन बोले--'दुःशासन ! याद है न यह
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5077)
- **Original**: छगे। इसके बाद दुःशासनकी छाती फाइकर वें उसका दिन, जब कि तूने कर्ण और दुर्ोधनके साथ बड़े हर्षमें
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5077)
- **Original**: छगे। इसके बाद दुःशासनकी छाती फाइकर वें उसका दिन, जब कि तूने कर्ण और दुर्ोधनके साथ बड़े हर्षमें
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5078)
- **Original**: भरकर मुझे “बैल' कहा था। दुशत्मर्‌! राजसूय-यज्ञपें । अवभृषस्रानसे पवित्र हुए महारानी ड्रोपदीके केझोंको
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5078)
- **Original**: भरकर मुझे “बैल' कहा था। दुशत्मर्‌! राजसूय-यज्ञपें । अवभृषस्रानसे पवित्र हुए महारानी ड्रोपदीके केझोंको
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5079)
- **Original**: तूने किस हाथसे खींचा था ? बता, आज भीमसेन तुझसे इसका उत्तर चाहता है।' भीमका यह भयंकर बचन सुनकर दुःशासनने उनकी ओर देखा। उस समय उसकी त्यौरी बदल गयी, वह क्रोधसे जल उठा और बड़े आवेधझमें आकर बोला--'यह है यह
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5079)
- **Original**: तूने किस हाथसे खींचा था ? बता, आज भीमसेन तुझसे इसका उत्तर चाहता है।' भीमका यह भयंकर बचन सुनकर दुःशासनने उनकी ओर देखा। उस समय उसकी त्यौरी बदल गयी, वह क्रोधसे जल उठा और बड़े आवेधझमें आकर बोला--'यह है यह
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5080)
- **Original**: हाथ, जो हाथीके शुण्ड-दण्डके समान बलि है, जिसने
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5080)
- **Original**: हाथ, जो हाथीके शुण्ड-दण्डके समान बलि है, जिसने
- **Translation**: 

---

