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

### Verse 1 (Vishnu Puran 0.10921)
- **Original**: रुक्‍्मीने पहले ही दाँवमें बलूरमजीसे एक सहस्त्र निष्क जोते तथा दूसरे दाँवमें एक सहस्र निष्क और जीत लिये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10922)
- **Original**: तन बलभद्रजीने दस हजार निष्कका एक दाँव और लगाया । उसे भी पक्के जुआरी रुक्‍्मीने ही जीत लिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10923)
- **Original**: है द्विज ! इसपर मूठ कऑलिंगराज दाँत दिखाता हुआ जोरसे हँसने लगा और मदोन्मत्त रुक्मीने कहा--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10924)
- **Original**: “धूतक्रीडासे अनर्भिज्ञ इन बलभद्रजीको मैंने हरा दिया है; ये वृधा ही अक्षके घमप्डसे अन्धे होकर अक्षकुशल पुरुषोंका अपमान करते थे”
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10925)
- **Original**: इस प्रकार कलिंगराजको दाँत दिखाते और रुक्मीको दुर्बाक्‍् कहते देख हलायुध बलभद्रजों अत्यन्त क्रोधित हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10926)
- **Original**: तन्र उन्होंने अत्यन्त कुपित होकर करोड़ निष्कका दाँव छृगाया और रुक्‍्मीने भी उसे प्रहणकर उसके निमित्त पाँसे फेंके
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10927)
- **Original**: उसे बलदेवजीने ही जीता और से जोरसे बोल उठे, 'मैंने जीता।' इसपर रुक्मी भी चिल्ल्थकर बोल्म--“बलराम ! असत्य बोलनेसे कुछ ल्म्रभ नहीं हो सकता, यह दाँव भी मैंने ही जीता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10928)
- **Original**: आपने इस दाँवके विषयमें जिक्र अवश्य किया था, किंतु मैंने उसका अनुमोदन तो नहीं क्रिया । इस प्रकार यदि आपने इसे जीता है तो मैंने भी क्यों नहीं जीता ?”
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10929)
- **Original**: श्रीपराझसरजी जोलल--उसी समय महात्मा बलदेव- जीके क्रोघको बढ़ाती हुई आकाहवाणीने गम्भीर स्वस्में कहा--
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10930)
- **Original**: “इस दाँवको धघर्मानुसार तो बलरामजी ही जीते हैं; रुकमी झूठ बोलता है क्योंकि (अनुमोदनसूचक] वचन न कहनेपर भी [ पाँसे फेंकने आदि ] कार्यसे वह अनुमोदित ही माना जायगा”
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10931)
- **Original**: तब क्रोधसे अरुणनयन हुए महायस्त्री बलभद्रजीने उठकर राक्मीको जुआ खेलनेके पाँसोंसे ही मार
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10932)
- **Original**: आः 29 ] पश्चमम अंश 385 कलिड्रराजं चादाय विस्फुरन्त बलाइुल: । डाला
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10933)
- **Original**: फिर फड़कते हुए कलिंगराजको बलपूर्वक बभज्ञ दन्तान्कुपितो थे: प्रकाशं स॒ः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10934)
- **Original**: पकड़कर बलूरामजीने उसके दाँत, जिन्हें दिखत्वता हुआ 5 जहास रे यह हैंसा था, तोड़ दिये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10935)
- **Original**: इनके सिल्रा उसके पक्षके आकृष्य च महास्तम्भं जातरूपमर्य बल: ।
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10936)
- **Original**: और भी जो कोई राजालोग थे उन्हें बलरामजीने अत्यन्त जथान तान्ये तत्पक्षे भूभत: कुपितो भुश़म
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10937)
- **Original**: कुपित होकर एक सुवर्णमय स्तम्भ उज़ाड़कर उससे मार पत्ायनपरे डाला
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10938)
- **Original**: हे द्विज ! उस समय बलरामजीके कुपित ततो हाहाकृत॑ सर्व रैँ ट्विज। होनेसे हाह्मकार मच गया और सम्पूर्ण राजाल्‍्थरेग भयभीत तद्राजमण्डलं॑ भीत॑ बभूव कुपितिे खले
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10939)
- **Original**: देकर भागने लगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10940)
- **Original**: बलेन निहतं दृष्ठा रुक्मिणं मथुसूदन: । हे मैत्रेय ! उस समय रुक्मीको माय गया देख नोबाच किश्निनौत्रेय रुक्मिणीबलयोर्भयात्‌
- **Translation**: 

---

