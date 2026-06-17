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

### Verse 1 (Bramha 0.4721)
- **Original**: , हमलोग अभी वृत्रासुरका वध करनेवाले उस
- **Translation**: 

---

### Verse 2 (Bramha 0.4722)
- **Original**: £ इद्से युद्ध करनेके लिये चलें।' ऐसा निश्चय
- **Translation**: 

---

### Verse 3 (Bramha 0.4723)
- **Original**: करके असुरोंने वहाँ आकर महर्षि आत्रेयको और
- **Translation**: 

---

### Verse 4 (Bramha 0.4724)
- **Original**: उनके द्वारा निर्मित इन्द्रपुरीको भी घेर लिया। फिर । कक जे
- **Translation**: 

---

### Verse 5 (Bramha 0.4725)
- **Original**: * परुष्णीतीर्थ, नारसिंहतीर्थ, पैशाच्नाशनतीर्थ और शब्भुहददतौर्थंकी महिमा « 231 शीघ्र रक्षा कीजिये। पुझे फिर अपना वही आश्रम
- **Translation**: 

---

### Verse 6 (Bramha 0.4726)
- **Original**: गये। उनका जो यज्ञ चल रहा था, उसमें उन्होंने लौटा दीजिये, जहाँ मृग, पक्षी, वृक्ष और जल हैं। लज्जित होकर कहा-“अहो! मोहकी कैसी मुझे इन दिव्य भोगोंकी कोई आबश्यकता नहीं है।
- **Translation**: 

---

### Verse 7 (Bramha 0.4727)
- **Original**: महिमा है कि मेरे चित्तमें भी भ्रान्ति आ गयी। शास्त्रीय मर्यादाका उल्लह्लन करके प्राप्त की हुई
- **Translation**: 

---

### Verse 8 (Bramha 0.4728)
- **Original**: यह क्‍या मैंने महेन्द्रषद पाया और क्या-क्या कोई भी वस्तु सुखद नहीं होती।' उसके लिये किया।” *बहुत अच्छा' कहकर प्रजापतिने उस इन्द्रपु। कै
- **Translation**: 

---

### Verse 9 (Bramha 0.4729)
- **Original**: इस प्रकार लज्जित हुए आत्रेयसे देवताओंने वैभवकों समेट लिया। उस देशको निष्कण्टक
- **Translation**: 

---

### Verse 10 (Bramha 0.4730)
- **Original**: कहा-“महाबाहो? लज्जा छोड़ो। इससे तुम्हारी बनाकर दैत्य फिर अपने स्थानको चले गये।
- **Translation**: 

---

### Verse 11 (Bramha 0.4731)
- **Original**: बड़ी ख्याति होगी। जो लोग इस आगत्रियतीर्थमें स्नान विश्वकर्मा भी हँसते-हँसते अपने धामको पधारे।
- **Translation**: 

---

### Verse 12 (Bramha 0.4732)
- **Original**: करेंगे, वे भविष्यमें इन्द्र होंगे और इसके स्मरणसे आत्रेय भी अपने शिष्यों और पत्नीके साथ ' उन्हें सुखकी प्राप्ति होगी।' यों कहकर देवता चले गौतमी-तटपर रहते हुए तपस्यामें संलग्र हो
- **Translation**: 

---

### Verse 13 (Bramha 0.4733)
- **Original**: गये और आत्रिय मुनि भी बहुत संतुष्ट हुए। >> परुष्णीतीर्थ, नारसिंहतीर्थ, पैशाचनाशनतीर्थ, निप्नभेद- तीर्थ और शद्भुहदतीर्थकी महिमा ख्रह्माजी कहते हैं--परुष्णी नामक तीर्थ! थीं। आत्रियीके गर्भसे महान्‌ बलवान्‌ और पराक्रमी तौनों लोकोंमें विख्यात है। उसके पापनाशक
- **Translation**: 

---

### Verse 14 (Bramha 0.4734)
- **Original**: आड्रिरस नामक पुत्र हुए। अज्विरा आत्रेयीको स्वरूपका वर्णन करता हूँ, सुनो। एक बार महर्षि
- **Translation**: 

---

### Verse 15 (Bramha 0.4735)
- **Original**: प्रतिदिन कटु वचन सुनाते और आज्िरस नामवाले अत्रिने ब्रह्मा, विष्णु और महादेवजीकी आराधना
- **Translation**: 

---

### Verse 16 (Bramha 0.4736)
- **Original**: पुत्र सदा अपने पिताकों शान्त किया करते थे। की। उन तीनोंके संतुष्ट होनेपर महर्षिने कहा--
- **Translation**: 

---

### Verse 17 (Bramha 0.4737)
- **Original**: एक दिन आत्रेयी पतिके कठोर वाक्यसे उद्विग्र हो 'आपलोग मेरे पुत्र हों। साथ ही मेरे एक परम
- **Translation**: 

---

### Verse 18 (Bramha 0.4738)
- **Original**: उठीं और दीनभावसे हाथ जोड़कर अपने श्वशुर सुन्दरी कन्या भी हो।' इस वरदानके अनुसार वे
- **Translation**: 

---

### Verse 19 (Bramha 0.4739)
- **Original**: अग्रिदेवसे बोलों--' भगवन्‌ हव्यवाह! मैं अत्रिकी तीनों देवता उनके पुत्र हुए। महर्षिने जो कन्या
- **Translation**: 

---

### Verse 20 (Bramha 0.4740)
- **Original**: कन्या और आपके पुत्रको पत्नी हूँ, पुत्रों और उत्पन्न की, उसका नाम आत्रेयी हुआ। अत्रिके
- **Translation**: 

---

