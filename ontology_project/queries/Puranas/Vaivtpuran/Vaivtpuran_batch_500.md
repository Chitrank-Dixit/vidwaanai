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

### Verse 1 (Vaivtpuran 28.7198)
- **Original**: हरिद्वार और बदरी-इनका बारंबार स्मरण करो। हैं और प्रत्येक जन्ममें उसीके साथ स्वर्गमें
- **Translation**: 

---

### Verse 2 (Vaivtpuran 28.7199)
- **Original**: फिर चन्दन, अगुरु, कस्तूरी तथा सुगन्धित पुष्प पुण्यका उपभोग करती हैं। पतिब्रते! गृहस्थोंकी
- **Translation**: 

---

### Verse 3 (Vaivtpuran 28.7200)
- **Original**: देकर और वस्त्रसे आच्छादित करके पिताके यह व्यवस्था तो मैंने तुम्हें बदला दी। अब तीर्थमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 28.7201)
- **Original**: शवको चिताके ऊपर स्थापित करो। तात! फिर मरनेवाले ज्ञानियों तथा बैष्णवॉंके विषयमें श्रवण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 28.7202)
- **Original**: सोनेकी सलाईसे कान, आँख, नाक और मुखमें करो। जो साध्वी नारी जहाँ-जहाँ अपने वैष्णव
- **Translation**: 

---

### Verse 6 (Vaivtpuran 28.7203)
- **Original**: निर्मनथन करके उसे आदरसहित ब्राह्मणको दान पतिका अनुगमन करती है, वहाँ-वहाँ वह
- **Translation**: 

---

### Verse 7 (Vaivtpuran 28.7204)
- **Original**: कर दो। तत्पश्चात्‌, तिलसहित ताँबेका पात्र, गौ, स्वामीके साथ वैकुण्ठमें जाकर श्रीहरिकी संनिधि
- **Translation**: 

---

### Verse 8 (Vaivtpuran 28.7205)
- **Original**: चाँदी और सोना दक्षिणासहित दान करके स्वस्थचित्त प्राप्त करती है। नारद ! कृष्णभक्तिपरायण जीवन्मुक्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 28.7206)
- **Original**: हो दाह-कर्म करों। '3» जो जानकारीमें अथवा भक्तोंके तीर्थमें अथवा अन्यत्र मरनेमें कोई
- **Translation**: 

---

### Verse 10 (Vaivtpuran 28.7207)
- **Original**: अनजानमें पाप-कर्म करके मृत्यु-कालके वशीभूत विशेषता नहीं है; क्योंकि उन्हें दोनों जगह समान
- **Translation**: 

---

### Verse 11 (Vaivtpuran 28.7208)
- **Original**: हो पञ्चत्वको प्राप्त हुआ। 3& धर्म-अधर्मसे युक्त 'फल मिलता है। इसलिये यदि स्त्री अथवा पुरुष
- **Translation**: 

---

### Verse 12 (Vaivtpuran 28.7209)
- **Original**: तथा लोभ-मोहसे समावृत उस मनुष्यके सारे भगवान्‌ नारायण तथा कमलालया लक्ष्मीका भजन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 28.7210)
- **Original**: शरीरको जलाता हूँ; वह दिव्य लोकोंमें जाय।' करे तो उस भजनके प्रभावसे महाप्रलय होनेपर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 28.7211)
- **Original**: इस मन्त्रकों पढ़कर पिताकी प्रदक्षिणा करो और भी उन दोनोंका नाश नहीं होता। वहाँ रेणुकासे
- **Translation**: 

---

### Verse 15 (Vaivtpuran 28.7212)
- **Original**: फिर '3» तुम हमारे कुलमें उत्पन्न हुए हो, मैं * स पुत्रों भक्तिदाता यः सा च स्त्री यानुगच्छति । स बन्धुदनिदाता यः स शिष्यो गुरुमर्चयेत्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 28.7213)
- **Original**: स्रो5भीष्टदेवो यो रक्षेत्‌ स राजा पालबेत्‌ प्रजा: । स च स्वामी प्रियां धर्म मतिं दातुमिहेश्वर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 28.7214)
- **Original**: स॒ गुरु्र्धर्माता यो हरिभक्तिप्रदायक: । एते प्रश॑स्था वेदेषु पुराणेचु च निमश्चितम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 28.7215)
- **Original**: (गणपतिखण्ड 28। 7-9)
- **Translation**: 

---

### Verse 19 (Vaivtpuran 28.7216)
- **Original**: + गणपतिखण्ड * 349 कक ऋं###ं###### 4 ###########ऋऋ््््क््कऊऋऋऊऋअऋऋऋऋ# ###########%#### 55% 4868 ### # पुनः तुम्हारा होकर उत्पन्न होऊँ, तुम्हें स्वर्गलोककी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 28.7217)
- **Original**: उनके गलेमें वनमाला लटक रही थी और वे प्राप्ति हो स्वाहा' इस प्रकार उच्चारण करो तथा
- **Translation**: 

---

