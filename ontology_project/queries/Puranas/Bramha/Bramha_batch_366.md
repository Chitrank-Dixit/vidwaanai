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

### Verse 1 (Bramha 0.7301)
- **Original**: यमदूतोंको, यमलोकके मार्गकों, यमपुरीको तथा लगती है। हजारों जन्मोंके पश्चात्‌ दुर्लभ मनुष्य-
- **Translation**: 

---

### Verse 2 (Bramha 0.7302)
- **Original**: बहाँके नरकोंको किसी प्रकार नहों देख पाते। मोहमें जीवनको पाकर जो धर्मका आचरण नहीं करता, वह
- **Translation**: 

---

### Verse 3 (Bramha 0.7303)
- **Original**: पड़कर अनेकों बार पाप कर लेनेपर भी यदि मानव निश्चय ही सौभाग्यसे बच्चित है। जो लोग कुत्सित,
- **Translation**: 

---

### Verse 4 (Bramha 0.7304)
- **Original**: सर्वपापहारी श्रीहरिको नमस्कार करते हैं तो वे दख्ि, कुरूप, रोगी, दूसरोंके सेवक और मूर्ख हैं,
- **Translation**: 

---

### Verse 5 (Bramha 0.7305)
- **Original**: नरकमें नहीं पड़ते। जो लोग शठतासे भी सदा उन्होंने पूर्वजन्ममें धर्म नहीं किया है--ऐसा जानना भगवान्‌ जनार्दनका स्मरण करते हैं, वे भी देहत्यागके चाहिये। जो दीर्घायु, शूरबीर, पण्डिठ, भोगसाधनसे
- **Translation**: 

---

### Verse 6 (Bramha 0.7306)
- **Original**: पश्चात्‌ रोण-शोकसे रहित श्रीविष्णुधामको प्राप्त होते सम्पन्न, धनवानू, नोरोग तथा रूपवान्‌ हैं, उन्होंने
- **Translation**: 

---

### Verse 7 (Bramha 0.7307)
- **Original**: हैं। अत्यन्त क्रोधमें आसक्त होकर भी जो कभी पूर्वन्‍न्ममें अवश्य ही धर्मका अनुषान किया है।
- **Translation**: 

---

### Verse 8 (Bramha 0.7308)
- **Original**: श्रीहरिके नामोंका कीर्तन करता है, वह भी चेदिराज ब्राह्मणो! इस प्रकार धर्मपतायण मनुष्य उत्तम गतिको
- **Translation**: 

---

### Verse 9 (Bramha 0.7309)
- **Original**: शिशुपालकी भाँति सम्पूर्ण दोषोंका क्षय हो जानेसे प्राप्त होते हैं और अधर्मका सेबन करनेवाले लोग पशु- । मोक्षको प्राप्त करता है * तस्माद्म॑: सेवितव्य:.. सदामुक्तिफलप्रद: । धर्मादर्थस्तथा कामों मोक्षक्ष परिकौर्त्यते
- **Translation**: 

---

### Verse 10 (Bramha 0.7310)
- **Original**: धर्मों माता पिता भ्राता थर्मो नाथ: सुदृतथा। धर्म: स्वामी सखा गोपता तथा धाता थ पोषक:
- **Translation**: 

---

### Verse 11 (Bramha 0.7311)
- **Original**: (216। 73-74) +ये भरा नरकध्यंसिवासुदेवमनुत्रता:
- **Translation**: 

---

### Verse 12 (Bramha 0.7312)
- **Original**: ते स्वप्रेडपि न पश्यन्ति यमं वा नरकाणि बा
- **Translation**: 

---

### Verse 13 (Bramha 0.7313)
- **Original**: अनादिनिधनं देव दैत्वदानवदारणम्‌
- **Translation**: 

---

### Verse 14 (Bramha 0.7314)
- **Original**: ये नमन्ति गरा नित्य॑ न हि पश्यन्ति ते यमम्‌
- **Translation**: 

---

### Verse 15 (Bramha 0.7315)
- **Original**: कर्मणा भनसा बाचा ये5च्युतं शरणं गता:। न समर्थों यमस्तेषां ते मुक्तिफलभागिन:
- **Translation**: 

---

### Verse 16 (Bramha 0.7316)
- **Original**: थे जना जगतां नाय॑ नित्य नारायण ट्विजा:
- **Translation**: 

---

### Verse 17 (Bramha 0.7317)
- **Original**: नमन्ति न हि ते विष्णों: स्थानादन्यत्र गामित:
- **Translation**: 

---

### Verse 18 (Bramha 0.7318)
- **Original**: न ते दूतान्न तनन्‍्मा्ग न यम॑ न च त॑ पुरीम्‌। प्रणम्य विष्णु पश्यन्ति नरकाणि कर्धंचन
- **Translation**: 

---

### Verse 19 (Bramha 0.7319)
- **Original**: कृत्वाप बहुश: पाप नरा मोहसमन्विता:
- **Translation**: 

---

### Verse 20 (Bramha 0.7320)
- **Original**: त यान्ति नरक॑ तत्या सर्वपापहर॑ हरिम्‌
- **Translation**: 

---

