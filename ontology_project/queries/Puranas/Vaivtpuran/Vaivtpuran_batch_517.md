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

### Verse 1 (Vaivtpuran 31.7511)
- **Original**: पृथ्वीरूप हैं; उन सर्वरूपको मेरा प्रणाम है। जो सर्वस्वरूप और स्वेच्छानुसार रूप धारण करनेवाले
- **Translation**: 

---

### Verse 2 (Vaivtpuran 31.7512)
- **Original**: पत्रोंमें तुलसीपत्र, लकडियोंमें चन्दन और वृक्षोंमें हैं; उन प्रभुको मेरा अभिवादन है। जिनका रूप
- **Translation**: 

---

### Verse 3 (Vaivtpuran 31.7513)
- **Original**: कल्पवृक्ष हैं; उन जगत्पतिको मेरा अभिवादन अत्यन्त सुन्दर है, जो उपमारहित हैं और अत्यन्त
- **Translation**: 

---

### Verse 4 (Vaivtpuran 31.7514)
- **Original**: है। जो पुष्पोंमें पारिजात, अन्नोंमें धान और भक्ष्य कराल रूप धारण करते हैं; उन सर्वव्यापी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 31.7515)
- **Original**: पदार्थोमें अमृत हैं; उन अनेक रूपधारीको मैं भगवान्‌को मैं सिर झुकाता हूँ। जो कर्मके
- **Translation**: 

---

### Verse 6 (Vaivtpuran 31.7516)
- **Original**: सिर झुकाता हूँ। जो गजराजोंमें ऐरावत, पक्षियोंमें कर्मरूप, समस्त कर्मोके साक्षी, फल और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 31.7517)
- **Original**: गरुड और गौओंमें कामधेनु हैं; उन सर्वरूपको फलदाता हैं; उन सर्वरूपको मेरा नमस्कार है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 31.7518)
- **Original**: मैं नमन करता हूँ। जो तैजस पदार्थोमें सुवर्ण, जो पुरुष अपनी कलासे विभिन्न मूर्ति धारण करके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 31.7519)
- **Original**: धान्योंमें यव और पशुओमें सिंह हैं; उन श्रेष्ठ सृष्टिका रचयिता, पालक और संहारक हैं तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 31.7520)
- **Original**: रूपधारीके समक्ष मैं नत होता हूँ। जो यक्षोंमें जो कलांशसे नाना प्रकारकी मूर्ति धारण करते कुबेर, ग्रहोंमें बृहस्पति और दिकृपालोंमें महेन्द्र हैं; उनके चरणोंमें मैं प्रणिषात करता हूँ। जो हैं; उन श्रेष्ठ परमात्माकों मैं नमस्कार करता हूँ। मायाके वशीभूत होकर स्वयं प्रकृतिरूप हैं और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 31.7521)
- **Original**: जो शास्त्रोंमें बेदसमुदाय, सदसदूविवेकशील स्वयं पुरुष हैं तथा स्वयं इन दोनोंसे परे हैं; बुद्धिमानोंमें सरस्वतो और अक्षरोंमें अकार हैं; उन परात्परको मैं सदा नमस्कार करता हूँ। जो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 31.7522)
- **Original**: उन प्रधान देवको मैं प्रणाम करता हूँ। जो मन्त्रोंमें अपनी माणसे स्त्री, पुरुष और नपुंसकका रूप
- **Translation**: 

---

### Verse 13 (Vaivtpuran 31.7523)
- **Original**: विष्णुमन्त्र, तौथॉमें स्वयं गड्ा और इन्द्रियोंमें मन
- **Translation**: 

---

### Verse 14 (Vaivtpuran 31.7524)
- **Original**: 360 » संक्षिप्त गरहमवैचर्तपुराण * न 4
- **Translation**: 

---

### Verse 15 (Vaivtpuran 31.7525)
- **Original**: 4444444444 43433 >> जे हैं; उन सर्वश्रेष्ठकों मेरा नमस्कार है। जो शस्त्रोंमें
- **Translation**: 

---

### Verse 16 (Vaivtpuran 31.7526)
- **Original**: पा सकता है? जिनकी स्तुति करनेमें बेद समर्थ सुदर्शनचक्र, व्याधियोंमें वैष्णव-ज्वर और तेजोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 31.7527)
- **Original**: नहीं हैं तथा सरस्वती जड-सी हो जाती हैं, ब्रह्मतेज हैं; उन वरणीय प्रभुको मेरा प्रणाम है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 31.7528)
- **Original**: मन-वाणीसे परे उन भगवान्‌का कौन विद्ठान्‌ जो बलवानोंमें निषेक-कर्मफलभोग, शीघ्र स्तवन कर सकता है? जो शुद्ध तेज:स्वरूप, चलनेवालोंमें मम और गणना करनेवालोंमें काल
- **Translation**: 

---

### Verse 19 (Vaivtpuran 31.7529)
- **Original**: भक्तोंक लिये मूर्तिमान्‌ अनुग्रह और अत्यन्त हैं; उन बिलक्षण देवको मैं अभिवादन करता सुन्दर हैं; उन श्याम-रूपधारी प्रभुको मेरा हूँ। जो गुरुऑँमें ज्ञानदाता, बन्धुओंमें मातृरूप और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 31.7530)
- **Original**: अभिवादन है। जिनके दो भुजाएँ हैं, मुखपर मित्रोंमें जन्मदाता-पितृरूप हैं; उन साररूप
- **Translation**: 

---

