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

### Verse 1 (Markende Puran 0.341)
- **Original**: पहुँचाते, वे पृत्युकालमें प्राणधांतिनी बेदनाक्ा बारंबार अनुभक्ष किया है, उसे बतलाता हूँ;
- **Translation**: 

---

### Verse 2 (Markende Puran 0.342)
- **Original**: अनुभव नहीं करते। मोह और अज्ञान फैल्ानेवाले सुनिये। बह क्षणभक्नुर संक्षार-चक्र प्रबाहरूपसे
- **Translation**: 

---

### Verse 3 (Markende Puran 0.343)
- **Original**: लोग महान्‌ भयकी प्राप्त होते हैं। नीच मतुष्द तीक्न अजर है, निरन्तर चलते रहनेवाला है, क्रभी स्थिर
- **Translation**: 

---

### Verse 4 (Markende Puran 0.344)
- **Original**: वेदनाओंसे पीड़ित होते 26ते हैं। छो झूठी गत्राह़ी नहीं रहता। तात! आपकी आज्ञासे मैँ मृत्युकालसे
- **Translation**: 

---

### Verse 5 (Markende Puran 0.345)
- **Original**: देते, झूठ बोलते, बुरी ब्रात्नोंका उपदेश देते और लेकर अबतकको सब बातोंका वर्णन करता हूँ।
- **Translation**: 

---

### Verse 6 (Markende Puran 0.346)
- **Original**: वेदोंकी निन्‍दा करते हैं, वे सत्र लोग मूल्छांग्रस्त शरीरमें जो गर्मी या पित्त है, वह तीन्न बायुसे
- **Translation**: 

---

### Verse 7 (Markende Puran 0.347)
- **Original**: होकर मृत्युक्रों प्रास्त होते हैं। प्रेरित होकर जब अत्यन्त कुपित हो जाता है, उल्
- **Translation**: 

---

### Verse 8 (Markende Puran 0.348)
- **Original**: ऐसे ज्ञोगोंको मृत्युके समय यमग़जके दुष्ट समय बिना ईंधनके ही उद्दी् हुई अग्निकी भाँति
- **Translation**: 

---

### Verse 9 (Markende Puran 0.349)
- **Original**: दूत हाथोंमें हथौड़ी एवं मुद्रर लिये आते हैं, दे बढ़कर मर्मस्थानोंकों विदीर्ण कर देता है, तत्पश्रात्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.350)
- **Original**: बड़े भयज्लूर होते हैं और उनकी देहसे दुर्गन्ध उदान नामक वायु ऊपरकी ओर उठता है और
- **Translation**: 

---

### Verse 11 (Markende Puran 0.351)
- **Original**: निकलती रहती है। ठन यमदूतोंपर दृष्टि पड़ते हो खाये-पीये हुए अज्न-जलकों नीचेकी ओर जानेसे
- **Translation**: 

---

### Verse 12 (Markende Puran 0.352)
- **Original**: मनुष्य छाँप उठता है और श्राता, माता तथा रोक देता डै। उस आपत्तिकी अवस्थामें भी
- **Translation**: 

---

### Verse 13 (Markende Puran 0.353)
- **Original**: पुत्रोंका नाम लेकर बारंबार चिह्लने लगता हैं। उसीको प्रमन्नता रहती है, जिसने पहले जल, अन्न
- **Translation**: 

---

### Verse 14 (Markende Puran 0.354)
- **Original**: उस समय उम्तकी वाणों स्पष्ट समझमें नहों एबं रसका दान किया हैं। जिस पुरुषने श्रद्धासे
- **Translation**: 

---

### Verse 15 (Markende Puran 0.355)
- **Original**: आती। एक ही शब्द, एक हो आवाज-सी जान पवित्र किये हुए अन्तःकरणके द्वारा पहले अन्नदान
- **Translation**: 

---

### Verse 16 (Markende Puran 0.356)
- **Original**: पड़ती है। भय्के पारें रोगीकी आँखें झूमने लगती किया है, वह उस रुग्णावस्थामें अन्नके बिना भी
- **Translation**: 

---

### Verse 17 (Markende Puran 0.357)
- **Original**: हैं और उसका मुख सूख जाता है। उसकी साँस तृसि लाभ करता है। जिसने कभी सिंश्या भाषण
- **Translation**: 

---

### Verse 18 (Markende Puran 0.358)
- **Original**: ऊपरको उठने लगती है। दृश्टिकी शक्ति भी नए नहीं किया, दो प्रेमियोंके पारस्परिक प्रेपें ब्राथा
- **Translation**: 

---

### Verse 19 (Markende Puran 0.359)
- **Original**: हो जाती है, फिर तरह अत्यन्त बेंदनासे पीड़ित नहीं डालो तथा जो आस्तिक और श्रद्धालु है, बह
- **Translation**: 

---

### Verse 20 (Markende Puran 0.360)
- **Original**: होकर उस शरीरकों छोड़ देता हैं और वायुके सुखपूर्तक मृत्थुकी प्राप्त होता हैं। जो देवता और
- **Translation**: 

---

