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

### Verse 1 (Vaivtpuran 19.6854)
- **Original**: धारण नहीं करेगा, वह अपनी जातिवालोंके उन्हें प्रणाम किया। मुनिने आशीर्वाद दिया। फिर
- **Translation**: 

---

### Verse 2 (Vaivtpuran 19.6855)
- **Original**: सहित श्रीभ्रष्ट हो जायगा।' इतना कहकर भगवान्‌ नारायणका दिया हुआ पारिजात-पुष्प
- **Translation**: 

---

### Verse 3 (Vaivtpuran 19.6856)
- **Original**: दुर्वासाजी शंकरालयको चले गये। इन्द्रने उस इन्द्रको देकर मुनिने कहा--'देवराज! भगवान्‌
- **Translation**: 

---

### Verse 4 (Vaivtpuran 19.6857)
- **Original**: पुष्पकों अपने सिरपर न धारण करके ऐरावत नारायणके निवेदित यह पुष्प सब विप्लोंका नाश
- **Translation**: 

---

### Verse 5 (Vaivtpuran 19.6858)
- **Original**: हाथीके मस्तकपर रख दिया। इससे इन्द्र श्रीभ्रष्ट करनेवाला है। यह जिसके मस्तकपर रहेगा,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 19.6859)
- **Original**: हो गये। इन्द्रको श्रीभ्रष्ट देख रम्भा उन्हें छोड़कर वह सर्वत्र विजय प्राप्त करेगा और देवताओंमें [स्वर्ग चली गयी। गजराज इन्भधकों नीचे गिराकर अग्रगण्य होकर अग्रपूजाका अधिकारी होगा।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 19.6860)
- **Original**: महान्‌ अरण्यमें चला गया और हथिनीके साथ भ्रैलोक्यलोचनं लोकनार्थ पापप्रमोचनम्‌ । तपसां फलदातारं दुःखदं पापिनां सदा
- **Translation**: 

---

### Verse 8 (Vaivtpuran 19.6861)
- **Original**: कर्मानुरूपफलर्द कर्मबीज॑ दयानिधिम्‌ । कर्मरूप॑ क्रियारूपमरूप॑. कर्मबीजकम्‌
- **Translation**: 

---

### Verse 9 (Vaivtpuran 19.6862)
- **Original**: ब्रह्मविष्णुमहेशानामंशरं. च..त्रिगुणात्मकम्‌ । व्याधिद॑ व्याधिहन्तारं शोकमोहभयापहम्‌। सुखद मोक्षद॑सार॑ भक्तिदं॑ सर्वकामदम्‌
- **Translation**: 

---

### Verse 10 (Vaivtpuran 19.6863)
- **Original**: सर्वेश्व
- **Translation**: 

---

### Verse 11 (Vaivtpuran 19.6864)
- **Original**: सर्वरूप॑. साक्षिणं. सर्वकर्मणाम्‌। प्रत्यक्ष सर्वलोकानामप्रत्यक्षमनूहकम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 19.6865)
- **Original**: शबश्वद्रसहर॑ पश्चाद्‌ रस सर्वसिद्धिदम्‌। सिद्धिस्वरूपं सिद्धेशं॑ सिद्धानां परम॑ गुरुमू। स्तवराजमिति प्रोक्त॑ गुद्दादगुद्यातर परम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 19.6866)
- **Original**: . (गणपतिखण्ड 19
- **Translation**: 

---

### Verse 14 (Vaivtpuran 19.6867)
- **Original**: 36-42)
- **Translation**: 

---

### Verse 15 (Vaivtpuran 19.6868)
- **Original**: शए20889292982928925522929099 79777 अअश्शश्श्श्श्य्््््ग्ल्यदडद- विहार करने लगा। उस वनमें उसके बहुत-से
- **Translation**: 

---

### Verse 16 (Vaivtpuran 19.6869)
- **Original**: तो सदा सभी सभाओंमें निन्दाका विषय बना बच्चे हुए। इसी समय श्रीहरिने उस हाथीका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 19.6870)
- **Original**: रहता है। रम्भाने तुम्हें हतबुद्धि बना दिया था। मस्तक काटकर बालक (गणेश)-के सिरपर लगा
- **Translation**: 

---

### Verse 18 (Vaivtpuran 19.6871)
- **Original**: इसी कारण तुमने दुर्वासाद्वारा दिये गये श्रीहरिके दिया। वत्स! गजमुखके लगानेका प्रसड्भ तुमको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 19.6872)
- **Original**: नैवेद्ययों गजराजके मस्तकपर डाल दिया। इस सुना दिया। इसके श्रवणसे पाप नष्ट होते हैं।समय सबके द्वारा भोगी जानेवाली वह रम्भा अब और कया सुनना चाहते हो, सो कहो।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 19.6873)
- **Original**: कहाँ है और श्रीसे भ्रष्ट हुए तुम कहाँ ? जिसके नारदने पूछा--प्रभो! किस ब्रह्मशापके कारण वे सभी देवता श्रीभ्रष्ट हो गये थे। 0] किस प्रकार उन्होंने उन जगज्जननी कमलाकों
- **Translation**: 

---

