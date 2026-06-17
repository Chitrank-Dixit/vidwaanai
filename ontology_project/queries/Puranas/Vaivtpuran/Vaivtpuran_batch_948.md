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

### Verse 1 (Vaivtpuran 543.17274)
- **Original**: वृन्दावन नामक पुण्यवनमें स्थित 'सिद्धाश्रम' में तथा श्रेष्ठ हैं; जिनके हाथमें प्रफुल्ल क्रीड़ा-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.17275)
- **Original**: तुम्हें गणेशके चरणकमलका दर्शन होगा। तुम तो कमल, पारिजातका पुष्प और अमूल्य रत्लतजटित
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.17276)
- **Original**: विषयों हो, अतः तुम्हें राधा-माधवकी दासता स्वच्छ दर्पण शोभा पाते हैं; जो नाना प्रकारके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.17277)
- **Original**: कहाँसे प्राप्त होगी ? इसलिये महाभाग! तुम उससे रत्लोंकी विचित्रतासे युक्त रत्नसिंहासनपर विराजमान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.17278)
- **Original**: निवृत्त हो जाओ; क्योंकि वह परम दुर्लभ है।' यों होती हैं, जो परमात्मा श्रीकृष्णके पद्माद्वारा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.17279)
- **Original**: सुनकर मेरा मन टूट गया और मैं उस तपस्यासे समर्चित मड्जलरूप चरणकमलका अपने इृदयकमलमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.17280)
- **Original**: बिर्त हो गया। पर उस तपस्याके फलस्वरूप मेरा ध्यान करती रहती हैं तथा मन-वचन-कर्मसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.17281)
- **Original**: वह मनोरथ आज परिपूर्ण हो गया। स्वप्न अथवा जाग्रतू कालमें श्रीकृष्णकी प्रीति और श्रीमहादेवजीने कहा--देवि! ब्रह्मा आदि प्रेम-सौभाग्यका नित्य नूतन रूपमें स्मरण करती
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.17282)
- **Original**: देवता, मुनिगण, मनु, सिद्ध, संत और योगीलोग रहती हैं; जो प्रगाढ़भावानुरक्त, शुद्धभक्त, पतिक्रता,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.17283)
- **Original**: ध्याननिष्ठ हो जिनके चरणकमलका, जो पद्माद्वारा धन्या, मान्या, गौरवर्णा, निरन्तर श्रीकृष्णके वक्ष:-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.17284)
- **Original**: कमल-पुष्पोंसे समर्चित एवं अत्यन्त दुर्लभ है, स्थलपर वास करनेवाली, प्रियाओं तथा प्रिय
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.17285)
- **Original**: निरन्तर ध्यान करते रहते हैं; परंतु स्वप्रमें भी भक्तोमें परम प्रिय, प्रियवादिनी, श्रीकृष्णके बामाड्रसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.17286)
- **Original**: उसका दर्शन नहीं कर पाते, तुम उन्हींके वक्ष:- आबिर्भूत, गुण और रूपमें अभिन्न, गोलोकमें वास
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.17287)
- **Original**: स्थलपर वास करनेवाली हो। करनेवाली, देवाधिदेवी, सबके ऊपर विराजमान, अनन्त बोले---सुब्रते ! बेद, वेदमाता, पुराण, गोपीश्वरी, गुप्तिरूपा, सिद्धिदा, सिद्धिरूपिणी, ध्यानद्वारा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.17288)
- **Original**: मैं (शेषनाग), सरस्वती और संतगण तुम्हारी असाध्य, दुराशध्य, सद्धभक्तोंद्रारा बन्दित और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.17289)
- **Original**: स्तुति करनेमें समर्थ नहीं हैं। पुण्यक्षेत्र भारतमें वृषभानु-नन्दिनौके रूपमें प्रकटक।[ . नारद! इस प्रकार वहाँ जितने देव, देवी हुई हैं; उन राधाकी मैं बन्दना करता हूँ। जो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.17290)
- **Original**: तथा अन्यान्य मुनि, मनु आदि आये थे, उन ध्यानपरायण मानव समाधि-अवस्थामें ध्याननिष्ठ
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.17291)
- **Original**: सबने विनम्रभावसे राधाका स्तवन किया। यह हो राधाका ध्यान करते हैं; वे इस लोकमें तो
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.17292)
- **Original**: देखकर रुक्मिणों आदि महिलाओंका मुख लज्ञजासे जीवन्मुक्त हैं ही, परलोकमें श्रीकृष्णके पार्षद होते
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.17293)
- **Original**: झुक गया। उन्होंने अपने शोकोच्छवाससे रत्नदर्पणको हैं। तदनन्तर लोकोंके विधाता स्वयं ब्रह्माने
- **Translation**: 

---

