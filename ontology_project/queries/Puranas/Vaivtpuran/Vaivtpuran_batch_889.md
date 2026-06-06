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

### Verse 1 (Vaivtpuran 543.16094)
- **Original**: विभूषित करके केशोंका श्रृज्ञार करो। कल्याणि! असंख्य गोपियाँ विविध भाँतिसे उनकी सेवामें इस प्रकार सुन्दर वेष बनाकर कपोलोंपर पत्र- व्यस्त थीं। उनको इस अवस्थामें पहुँची हुई
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16095)
- **Original**: भंगी (सौन्दर्यवर्धक विचित्र पत्रावली) कर लो। देखकर उद्धव डरे हुएकी भाँति पुनः विनयपूर्बक
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16096)
- **Original**: माँगमें कस्तूरी-चन्दनयुक्त सिन्दूर भर लो और कानोंको अमृतके समान लगनेवाले परम प्रिय
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16097)
- **Original**: बेंदी लगा लो। पैरोंमें मेंहदी लगाकर उसे वचन बोले। महावरसे रँग लो। सति! शोकके साथ-साथ इस उद्धवने कहा--देवि! मैं समझ गया। तुम
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16098)
- **Original**: कीचडयुक्त कमल-पुष्पोंकी शय्याको त्याग दो देवाड्रनाओंकी अधीश्वरी, परम कोमल, सिद्धयोगिनी,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16099)
- **Original**: और उठो। इस उत्तम रत्नसिंहासनपर बैठों। मन- सर्वशक्तिस्वरूपा, मूलप्रकृति, ईश्वरी और गोलोककी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16100)
- **Original**: ही-मन श्रीकृष्णके साथ विशुद्ध एवं मधुर मधुमय सुन्दरी हो; श्रीदामके शापसे तुम भूतलपर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16101)
- **Original**: पदार्थ खाओ, संस्कारयुक्त स्वच्छ जल पीओ और अवतीर्ण हुई हो। देवि! तुम श्रीकृष्णकी प्राणप्रिया
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16102)
- **Original**: सुवासित पानका बीड़ा चबाओ। देवेशि! तत्पश्चात्‌ तथा उनके वक्ष:स्थलपर निवास करनेवाली हो।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16103)
- **Original**: जिसपर अग्नि-शुद्ध वस्त्र बिछा है; जो मालतीकी देवि! मैं हृदयको स्रिग्ध करनेवाली अभीष्ट
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16104)
- **Original**: मालाओंसे सुशोभित, कस्तूरी, जाती, चम्पा और शुभवार्ताका वर्णन करता हूँ; तुम उसे सखियोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16105)
- **Original**: चन्दनकी सुगन्धसे सुवासित, चारों ओरसे साथ सुस्थिर चित्तसे श्रवण करो। वह वार्ता
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16106)
- **Original**: मालतीकौं मालाओं और हीरोंके हारोंसे विभूषित दुःखरूपी दाबाग्रिमें झुलसी हुईके लिये अमृतकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16107)
- **Original**: एवं सुन्दर-सुन्दर मणियों, मोतियों और माणिक्योंसे वर्षके समान तथा विरहव्याधि-ग्रस्ताके लिये
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16108)
- **Original**: परिष्कृत है; जिसके उपधान (तकिया)-में उत्तम रसायनके सदृश है। नन्‍्दजी सदा प्रसन्न
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16109)
- **Original**: पुष्पोंकी मालाएँ लटक रही हैं और जो सब हैं। उन्हें वसुदेवने निमन्त्रित कर रखा है; अतः
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16110)
- **Original**: तरहसे मड्गलके योग्य है; उस अमूल्य र्त्लोंद्वार वे वहाँ आनन्दपूर्वक श्रीकृष्फे उपनयन-
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16111)
- **Original**: निर्मित परम मनोहर पलंगपर सदा गोपियोंद्वारा संस्कारतक ठहरेंगे। उस मड्जल-कार्यके साड्रोपाड़
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16112)
- **Original**: सेवित होती हुई हर्षपूर्वक शवन करों। मनोहरे ! सम्पन्न हो जानेपर परमानन्द-स्वरूप नन्दजी
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16113)
- **Original**: तुम्हारी प्रिय सखी एवं भक्त गोपी निरन्तर तुमपर बलराम और श्रीकृष्णको साथ लेकर हर्षपूर्वक
- **Translation**: 

---

