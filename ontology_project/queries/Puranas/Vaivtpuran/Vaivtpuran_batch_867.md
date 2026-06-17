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

### Verse 1 (Vaivtpuran 543.15654)
- **Original**: पुष्कर, पुरियोंमें काशी, ज्ञानियोंमें शंकर, शास्त्रोंमें पड़ता है। जो पुरुष कामभावसे स्त्रियोंकी कि,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15655)
- **Original**: वेद, वृक्षोंमें पीपल, तपस्याओंमें मेरी पूजा तथा स्तन और मुखकी ओर निहारता है, बह दूसरे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15656)
- **Original**: ब्रतोंमें उपबास सर्वश्रेष्ठ है; उसी तरह समस्त जन्ममें दृष्टिहीन और नपुंसक होता है। जो
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15657)
- **Original**: जातियोंमें ब्राह्मण श्रेष्ठ होता है। समस्त पुण्य, ब्राह्मण ज्ञानहीन होते हुए आभिचारिक कर्म
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15658)
- **Original**: तीर्थ और ब्रत ब्राह्मणके चरणोंमें निवास करते करनेवाला तथा हिंसक होता है; वह इस प्रकार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15659)
- **Original**: हैं। ब्राह्मणकी चरणरज शुद्ध तथा पाप और दस हजार वर्षोतक अन्धतामिस्न नरकमें वास
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15660)
- **Original**: रोगका विनाश करनेबाली होती है। उनका करता है। तत्पश्चात्‌ कर्मके भोगके अनुसार
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15661)
- **Original**: शुभाशीवांद सारे कल्याणोंका कारण होता है। वह ब्राह्मण शूद्र होता है। जो शास्त्रज्ञ ज्योतिषी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15662)
- **Original**: तात! इस प्रकार मैंने अपनी जानकारी तथा लोभवश झूठ बोलता है; वह सात जन्‍्मोंतक
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15663)
- **Original**: शास्त्रज्ञाके अनुसार आपसे कर्मविपाकका वानरोंका सरदार होता है--यह धुव है। तत्पश्चात्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15664)
- **Original**: वर्णन कर दिया। अब जो अबशिष्ट है, उसे श्रवण वह ॒धर्महीन पापी अनेक जन्मोंकी तपस्याके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15665)
- **Original**: करो। इस कर्मविपाककों सुनकर उस बाचककों फलस्वरूप भारतवर्षमें उत्तम बुद्धिसम्पन्न परम
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15666)
- **Original**: सोना, चाँदी, वस्त्र और पान देना चाहिये। धर्मात्मा ब्राह्मण होता है। अपने धर्ममें तत्पर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15667)
- **Original**: मनुष्यकों चाहिये कि मेरी प्रसन्नताके लिये उस रहनेवाला ब्राह्मण अग्रिसे भी बढ़कर पवित्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15668)
- **Original**: ब्राह्मणको तुरंत सौं स्वर्णमुद्राएं, बहुत-सौ गायें, और अत्यन्त तेजस्वी होता है, उससे देवगण
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15669)
- **Original**: चाँदी, वस्त्र और ताम्बूल दक्षिणारूपमें समर्पित सदा डरते रहते हैं। जैसे नदियोंमें गड्भा, तीर्थोंमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15670)
- **Original**: करे। (अध्याय 85) #3167//-गरप80/-005000 केदार-कन्याके वृत्तान्तका वर्णन नन्दजीने पूछा--प्रभो! आपने स्त्रियों
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15671)
- **Original**: लिये वे प्रतिदिन राजदरबारमें सुन्दर रूप- प्रसज्बसे केदार-कन्याका प्रस्ताव करके कर्मविपाकका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15672)
- **Original**: रंगवाली, सीधी, नौजवान गायें, जिनके सॉंगोंमें वर्णन किया। अब विस्तारपूर्वक केदार-कन्याका
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15673)
- **Original**: सोना मढ़ा गया था, ब्राह्मणोंकों दान करते थे। चरित्र बतलाइये। वह केदार-कन्या कौन थी?]
- **Translation**: 

---

