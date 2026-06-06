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

### Verse 1 (Padam Puran 7.3181)
- **Original**: करू नमः वियायेति खिश्वसूर्ते नम: कटिम्‌
- **Translation**: 

---

### Verse 2 (Padam Puran 7.3182)
- **Original**: कत्दर्पाय नमो मेद्मादित्वाय फल तथा । दामोदराय जठरें बासुदेखाय से. स्तनौ
- **Translation**: 

---

### Verse 3 (Padam Puran 7.3183)
- **Original**: श्रीधराय मुख केशान्‌ केझवायेति वै नमः ।पृष्ठ॑ पाईधरायेति चरणों खरदाय चा
- **Translation**: 

---

### Verse 4 (Padam Puran 7.3184)
- **Original**: उद्भयक्रासिगदापरशुण्णये । सर्वात्मते उमस्तुध्थ॑ दिर॒ इत्यभिघीयते
- **Translation**: 

---

### Verse 5 (Padam Puran 7.3185)
- **Original**: मत्त्वे कूर्म चर आगहं नारसिंहे चर वामनम्‌
- **Translation**: 

---

### Verse 6 (Padam Puran 7.3186)
- **Original**: ग़म राम॑ च कृष्णे च बुद्ध कल्कि नमोउस्तु ते
- **Translation**: 

---

### Verse 7 (Padam Puran 7.3187)
- **Original**: सर्वपापौधनाशार्थ पूजयामि नमो. नमः
- **Translation**: 

---

### Verse 8 (Padam Puran 7.3188)
- **Original**: एभिश्व सर्वशों मरैर्थिष्णु ध्याखा प्रपूजयेत्‌
- **Translation**: 

---

### Verse 9 (Padam Puran 7.3189)
- **Original**: 45--52)
- **Translation**: 

---

### Verse 10 (Padam Puran 7.3190)
- **Original**: यज्ञोपवीतका निर्माण कराया है, आप इसे ग्रहण करें और प्रसन्न होकर मेरा मनोरथ पूर्ण करें ।' तास्वूरू-सन्र हदें दर्स ला साम्बूले यथाझक्ति सुझोभनम्‌
- **Translation**: 

---

### Verse 11 (Padam Puran 7.3191)
- **Original**: अतिगुद्ीत्र देवेडा सापुद्धर भवार्णवात्‌ । (68
- **Translation**: 

---

### Verse 12 (Padam Puran 7.3192)
- **Original**: 66-67) “देवेश ! मैंने यथाशक्ति उत्तम झोभासम्पन्न ताम्बूल दाल किया है, इसे स्वीकार करें और भवसागरसे मेरा उद्धार कर दें।' मोहान्धकारपदुमणे भक्तियुक्तो भवातिहन्‌। (68
- **Translation**: 

---

### Verse 13 (Padam Puran 7.3193)
- **Original**: 67-68 ) 'देवेश ! आप मोहरूपी अन्धकार दूर करनेके लिये सूर्यरूप हैं । भव-बन्धनकी पीड़ा हरनेबाले परमात्मन्‌ ! मैं अक्तियुक्त होकर आपकी सेवामें यह पाँच बत्तियॉंका दीपक प्रस्तुत करता हूँ। यह आपके लिये आरती है ।' नैवेद्ा-मन्त्र परपणाज्न सुपक्काज्न समस्तरससंयुतम्‌
- **Translation**: 

---

### Verse 14 (Padam Puran 7.3194)
- **Original**: निवेदित सया भक्तया भगयन्‌ प्रतिगुृाताम्‌। (68
- **Translation**: 

---

### Verse 15 (Padam Puran 7.3195)
- **Original**: 68-69 ) 'भगवन्‌ ! मैंने सब रसोंसे युक्त सुन्दर पकवान, जो परम उत्तम अन्न है, भक्तिपूर्वक सेवामें निवेदन किया है; आप इसे स्वीकार करें ।' जयप-समर्पण द्वादशा क्षरमन्त्रेण यथार्सख्यजपेन तब अ्रीयतां में भ्रियः कान्तः प्रीतो यच्छतु लाज्छितम्‌
- **Translation**: 

---

### Verse 16 (Padam Puran 7.3196)
- **Original**: 69-70 ) *द्वादशाक्षर मन्त्रका यथाशक्ति जप करनेसे भगवान्‌ लक्ष्मीकात्त मुझपर प्रसत्न हों और प्रसन्न होकर मुझे मनोथाउिछित यस्तु प्रदान करें ।' इस प्रकार श्रीहरिका पूजन करनेके बाद निम्नाद्धित मन्त्र पढ़कर गौको प्रणाम करें-- पश्च गावः ससुस्यज्ञा मध्यमाने महोदथों। तासां मथ्ये तु या नन्‍्दा तस्वै थेन्ले नसों नसः
- **Translation**: 

---

### Verse 17 (Padam Puran 7.3197)
- **Original**: 770-71) थीं। उनमेंसे जो नन्‍दा नामकी घेनु है, उसे मेरा बारम्बार नमस्कार है।' तत्पश्चात्‌ विधिपूर्वक गौकी पूजा करके निम्नाड्ल्ति मन्त्रोंद्रार एकाग्रचित्त हो अर्ध्य प्रदान करें सर्वकामदहे.._ देखि.. सर्वार्तिकनिवारिणि । आरोग्य॑ संतर्ति दीर्घा देहि नन्दिनि थे सदा
- **Translation**: 

---

### Verse 18 (Padam Puran 7.3198)
- **Original**: । प्रुजिता च वसिप्ठेन चिश्वामिप्रेण धीमता । कपिले हर में पाप॑ यच्यया पूर्ससझितम्‌
- **Translation**: 

---

### Verse 19 (Padam Puran 7.3199)
- **Original**: गालों में अग्मतः सन्‍्तु गालों से सनन्‍्तु पृष्ठतः । नाके मासमुपतिष्ठन्लु_ हेमम्यूदण्य: पयोमुचः
- **Translation**: 

---

### Verse 20 (Padam Puran 7.3200)
- **Original**: । सुरध्य: सौरभेयाश॒ सरितिःसागरास्तशा । सव्दिवमये. देखि सुभदरे. भक्तवत्सले
- **Translation**: 

---

