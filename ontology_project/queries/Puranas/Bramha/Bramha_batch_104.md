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

### Verse 1 (Bramha 0.2061)
- **Original**: निरञ्ञन हैं। आपका जो परम स्वरूप है, बह भाव पृथ्वीका रसावलसे उद्धार किया था, उसी प्रकार
- **Translation**: 

---

### Verse 2 (Bramha 0.2062)
- **Original**: और अभावसे रहित, निर्लेप, निर्गुण, श्रेष्ठ, मेरा भी दुःखके समुद्रसे उद्धार कौजिये। कृष्ण!
- **Translation**: 

---

### Verse 3 (Bramha 0.2063)
- **Original**: कूटस्थ, अचल, ध्रुव, समस्त उपाधियोंसे निर्मुक्त आपके इन वरदायक स्वरूपोंका मैंने स्तवन किया
- **Translation**: 

---

### Verse 4 (Bramha 0.2064)
- **Original**: और सत्तामात्र रूपसे स्थित है। प्रभो! उसे देवता है। ये बलदेव आदि, जो पृथकुरूपसे स्थित
- **Translation**: 

---

### Verse 5 (Bramha 0.2065)
- **Original**: भी नहीं जानते, फिर मैं ही कैसे उसे जान सकता दिखायी देते हैं, आपके ही अड्ग हैं। देवेश!
- **Translation**: 

---

### Verse 6 (Bramha 0.2066)
- **Original**: हूँ। इसके सिवा आपका जो अपर स्वरूप है, बह प्रभो! अच्युत! गरुड़ आदि पार्षद, आयुधोंसहित
- **Translation**: 

---

### Verse 7 (Bramha 0.2067)
- **Original**: पीताम्यरधारी और चार भुजाओंवाला है। उसके दिक्‍्पाल तथा केशव आदि जो आपके अन्य भेद
- **Translation**: 

---

### Verse 8 (Bramha 0.2068)
- **Original**: हाथोंमें शड्ख, चक्र और गदा सुशोभित हैं। वह मनीषियोंद्वार बतलाये गये हैं, उन सबका मैंने
- **Translation**: 

---

### Verse 9 (Bramha 0.2069)
- **Original**: मुकुट और अड्भद धारण करता है। उसका वक्ष:- पूजन किया है। प्रसन्‍न तथा विशाल नेत्रोंबाले
- **Translation**: 

---

### Verse 10 (Bramha 0.2070)
- **Original**: स्थल श्रीवत्सचिहसे युक्त है तथा वह बनमालासे जगन्नाथ! देवेश्वर! पूर्वोक्त सब स्वरूपोंके साथ
- **Translation**: 

---

### Verse 11 (Bramha 0.2071)
- **Original**: विभूषित रहता है। उसीकी देवता तथा आपके मैंने आपका स्तवन और वन्दन किया है। आप
- **Translation**: 

---

### Verse 12 (Bramha 0.2072)
- **Original**: अन्यान्य शरणागत भक्त पूजा करते हैं। देवदेव ! मुझे धर्म, अर्थ, काम एवं मोक्ष देनेवाला वर
- **Translation**: 

---

### Verse 13 (Bramha 0.2073)
- **Original**: आप सब देवताओंमें श्रेष्ठ एवं भक्तोंको अभय प्रदान करें। हरे! संकर्षण आदि जो आपके भेद
- **Translation**: 

---

### Verse 14 (Bramha 0.2074)
- **Original**: देनेवाले हैं। कमलनयन! मैं विषयोंके समुद्रमें बताये गये हैं, बे सत्र आपको पूजाके लिये ही , डूबा हूँ। आप मेरी रक्षा कोजिये। लोकेश! मैं प्रकट हुए हैं; अत: वे आपके ही आश्रित हैं।। आपके सिवा और किसीको नहीं देखता, जिसकी देवेश! वस्तुत: आपमें कोई भेद नहों है। आपके
- **Translation**: 

---

### Verse 15 (Bramha 0.2075)
- **Original**: शरणमें जाऊँ। कमलाकान्त! मधुसूदन! मुझपर जो अनेक प्रकारके रूप बताये जाते हैं, वे सब
- **Translation**: 

---

### Verse 16 (Bramha 0.2076)
- **Original**: प्रसन्‍न होइये।* नमस्ते बलिनां श्रेष्ठ नमस्ते लाक़लायुध! चतुर्मुख जगद्धाम त्राहि मां प्रपितामह
- **Translation**: 

---

### Verse 17 (Bramha 0.2077)
- **Original**: नमस्ते नीलमेघाभ नमस्ते अत्रिदशार्थित । त्राहि विष्णों जगन्नाथ मग्नं मां भवसागरे
- **Translation**: 

---

### Verse 18 (Bramha 0.2078)
- **Original**: (49। 1--7) * प्रलयातनलसंकाश नमस्ते. दितिजात्तक । नरसिंह महावीर्थ जाहि मां दीक्रलोचन
- **Translation**: 

---

### Verse 19 (Bramha 0.2079)
- **Original**: यथा रसातलादुरवों त्ववा दंष्टरोद्यूता पुरा। तथा महावराहस्त्वं त्राहि मां दुःखसागरात्‌
- **Translation**: 

---

### Verse 20 (Bramha 0.2080)
- **Original**: तबैता मूर्तय: कृष्ण वरदा: संस्तुता मया। तवेमे बलदेवाद्या: पृथग्रूपेणः संस्थिता:
- **Translation**: 

---

