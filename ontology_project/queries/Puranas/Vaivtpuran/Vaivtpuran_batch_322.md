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

### Verse 1 (Vaivtpuran 15.6793)
- **Original**: आहाररहित होनेके कारण वे चलने-फिरनेमें व्याधिग्रस्त हो गये, तब उन्होंने स्तवन करनेके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 15.6794)
- **Original**: असमर्थ हो गये थे। तब स्वयं दयालु ब्रह्माने लिये शिव-मन्त्र प्रदान करनेवाले ब्रह्माका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 15.6795)
- **Original**: उन दोनोंसे कहा। स्मरण किया। ब्रह्माने वैकुण्ठमें जाकर कमलापति
- **Translation**: 

---

### Verse 4 (Vaivtpuran 15.6796)
- **Original**: . ब्रह्मा बोले--वत्सो! तुम दोनों कबच, विष्णुसे पूछा। उस समय शिव भी वहीं स्तोत्र और पूजाकी विधिका क्रम ग्रहण करके श्रीहरिके संनिकट विराजमान थे। पुष्करमें जाओ और वहाँ विनमप्रभावसे सूर्यका ब्रह्मा बोले--हरे ! माली और सुमाली दोनों
- **Translation**: 

---

### Verse 5 (Vaivtpuran 15.6797)
- **Original**: भजन करो। दैत्य व्याधिग्रस्त हो गये हैं, अत: उनके रोगके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 15.6798)
- **Original**: . उन दोनोंने कहा--ब्रह्मनन्‌! किस विधिसे विनाशका कौन-सा उपाय है-यह बतलाइये।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 15.6799)
- **Original**: और किस मन्त्रसे हम सूर्यका भजन करें, उनका विष्णुने कहा--ब्रह्मन्‌! वे दोनों पुष्करमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 15.6800)
- **Original**: स्तोत्र कौन-सा है और कवच क्या है--वह सब जाकर वर्षभरतक मेंरे अंशभूत व्याधिहन्ता सूर्यकी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 15.6801)
- **Original**: हमें प्रदान कीजिये। सेवा करें, इससे वे रोगमुक्त हो जाय॑ँगे। ब्रह्माने कहा--वत्स ! वहाँ त्रिकाल ज्लरान शंकरने कहा--जगदीश्वर! उन दोनोंको
- **Translation**: 

---

### Verse 10 (Vaivtpuran 15.6802)
- **Original**: करके इस मन्त्रसे भक्तिपूर्वक भास्करकी भलीभाँति रोगनाशक महात्मा सूर्यका स्तोत्र, कबच और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 15.6803)
- **Original**: सेवा करनेपर तुमलोग नीरोग हो जाओगे। (वह मन्त्र, जो कल्पतरुके समान है, प्रदान कीजिये।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 15.6804)
- **Original**: मन्त्र इस प्रकार है--)' *0 हीं नमो भगबते सूर्याय ब्रह्मन्‌! स्वयं श्रीहरि तो सर्वस्व प्रदान करनेवाले
- **Translation**: 

---

### Verse 13 (Vaivtpuran 15.6805)
- **Original**: परमात्मने स्वाहा '--इस मन्त्रसे सावधानतया सूर्यका हैं और सूर्य रोगनाशक हैं। जिसका जो-जो विषय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 15.6806)
- **Original**: पूजन करके उन्हें भक्तिपूर्वक सोलह उपहार प्रदान है, अपने विषयमें ये दोनों सम्पत्ति-प्रदायक हैं।
- **Translation**: 

---

### Verse 15 (Vaivtpuran 15.6807)
- **Original**: करना चाहिये। यों हो पूरे वर्षभरतक करना होगा। इस प्रकार विष्णु और शिवकी अनुमति पाकर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 15.6808)
- **Original**: इससे तुमलोग निश्चय ही रोगमुक्त हो जाओगे।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 15.6809)
- **Original**: + गणपतिखण्ड + 333 ।][]0[[[/]//]]]।।[।।।।।[4]8]
- **Translation**: 

---

### Verse 18 (Vaivtpuran 15.6810)
- **Original**: 40 पूर्वकालमें अहल्याका हरण करनेके कारण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 15.6811)
- **Original**: दिया। पूर्वकालमें पुलस्त्यने पुष्करक्षेत्रमें प्रसन्न गौतमके शापसे जब इन्द्रके शरीरमें सहस्न भग हो
- **Translation**: 

---

### Verse 20 (Vaivtpuran 15.6812)
- **Original**: होकर इसे मनुको दिया था, वहीं मैं तुम्हें दे रहा गये थे, उस संकट-कालमें बृहस्पतिजीने प्रेमपूर्वक
- **Translation**: 

---

