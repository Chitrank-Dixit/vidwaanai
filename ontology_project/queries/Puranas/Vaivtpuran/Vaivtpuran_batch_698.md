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

### Verse 1 (Vaivtpuran 265.5097)
- **Original**: हैं। उनके प्रिय सखा बारह ग्वालबाल सफेद वरुण, चन्द्रमा, सूर्य, रुद्र, अग्नि तथा कृष्णमन्त्रके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 265.5098)
- **Original**: चँवर लिये उनकी सेवा करते हैं। प्रेमपीडिता, उपासक भारतीय वैष्णव--इन सबने ही गोलोकको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 265.5099)
- **Original**: सुस्थिरयौवना, वहिशुद्ध चिन्मय वस्त्रधारिणी, देखा है। दूसरोंने इसे कभी नहीं देखा है।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 265.5100)
- **Original**: रत्रभूषणभूषिता एवं परम मनोहारिणी गोपिकाएँ उस गोलोकधाममें श्यामसुन्दर श्रीकृष्ण
- **Translation**: 

---

### Verse 5 (Vaivtpuran 265.5101)
- **Original**: मन्द-मन्द मुस्कराती हुई उनको छबि निहारती निरामय रल्नसिंहासनपर विराजमान हैं । रत्रोंके हार,
- **Translation**: 

---

### Verse 6 (Vaivtpuran 265.5102)
- **Original**: रहती हैं। रासमण्डलके मध्यभागमें परात्पर पुरुष किरीट तथा रज्लमय भूषणोंसे वे विभूषित हैं।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 265.5103)
- **Original**: श्रीकृष्णके राजा सुयज्ञने इसी रूपमें दर्शन किये। अग्निशुद्ध, अत्यन्त निर्मल चिन्मय पीताम्बर उनके
- **Translation**: 

---

### Verse 8 (Vaivtpuran 265.5104)
- **Original**: श्रीराधाने ही वहाँ उन्हें अपने प्राणवल्लभके दर्शन श्रीअड्रोंकी शोभा बढ़ाता है। उनके सारे अड्ग
- **Translation**: 

---

### Verse 9 (Vaivtpuran 265.5105)
- **Original**: कराये थे। चारों वेद मनोहर मूर्ति धारण करके अन्दनसे चर्चित हैं। वे किशोर गोपबालकके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 265.5106)
- **Original**: उनके दर्शन करते थे। राग-रागिनियाँ भी मूर्तिमती रूपमें दिखायी देते हैं। नूतन जलधरके समान
- **Translation**: 

---

### Verse 11 (Vaivtpuran 265.5107)
- **Original**: होकर वाच्ययन्त्र और मुखसे उन्हें अत्यन्त मनोहर श्याम कान्ति, श्वेत कमलके समान नेत्र, शरत्‌की
- **Translation**: 

---

### Verse 12 (Vaivtpuran 265.5108)
- **Original**: संगीत सुनाती थीं। शिवे ! नित्य सनातनी प्रकृतिके पूर्णिमाके चन्द्रमण्डलकों तिरस्कृत करनेवाला
- **Translation**: 

---

### Verse 13 (Vaivtpuran 265.5109)
- **Original**: साथ तुम भी सदा उनके चरणारविन्दोंकी सेवा मन्द हास्यसे सुशोभित मुख, मनोहर आकृति,
- **Translation**: 

---

### Verse 14 (Vaivtpuran 265.5110)
- **Original**: करती हो। वे तुलसीदलसे मण्डित होते हैं तथा दो भुजाएँ और हाथोंमें मुरली-यही उनके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 265.5111)
- **Original**: कस्तूरी, कुछ्रुम, गनन्‍्ध, चन्दन, दूर्वा, अक्षत,
- **Translation**: 

---

### Verse 16 (Vaivtpuran 265.5112)
- **Original**: * प्रकृतिखाण्ड + 269 अंक ऋ$%$%$$% %#%%## ## #% # #### %##### #### ###ऋकऋऋकऋऊऋकऊऋऊऋऊऊ््ुऊ कक #
- **Translation**: 

---

### Verse 17 (Vaivtpuran 265.5113)
- **Original**: ############%# 5 पारिजातपुष्प तथा विरजाके निर्मल जलसे उनके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 265.5114)
- **Original**: सहसा उठकर खड़े हो गये। उन्होंने मनद मुस्कानके लिये नित्य अर्घ्य दिया जाता है। उस समय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 265.5115)
- **Original**: साथ श्रीराधाके साथ वार्तालाप और उनका सम्मान उनकी बड़ी शोभा होती है। वे सुप्रसन्न, स्वतन्त्र,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 265.5116)
- **Original**: किया। प्राचीनकालके वे वेदवेत्ता विद्वान्‌ बेदोंके समस्त कारणोंके भी कारण, सर्वान्तरात्मा, सर्वेश्वर,
- **Translation**: 

---

