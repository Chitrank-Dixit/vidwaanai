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

### Verse 1 (Vaivtpuran 543.12994)
- **Original**: समान प्रतीत होते थे। वैष्णबोंको महाविष्णु तथा दिया और मुनियों तथा शिवके पार्षदोंका पूजन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12995)
- **Original**: शैवोंकों सदाशिवके रूपमें दृष्टिगोचर होते थे। किया। उस समय मेना स्त्रियोंके साथ वहाँ
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12996)
- **Original**: शक्तिके उपासकोंकों शक्तिस्वरूप, सूर्यभक्तोंको आयी। उसने वटके नीचे आसन लगाये
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12997)
- **Original**: सूर्यरूप, दुष्टोंकों कालरूप तथा श्रेष्ठ पुरुषोंको चन्द्रशेखर शिवको देखा। उनके प्रसन्न मुखपर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12998)
- **Original**: परिपालकके रूपमें दिखायी देते थे। कालको मन्द हास्यकी छटा छा रही थी। वे व्याप्रचर्म कालके समान, मृत्युकों मृत्यु एवं अत्यन्त धारण किये मुनि-मण्डलीके मध्य भागमें ब्रह्मतेजसे
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12999)
- **Original**: भयानक जान पड़ते थे। स्थ्रियोंके लिये उनका प्रकाशित हो रहे थे, मानो आकाशमें तारिकाओंके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13000)
- **Original**: व्याप्रचर्म मनोहर वस्त्र बन गया। भस्म चन्दन बीच द्विजराज चन्द्रमा शोभा पा रहे हों। करोड़ों
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13001)
- **Original**: हो' गया। सर्प सुन्दर मालाओंके रूपमें परिणत कन्दर्पोोके समान उनका मनोहर रूप अत्यन्त हो गये। कण्ठमें कालकूटकी प्रभा कस्तूरीके आह्वाद प्रदान करनेवाला था। वे वृद्धावस्था
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13002)
- **Original**: समान प्रतीत हुई। जटा सुन्दर सँवारी हुई चूड़ा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13003)
- **Original**: पद8 + संक्षिप्त ब्रह्मवैवर्तपुराण * 44004 44440404/ 72 040000]]
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13004)
- **Original**: या पा आप नाप उप] जान पड़ी। चन्द्रमा भाल-देशमें चन्दन जान
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13005)
- **Original**: ओऔर सुन्दर पति प्राप्त हो। शुभे! तुम्हारा पड़े। मस्तकपर गड्जाकी मनोहारिणी धारा परम
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13006)
- **Original**: पतिविषयक सौभाग्य सतत बना रहे। साध्वि! सुन्दर मालती मालाके रूपमें परिणत हो गयी।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13007)
- **Original**: तुम्हारा पुत्र नारायणके समान गुणवान्‌ होगा। अस्थियोंकी माला रत्मरमाला बन गयी। धतूर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13008)
- **Original**: जगदम्बिके! तीनों लोकोमें तुम्हारी उत्कृष्ट पूजा मनोहर चम्पाके रूपमें बदल गया। पाँच मुखके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13009)
- **Original**: होगी। तुम समस्त ब्रह्माण्डोंमें सबसे श्रेष्ठ होओ। स्थानमें उन्हें एक ही मुख दिखायी देने लगा,
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13010)
- **Original**: सुन्दरि! तुमने सात बार परिक्रमा करके भक्ति भावसे जो दो नेत्र-कमलोंसे सुशोभित था। मुख
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13011)
- **Original**: मुझे नमस्कार किया है। अतः मैं सात शरत्पूर्णिमाके चन्द्रमाका आभाको प्रतिहत करके जन्मोंके लिये संतुष्ट हो गया। तुम उसका अत्यन्त देदीप्यमान हो रहा था। बन्धुजीव
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13012)
- **Original**: फल पाओ। तीर्थ, प्रियतम पति, इष्टदेवता, (दुपहरिया)-की लालीकों तिरस्कृत करनेवाले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13013)
- **Original**: गुरुमन्त्र तथा औषधमें जिनको जैसी आस्था उनके ओष्ठ और अधरसे मुखकी मनोहरता बढ़
- **Translation**: 

---

