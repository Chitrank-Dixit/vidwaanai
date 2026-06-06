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

### Verse 1 (Vishnu Puran 0.12621)
- **Original**: श्रीपराहरजी घोले--तब खाण्डिक्य जनकने अपने जात्रु केशिध्वजके पास आकर कहा--'तुफ्हें जो कुछ पूछना हो पूछ लो, मैं उसबच्र उत्तर दूँगा'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12622)
- **Original**: हे द्विज ! तब केजिध्वजने जिस प्रकार धर्मधेनु मारी गयो थो बह सब वृत्तान्त खाप्डिक्ससे कहा और उसके लिये प्रायश्चित्त पूछा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12623)
- **Original**: खाण्डिक्यने भी वह सम्पूर्ण च्रायक्षित, जिसका कि उसके लिये विधान था, केदिभ्वजको विधिपूर्वक बतला दिया
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12624)
- **Original**: तदनन्तर हुए अर्थको जान लेनेपर महात्मा खाण्डिक्पकी आज्ञा लेकर वे यज्ञभूमिमें आये और क्रमद्ा: सम्पूर्ण कर्म समाप्त किया
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12625)
- **Original**: फिर कालक्रमसे यज्ञ समाप्त होनेपर अवभुथ (यज्ञान्त) स्लानके अनन्तर कृतकृत्थ होकर राजा केशिध्वजने सोचा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12626)
- **Original**: “मैंने सम्पूर्ण ऋत्विज्‌ ब्राह्मणोंक्र पूजन किया, समस्त सदस्यॉका मान किया याचकॉक्प्र उनकी इच्छित वस्तुएँ दीं, लोकाचारके अनुसार जो कुछ कर्तव्य था वह सभी गँने किया, तथापि न जाने, क्यों मेरे चित्तों किसी क्रियाका अभाव खटक रहा है 7”
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12627)
- **Original**: इस प्रकार सोचते-सोचते राजाकों स्मरण हुआ कि मैंने अभीतक स्वाष्डिक्यकों गुरु-दक्षिणा नहीं दी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12628)
- **Original**: हे मैत्रेय
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12629)
- **Original**: तब वे रथपर चढ़कर फिर उसी दुर्गम जनमें गये, जहाँ स्लाप्डिक्य रहते थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12630)
- **Original**: स्वाष्डिक्य भी उन्हें फिर शस्म धारण किये आते देख मारनेके लिये उच्यत हुए। तब राजा केद्धिध्बजने कहा--
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12631)
- **Original**: “'खाण्डिक्य ! तुम क्रोध न करो, मैं तुम्हारा कोई अनिष्ट करनेके लिये नहीं आया, बल्कि तुम्हें गुरु-दक्षिणा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12632)
- **Original**: डेडे6 श्रीविष्णुपुराण ( अच7 निष्पादितो मया याग: सम्यवक्‍त्वदुपदेशत: । सोऊह ते दातुमिच्छामि वृणीष्र्‌ गुरुदक्षिणाम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12633)
- **Original**: 43 अीपराइर उवाच भूयस्स मन्त्रिभिस्सारध मन्त्रयामास पार्थिव: । गुरुनिष्क्रयकामो5यं कि मया प्रार्श्यतामिति
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12634)
- **Original**: 44 तमूचुर्मन्त्रिणो राज्यमशेषं प्रार्थ्यतामयम्‌ । जन्नुभिः प्रार्थ्यते राज्यमनायासितसैनिकैः
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12635)
- **Original**: 45 प्रहस्य तानाह नृपस्स खाण्डिक्यो महामति: । स्वल्पकालं महीपाल्य मादृषैः प्रार्थ्ते कथम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12636)
- **Original**: 46 एबमेतद्भवन्तोडत्न॒ हार्थसाधनमन्त्रिण: । परमार्थ: कर्थ कोउन्न यूय॑ं नात्र विच्रक्षणा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12637)
- **Original**: 47 अऔपराशर उवाच इत्युक्त्वा समुपेत्यैनं स तु केशिध्वर्ज नृष: । उबाच किमवहयं त्वय॑ ददासि गुरुदक्षिणाम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12638)
- **Original**: 48 बाढमित्येव तेनोक्त: खाण्डिक्यस्तमथाब्रवीत्‌ भ्रवानध्यात्मविज्ञानपरमार्थविच्धक्षण:...
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12639)
- **Original**: 49 यदि चेद्दीयते महां भवता गुरुनिष्क्रय: । देनेके लिये आया हुँ---ऐसा समझो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12640)
- **Original**: मैंने तुम्हारे डपदेशानुसार अपना यज्ञ भली प्रकार समाप्त कर दिया है, अब मैं तुम्हें गुरु-दक्षिणा देना चाहता हूँ , तुप्हें जो इच्छा हो माँग लो'”
- **Translation**: 

---

