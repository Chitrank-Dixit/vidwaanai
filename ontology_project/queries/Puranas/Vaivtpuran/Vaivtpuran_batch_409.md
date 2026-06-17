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

### Verse 1 (Vaivtpuran 21.18782)
- **Original**: भये5भये बाघ शुभेशशुभे वा सुखेयषु दुःखेषु च दीननाथ। त्वया विनान्यं शरणं भवार्णवे न नोउस्ति हे माधव रक्ष रक्ष
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.18783)
- **Original**: जय जय गुणसिन्थोी कृष्ण भक्तैकबन्धो बहुतरभययुक्तानू बालकान्‌ रक्ष रक्ष। जहि दनुजकुलानामीशमस्माकमन्तं सुरकुलबलदर्प सर्धयेमं निहत्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.18784)
- **Original**: इ्ति औब्रह्मवैवर्ते गोपवालकै: कृत श्रीकृष्णस्तवनं सम्पूर्णम्‌ ( श्रीकृष्णजन्मखण्ड 22। 20--24) 00 7628 7ज 0 मत दानवकृतं अश्रीकृष्णस्तोत्रम्‌ कृष्णदर्शनप्रात्रेण बभूवास्थ पुरा स्मृति: । आत्मान॑ बुबुधे कृष्ण जगतां कारण परम्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.18785)
- **Original**: तेज:स्वरूपमीशं त॑ दृष्ठा तुष्टाव दानव: । यथागर् यथाजन्म गुणातीत॑ श्रुतेः परम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.18786)
- **Original**: दानव उबाच वामनोईइसि त्वमंशेन मत्पितुर्यज्ञभिक्षुक: । राज्यहर्ता च श्रीहर्ता सुतलस्थलदायक:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.18787)
- **Original**: बलिभक्तिवशों वीर: सर्वेशों भक्तवत्सल: । शीघ्र त्वं हिंस मां पाप॑ शापाद गर्दभरूपिणम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.18788)
- **Original**: मुनेर्दृ्बासस: शापादीदृर्श जन्म कुत्सितम्‌ । मृत्युरुक्तश्न॒ मुनिना त्वत्तों मम जगत्पते
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.3809)
- **Original**: + प्रकृतिख॒ण्ड + 169 इस प्रकार स्तुति करके लक्ष्मीकान्त भगवान्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.3810)
- **Original**: तुलसीकी भक्तिभावसे पूजा करता है, वह सम्पूर्ण श्रीहरि वहीं बैठ गये। इतनेमें उनके सामने साक्षात्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.3811)
- **Original**: पापोंसे मुक्त होकर भगवान्‌ विष्णुके लोकमें चला तुलसी प्रकट हो गयी। उस साध्वीने उनके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.3812)
- **Original**: जाता है। जो कार्तिक महीौनेमें भगवान्‌ विष्णुको चरणोंमें तुरंत मस्तक झुका दिया। अपमानके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.3813)
- **Original**: तुलसोपत्र अर्पण करता है, वह दस हजार कारण उस मानिनीकी आँखोंसे आँसू बह रहे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.3814)
- **Original**: गोदानका फल निश्चितरूपसे पा जाता है। इस थे; क्योंकि पहले उसे बड़ा सम्मान मिल चुका
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.3815)
- **Original**: तुलसीनामाष्टकके स्मरणमात्रसे संतानहीन पुरुष था। ऐसी प्रिया तुलसीको देखकर प्रियतम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.3816)
- **Original**: पुत्रवानू बन जाता है। जिसे पत्नी न हो, उसे भगवान्‌ श्रीहरिने तुरंत उसे अपने हृदयमें स्थान
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.3817)
- **Original**: पत्नी मिल जाती है तथा बन्धुहीन व्यक्ति दिया। साथ ही सरस्वतीसे आज्ञा लेकर उसे अपने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.3818)
- **Original**: बहुत-से बान्धबोंको प्राप्त कर लेता है। इसके महलमें ले गये। उन्होंने शीघ्र ही सरस्वतीके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.3819)
- **Original**: स्मरणसे रोगी रोगमुक्त हो जाता है, बन्धनमें साथ तुलसीका प्रेम स्थापित करवाया। साथ ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.3820)
- **Original**: पड़ा हुआ व्यक्ति छुटकारा पा जाता है, भयभीत भगवान्‌ने तुलसीको बर दिया--'देवि! तुम
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.3821)
- **Original**: पुरुष निर्भय हो जाता है और पापी पापोंसे मुक्त सर्वपूज्या और शिरोधार्या होओ। सब लोग तुम्हारा [हो जाता है। आदर एवं सम्मान करें।' भगवान्‌ विष्णुके इस नारद! यह तुलसी-स्तोत्र बतला दिया। अब प्रकार कहनेपर वह देवी परम संतुष्ट हो गयी।
- **Translation**: 

---

