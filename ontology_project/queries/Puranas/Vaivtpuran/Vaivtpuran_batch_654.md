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

### Verse 1 (Vaivtpuran 67.5875)
- **Original**: भक्तिसहित तुलसीदलसे संयुक्त अनेक प्रकारके श्रतका आरम्भ शुभ होता है। उत्तम ब्रतीको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 67.5876)
- **Original**: पुष्प निवेदन करना चाहिये। ब्रतीको चाहिये कि चाहिये कि वह ब्रतारम्भके पूर्वदिन उपवास करे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 67.5877)
- **Original**: वह ब्रतकालमें जन्म-जन्मान्तरमें अपने धन- और शरीरको अत्यन्त निर्मल करके यल्रपूर्वक
- **Translation**: 

---

### Verse 4 (Vaivtpuran 67.5878)
- **Original**: धान्‍्यकी समृद्धिके लिये प्रतिदिन एक सहस्र वस्त्रको धोकर स्वच्छ कर ले। फिर दूसरे दिन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 67.5879)
- **Original**: ब्राह्मणोंको भोजन करावे। देवि! प्रतिदिन पूजनकालें अरुणोदय-वेलामें शय्यासे उठ जाय और मुखको
- **Translation**: 

---

### Verse 6 (Vaivtpuran 67.5880)
- **Original**: पुष्पोंसे भरी हुई सौ अञ्जलियाँ समर्पित करे तथा शुद्ध करके निर्मल जलमें स्नान करे। तत्पश्चात्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 67.5881)
- **Original**: भक्तिकी वृद्धिक लिये सौं बार प्रणाम करना हरिस्मरणपूर्वक आचमन करके पवित्र हो जाय।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 67.5882)
- **Original**: चाहिये। सुत्रते ! ब्रतकालमें छः मासतक हविष्यान्न, फिर भक्तिसहित श्रीहरिको अर्घ्य देकर शीघ्र ही
- **Translation**: 

---

### Verse 9 (Vaivtpuran 67.5883)
- **Original**: पाँच मासतक फलाहार और एक पक्षतक हविका घर लौट आये। वहाँ धुली हुई धोती और चादर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 67.5884)
- **Original**: भोजन करे तथा एक पक्षतक केवल जल पीकर धारण करके पवित्र आसनपर बैठे। फिर आचमन
- **Translation**: 

---

### Verse 11 (Vaivtpuran 67.5885)
- **Original**: रहना चाहिये। अग्रिदेवके लिये सौ अखण्ड और तिलक करके अपना नित्यकर्म समाप्त करे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 67.5886)
- **Original**: रत्रदीपोंका दान करना चाहिये। रात्रिमें कुशासन तत्पश्चात्‌ पहले प्रयत्रपूर्वक पुरोहितका वरण करके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 67.5887)
- **Original**: बिछाकर नित्य जागरण करना उत्तम है। ब्रतीको स्वस्तिवाचनपूर्वक कलश-स्थापन करे। फिर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 67.5888)
- **Original**: चाहिये कि ब्रतकी शुद्धिके लिये स्मरण, कीर्तन, वेदबिहित संकल्प करके इस ब्रतका अनुष्ठान
- **Translation**: 

---

### Verse 15 (Vaivtpuran 67.5889)
- **Original**: केलि, प्रेक्षण, गुद्ठभाषण, संकल्प, अध्यवसाय आरम्भ करे। तथा क्रियानिष्पत्ति-इन अष्टविध मैथुनोंका तदनन्तर सौन्दर्य, नेत्रदी2म्ति, विविध अड्जोंके
- **Translation**: 

---

### Verse 16 (Vaivtpuran 67.5890)
- **Original**: परित्याग कर दे। सौन्दर्य, पति-सौभाग्य आदिके लिये विभिन्न
- **Translation**: 

---

### Verse 17 (Vaivtpuran 67.5891)
- **Original**: . देवि! इस प्रकार ब्रतके भलीभाँति पूर्ण वस्तुओंके संख्यासहित समर्पण करनेकी बात
- **Translation**: 

---

### Verse 18 (Vaivtpuran 67.5892)
- **Original**: होनेपर तदनन्तर ब्रतोद्यापन करना चाहिये। उस कहकर शंकरजी पुनः बोले-देवि! पुत्र-प्राप्तिक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 67.5893)
- **Original**: समय तीन सौ साठ डलियाएँ, जो बस्त्रोंसे लिये कृष्माण्ड, नारियल, जम्बीर तथा श्रीफल--इन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 67.5894)
- **Original**: आच्छादित तथा भोजनके पदार्थ, यज्ञोपवीत और फलोंको श्रीहरिके अर्पण करना चाहिये। असंख्य
- **Translation**: 

---

