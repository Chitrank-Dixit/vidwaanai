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

### Verse 1 (Vaivtpuran 15.6713)
- **Original**: मुख प्रसन्न था तथा उसपर थोड़ी- थोड़ी मुस्कानकी आगे करके वहाँ आयीं। तदनन्तर देवगण,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6714)
- **Original**: छटा छा रही थी। वे भक्तोंपर अनुग्रह करनेके मुनिसमुदाय, पर्वत, गन्धर्व तथा किन्नर सब-के-
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6715)
- **Original**: लिये कातर हो रहे थे। उनपर श्वेत चँंबर डुलाया सब आनन्दमग्र हो कुमारके स्वागतमें गये। जा रहा था और देवेन्द्र तथा मुनीन्द्र उनका स्तवन महेश्वर भी नाना प्रकारके बाजों, रुद्रगणों, पार्षदों,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6716)
- **Original**: कर रहे थे। उन जगन्नाथको देखकर कार्तिकेयके भैरवों तथा क्षेत्रपालोंके साथ वहाँ पधारे। तत्पश्चात्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6717)
- **Original**: सर्वाज्गमें रोमाज्न हो आया। उन्होंने भक्तिभावपूर्वक शक्तिधारी कार्तिकेय पार्वतीको निकट देखकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6718)
- **Original**: सिर झुकाकर उन्हें प्रणाम किया। इसके बाद
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6719)
- **Original**: 330 + संक्षिप्त ब्रह्मवैवर्तपुराण ] स4]444
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6720)
- **Original**: 00%49494444/53344>>ननननननन्‍न ने ब्रह्मा, धर्म, देवताओं और हर्षित मुनिवरोंमें
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6721)
- **Original**: पूछकर वे एक रत्नसिंहासनपर बैठे। उस समय प्रत्येकको प्रणाम किया और उनका शुभाशीर्वाद
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6722)
- **Original**: पार्वतीसहित शंकरने ब्राह्मणोंको बहुत-सा धन पायां। फिर बारी-बारीसे सबसे कुशल-समाचार
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6723)
- **Original**: दान किया। (अध्याय 16) #3++_+“- गयी 28क्‍050>00+ कार्तिकेयका अभिषेक तथा देवताओंद्वारा उन्हें उपहार-प्रदान श्रीनारायणजी कहते हैं--नारद! तदनन्तर
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6724)
- **Original**: कामशास्त्र और क्षीरसागरने अमूल्य रत्र तथा जगदीश्वर विष्णुने प्रसन्नमनसे शुभ मुहूर्त निश्चय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6725)
- **Original**: रत्नोंके बने हुए विशिष्ट नूपुर दिये। पार्वतीका करके कार्तिकेयकों एक रमणीय रज्नसिंहासनपर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6726)
- **Original**: मन तो उस समय परमानन्दमें निमग्र था, उन्होंने बैठाया और कौतुकवश नाना प्रकारके झाँझ-
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6727)
- **Original**: मुस्कराते हुए महाविद्या, सुशीलाविद्या, मेधा, मँजीरा तथा यन्त्रमय बाजे बजवाये। फिर अमूल्य
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6728)
- **Original**: दया, स्मृति, अत्यन्त निर्मल बुद्धि, शान्ति, तुष्टि, रत्रोंके बने हुए सैकड़ों घड़ोंसे, जो वेदमन्त्रोंद्वारा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6729)
- **Original**: पुष्टि, क्षमा, धृति, श्रीहरिमें सुदृढ़ भक्ति और अभिषिक्त तथा सम्पूर्ण तीथॉके जलोंसे परिपूर्ण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6730)
- **Original**: श्रीहरिकी दासता प्रदान की। नारद! प्रजापतिने थे, कार्तिकेयको हर्षपूर्वक स्नान कराया। तत्पश्चात्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6731)
- **Original**: देवसेनाको, जो रत्नाभरणोंसे विभूषित, परम कार्तिकेयको प्रसन्नमनसे बहुमूल्य रत्नोंद्वारा निर्मित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6732)
- **Original**: विनीत, उत्तम शीलवती, मनकों हरण कर किरीट, दो माज़लिक बाजूबंद, अमूल्य रत्नोंके
- **Translation**: 

---

