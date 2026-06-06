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

### Verse 1 (Bramha 0.3861)
- **Original**: दिन भगवान्‌ शंकर एकान्तमें पार्वतीजीके साथ समीप क्यों नहीं आती?' पुत्रकी यह बात सुनकर
- **Translation**: 

---

### Verse 2 (Bramha 0.3862)
- **Original**: बैठे थे। वहाँ पार्वतीजीने एक बात कही, जिसे उसकी माताने धायसे कहा-'तुम भोगवततीसे
- **Translation**: 

---

### Verse 3 (Bramha 0.3863)
- **Original**: सुनकर भगवान्‌ शिव ठठाकर हँस पड़े। उस जाकर कहो, 'तुम्हारा पति एक सर्प है। देखो,
- **Translation**: 

---

### Verse 4 (Bramha 0.3864)
- **Original**: समय मुझे भी हँसी आ गयी। इससे कुपित होकर इसपर क्या कहती है।' 'बहुत अच्छा' कहकर
- **Translation**: 

---

### Verse 5 (Bramha 0.3865)
- **Original**: भगवान्‌ने मुझे यह शाप दिया-- तू मनुष्य-योनिमें धाय भोगवतीके पास गयी और एकान्तमें विनीत
- **Translation**: 

---

### Verse 6 (Bramha 0.3866)
- **Original**: सर्परूपसे जन्म लेकर ज्ञानी होगा।' कल्याणी! भावसे बोली-“कल्याणी! मैं तुम्हारे पतिको
- **Translation**: 

---

### Verse 7 (Bramha 0.3867)
- **Original**: यह शाप सुनकर तुमने और मैँने भी भगवान्‌कों जानती हूं। वे देवता हैं। किंतु यह बात किसीपर
- **Translation**: 

---

### Verse 8 (Bramha 0.3868)
- **Original**: प्रसन्न करनेकी चेष्टा की। तब उन्होंने कहा--' जब प्रकट न करना--वे मनुष्य नहीं, सर्पकि रूपमें हैं।'
- **Translation**: 

---

### Verse 9 (Bramha 0.3869)
- **Original**: तुम गौतमीके तटपर मेरा पूजन करोगे और मैं धायकी बात सुनकर भोगवतीने कहा--'मनुष्य-
- **Translation**: 

---

### Verse 10 (Bramha 0.3870)
- **Original**: तुम्हारे अन्तःकरणमें ज्ञानका आधान करूँगा, उस कन्याको सामान्यतः मनुष्य ही पति मिला करता
- **Translation**: 

---

### Verse 11 (Bramha 0.3871)
- **Original**: समय तुम भोगवतीके प्रसादसे शापमुक्त हो है; यदि देवजातिका पुरुष पतिरूपमें प्राप्त हो, तब
- **Translation**: 

---

### Verse 12 (Bramha 0.3872)
- **Original**: जाओगे” इसीलिये मुझपर यह संकट आया है। तो क्‍या कहना। वह तो बड़े पुण्यसे मिलता है।'
- **Translation**: 

---

### Verse 13 (Bramha 0.3873)
- **Original**: तुम मुझे गौतमीके तटपर ले चलो और मेरे साथ धायने भोगवर्तीकी बात सर्पसे, उसको मातासे
- **Translation**: 

---

### Verse 14 (Bramha 0.3874)
- **Original**: ही भगवान्‌की पूजा करों। इससे मेरा शाप छूट और महाराज शूरसेनसे भी कही। भोगवतीने भी
- **Translation**: 

---

### Verse 15 (Bramha 0.3875)
- **Original**: जायगा और हम दोनों पुनः भगवान्‌ शिवका धायको बुलाकर कहा--'तुम्हारा कल्याण हो,
- **Translation**: 

---

### Verse 16 (Bramha 0.3876)
- **Original**: सांनिध्य प्राप्त करेंगे। कष्टमें पड़े हुए समस्त मुझे मेरे स्वामीका दर्शन तो कराओ।' प्राणियोंके लिये सदा भगवान्‌ शिव ही परम गति तब धायने उसे ले जाकर अत्यन्त भयानक
- **Translation**: 

---

### Verse 17 (Bramha 0.3877)
- **Original**: हैं।'” पतिको यह बात सुनकर भोगवती उन्हें सर्पका दर्शन कराया। वह सुगन्धित फूलोंसे
- **Translation**: 

---

### Verse 18 (Bramha 0.3878)
- **Original**: साथ ले गौतमी-तटपर गयी और वहाँ गौतमीगें आच्छादित पलंगपर विराजमान था। एकान्त गृहमें
- **Translation**: 

---

### Verse 19 (Bramha 0.3879)
- **Original**: स्नान करके उसने शिवका पूजन किया। इससे रत्लॉसे विभूषित भयानक सर्पके आकारमें बैठे
- **Translation**: 

---

### Verse 20 (Bramha 0.3880)
- **Original**: प्रसन्त होकर भगवान्‌ने उस सर्पको दिव्य रूप हुए अपने स्वामीको देखकर भोगवततीने हाथ
- **Translation**: 

---

