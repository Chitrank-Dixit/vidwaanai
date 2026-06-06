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

### Verse 1 (Bramha 0.8541)
- **Original**: उपायसे चञ्लल मनको रोका जा सके, उसमें मनको बुद्धिमें स्थापित करनेपर जब ये इन्द्रिय
- **Translation**: 

---

### Verse 2 (Bramha 0.8542)
- **Original**: तत्परतापूर्वक लग जाय और साधनासे कभी और मन स्थिर हो जाते हैं, उस समय इनकी , बिचलित न हो। अपने रहनेके लिये शून्य गृहको ध्वानमध्ययन॑ दान॑ सत्य॑ होराज॑वं क्षमा
- **Translation**: 

---

### Verse 3 (Bramha 0.8543)
- **Original**: शौच॑ चैवात्मन: शुद्धिरिन्द्रियाणां भ्र निग्रह:
- **Translation**: 

---

### Verse 4 (Bramha 0.8544)
- **Original**: एतैविंवर्धते तेज: पाप्मानं॑ चापकर्षति
- **Translation**: 

---

### Verse 5 (Bramha 0.8545)
- **Original**: (235। 45-46 )
- **Translation**: 

---

### Verse 6 (Bramha 0.8546)
- **Original**: * कर्म तथा ज्ञानका अन्तर, परमात्मतत्त्वका निरूपण तथा अध्यात्मज़ानका वर्णन 409 शैबोकार करे, क्योंकि वहाँ चित्त एकांग्र रह
- **Translation**: 

---

### Verse 7 (Bramha 0.8547)
- **Original**: जाता है। दूसरे लोग धनकी इच्छा या संप्रह करनेके सकता है। योगका साधक मन, वाणी अथवा
- **Translation**: 

---

### Verse 8 (Bramha 0.8548)
- **Original**: कारण अत्यन्त विकल हैं, यह देखकर उसकी क्रियाद्वारा भी कहीं आसक्त न हो। वह सबकी
- **Translation**: 

---

### Verse 9 (Bramha 0.8549)
- **Original**: ओरसे विरक्त हो जाय। मिट्टीके ढेले, पत्थर और ओरस्ते उपेक्षाका भाव रखे, नियमित भोजन करे
- **Translation**: 

---

### Verse 10 (Bramha 0.8550)
- **Original**: सुवर्णको समान समझे। इस प्रकार योग-मार्गपर तथा लाभ और अलाभको समान समझे। जो उस
- **Translation**: 

---

### Verse 11 (Bramha 0.8551)
- **Original**: चलनेवाला साधक मोहबश कभी उससे विचलित योगीकौ निन्‍्दा करे और जो उसको मस्तक
- **Translation**: 

---

### Verse 12 (Bramha 0.8552)
- **Original**: न हो। कोई नीच वर्णका पुरुष अथवा स्त्री ही क्यों झुकाये, उन दोनोंके ही प्रति वह समान भाव
- **Translation**: 

---

### Verse 13 (Bramha 0.8553)
- **Original**: न हो, यदि उसे धर्म करनेकी अभिलाषा हो तो वह रखे। वह किसी एककी बुराई या भलाई न सोचे।
- **Translation**: 

---

### Verse 14 (Bramha 0.8554)
- **Original**: भी इस योगमार्गसे परम गतिकों प्राप्त कर सकता कुछ लाभ होनेपर हर्षसे फूल न उठे और लाभ
- **Translation**: 

---

### Verse 15 (Bramha 0.8555)
- **Original**: है। योगी पुरुष अजन्मा, पुरातन, जरावस्थासे रहित, न होनेपर चिन्ता न करें। अपितु वायुका सहधर्मी'
- **Translation**: 

---

### Verse 16 (Bramha 0.8556)
- **Original**: सनातन, इन्द्रियातीत एवं अगोचर ब्रह्मको प्राप्त होते होकर सब प्राणियोंके प्रति समान भाव रखे।' इस
- **Translation**: 

---

### Verse 17 (Bramha 0.8557)
- **Original**: हैं। जो मनीषी पुरुष इस योगकी पद्धतिपर प्रकार स्वस्थचित्त होकर सर्वत्र समान दृष्टि रखनेवाला
- **Translation**: 

---

### Verse 18 (Bramha 0.8558)
- **Original**: दृष्टिपात करके इसे अपनाते हैं, वे ब्रह्माजीके साधक यदि छ: महीने भी निरन्तर योगके
- **Translation**: 

---

### Verse 19 (Bramha 0.8559)
- **Original**: समान हो उस उत्तम गतिको प्राप्त करते हैं, जहाँसे अभ्यासमें लगा रहे तो उसे ब्रह्मका साक्षात्कार हो
- **Translation**: 

---

### Verse 20 (Bramha 0.8560)
- **Original**: पुन: इस संसारमें नहीं आना पड़ता। “+“स्फ224957.000 कर्म तथा ज्ञानका अन्तर, परमात्मतत्त्वका निरूपण तथा अध्यात्मज्ञान और उसके साथनोंका वर्णन मुनि बोले--महसयें ! यदि वेदकी ऐसी आज्ञा है
- **Translation**: 

---

