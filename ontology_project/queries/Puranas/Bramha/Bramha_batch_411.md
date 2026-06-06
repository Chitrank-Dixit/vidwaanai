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

### Verse 1 (Bramha 0.8201)
- **Original**: लगेंगे और वृक्षोंके फल सारहीन होंगे। कलितें धारण करनेवाले और दुष्ट अन्तःकरणवाले होंगे;
- **Translation**: 

---

### Verse 2 (Bramha 0.8202)
- **Original**: प्रायः लोग घुटनोंतक बस्त्र पहनेंगे। वृक्षोंमें शमीको अत: ये थोड़े ही समयमें नष्ट हो जायँगे। हो अधिकता होगी। चारों बर्णोके सब लोग प्राय ब्राह्मणो! जब-जब इस जगतूमें पाखण्ड-वृत्ति
- **Translation**: 

---

### Verse 3 (Bramha 0.8203)
- **Original**: शूद्रवत्‌ हो जायँंगे।& कलियुगके आनेपर प्राय अरक्षितारों हर्तार: शुल्कव्याजेन पार्थिवा:। हारिणो जतवित्तानां सम्प्राप्ते च कलौ युगे
- **Translation**: 

---

### Verse 4 (Bramha 0.8204)
- **Original**: (229। 34) + यबदा यदा हि पाखण्डवृत्तिरत्रोपलक्ष्यों।तदा तदा कलेबृंद्धिरनुमेषबा विचक्षणै:
- **Translation**: 

---

### Verse 5 (Bramha 0.8205)
- **Original**: यदा यदा सतां हानिर्वेदमार्गानुसारिणामू। तदा तदा कलेवृद्धिरनुमेया विचक्षणै:
- **Translation**: 

---

### Verse 6 (Bramha 0.8206)
- **Original**: प्रार्म्भाश्चावसीदन्ति. दा धर्मकृतां नृणाम्‌। तदानुमेय॑ प्राधान्य॑ कलेविंप्रा वियशक्षणै:
- **Translation**: 

---

### Verse 7 (Bramha 0.8207)
- **Original**: (229। 44-46) + किं देवै: कि द्विजैवेंदं: कि शौचेनाम्बुजन्मता। इत्येब॑ प्रलपिष्यन्ति पाखण्डोपहता नरा;
- **Translation**: 

---

### Verse 8 (Bramha 0.8208)
- **Original**: (229। 50) & जानुप्रायाणि अस्त्राणि शमौप्राया महोरुहा:। शुद्र॒प्रायास्तथा वर्षा भविष्यन्ति कलौं युगे
- **Translation**: 

---

### Verse 9 (Bramha 0.8209)
- **Original**: नि (3229। 52)
- **Translation**: 

---

### Verse 10 (Bramha 0.8210)
- **Original**: 394 * संक्षिप्त ब्रह्मपुराण « छोटे-छोटे धान्य होंगे। अधिकतर बकरियोंका
- **Translation**: 

---

### Verse 11 (Bramha 0.8211)
- **Original**: इसीलिये मैंने कलियुगको श्रेष्ठ बताया। सत्ययुगमों दूध मिलेगा और उशीर (खस) ही एकमात्र
- **Translation**: 

---

### Verse 12 (Bramha 0.8212)
- **Original**: ध्यान, ज़ेतामें यज्ञोंद्रार यजत और द्वापरमें पूजन अनुलेपन होगा। कलियुगमें अधिकतर सास और
- **Translation**: 

---

### Verse 13 (Bramha 0.8213)
- **Original**: करनेसे मनुष्य जिस फलको पाता है, वही कलियुगमें ससुर ही लोगोंके गुरुजन होंगे। मुनिवरों! उस
- **Translation**: 

---

### Verse 14 (Bramha 0.8214)
- **Original**: केशवका नाम-कीर्तन करनेमात्रसे मिल जाता है। समय मनोहारिणी भार्या और साले आदि ही सुदहद्‌
- **Translation**: 

---

### Verse 15 (Bramha 0.8215)
- **Original**: धर्मज्ञ ब्राह्मणो! इस कलियुगमें थोड़े-से परिश्रमसे समझे जायँगे। लोग अपने ससुरके अनुगामी
- **Translation**: 

---

### Verse 16 (Bramha 0.8216)
- **Original**: ही मनुष्यको महान्‌ धर्मकी प्राप्ति हो जाती है। होकर कहेंगे कि 'कौन किसको माता है और , इसीलिये मैं कलियुगसे अधिक संतुष्ट हूँ ए कौन किसका पिता। सब जीव अपने कर्मोके
- **Translation**: 

---

### Verse 17 (Bramha 0.8217)
- **Original**: अब शुद्रॉकी विशेषताका वर्णन सुनो। ट्विजोंको अनुसार हो जन्मते और परते हैं।'* उस समय
- **Translation**: 

---

### Verse 18 (Bramha 0.8218)
- **Original**: पहले ब्रह्मचर्य-व्रतका पालन करते हुए बेदाध्ययन थोड़ी बुद्धिवाले मनुष्य मन, वाणी और शरीरके
- **Translation**: 

---

### Verse 19 (Bramha 0.8219)
- **Original**: करना पड़ता है। फिर धर्मत: प्राप्त हुए धनके द्वारा दोषोंसे प्रभावित होकर प्रतिदिन बारंबार पाप
- **Translation**: 

---

### Verse 20 (Bramha 0.8220)
- **Original**: विधिपूर्वक यज्ञ करना पड़ता है। इसमें भी व्यर्थ करेंगे। सत्य, शौच और लज्ञासे रहित मनुष्योंके
- **Translation**: 

---

