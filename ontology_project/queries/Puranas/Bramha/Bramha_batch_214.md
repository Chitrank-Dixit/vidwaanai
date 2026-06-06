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

### Verse 1 (Bramha 0.4261)
- **Original**: सो रही। इद्धने मनमें कहा 'यही अच्छा अवसर थोड़ा दूँ या अधिक।' उसके यों कहनेपर इन्द्र
- **Translation**: 

---

### Verse 2 (Bramha 0.4262)
- **Original**: है।' यों कहकर वे वज्र हाथमें ले दितिके उदरमें बोले--' मैं तुम्हारे साथ मित्रता चाहता हूँ।' यह
- **Translation**: 

---

### Verse 3 (Bramha 0.4263)
- **Original**: प्रवेश कर गये। गर्भमें जो बालक था, वह आयुध सुनकर मय दैत्यने कहा--'विप्रवर! ऐसे बरसे
- **Translation**: 

---

### Verse 4 (Bramha 0.4264)
- **Original**: लिये मारनेकी इच्छासे आये हुए इन्द्रको देखकर क्या लाभ। आपके साथ मेरा वैर तो है नहीं।'
- **Translation**: 

---

### Verse 5 (Bramha 0.4265)
- **Original**: भी भयभीत न हुआ और बोला--'वज्रधारी तब इन्द्रने अपने वास्तविक रूपकों प्रकट किया।
- **Translation**: 

---

### Verse 6 (Bramha 0.4266)
- **Original**: इन्द्र! मैं तुम्हारा भाई हूँ। तुम मेरी रक्षा क्यों नहीं इन्द्रकों पहचानकर मयके मनमें बड़ा विस्मय
- **Translation**: 

---

### Verse 7 (Bramha 0.4267)
- **Original**: करते? क्या मुझे मारना चाहते हो? युद्धके बिना हुआ। 'सखे! यह क्‍या बात है? तुम तो
- **Translation**: 

---

### Verse 8 (Bramha 0.4268)
- **Original**: अन्य अवसरपर किसीको मारनेसे बढ़कर दूसरा वज़धारी हो। तुम्हारे योग्य यह कार्य नहीं है।”
- **Translation**: 

---

### Verse 9 (Bramha 0.4269)
- **Original**: कोई पातक नहीं है। मैं गर्भसे निकलूँ, तब मुझसे इन्द्रने हँसकर मयकों हृदयसे लगाया और युद्ध कर लेना। यहाँ आकर इस प्रकार मारना कहा--'विद्वान्‌ पुरुष किसी भी उपायसे अपने
- **Translation**: 

---

### Verse 10 (Bramha 0.4270)
- **Original**: तुम्हारे लिये उचित नहीं होगा। बड़े लोग विपत्तिमें अभीष्ट कार्यकी सिद्धि करते हैं।' तबसे मयके
- **Translation**: 

---

### Verse 11 (Bramha 0.4271)
- **Original**: पड़नेपर भो कुमार्गपर पैर नहीं रखते। मैंने न तो साथ इन्द्रकी गहरी मैत्री हो गयी। मय सदाके
- **Translation**: 

---

### Verse 12 (Bramha 0.4272)
- **Original**: अभी विद्या पढ़ी है, न शस्त्र चलाना सीखा है लिये इन्द्रका हितैषी हो गया। उसने इन्द्रभवनमें
- **Translation**: 

---

### Verse 13 (Bramha 0.4273)
- **Original**: और न आयुधोंका ही संग्रह किया है। तुम विद्वान जाकर सब बातें बतायीं, साथ ही इन्द्रको माया
- **Translation**: 

---

### Verse 14 (Bramha 0.4274)
- **Original**: हो। तुम्हारे हाथमें वज़ शोभा पा रहा है। क्या मुझे भी प्रदान की। इन्द्रने प्रसन्‍न होकर पूछा--' मय!
- **Translation**: 

---

### Verse 15 (Bramha 0.4275)
- **Original**: मारते समय तुम्हें लज्जा नहीं आती? कुलीन पुरुष बताओ, अब मुझे क्‍या करना चाहिये?! कभी भी कुत्सित कर्म नहीं करते। मुझे मारनेसे मयने कहा--अगस्त्यके आश्रमपर जाओ।
- **Translation**: 

---

### Verse 16 (Bramha 0.4276)
- **Original**: तुम्हें क्‍या मिलेगा, यश अथवा पुण्य? गर्भमें आये वहीं गर्भवती दिति रहती है। उसकी सेवा करते
- **Translation**: 

---

### Verse 17 (Bramha 0.4277)
- **Original**: हुए प्राणी इच्छानुसार मारे जा सकते हैं, किंतु हुए आश्रममें कुछ दिन निवास करो; फिर अवसर
- **Translation**: 

---

### Verse 18 (Bramha 0.4278)
- **Original**: इसमें कौन-सा पुरुषार्थ है। भाई! यदि तुम्हें देखकर वज्र हाथमें लिये दितिके गर्भमें प्रवेश कर
- **Translation**: 

---

### Verse 19 (Bramha 0.4279)
- **Original**: युद्धसे प्रेम है और मुझसे ही भिड़ना चाहते हो जाओ और वज़से उस बढ़ते हुए गर्भके दुकड़े-
- **Translation**: 

---

### Verse 20 (Bramha 0.4280)
- **Original**: तो निःसंदेह चले आओ।' यों कहकर वह बालक डुकड़े कर डालों। इससे तुम्हारे उस शत्रुका
- **Translation**: 

---

