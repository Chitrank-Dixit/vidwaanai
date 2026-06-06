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

### Verse 1 (Bramha 0.5081)
- **Original**: था। उसने एकमात्र गज्जाकी शरण ली और उठा लिया और ले जाकर उसे गौतमी गड्जा . 'गड़े! मेरी रक्षा करो' इस प्रकार कहते हुए तथा भगवान्‌ गदाधरका दर्शन कराया। चिच्चिकने
- **Translation**: 

---

### Verse 2 (Bramha 0.5082)
- **Original**: स्नान किया। तदनन्तर भगवान्‌ गदाधरको प्रणाम स्रान करके जैलोक्यपावनी गड़ासे कहा--' माता
- **Translation**: 

---

### Verse 3 (Bramha 0.5083)
- **Original**: करके राजा पवमानसे विदा ले पर्वतनिवासियोंके गौतमी ! तुम तीनों लोकॉंको पवित्र करनेवाली
- **Translation**: 

---

### Verse 4 (Bramha 0.5084)
- **Original**: देखते-देखते वह स्वर्गमें चला गया। पवमान भी हो। मनुष्य जबतक तुम्हारा दर्शन नहीं करता,
- **Translation**: 

---

### Verse 5 (Bramha 0.5085)
- **Original**: अपनी सेनाके साथ अपने नगरकों लौट गये। तभीतक इस लोक और परलोकमें पातकी
- **Translation**: 

---

### Verse 6 (Bramha 0.5086)
- **Original**: तबसे बेदवेत्ता विद्वानॉने उस तीर्थका नाम कहलाता है। यद्यपि मैंने सब प्रकारके पाप
- **Translation**: 

---

### Verse 7 (Bramha 0.5087)
- **Original**: पावमानतीर्थ, चिच्चिकतीर्थ और गदाधरतीर्थ रख किये हैं तो भी अब तुम्हारी शरणमें आया हूँ।
- **Translation**: 

---

### Verse 8 (Bramha 0.5088)
- **Original**: दिया। उस तीर्थमें किया हुआ पुण्यकर्म कोटिं- मेगा उद्धार करो। तुम भगवान्‌ विष्णुके चरणकमलेसे
- **Translation**: 

---

### Verse 9 (Bramha 0.5089)
- **Original**: कोटिगुना हो जाता है। +2*>-म्विलथी (>> भद्गतीर्थ, पतत्रितीर्थ और विप्रतीर्थकी महिमा ब्रह्माजी कहते हैं--भद्गतीर्थ सब प्रकारके
- **Translation**: 

---

### Verse 10 (Bramha 0.5090)
- **Original**: पितासे कहा--“ पिताजी ! धनवान्‌, विद्वान, तरुण, अनिष्टोंका निवारण करनेवाला है। बह समस्त कुलीन, यशस्वी, उदार और सनाथ वरको कन्या पापोंका नाशक तथा परम शान्तिदायक है।
- **Translation**: 

---

### Verse 11 (Bramha 0.5091)
- **Original**: देनी चाहिये।* जो पिता इसके विपरीत आचरण विश्वकर्माकी पुत्री उषा भगवान्‌ सूर्यको पतिब्रता
- **Translation**: 

---

### Verse 12 (Bramha 0.5092)
- **Original**: करता है, वह नरकमें पड़ता है। सूर्यदेव! कन्या एवं प्रिया भार्या हैं। छाग्रा भी उनकी ही भार्या
- **Translation**: 

---

### Verse 13 (Bramha 0.5093)
- **Original**: विद्वानोंके लिये भी धर्मका साधन है। एक ओर हैं। छायाके पुत्र शनैश्षर हैं। शनैश्वरकी बहिन
- **Translation**: 

---

### Verse 14 (Bramha 0.5094)
- **Original**: पर्बत, बन और काननोंसहित समूची पृथ्वी और विष्टि हुई। उसकी आकृति भयानक थी। वह
- **Translation**: 

---

### Verse 15 (Bramha 0.5095)
- **Original**: दूसरी ओर वबस्त्राभूषणोंसे अलंकृत नीरोग पापमयी थो। भगवान्‌ सूर्यने सोचा, 'यह कन्या
- **Translation**: 

---

### Verse 16 (Bramha 0.5096)
- **Original**: कनन्‍्या-दोनों एक समान हैं। उस कन्याके किसको दूँ?' वे जिस-जिसको कन्या देना दानसे पृथ्वीदानका फल होता है। जो कन्या, चाहते, वही-वही ठसकी भयंकरताका समाचार
- **Translation**: 

---

### Verse 17 (Bramha 0.5097)
- **Original**: अश्व, गौ और तिलकी बिक्री करता है, उसका सुनकर उसे लेना अस्वीकार कर देता और
- **Translation**: 

---

### Verse 18 (Bramha 0.5098)
- **Original**: रौरव आदि नरकोंसे कभी छुटकारा नहीं होता। कहता, 'ऐसी भार्या लेकर हम क्‍या करेंगे।'
- **Translation**: 

---

### Verse 19 (Bramha 0.5099)
- **Original**: कन्‍्याके विवाहमें कभी विलम्ब नहीं करना ऐसी अबस्थामें विष्टिने दुखी होकर अपने
- **Translation**: 

---

### Verse 20 (Bramha 0.5100)
- **Original**: चाहिये। उसमें विलम्ब करनेपर पिताकों जो * ओमते विदुषे यूने कुलौताय यशस्विने । उदाराय सनाधाय कन्या देया यराय वै
- **Translation**: 

---

