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

### Verse 1 (Bramha 0.5901)
- **Original**: भगवान्‌ अनन्त पृथ्वीपर तुम्हारी रक्षा करें।' हो जाता था। श्रीकृष्णने उसके स्तनकों दोनों। इस प्रकार नन्दगोपद्वारा स्वस्तिवाचन होनेपर हाथोंसे पकड़कर खूब जोरसे दबाया और क्रोधमें
- **Translation**: 

---

### Verse 2 (Bramha 0.5902)
- **Original**: बालक श्रीकृष्ण छकड़ेके नीचे एक खटोलेपर भरकर उसके प्राणोंसहित दूध पीना आरभ्भ
- **Translation**: 

---

### Verse 3 (Bramha 0.5903)
- **Original**: सुलाये गये। गोपोंको मरी हुई पूतनाका विशाल किया! उस राक्षसीके शरीरकौ नस-नाड़ियोंके , शरीर देखकर अत्यन्त भय और आश्चर्य हुआ। बन्धन छिन्न-भिन्न हो गये। वह जोर-जोरसे
- **Translation**: 

---

### Verse 4 (Bramha 0.5904)
- **Original**: एक दिनकी बात है, मधुसूदन श्रीकृष्ण छकड़ेके कराहती हुई पृथ्वीपर गिर पड़ी। मरते समय
- **Translation**: 

---

### Verse 5 (Bramha 0.5905)
- **Original**: नीचे सोये हुए थे। उस समय वे दूध पीनेके लिये उसका शरीर बड़ा भयंकर हो गया। पूतनाका
- **Translation**: 

---

### Verse 6 (Bramha 0.5906)
- **Original**: जोर-जोरसे रोने लगे। रोते-ही-रोते उन्होंने अपने
- **Translation**: 

---

### Verse 7 (Bramha 0.5907)
- **Original**: 282 + संक्षिप्त ग्रह्मपुराण « दोनों पैर ऊपरकी ओर फेंकने आरम्भ किये।
- **Translation**: 

---

### Verse 8 (Bramha 0.5908)
- **Original**: रखा। थोड़े ही दिनोंमें वे दोनों बालक महाबलवान्‌के उनका एक पैर छकड़ेसे छू गया। उसके हल्के
- **Translation**: 

---

### Verse 9 (Bramha 0.5909)
- **Original**: रूपमें प्रसिद्ध हो गये। घुटनोंके बलसे चलनेके आघातसे ही वह छकड़ा उलटकर गिर पड़ा।
- **Translation**: 

---

### Verse 10 (Bramha 0.5910)
- **Original**: कारण उनके दोनों घुटनों और हाथोंमें रगड़ पड़ उसपर रखे हुए मटके और घड़े आदि टूट-फूट
- **Translation**: 

---

### Verse 11 (Bramha 0.5911)
- **Original**: गयी थी। वे शरीरमें गोबर और राख लपेटे इधर- गये। उस समय समस्त गोप-गोपियाँ हाहाकार
- **Translation**: 

---

### Verse 12 (Bramha 0.5912)
- **Original**: उधर घूमा करते थे। यशोदा और रोहिणी उन्हें करती हुई वहाँ आ पहुँचों। उन्होंने देखा, 'बालक
- **Translation**: 

---

### Verse 13 (Bramha 0.5913)
- **Original**: रोक नहीं पाती' थीं। कभी गौओंके बाड़ेमें श्रीकृष्ण उतान सोये हुए हैं।' तब गोपोंने पूछा-- खेलते-खेलते बछड़ोंके बाड़ेमें निकल जाते थे। 'किसने इस छकड़ेको उलट दिया?' वहीं कुछ
- **Translation**: 

---

### Verse 14 (Bramha 0.5914)
- **Original**: कभी उसी दिन पैदा हुए बछड़ोंको पूँठ पकड़कर बालक खेल रहे थे। उन्होंने कहा-“इस बच्चेने
- **Translation**: 

---

### Verse 15 (Bramha 0.5915)
- **Original**: खींचने लगते थे। वे दोनों बालक एक हो ही गिराया है।' यह सुनकर गोपोंके मनमें बड़ा
- **Translation**: 

---

### Verse 16 (Bramha 0.5916)
- **Original**: स्थानपर साथ-साथ खेलते और अत्यन्त चपलता आश्चर्य हुआ। नन्दगोपने अत्यन्त विस्मित होकर
- **Translation**: 

---

### Verse 17 (Bramha 0.5917)
- **Original**: दिखाते थे। एक दिन, जब यशोदा उन्हें किसी बालकक गोदमें उठा लिया। यशेदाने भी आश्चर्यचकित
- **Translation**: 

---

### Verse 18 (Bramha 0.5918)
- **Original**: प्रकार रोक न सकीं, तब उनके मनमें कुछ क्रोध हो टूटे-फूटे भाँड़ोंके टुकड़ों और छकड़ेकी दही,
- **Translation**: 

---

### Verse 19 (Bramha 0.5919)
- **Original**: हो आया। उन्होंने अनायास ही बड़े-बड़े कार्य फूल, फल और अक्षतसे पूजा की। करनेवाले श्रीकृष्णकी कमरमें रस्सी कस दी और उन्हें ऊखलसे बाँध दिया। उसके बाद कहा--' ओ
- **Translation**: 

---

### Verse 20 (Bramha 0.5920)
- **Original**: चञझ्जल! तू बहुत ऊधम मचा रहा था। अब तुझमें सामर्थ्य हो तो जा।' यों कहकर गृहस्वामिनी यशोदा अपने काम-काजमें लग गयीं। जब ) 500
- **Translation**: 

---

