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

### Verse 1 (Vaivtpuran 543.13754)
- **Original**: करनेपर तेरे शरीरकी योनिययाँ नेत्रोंके रूपमें ताराके पास गये। वहाँ उन्होंने भक्तिभावसे मस्तक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13755)
- **Original**: परिणत हो जायँगी। मेंरे शाप और गुरुके क्रोधसे झुका दोनों हाथ जोड़कर माता ताराकों प्रणाम
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13756)
- **Original**: इस समय तू राजलक्ष्मीसे भ्रष्ट हो जा। ओ मूढ़! किया और सारी बातें बतायीं। फिर वे उच्चस्वरसे । तेरे गुरु बड़े तेजस्वी और मेरे अत्यन्त प्रेमी बन्धु बारंबार रोदन करने लगे। पुत्रकों रोते देख माता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13757)
- **Original**: हैं। हम दोनों बन्धुओंमें फूट न पड़ जाय; इस तारा भी बहुत रोयीं और बोलीं--“बेटा! तू घर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13758)
- **Original**: भयसे तेरे गुरुका ही खयाल करके मैंने इस समय जा। इस समय तुझे गुरुदेवके दर्शन नहीं होंगे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13759)
- **Original**: तेरे प्राण नहीं लिये हैं। जब दुर्दिनका अन्त होगा, तभी तुझे गुरुजी मिलेंगें।... तदनन्तर पैरोंमें पड़ी हुई अहल्याको लक्ष्य और उनकी कृपासे पुनः लक्ष्मीकी प्राप्ति होगी।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13760)
- **Original**: करके मुनिवर गौतमने कहा--प्रिये! अब तू मूढ़ ! तेरा अन्तःकरण दूषित है; अत: अब अपने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13761)
- **Original**: वनमें जा अपने शरीरको पत्थर बनाकर चिरकाल- कर्मोका फल भोग। दुर्दिनमें अपने गुरुपर
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13762)
- **Original**: तक उसी अवस्थामें रह। इस बातकों मैं अच्छी दोषारोपण करता है और अच्छे दिनोंमें अपने-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13763)
- **Original**: तरह जानता हूँ कि तेरे मनमें कोई कामना नहीं आपको ही संतुष्ट करनेमें लगा रहता है। (गुरुकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13764)
- **Original**: थी। इन्ध्रने स्वयं आसक्त होकर तेरे साथ छल परवा नहीं करता।) इन्द्र! सुदिन और दुर्दिन ही [किया है।' सुख और दुःखके कारण हैं।'
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13765)
- **Original**: . स्वामीकी ऐसी आज्ञा होनेपर अहल्या बहुत यों कहकर पतिक्रता तारादेवी चुप हो गयीं।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13766)
- **Original**: डर गयी और “हा नाथ! हा नाथ !' पुकारती तथा तदनन्तर इन्द्र वहाँसे लौट आये और एक दिन रोती हुई वनमें चली गयी। साठ हजार वर्षोतक मन्दाकिनीके तटपर स्नानके लिये गये। वहाँ! कर्मफलका भोग करनेके बाद मुनिप्रिया अहल्या उन्होंने स्नान करतो हुई गौतमपत्री अहल्याको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13767)
- **Original**: श्रोरामचन्द्रजीके चरणोंका स्पर्श पाकर तत्काल देखा। इन्द्रकी बुद्धि भ्रष्ट हो चुकौ थी। उन्होंने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13768)
- **Original**: शुद्ध हो गयी। फिर वह अत्यन्त सुन्दर रूप धारण गौतमका रूप धारण करके अहल्याका शोल भड्ढ
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13769)
- **Original**: करके गौतमजीके पास गयी। मुनिने सुन्दरी कर दिया। इसी बीच गौतमजी भी वहाँ आ गये।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13770)
- **Original**: अहल्याकों पाकर प्रसन्नताका अनुभव किया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13771)
- **Original**: ष्र8 # संक्षिप्त ब्रह्मवैवर्तपुराण # अं #### ##ऋ$% कक %%%#####%$%ऋऋऋ##ऋ#######$##$%$%%ऋ$#ऋऋऋऋदद##$###$#ऊऋ%ऋ$%%ऊऋककक्ल्क्कढ ढक ढक 6 6 सुन्दरि राधिके! अब इन्द्रका उत्तम वृत्तान्त
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13772)
- **Original**: खो बैठे थे। उसका स्वभाव निर्दय था और वह सुनो, जो पुण्यका बीज तथा पापका नाशक है।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13773)
- **Original**: हाथमें तलवार लेकर बड़े वेगसे दौड़ रही थी। मैं विस्तारपूर्वक उसका वर्णन करता हूँ। गुरुके
- **Translation**: 

---

