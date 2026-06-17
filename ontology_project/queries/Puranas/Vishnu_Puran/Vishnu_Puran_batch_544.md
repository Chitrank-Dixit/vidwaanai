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

### Verse 1 (Vishnu Puran 0.10861)
- **Original**: 25 एप ते तनयः सुश्रु हत्वा शम्बरमागत:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10862)
- **Original**: हतो येनाभबद्वालो भवत्यास्सूतिकागृहात्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10863)
- **Original**: 26 इये मायावती भार्या तनयस्यास्थ ते सती । शम्बरस्थ न भार्येयं श्रूयतामत्र कारणम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10864)
- **Original**: 27 मन्मथे तु गते नाश तदुद्धवपरायणा
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10865)
- **Original**: शाम्बर॑ मोहयामास मायारूपेण रूपिणी
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10866)
- **Original**: 28 श्रीविष्णुपुराण और झ श्रोविषपुराण 0 [0 27 ( अ0 27 है महामुने ! जो अपना हृदय और नेत्र प्रशुच्नमें अर्पित तन््यस्तहदयेक्षणा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10867)
- **Original**: कर चुकी थी उस मायायतीने अनुरागसे अन्धो होकर उसे सब प्रकारकी माया सिखा दी
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10868)
- **Original**: इस प्रकार अपने ऊपर आसक्त हुई उस कमललोचनासे कृष्णनन्दन प्रयुम्नने कहा--''आज तुम मातृ-भावको छोड़कर यह अन्य प्रकासका भाव क्‍यों प्रकट करती हो ?''
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10869)
- **Original**: तब मायावतीने कहम-- “तुम मेरे पुत्र नहीं हो, तुम भगवान्‌ विष्णुके तनय हो । तुम्हें कालझम्बरने हरकर समुद्रमें फँंक दिया था; तुम मुझे एक मत्स्यके उदरमें मिले हो। है कान्त ! आपकी पुज़्वत्सला जननी आज भी गोती होगी”
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10870)
- **Original**: श्रीपराशरजी खोले--मायावतोके इस प्रकार कहनेपर महाबलवान्‌ प्रधुप्नजोने क्रोधसे विद्वक हो शम्बरासुरकों युदके लिये ललक्प्रय और उससे युद्ध करने लगे
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10871)
- **Original**: यादवश्रेष्ठ भ्रद्मुप्नजीने उस टैल्यकी सम्पूर्ण सेना मार डाली और उसकी सात मायाओऑको जीतकर स्वये आठवीं मायाका प्रयोग किया
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10872)
- **Original**: उस मायासे उन्होंने दैत्याज कालशम्बरकों मार डाला और मायावतौके साथ [विमानद्वारा] उड़कर आकाहामार्गसे अपने पिताके नगरमें आ गये
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10873)
- **Original**: मायावतीके सहित अन्तःपुरमें उतरनेपर श्रीकृष्णचन्द्रकी रानियोंने उन्हें देखकर कृष्ण ही समझा
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10874)
- **Original**: किन्तु अनिन्दिता रुक्मिणीके नेत्रॉमें प्रेममश आँसू भर आये और वे कहने लगीं--““अवदश्य हो यह नवयौवनको प्राप्त हुआ किसी बड़भागिनीका पुत्र है
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10875)
- **Original**: यदि मेरा पुत्र प्रद्यु् जाखित होगा तो उसकी भी यही आयु होगी
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10876)
- **Original**: हे वत्स ! तू ठीक-ठीक बता तूने किस भाग्यवती जननीको विभूषित किया है ?
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10877)
- **Original**: अथबवा, बेटा ! जैसा मुझे तेरे प्रति स्नेह हो रहा है और जैसा तेरा स्वरूप है उससे मुझे ऐसा भी प्रतीत होता है कि तू श्रीहरिका ही पुत्र है''
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10878)
- **Original**: श्रीपराशरजी बोले--इसी समय श्रीकृष्णचन्द्रके साथ वहाँ नारदजी आ गये। उन्होंने अन्तःपुरनिवासिनी देवी रुक्मिणीकों आनन्दित करते हुए कहा--
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10879)
- **Original**: “हे सुभु ! यह तेरा ही पुत्र है। यह झाम्बरासुस्कों मारकर आ रहा है, जिसने कि इसे बाल्यावस्थामें सू्तिक्य्रगृहसे हर लिया था
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10880)
- **Original**: यह सतो मायावती भी तेरे पुत्रको ही खो है; यह दाम्बयसुरकी पत्नी नहीं है । इसका कारण सुन
- **Translation**: 

---

