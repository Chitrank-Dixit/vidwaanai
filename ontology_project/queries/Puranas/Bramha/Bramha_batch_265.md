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

### Verse 1 (Bramha 0.5281)
- **Original**: बान्धव वृद्धकौशिक आदिको उन्होंने बुलबाया हुआ। उन्होंने पूछा-'आप कौन हैं?” चैश्यने
- **Translation**: 

---

### Verse 2 (Bramha 0.5282)
- **Original**: और सबके साथ देवपूजनपूर्वक गौतमीके तटपर राजासे अपना सब हाल ठीक-टीक कह सुनाया।
- **Translation**: 

---

### Verse 3 (Bramha 0.5283)
- **Original**: यज्ञ किया। तदनन्तर शरीरका अन्त होनेपर वे फिर बोला--ब्राह्मणेके प्रसादसे तथा धर्म,
- **Translation**: 

---

### Verse 4 (Bramha 0.5284)
- **Original**: स्वर्गलोकमें गये। वह स्थान मृतसंजीवनतीर्थ तपस्या, दान, यज्ञ और दिव्य ओषधिके प्रभावसे
- **Translation**: 

---

### Verse 5 (Bramha 0.5285)
- **Original**: चक्षुस्तीर्थ और योगेश्वरतीर्थ कहलाने लगा। वह मुझमें ऐसी शक्ति आयी है।' वैश्यका यह कथन
- **Translation**: 

---

### Verse 6 (Bramha 0.5286)
- **Original**: स्मरणमात्रसे पुण्य देनेवाला, मनको प्रसन्न रखनेवाला सुनकर महाराजको अत्यन्त आश्चर्य हुआ। बे और समस्त दुर्भावनाओंका नाश करनेवाला है। * एतदेव सुजातानां लक्षणं भुवि देहिनाम्‌। कृपाई यन्मनो नित्य तेषामप्यहितेषु हि
- **Translation**: 

---

### Verse 7 (Bramha 0.5287)
- **Original**: (170। 83)
- **Translation**: 

---

### Verse 8 (Bramha 0.5288)
- **Original**: 256 + संक्षिप्त ख्रह्मपुराण * सामुद्र, ऋषिसत्र आदि तीर्थोक्री महिमा तथा गौतमी-माहात्म्यका उपसंहार ब्रह्माजी कहते हैं--नारद! सामुद्रतीर्थ सब
- **Translation**: 

---

### Verse 9 (Bramha 0.5289)
- **Original**: शयन करते हैं। इस चराचर जगत्में मेरे तीथोंका फल देनेवाला है
- **Translation**: 

---

### Verse 10 (Bramha 0.5290)
- **Original**: उसके स्वरूपका वर्णन
- **Translation**: 

---

### Verse 11 (Bramha 0.5291)
- **Original**: लिये कुछ भी असम्भव नहीं है। मैं तुम्हारे करता हूँ, मन लगाकर सुनो। गौतमके विदा स्वागतमें यहाँतक आया हूँ। जो अपनेसे बड़ेके करनेपर पापनाशिनी गड्जा जब तीनों लोकोंका
- **Translation**: 

---

### Verse 12 (Bramha 0.5292)
- **Original**: आनेपर अहंकारवश आगे बढ़कर उसका स्वागत उपकार करनेके लिये ब्रह्मगिरिसे पूर्व-समुद्रकी
- **Translation**: 

---

### Verse 13 (Bramha 0.5293)
- **Original**: नहीं करता, वह धर्म आदिसे भ्रष्ट होकर नरकमें ओर चलीं, तब मार्गमें मैंने उनके जलको लेकर
- **Translation**: 

---

### Verse 14 (Bramha 0.5294)
- **Original**: पड़ता है।* भगवती गद्जा! तुमसे एक प्रार्थना कमण्डलुमें धारण किया। परमात्मा शिवने उन्हें
- **Translation**: 

---

### Verse 15 (Bramha 0.5295)
- **Original**: करता हूँ। तुम सात धाराओंमें आकर मुझसे मस्तकपर चढ़ाया। वे भगवान्‌ विष्णुके चरणोंसे
- **Translation**: 

---

### Verse 16 (Bramha 0.5296)
- **Original**: मिलो। यदि एक ही धाराके रूपमें आकर मिलोगी प्रकट हुई हैं। ब्रह्मर्थि गौतमने मर्त्यलोकमें उनका
- **Translation**: 

---

### Verse 17 (Bramha 0.5297)
- **Original**: तो मैं तुम्हारे दुःसह बेगकों धारण न कर अवतरण कराया है। वे स्मरणमात्रसे सब पापोंका
- **Translation**: 

---

### Verse 18 (Bramha 0.5298)
- **Original**: सकूँगा।' समुद्रका यह वचन सुनकर गौतमी नाश करनेवाली हैं और गुरुओंकी भी गुरु हैं।
- **Translation**: 

---

### Verse 19 (Bramha 0.5299)
- **Original**: गछ्लने कहा--' तुम मेरी यह बात मानो; ससर्पियोंकी समुद्रने जब उन्हें अपनी ओर आते देखा, तब
- **Translation**: 

---

### Verse 20 (Bramha 0.5300)
- **Original**: जो अरुन्धती आदि पत्रनियाँ हैं उन सबको उनके मन-ही-मन विचार किया--'जो सम्पूर्ण जगत्‌की
- **Translation**: 

---

