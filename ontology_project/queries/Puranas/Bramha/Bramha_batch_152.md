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

### Verse 1 (Bramha 0.3021)
- **Original**: तुमको सुनाया है। #4+8-*ऑपिफसक्‍+->+ भागीरथी गड्डाके अवतरणकी कथा भारदजीने कहा--सुस्श्रे्टट एक ही गद्जाके
- **Translation**: 

---

### Verse 2 (Bramha 0.3022)
- **Original**: उपायसे मुझे संतान होगी?” उनकी यह बात आपने दो भेद बतलाये हैं। एक तो वह है, जो
- **Translation**: 

---

### Verse 3 (Bramha 0.3023)
- **Original**: सुनकर महर्षि बसिष्ठने कुछ कालतक ध्यान गौतम नामक ब्राह्मणके द्वारा लाया गया और
- **Translation**: 

---

### Verse 4 (Bramha 0.3024)
- **Original**: किया। उसके बाद राजासे कहा--'राजन्‌! तुम दूसरा अंश भगवान्‌ शंकरकी जटामें ही रह गया,
- **Translation**: 

---

### Verse 5 (Bramha 0.3025)
- **Original**: पत्रीसहित सदा ऋषि-महर्षियोंका सेवन करते जिसे क्षत्रिय राजा भगीरथ ले आये। अत: उसीका
- **Translation**: 

---

### Verse 6 (Bramha 0.3026)
- **Original**: रहो।' यों कहकर महर्षि वसिष्ठ अपने आश्रमको प्रसड्ग मुझे सुनाइये। चले गये। एक समयकी बात है--राजर्षि सगरके ब्रह्माजी बोले--देवर्ये ! बैवस्वत मनुके वंशमें
- **Translation**: 

---

### Verse 7 (Bramha 0.3027)
- **Original**: घरपर एक तपस्वी महात्मा पधारें। राजाने उन राजा इक्ष्वाकुके कुलमें सगर नामके एक अत्यन्त
- **Translation**: 

---

### Verse 8 (Bramha 0.3028)
- **Original**: महर्षिका पूजन किया। इससे संतुष्ट होकर वे धार्मिक राजा हो गये हैं। वे यज्ञ करते, दान देते
- **Translation**: 

---

### Verse 9 (Bramha 0.3029)
- **Original**: बोले--'महाभाग! वर माँगो।' यह सुनकर राजाने और सदा धार्मिक आचार-बिचारसे रहते थे।
- **Translation**: 

---

### Verse 10 (Bramha 0.3030)
- **Original**: पुत्र होनेके लिये प्रार्थना की। मुनि बोले--' तुम्हारी उनके दो पत्नियाँ थीं। वे दोनों हो पतिभक्ति-
- **Translation**: 

---

### Verse 11 (Bramha 0.3031)
- **Original**: एक पत्नीके गर्भसे एक ही पुत्र होगा, किंतु वह परायणा थों, किंतु उनमेंसे किसीको भी संतान न
- **Translation**: 

---

### Verse 12 (Bramha 0.3032)
- **Original**: वंशधर होगा; और दूसरी स्त्रीके गर्भसे साठ हजार हुई। इसलिये राजाके मनमें बड़ी चिन्ता थी। एक
- **Translation**: 

---

### Verse 13 (Bramha 0.3033)
- **Original**: पुत्र उत्पन्न होंगे।' बरदान देकर जब मुनि चले दिन उन्होंने महर्षि वसिष्ठको अपने घर बुलाया
- **Translation**: 

---

### Verse 14 (Bramha 0.3034)
- **Original**: गये, तब उनके कथनानुसार यथासमय राजाके और विधिपूर्वक उनकी पूजा करके पूछा--'किस
- **Translation**: 

---

### Verse 15 (Bramha 0.3035)
- **Original**: हजारों पुत्र हुए। राजा सगरने उत्तम दक्षिणासे
- **Translation**: 

---

### Verse 16 (Bramha 0.3036)
- **Original**: » धागीरथी गझ्कके अवतरणकी कथा * 147 युक्त बहुतैरे अश्वमेध-यज्ञ किये। फिर एक अश्वमेघ-
- **Translation**: 

---

### Verse 17 (Bramha 0.3037)
- **Original**: शूरबीर राजा हैं, शासक हैं। इस पाषीको उठायें यज्ञके लिये उन्होंने विधिपूर्वक दीक्षा ग्रहण की
- **Translation**: 

---

### Verse 18 (Bramha 0.3038)
- **Original**: और क्षत्रियोचित्त तेजसे इसका बध कर डालें
- **Translation**: 

---

### Verse 19 (Bramha 0.3039)
- **Original**: ! और अश्वकी रक्षाके लिये सेनासहित अपने
- **Translation**: 

---

### Verse 20 (Bramha 0.3040)
- **Original**: फिर क्‍या था, वे मुनिको कट वचन सुनाते हुए पुत्रोंको नियुक्त किया। अश्व पृथ्वीपर भ्रमण करने
- **Translation**: 

---

