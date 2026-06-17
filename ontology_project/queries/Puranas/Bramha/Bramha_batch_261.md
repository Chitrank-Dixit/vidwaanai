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

### Verse 1 (Bramha 0.5201)
- **Original**: अपने घरको लौट आयेंगे।' वैश्य तो अपनी सद्भावनाके शजा भौवन निवास करते थे। उसी नगरमें वृद्धकौशिक
- **Translation**: 

---

### Verse 2 (Bramha 0.5202)
- **Original**: अनुसार सत्य ही कहता था, किंतु ब्राह्मण उसे धोखा नामके एक ब्राह्मण थे, जिनके वेदवेत्ताओंमें श्रेष्ठ
- **Translation**: 

---

### Verse 3 (Bramha 0.5203)
- **Original**: दे रहा था। उसके मनमें पाप था। किंतु वैश्य उसे गौतम नामक पुत्र हुआ। गौतमकी एक वैश्यके साथ
- **Translation**: 

---

### Verse 4 (Bramha 0.5204)
- **Original**: ऐसा नहीं समझता था। दोनेंनि आपसमें सलाह की मित्रता हुई। वैश्यका नाम मणिकुण्डल था। इनमें
- **Translation**: 

---

### Verse 5 (Bramha 0.5205)
- **Original**: और माता-पिताको सूचना दिये बिना हो धन एक दरिद्र और दूसरा धनी था तो भी दोनों एक-
- **Translation**: 

---

### Verse 6 (Bramha 0.5206)
- **Original**: कमानेके लिये देश-देशान्तरमें चल दिये। ब्राह्मण दूसरेके हितैषी थे। एक दिन गौतमने अपने धनी
- **Translation**: 

---

### Verse 7 (Bramha 0.5207)
- **Original**: सोचने लगा-'जिस किसी उपायसे हो सके, वैश्यका मित्र मणिकुण्डलसे एकान्तमें प्रेमपूर्वकत कहा--'मित्र!
- **Translation**: 

---

### Verse 8 (Bramha 0.5208)
- **Original**: धन ले लूँ। अहो, पृथ्वीपर सहस्त्रों सुन्दर नगर हैं, हमलोग धनका उपार्जन करनेके लिये पर्वतों और
- **Translation**: 

---

### Verse 9 (Bramha 0.5209)
- **Original**: जहाँ कामकी अधिक्ठात्रो देवी-जैसी अभीष्ट भोग समुद्रोंकी यात्रा करें। यदि अनुकूल सुख न प्राप्त
- **Translation**: 

---

### Verse 10 (Bramha 0.5210)
- **Original**: प्रदान करनेवाली युवतियाँ हैं। यदि यत्रपूर्वक धन हुआ तो समझना चाहिये जवानी व्यर्थ गयी। धनके
- **Translation**: 

---

### Verse 11 (Bramha 0.5211)
- **Original**: लाकर उनको दिया जाय तो वे सदा भोगी जा सकती बिना सौख्य कैसे प्राप्त हो सकता है। अहो! निर्धन
- **Translation**: 

---

### Verse 12 (Bramha 0.5212)
- **Original**: हैं और वही जीवन सफल है। किस प्रकार वैश्यसे मनुष्यको धिक्कार है।' कुण्डलने ब्राह्मणसे कहा--' मेरे
- **Translation**: 

---

### Verse 13 (Bramha 0.5213)
- **Original**: अपने हाथमें आये हुए धनको हड़पकर उसका पिताने बहुत धन कमाया है। अब अधिक धन
- **Translation**: 

---

### Verse 14 (Bramha 0.5214)
- **Original**: इच्छानुसार उपभोग करूँ?” यह सोचते हुए गौतमने लेकर क्या करूँगा।' तब ब्राह्मणने पुनः मणिकुण्डलसे
- **Translation**: 

---

### Verse 15 (Bramha 0.5215)
- **Original**: मणिकुण्डलसे हँसते-हँसते कहा--' पापसे ही जीवोंकी कहा-'जो धर्म, अर्थ, ज्ञान और भोगोंसे तृप्त हो
- **Translation**: 

---

### Verse 16 (Bramha 0.5216)
- **Original**: उन्नति होती है और वे मनोवाज्छित सुख प्राप्त करते जाय, ऐसा कौन पुरुष प्रशंसनीय माना जाता है।
- **Translation**: 

---

### Verse 17 (Bramha 0.5217)
- **Original**: हैं। संसारमें धर्मात्मा लोग दुःखके ही भागी देखे जाते सखे! इन सबकी अधिकाधिक वृद्धि ही समस्त
- **Translation**: 

---

### Verse 18 (Bramha 0.5218)
- **Original**: हैं। अत: एक मात्र दुःख ही जिसका फल है, उस शरीरधारियोंको अभीष्ट होती है। जो प्राणी अपने ही
- **Translation**: 

---

### Verse 19 (Bramha 0.5219)
- **Original**: धर्मसे क्या लाभ।' व्यवसायसे जीवन-निर्वाह करते हैं, वे धन्य हैं। जो
- **Translation**: 

---

### Verse 20 (Bramha 0.5220)
- **Original**: . बैश्यने कहा--ऐसी बात नहीं है। धर्ममें ही दूसरेके दिये हुए धनसे संतोष-लाभ करते हैं, वे कष्से
- **Translation**: 

---

