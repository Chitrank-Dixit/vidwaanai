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

### Verse 1 (Vaivtpuran 22.6939)
- **Original**: बभूवुर्मनव: सर्वे. सर्वैश्चर्ययुता यतः । सर्वश्चर्यप्रदस्यास्य कवचस्य ऋषिरविधि:
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.6940)
- **Original**: पड्क्तिश्छन्दश सा देवी स्वयं पद्मालया सुर । सिद्धैश्वर्यजयेप्लेव विनियोग: प्रकी्तित:
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.6941)
- **Original**: यद्‌ धृत्वा कवचं लोक: सर्वत्र विजयी भवेतू
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.6942)
- **Original**: मस्तक पातु मे पद्मा कण्ठ॑ पातु हरिप्रिया । नासिकां पातु मे लक्ष्मी: कमला पातु लोचनम्‌
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.6943)
- **Original**: केशवकान्ता च कपाल॑ कमलालया। जगत्पसूर्गण्डयुग्म॑ स्कनन्‍्ध॑ सम्पत्पदा सदा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.6944)
- **Original**: 3&» श्री कमलवासिन्ये॑ स्वाहा हट व है. 4 हों श्री नमः पद्मायै स्वाहा पातु नितम्बकम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.6945)
- **Original**: हों त्रीं क्‍लीं महालक्ष्म्यै स्वाहा मां पातु सर्वत:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.6946)
- **Original**: नाम कवच परमाद्भधुतम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.6947)
- **Original**: दक्षिणे बाहौँ स सर्वविजयी भवेत्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.6948)
- **Original**: तस्य छायेब सतत॑ सा च जन्मनि जन्मनि
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.6949)
- **Original**: शतलक्षप्रजत्तोॉपपि. न मन्त्र: सिद्धिदायक:
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.6950)
- **Original**: (गणपतिखण्ड 22। 5--19)
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.6951)
- **Original**: 338 * संख्तिप्त क्रह्म॑वैवर्तपुराण * #ऋऋ#ऋ#ऋ##%#%##&###&####&##&#############ऋऋऋश्षकऋऋ॑ऋष्कऋक अंक ऋकऋऋऊऋअ 4 45858 58
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.6952)
- **Original**: 58888 # वस्तुहीन एवं निष्फल हो जाता है, जैसे दूध पीनेवाले बच्चोंकों माताके बिना सुख नहीं मिलता। आप तो जगत्‌की माता हैं; अतः प्रसन्न हो जाइये और हम अत्यन्त भयभीतोंकी रक्षा कीजिये। हमलोग आपके चरणकमलका आश्रय लेकर शरणापन्न हुए हैं। आप शक्तिस्वरूपा जगज्जननीको बारंबार उमस्कार है। ज्ञान, बुद्धि होनेपर माता उसे छोड़कर चली जाती है? हे मात:! आप कृपासिन्धु श्रीहरिकी प्राणप्रिया हैं और भक्तोंपर अनुग्रह करना आपका स्वभाव है; अतः दुधमुँहे बालकोंकी तरह हमलोगोंपर कृपा करो, हमें दर्शन दो। बत्स! इस प्रकार लक्ष्मीका वह शुभकारक स्तोत्र, जो सुखदायक, ,मोक्षप्रद, साररूप, शुभद और सम्पत्तिका आश्रयस्थान है, तथा सर्वस्व प्रदान करनेवाली आपको पुन:-पुन:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.6953)
- **Original**: तुम्हें बता दिया। जो मनुष्य पूजाके समय इस प्रणाम है। महालक्ष्मी! आप हरि-भक्ति प्रदान
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.6954)
- **Original**: महान्‌ पुण्यकारक स्तोत्रका पाठ करता है, उसके करनेवाली, मुक्तिदायिनी, सर्वज्ञा और सब कुछ
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.6955)
- **Original**: गृहका महालक्ष्मी कभी परित्याग नहीं करतों। देनेवाली हैं। आप बारंबार मेरा प्रणिपात स्वीकार
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.6956)
- **Original**: इन्द्रसे इतना कहकर श्रीहरि वहीं अन्तर्धान हो करें। माँ! कुपुत्र तो कहाँ-कहीं होते हैं, परंतु
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.6957)
- **Original**: गये। तब उनकी आज्ञासे देवताओंके साथ देवराज कुमाता कहीं नहीं होती। क्‍या कहीं पुत्रके दुष्ट
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.6958)
- **Original**: क्षीससागरपर गये*। (अध्याय 22) जज >> नियाएया 50000 देवताओंके स्तवन करनेपर महालक्ष्मीका प्रकट होकर देवों और मुनियोंके समक्ष अपने निवास-योग्य स्थानका वर्णन करना नारायण कहते हैं--नारद! तदनन्तर इन्द्र
- **Translation**: 

---

