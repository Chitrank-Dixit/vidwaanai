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

### Verse 1 (Vishnu Puran 0.21)
- **Original**: 91 श्रीपराझर उबाच साथु मैग्रेय धर्मज्ञ स्मारितो5स्मि पुरातनम्‌। पितुः पिता मे भगवान्‌ वसिष्ठो यदुवाच ह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.22)
- **Original**: 12 विश्वामित्रप्रयुक्तेन रक्षसा भक्षित: पुरा। श्रुतस्तातस्तत: क्रोधो मेत्रेयाभून्ममातुलः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.23)
- **Original**: 13 ततो5हं रक्षसां सन्रं बिनाशाय समारभम्‌ । भस्मीभूताअ शतशस्तस्मिन्सब्रे निशाचरा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.24)
- **Original**: 14 मामुवाच महाभागो वसिष्ठो मत्पितामहः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.25)
- **Original**: 157 अलमत्यन्तकोपेन तात मन्युमिम॑ जहि। राक्षसा नापराध्यन्ति पितुस्ते विहितं हि तत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.26)
- **Original**: 16 मूढानामेत्र भवति क्रोधो ज्ञानवर्ता कुतः । इन्यते तात कः केन यत: स्वकृतभुक्पुमान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.27)
- **Original**: 17 सख्वितस्थापि महता वत्स क्लेशेन मानते: । यहासस्तपसश्ैव क्रोधो नाशकरः परः
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.28)
- **Original**: 18 स्वर्गापवर्गव्यासेधकारणं परमर्षय: । बर्जयन्ति सदा क्रोध तात पा तद्॒शो भव
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.29)
- **Original**: 19 अल -.._ निशाचरैर्दग्यैदीनिरमपकारिभि: । सन्न॑ ते विरमत्वेतत्क्षमासारा हि साधव:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.30)
- **Original**: 20 एवं तातेन तेनाहमनुनीतो महात्मना। उपसंहतवान्सत्र सद्यस्तद्वाक्यगोरवात्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.31)
- **Original**: 21 तत: प्रीतः स भगवान्वसिष्ठो मुनिसत्तम: । सम्प्राप्तश्न तदा तत्न पुलस्त्यो ब्रह्मण: सुत:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.32)
- **Original**: 22 पितामहेन द््तार्ष्य: कृतासनपरिग्रह: । मामुवात्न महाभागो मैत्रेब पुलहाग्रज:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.33)
- **Original**: 23 पृथक्‌-पृथक्‌ सम्पूर्ण धर्म, देवर्षि और राजर्पियोंके चरित्र, श्रोव्यासजोकृत वैदिक शाखाओंकी यथावत्‌ रचना तथा ब्राह्मणादि वर्ण और ब्रह्मच्यांदि आश्रमोंके घ॒र्म--ये सब, है महापुनि कक्तिनन्दन ! थैं आपसे सुनना चाहता हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.34)
- **Original**: 6-- 10
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.35)
- **Original**: हैं ब्रहान्‌ ! आप मेरे प्रति अपना चित्त प्रसादोमुख कीजिये जिससे हे महामुने ! मैं आपकी कृपासे यह सब जान सकूँ''
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.36)
- **Original**: श्रीपराइरजी बोले--“हे धर्मज्ञ मैत्रेय ! मेरे पिताजीके पिता श्रीवसिष्ठजीने जिसका वर्णन किया था, उस पूर्व प्रसज़ञका तुमने मुझे अच्छा स्मरण कराया-- [ इसके लिये तुम धन्यवादके पात्र हो]
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.37)
- **Original**: हे मैत्रेय / जब मैंने सुना कि पिताजीको विश्वामित्रकी ब्रेरणासे राक्षसने खा स्त्या है, तो मुझको बड़ा भारी क्रोघ हुआ
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.38)
- **Original**: तब राक्षसोंका ध्वेस करनेके लिये मैंने यज्ञ करना आरम्भ किया। उस यज्ञमें सैकड़ों राक्षस जलकर भस्म हो गये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.39)
- **Original**: इस प्रकार तन राक्षसॉक्य सर्वथा नष्ट होते देख मेरे महाभाग पितामह बसिष्ठजी सुझसे बोले--
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.40)
- **Original**: “है वत्स ! अत्यन्त क्रोध करना ठोक नहीं, अब इसे झ्ञान्त करो। राक्षसोंका कुछ भी अपराध नहीं है, तुम्हारे पिताके लिये तो ऐसा हो होता था
- **Translation**: 

---

